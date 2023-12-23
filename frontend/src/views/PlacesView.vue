<template>
    <div id="main-page">
        <div class="container">
            <h1 class="title">Place to visit</h1>
            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Deserunt nostrum pariatur, incidunt quod sed rem ipsam repellat nisi voluptatum, odit nam eligendi non ipsum nesciunt voluptatem sint animi dolor facilis ab commodi sapiente. Eaque esse consectetur quas, placeat ex non ipsa natus repellendus nihil error laboriosam ullam, a eligendi eos! Quibusdam, odio. Consequatur ex ipsa repellendus nisi facilis consequuntur nihil quaerat quidem quae totam, modi quas voluptas culpa laborum deserunt, atque est architecto labore itaque eaque nostrum suscipit nesciunt. Optio, eveniet fuga. Rem natus, quasi officiis voluptas ex veritatis eos temporibus laborum error cupiditate voluptatem quidem odit animi in nulla?
            </p>
            <AppVisitCard/>
        </div>
    </div>
    
</template>

<script setup>
import AppVisitCard from './../components/AppVisitCard.vue';
import { useHouseStore } from '@/store/houseStore';
import { ref, onMounted } from 'vue';

const houseStore = useHouseStore();
const houseDetails = ref(null);

onMounted(async () => {
    await houseStore.fetchHouseDetails();
    houseDetails.value = houseStore.houseDetails;
});
</script>

<style scoped>
    #main-page {
        background-color: blanchedalmond;
        height: 100vh;
    }
</style>