<template>
    <div class="main-page">
        <div class="page-container">
            <div id="house-details" class="container pt-5" v-if="houseDetails">
                <h1 class="title">
                    {{ transformName(houseDetails.name) }}
                </h1>
                <hr>
                <div class="row gx-md-5 mb-3">
                    <div class="col-xs-12 col-xl-7 d-flex justify-center align-center">
                        <v-carousel>
                            <v-carousel-item 
                            v-for="(pic, index) in houseDetails.picture" 
                            :key="index"
                            >
                                <img 
                                    :src="backEndServer + pic" 
                                    alt="" 
                                    style="object-fit: cover; width: 100%; height: 100%;"
                                >
                            </v-carousel-item>
                        </v-carousel>
                    </div>
                    <div class="col-12 col-md-12 col-xl-5 mt-5 mt-lg-0">
                        <AppHouseSpecCard
                            :housePax="houseDetails.pax"
                            :housePricing="houseDetails.pricing"
                            :houseBedroom="houseDetails.specs.room.length"
                            :houseBathroom="houseDetails.specs.bathroom"
                            :houseKitchen="houseDetails.specs.kitchen"
                            :houseFridge="houseDetails.specs.fridge"
                            :houseKettle="houseDetails.specs.kettle"
                            :houseIron="houseDetails.specs.iron"
                        />
                    </div>
                    <div class="col-sm-12 col-lg-7 col-xl-8 mt-5">
                        <AppGmap
                            :houseDetails="houseDetails"
                            :markerId="markerId"
                        />
                    </div>
                    <div class="col-sm-12 col-lg-5 col-xl-4 mt-5">
                        <div class="d-flex flex-column float-md-right justify-center align-items-center">
                            <v-date-picker 
                                v-model="selectedDate" 
                                :min="minDate"
                                :max="maxDate"
                                :allowed-dates=allowedDates
                                :disabled="!houseDetails.status"
                                multiple
                                header="No date selected"
                                border="1"
                                rounded="3"
                            >    
                            </v-date-picker>    
                            <a
                                id="whatsApp-btn"
                                class="btn btn-primary mt-3"
                                type="button" 
                                :data-bs-toggle="selectedDate.length != 0 ? 'modal' : '' " 
                                :data-bs-target="selectedDate.length != 0 ? '#check-in-out' : '' "
                                :href="selectedDate.length == 0 ? whatsappLink : ''"
                                target="_blank"
                                rel="noopener noreferrer"
                            >
                                {{ selectedDate.length != 0 ? 'Select Check-In/Out Time' : 'Chat us in Whatsapp'}}
                                <i v-if="selectedDate.length == 0" class="fa-brands fa-whatsapp ms-1"></i>
                                <i v-if="selectedDate.length != 0" class="fa-regular fa-clock ms-1"></i>
                            </a>
                        </div>
                    </div>
                </div>    
                <AppModal
                    modalId="check-in-out"
                    ariaLabel="checkInOutLabel"
                    ariaHidden="true"
                    title="Select Time of Check-in/out"
                    confirmButtonText="Check Homestay Availability"
                    :confirmButtonClick="whatsappLink"
                >   
                    <div class="row">
                        <div class="col d-flex flex-column">
                            <h6>Select Check-in time</h6>
                            <vue-timepicker
                                v-model="checkedInTime"
                                format="HH:mm"
                                :minute-interval="30"
                                close-on-complete
                            >
                            </vue-timepicker>
                        </div>
                    </div>
                </AppModal>
            </div>
            <div id="house-details" class="container pt-5" v-else>
                <v-skeleton-loader type="card, paragraph"></v-skeleton-loader>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useHouseStore,  useServerStore } from '@/store/houseStore';
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import AppModal from '@/components/AppModal'
import AppHouseSpecCard from '@/components/AppHouseSpecCard'
import AppGmap from '@/components/AppGmap'
import VueTimepicker from 'vue3-timepicker'


const houseStore = useHouseStore();
const houseDetails = ref(null);
const selectedDate = ref([]);
const route = useRoute();
let bookedDateStrings = [];
let minDate = '';
let maxDate = '';

let checkedInTime = ref(
    {
        HH: "00",
        mm: "00"
    }
);
let checkedOutTime = ref(
    {
        HH: "",
        mm: ""
    }
);

let allowedHourRangeCheckIn = ref(["1"])
let allowedMinuteRangeCheckIn = ref([])
let allowedHourRangeCheckOut = ref([])
let allowedMinuteRangeCheckOut = ref([])

const backEndServer = useServerStore().backEndServer

onMounted(async () => {
    const houseName = route.params.houseName;

    await houseStore.fetchHouseDetails(backEndServer);
    houseDetails.value = houseStore.houseDetails.find(detail => detail.name === houseName);

    bookedDateStrings = Array.isArray(houseDetails.value?.booked_dates)
        ? houseDetails.value.booked_dates.flatMap(dateRange => {
            const startDate = new Date(dateRange.from_book_date).toISOString().split('T')[0];
            const endDate = new Date(dateRange.to_book_date).toISOString().split('T')[0];
            const dateStrings = [];
            let currentDate = startDate;

            while (currentDate <= endDate) {    
                dateStrings.push(currentDate);
                currentDate = new Date(currentDate);
                currentDate.setDate(currentDate.getDate() + 1);
                currentDate = currentDate.toISOString().split('T')[0];
            }

            return dateStrings;
        })
        : [];
    const currentDate = new Date();
    minDate = currentDate.toISOString().split('T')[0];
    const oneYearFromNow = new Date(currentDate);
    oneYearFromNow.setFullYear(oneYearFromNow.getFullYear() + 1);
    maxDate = oneYearFromNow.toISOString().split('T')[0];

});


const allowedDates = (date) => {
    const selectedDateValue = new Date(date).toISOString().split('T')[0];
    const bookedDateStringsWithoutTime = bookedDateStrings.map((bookedDate) => {
        const dateWithoutTime = new Date(bookedDate);
        dateWithoutTime.setHours(0, 0, 0, 0);
    
        return dateWithoutTime.toISOString().split('T')[0];
    });
     
  return !bookedDateStringsWithoutTime.includes(selectedDateValue);
};

const transformName = (name) => {
  return name.replace(/_/g, ' ').replace(/\b\w/g, (match) => match.toUpperCase());
};

const whatsappLink = computed(() => {
    if (selectedDate.value.length > 0) {
    const formattedDate = selectedDate.value.map(date =>
        new Date(date).toLocaleDateString('en-GB', {
        weekday: 'short',
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        })
    )
    const encodedMessage = encodeURIComponent(`Hello! I'm interested in booking on ${formattedDate} at ${checkedInTime.value.HH}:${checkedInTime.value.mm} for ${transformName(houseDetails.value.name)}. Can you provide more information?`);

    return `https://wa.me/+60179402337?text=${encodedMessage}`;
  } else {
    const encodedMessage = encodeURIComponent(`Hello! I'm interested in booking your ${transformName(houseDetails.value.name)} homestay. Can you provide more information which one is available?`);
    
    return `https://wa.me/+60179402337?text=${encodedMessage}`;
  }
});

const markerId = ref(null);
onMounted(() => {
    markerId.value = route.query.markerId;
});
</script>

<style scoped>
    .main-page {
        background: linear-gradient(45deg, #FFECD2, #FCB69F);
        min-height: calc(100vh);
    }

    #whatsApp-btn{
        width: 360px;
        color: white;
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