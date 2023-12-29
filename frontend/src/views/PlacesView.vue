<template>
    <div id="main-page">
        <div class="page-container">
            <div class="container">
                <h1 class="title mt-5">
                    Visit here while you at our homestay
                </h1>
                <div class="card-list">
                    <div class="row">
                        <AppVisitCard
                            markerId="2"
                            cardPicture="/NDAT.jpg"
                            cardTitle="Nasi Dagang Atas Tol (NDAT)"
                            cardSubtitle="Savor the authentic flavors of Terengganu at Nasi Dagang Atas Tol Restaurant. Indulge in the region's iconic dish, Nasi Dagang, served with a perfect blend of flavors and accompanied by a warm and inviting atmosphere."
                            cardLocation="10 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            markerId="3"
                            cardPicture="/muzium.jpg"
                            cardTitle="Muzium Terengganu"
                            cardSubtitle="Immerse yourself in Terengganu's past at the State Museum. Discover centuries-old artifacts, traditional crafts, and the vibrant history of this coastal state—all housed in a modern architectural gem."
                            cardLocation="40 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            markerId="4"
                            cardPicture="/draw_bridge.jpg"
                            cardTitle="Jabatan Angkat Kuala Terengganu"
                            cardSubtitle="Terengganu's skyline is transformed by the majestic Terengganu Drawbridge. Discover the beauty and functionality of this drawbridge, a symbol of progress that complements the region's rich cultural heritage."
                            cardLocation="10 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            markerId="5"
                            cardPicture="/pasar_payang.jpeg"
                            cardTitle="Pasar Payang"
                            cardSubtitle="Discover the heartbeat of Terengganu at Pasar Payang. This bustling market is a sensory delight, where the rich tapestry of local life unfolds through colorful stalls, aromatic spices, and unique handcrafted souvenirs."
                            cardLocation="10 KM from the location"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script setup>
import AppVisitCard from './../components/AppVisitCard.vue';
import { useHouseStore, useServerStore } from '@/store/houseStore';
import { ref, onMounted } from 'vue';

const houseStore = useHouseStore();
const houseDetails = ref(null);

onMounted(async () => {
    await houseStore.fetchHouseDetails(useServerStore().backEndServer);
    houseDetails.value = houseStore.houseDetails;
});
</script>

<style scoped>
    #main-page {
        background: linear-gradient(45deg, #A9F1DF , #FFBBBB);
        min-height: 100vh;
    }

    .card-list {
        margin-top: 40px;
    }

    @media (max-width: 576px) {
        .title {
            font-size: 45px !important;
        }

        .sub-title {
            font-size: calc(45 / 1.618 * 0.6px)
        }
    }
</style>