<template>
  <v-app class="hidden">
    <SpeedInsights />
    <AppNavbar v-motion-slide-top />
    <router-view :key="$route.fullPath"/>
  </v-app>
</template>

<script setup>
import AppNavbar from "./components/AppNavbar.vue";
import { SpeedInsights } from '@vercel/speed-insights/vue';

import { useServerStore } from '@/store/houseStore';
import { onMounted } from "vue";
import Axios from 'axios';

const backendServer = useServerStore().backEndServer

const startKeepAlive = async () => {
  try {
    await pingServer();
    setTimeout(() => {
      startKeepAlive();
    }, 840000); 
  } catch (error) {
    console.error('Failed to send ping request:', error);
  }
};

const pingServer = async () => {
  try {
    const pingTime = new Date();
    await Axios.get(backendServer);
    console.log(`Ping sent to ${backendServer} at ${pingTime}`);
  } catch (error) {
    console.error('Failed to send ping request:', error);
    throw error; 
  }
};

onMounted(() => {
  startKeepAlive();
});
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

</style>