<template>
    <div class="card mb-3">
        <div class="row g-0">
            <div class="col-xs-12 col-md-4">
                <img 
                    :src="cardPicture" 
                    class="img-fluid" 
                    alt="..."
                >
            </div>
            <div class="col-xs-12 col-md-8">
                <div class="card-body">
                    <h2 
                        class="card-title"
                    >
                        {{ props.cardTitle }}
                    </h2>
                    <p class="card-text">
                        {{ props.cardSubtitle }}    
                    </p>
                    <p class="card-text">
                        <router-link 
                        :to="{ name: 'HouseDetails', params: { houseName: 'rumah_kayu' }, query: { markerId: props.markerId } }"
                            >
                            <small class="text-body-secondary">
                                <i class="fa-solid fa-location-dot"></i>
                                ~{{ props.cardLocation }}  
                            </small>
                        </router-link>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps([
    'cardTitle',
    'cardSubtitle',
    'cardLocation',
    'cardPicture',
    'markerId'
])
</script>

<style scoped>
    .card {
        width: 100%;
        height: 200px;
        overflow: hidden;
    }

    img {
        width: 100%;
        height: 100%;
    }

    @media (max-width: 768px) {
        .card-title {
            margin-top: 1rem;
        }

        .card {
            height: 100%;
        }

        img {
        width: 100%;
        height: 100%;
        margin-top: calc(1 * 0.7rem);
        }
        .card-body {
            padding: 1rem 0px !important;
        }
    }
</style>

