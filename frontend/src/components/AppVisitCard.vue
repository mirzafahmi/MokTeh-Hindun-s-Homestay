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
                    <h3 
                        class="card-title"
                    >
                        {{ props.cardTitle }}
                    </h3>
                    <p class="card-text">
                        {{ props.cardSubtitle }}    
                    </p>
                    <p class="card-text">
                        <small class="text-body-secondary">
                            {{ props.cardLocation }}  
                        </small>
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
    'cardPicture'
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


</style>

