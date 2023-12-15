import { createRouter, createWebHistory } from "vue-router";
import WelcomeView from './../views/WelcomeView.vue';
import PlacesView from './../views/PlacesView.vue';

const routes = [
    {
        path: '/',
        name: "Home",
        component:  WelcomeView
    },
    {
        path: '/visit',
        name: "Visit",
        component: PlacesView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router