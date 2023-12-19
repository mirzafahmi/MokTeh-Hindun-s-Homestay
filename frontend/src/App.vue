<script setup>
import AppNavbar from "./components/AppNavbar.vue";
</script>

<template>
  <AppNavbar />
  <div id="router-view-main">
    <router-view />
  </div>
  <v-footer></v-footer>
</template>

<style>
:root {
  --primary: #f5f3ee;
  --primary-shade: #E3FDFD;
  --secondary: #CBF1F5;
  --secondary-shade: #A6E3E9;
  --accent: #71C9CE;
  --accent-shade: #65bbc0;
  --navbar: 56px;
}

#router-view-main {
  margin-top: var(--navbar);
}
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}*/


</style>
