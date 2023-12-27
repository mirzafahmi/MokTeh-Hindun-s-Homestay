<template>
    <div id="main-page">
        <div class="page-container">
            <div class="container">
                <h1 class="title mt-5">
                    Must visit place while in Terengganu
                </h1>
                <div class="card-list">
                    <div class="row">
                        <AppVisitCard
                            cardPicture="/NDAT.jpg"
                            cardTitle="Nasi Dagang Atas Tol (NDAT)"
                            cardSubtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque voluptatem sed omnis dolores assumenda quia fugit et expedita dolor cupiditate, nam illo suscipit adipisci consequatur impedit, nihil accusamus modi quidem?"
                            cardLocation="10 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            cardPicture="/sekayu.jpg"
                            cardTitle="Air Terjun Sekayu"
                            cardSubtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque voluptatem sed omnis dolores assumenda quia fugit et expedita dolor cupiditate, nam illo suscipit adipisci consequatur impedit, nihil accusamus modi quidem?"
                            cardLocation="40 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            cardPicture="/draw_bridge.jpg"
                            cardTitle="Jabatan Angkat Kuala Terengganu"
                            cardSubtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque voluptatem sed omnis dolores assumenda quia fugit et expedita dolor cupiditate, nam illo suscipit adipisci consequatur impedit, nihil accusamus modi quidem?"
                            cardLocation="10 KM from the location"
                        />
                    </div>
                    <div class="row">
                        <AppVisitCard
                            cardPicture="/pasar_payang.jpeg"
                            cardTitle="Pasar Payang"
                            cardSubtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque voluptatem sed omnis dolores assumenda quia fugit et expedita dolor cupiditate, nam illo suscipit adipisci consequatur impedit, nihil accusamus modi quidem?"
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
import AppBenefits from './../components/AppCard.vue';
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
        background-color: blanchedalmond;
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