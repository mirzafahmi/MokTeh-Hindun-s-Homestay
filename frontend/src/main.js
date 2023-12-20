import { createApp } from "vue";
import App from "./App.vue";
import router from './router/index.js';
import { createPinia } from 'pinia';
import './../node_modules/@fortawesome/fontawesome-free/css/all.css';
import "@mdi/font/css/materialdesignicons.css";

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
  })

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(vuetify);
app.use(router);

app.mount("#app");