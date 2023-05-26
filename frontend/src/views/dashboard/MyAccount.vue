<template>  
  <div class="columns is-multiline">
    <div class="column is-12">
      <h1 class="title">
        My Account
      </h1>
    </div>

    <div class="column is-12">
      <span>Username: {{ store.state.userData.username }}</span>
    </div>
  </div>         
</template>

<script setup>
    import axios from 'axios';
    import { useStore } from 'vuex';

    const store = useStore();

    async function getUserData() {
        store.commit('setIsLoading', true)

        const userData = await axios
        .get('/api/v1/users/me/')
        .then(response => {
            return response.data
        })
        .catch(error => {
            console.log(JSON.stringify(error))
            return {}
        })

        store.commit('setUserData', userData)
        store.commit('setIsLoading', false)
    }

    getUserData()
</script>