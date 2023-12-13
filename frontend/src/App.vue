<script setup>
import AppWelcome from "./components/AppWelcome.vue";


</script>

<template>
  <AppNavbar></AppNavbar>
  <AppWelcome></AppWelcome>
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
:root {
  --primary: #f5f3ee;
  --primary-shade: #E3FDFD;
  --secondary: #CBF1F5;
  --secondary-shade: #A6E3E9;
  --accent: #71C9CE;
  --accent-shade: #65bbc0;
}
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}*/

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
