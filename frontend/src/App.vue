<template>
  <NavComp />
  <router-view/>
</template>

<script>
import NavComp from './components/NavComp.vue';
export default {
    name: "App",
    components: { 
      NavComp 
  }
}
</script>

<style lang="scss">
@import '../node_modules/bootstrap';
</style>