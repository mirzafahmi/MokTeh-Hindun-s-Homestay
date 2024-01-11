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
    
    window.scrollTo(0, 0);

    next();
});

export default router