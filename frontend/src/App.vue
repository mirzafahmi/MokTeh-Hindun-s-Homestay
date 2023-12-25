<template>
  <v-app class="hidden">
    <AppNavbar />
    <div id="router-view-main">
      <router-view :key="$route.fullPath"/>
    </div>
  </v-app>
</template>

<script setup>
import AppNavbar from "./components/AppNavbar.vue";
</script>

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
/*
#router-view-main {
  margin-top: var(--navbar);
}*/

.page-container {
  padding-top: var(--navbar)
}

.custom-divider {
  margin:2px
}

.custom-margin {
  margin: 0px
}

.title{
  font-family: 'roboto', sans-serif;
  font-size: 72px;
  font-weight: 800;
  text-align: left;
}

.sub-title{
    font-family: 'Montserrat', sans-serif;
    font-size: calc(58 / 1.618 * 0.6px);
    font-weight: 100;
    text-align: left;
    margin: 30px 0px;
}
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

@media (min-width: 992px) {
    html, body {
    height: 100vh !important;
    overflow: hidden !important;
    margin: 0 !important;
    }

    #scroll-container {
    overflow: auto;
    height: calc(100vh - var(--navbar));
    scroll-snap-points-y: repeat(100vh);
    scroll-snap-type: y mandatory;
    }

    #page-1, #page-2, #page-3 {
    scroll-snap-align: start;
    position: relative;
    will-change: transform;
    }
}*/
</style>