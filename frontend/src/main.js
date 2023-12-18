import { createApp } from "vue";
import App from "./App.vue";
import router from './router/index.js';
import { createPinia } from 'pinia';
import './../node_modules/@fortawesome/fontawesome-free/css/all.css';

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);

app.mount("#app");
