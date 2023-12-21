<script setup>
import AppNavbar from "./components/AppNavbar.vue";
</script>

<template>
  <v-app class="hidden">
    <AppNavbar />
    <div id="router-view-main">
      <router-view :key="$route.fullPath"/>
    </div>
  </v-app>
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