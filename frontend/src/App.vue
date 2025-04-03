<template>
  <div id="app">
    <NavBar />
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/Common/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  },
  created() {
    this.$store.dispatch('fetchCurrentUser')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.container {
  padding: 20px;
}
</style>