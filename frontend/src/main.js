import { createApp } from "vue";
import App from "./App.vue";
import router from './router/index.js';
import './../node_modules/@fortawesome/fontawesome-free/css/all.css';

createApp(App).use(router).mount("#app");
