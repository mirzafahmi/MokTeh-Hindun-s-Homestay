import { createRouter, createWebHistory } from "vue-router";
import WelcomeView from './../views/WelcomeView.vue';
import PlacesView from './../views/PlacesView.vue';
import HouseView from './../views/HouseView.vue';
import TestView from './../views/testView.vue';

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
    },
    {
        path: '/test',
        name: "test",
        component: TestView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {
    const thresholdWidth = 991;
    const requiresOverflowHidden = to.path === '/' && window.innerWidth >= thresholdWidth;
    document.documentElement.style.overflow = requiresOverflowHidden ? 'auto' : 'auto';
    next();
});

export default router