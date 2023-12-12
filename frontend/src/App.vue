<template>
  <AppNavbar></AppNavbar>
  <button class="btn btn-primary">asd</button>
  <p>Hi Vue</p>
</template>

<script>
import AppNavbar from "./components/AppNavbar.vue";

export default {
  components: {
    AppNavbar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
