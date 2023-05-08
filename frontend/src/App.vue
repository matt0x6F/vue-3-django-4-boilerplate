<template>
  <div>
    <NavComp />
    
    <section class="section">
      <router-view/>
    </section>
  </div> 
</template>

<script>
import axios from 'axios'
import NavComp from '@/components/layout/NavComp'

export default {
    name: "App",
    components: { 
      NavComp 
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  
    if (this.$store.state.token) {
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    } 
  }
}
</script>

<style lang="scss">
//@import '../node_modules/bootstrap';
@import '../node_modules/bulma';
</style>