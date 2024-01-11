<template>
    <div id="housecard-list" class="row w-100 card-list" v-if="houseDetails">
        <AppHouseCard 
            v-for="(item, index) in houseDetails"
            :key="index"
            :houseName="transformName(item.name)"
            :houseImage="backendServer + '/media/' + item.name + '/card/card.jpg'"
            :housePax="item.pax"
            :housePricing="item.pricing"
            :houseBedroom="item.specs.room.length"
            :houseBathroom="item.specs.bathroom"
            :houseKitchen="item.specs.kitchen"
            :houseFridge="item.specs.fridge"
            :houseKettle="item.specs.kettle"
            :houseIron="item.specs.iron"
            :houseUrl="item.name"
        />
    </div>
    <div class="" v-if="houseDetails">
        <AppHouseSpecCard
            v-for="(item, index) in houseDetails"
            :key="index"
            :housePax="item.pax"
            :housePricing="item.pricing"
            :houseBedroom="item.specs.room.length"
            :houseBathroom="item.specs.bathroom"
            :houseKitchen="item.specs.kitchen"
            :houseFridge="item.specs.fridge"
            :houseKettle="item.specs.kettle"
            :houseIron="item.specs.iron"
        />
    </div>
</template>

<script setup>
import AppHouseCard from './../components/AppHouseCard.vue';
import AppHouseSpecCard from '@/components/AppHouseSpecCard'
import { useHouseStore, useServerStore } from '@/store/houseStore';
import { ref, onMounted } from 'vue';

const houseStore = useHouseStore();
const houseDetails = ref(null);

const transformName = (name) => {
  return name.replace(/_/g, ' ').replace(/\b\w/g, (match) => match.toUpperCase());
};

onMounted(async () => {
    await houseStore.fetchHouseDetails(useServerStore().backEndServer);
    houseDetails.value = houseStore.houseDetails;
});

</script>