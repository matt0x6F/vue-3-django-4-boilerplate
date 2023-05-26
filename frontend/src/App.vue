<template>
  <div>
    <NavComp />

    <div class="flex container">
      <Sidebar />
      <div class="flex-col flex-grow">
        <spinner v-if="store.state.isLoading" class="ml-auto mr-auto mt-4" size="10" />

        <section class="ml-2 mr-2">
          <router-view/>
        </section>
      </div>
    </div>
  </div> 
</template>

<script setup lang="ts">
  import { useStore } from 'vuex';
  import axios from 'axios';

  import { Spinner } from 'flowbite-vue'
  import NavComp from '@/components/layout/NavComp.vue'
  import Sidebar from '@/components/layout/Sidebar.vue'

  const store = useStore();

  store.commit('initializeStore')
    
  if (store.state.token) {
    axios.defaults.headers.common['Authorization'] = "Token " + store.state.token
  } else {
    axios.defaults.headers.common['Authorization'] = " "
  }
</script>

<style lang="scss">

</style>
