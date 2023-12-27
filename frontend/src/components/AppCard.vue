<script setup>
import { ref, defineProps } from 'vue';

const props = defineProps([
    "benefitsTitle",
    "benefitsText",
    "benefitsIcon",
    "benefitsShape",
    "gradientColor1",
    "gradientColor2",
    "benefitsIconViewBox"
]);

const gradientId = ref(generateUniqueId());

function generateUniqueId() {
  return Math.random().toString(36).substring(2, 15);
}
</script>
<template>
    <div class="col-xs-12 col-sm-6 col-lg-4">
        <div class="card">
            <div class="div-icon d-flex flex-column">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    :viewBox="props.benefitsIconViewBox"
                    class="position-absolute top-0 start-50 translate-middle-x icon"
                    style="transform: translateX(-50%); z-index: 1;"
                    >
                    <template v-for="(path, index) in props.benefitsIcon" :key="index">
                        <path class="cls-1" :d="path"></path>
                    </template>
                </svg>
                <svg class="shape" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" version="1.1">
                    <defs>
                        <linearGradient :id="'sw-gradient-' + gradientId" x1="0" x2="1" y1="1" y2="0">
                        <stop :stop-color="props.gradientColor1" offset="0%"></stop>
                        <stop :stop-color="props.gradientColor2" offset="100%"></stop>
                        </linearGradient>
                    </defs>
                    <path :fill="'url(#sw-gradient-' + gradientId + ')'" :d="props.benefitsShape" width="100%" height="100%" transform="translate(50 50)" style="transition: all 0.3s ease 0s;" stroke-width="0">
                    </path>
                </svg>
            </div>
            <div class="card-body">
                <h2 class="card-title text-center font-weight-bold">
                    {{ props.benefitsTitle }}
                </h2>
                <p class="card-text text-center">
                    {{ props.benefitsText }}
                </p>
            </div>
        </div>
    </div>    
</template>

<script setup>

</script>

<style scoped>
    .div-icon {
        height: 120px;
        width: 100%;
        position: relative;
    }

    .card{
        background-color: transparent;
        border: none;
        margin: 50px 25px 150px 25px;
    }

    svg {
        position: absolute;
        height: 100%;
        width: 100%;
    }

    .icon {
        z-index: 100;
    }
    .shape{
        height: 200px;
        top: -45px;
    }

    @media (max-width: 991px) {
        .card{
        margin: 10px 25px 70px 25px;
    }
        
    }
</style>
