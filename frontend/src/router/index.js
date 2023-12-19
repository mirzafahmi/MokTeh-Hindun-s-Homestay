import { createRouter, createWebHistory } from "vue-router";
import WelcomeView from './../views/WelcomeView.vue';
import PlacesView from './../views/PlacesView.vue';
import HouseView from './../views/HouseView.vue';

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
    },
    {
        path: '/:houseName',
        name: "HouseDetails",
        component: HouseView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router