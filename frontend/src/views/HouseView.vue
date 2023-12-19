<script setup>
import { useHouseStore } from '@/store/houseStore';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const houseStore = useHouseStore();
const houseDetails = ref(null);

onMounted(async () => {
    const route = useRoute();
    const houseName = route.params.houseName;
  
    await houseStore.fetchHouseDetails();
    houseDetails.value = houseStore.houseDetails;
    houseDetails.value = houseStore.houseDetails.find(detail => detail.name === houseName);
    console.log(houseDetails)
});
</script>
<template>
    <div v-if="houseDetails">
        <h1>{{ houseDetails.name }}</h1>
        <h1>asdasdas</h1>
    </div>
    <div v-else>
        <p>Loading house details...</p>
    </div>
</template>