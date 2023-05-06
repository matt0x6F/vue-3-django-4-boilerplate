<template>
  <div>
    <NavComp />

    <section class="section">
      <router-view/>
    </section>
  </div> 
</template>

<script>
import NavComp from '@/components/layout/NavComp';
export default {
    name: "App",
    components: { 
      NavComp 
  }
}
</script>

<style lang="scss">
//@import '../node_modules/bootstrap';
@import '../node_modules/bulma';
</style>