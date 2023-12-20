<template>
    <div class="main-page">
        <div id="house-details" class="container pt-5" v-if="houseDetails">
            <h1 class="title">{{ transformName(houseDetails.name) }}</h1>
            <div class="row gx-5 mb-3">
                <div class="col-md-12 col-xl-8 d-flex justify-center align-center">
                    <v-carousel>
                        <v-carousel-item v-for="(pic, index) in houseDetails.picture" :key="index">
                            <img :src="backEndServer + pic" alt="" style="object-fit: cover; width: 100%; height: 100%;">
                        </v-carousel-item>
                    </v-carousel>
                </div>
                <div class="col">
                    <div class="row d-flex flex-column justify-center align-center">
                        <v-date-picker 
                            v-model="selectedDate" 
                            :min="minDate"
                            :max="maxDate"
                            :allowed-dates=allowedDates
                            multiple
                            header="No date selected"
                            border="1"
                            rounded="3"
                            @change="onDateChange"
                        >    
                        </v-date-picker>    
                        <a
                            class="btn btn-primary mt-3"
                            :href="whatsappLink"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Chat with us on WhatsApp
                        </a>

                    </div>
                </div>
            </div>    
            <div class="row gx-5">
                <div class="col-8">
                    <div class="card p-3">
                        <h3 class="custom-margin mb-2">What we have?</h3>
                        <hr class="custom-divider">
                        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ea culpa laborum, aperiam iusto deleniti obcaecati?</p>
                        <h5>House Details</h5>
                        <div class="row">
                            <div class="col">
                                <p class="custom-divider">Bedroom</p>
                                <div class="house-details-part d-flex">
                                    <svg class="icon" data-name="Layer 1" id="Layer_1" style="width:24px;height:24px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" d="M43.93,307.53V423.77H74.7V347.55H437.3v76.22h30.77V307.53a38.67,38.67,0,0,0-38.67-38.67H82.6A38.67,38.67,0,0,0,43.93,307.53Z"/>
                                        <path fill="currentColor" d="M82.6,244h34.71V174.23a10.55,10.55,0,0,1,10.54-10.55H234.9a10.55,10.55,0,0,1,10.54,10.55V244h21.12V174.23a10.56,10.56,0,0,1,10.55-10.55h107a10.56,10.56,0,0,1,10.55,10.55V244H429.4a62.35,62.35,0,0,1,7.9.8V139.24a51,51,0,0,0-51-51H125.7a51,51,0,0,0-51,51V244.77A62.35,62.35,0,0,1,82.6,244Z"/>
                                    </svg>
                                    <div class="house-details">
                                        {{ houseDetails.specs.room.length }}
                                    </div>  
                                </div>
                                  
                            </div>
                            <div class="col">
                                <p class="custom-divider">Bathroom</p>
                                <div class="house-details-part d-flex">
                                    <svg class="icon" style="width:24px;height:24px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" d="M288 384c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C320 398.3 305.7 384 288 384zM416 256c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C448 270.3 433.7 256 416 256zM480 192c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C512 206.3 497.7 192 480 192zM288 320c0-17.67-14.33-32-32-32s-32 14.33-32 32c0 17.67 14.33 32 32 32S288 337.7 288 320zM320 224c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C352 238.3 337.7 224 320 224zM384 224c17.67 0 32-14.33 32-32c0-17.67-14.33-32-32-32s-32 14.33-32 32C352 209.7 366.3 224 384 224zM352 320c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C384 334.3 369.7 320 352 320zM347.3 91.31l-11.31-11.31c-6.248-6.248-16.38-6.248-22.63 0l-6.631 6.631c-35.15-26.29-81.81-29.16-119.6-8.779L170.5 61.25C132.2 22.95 63.65 18.33 21.98 71.16C7.027 90.11 0 114.3 0 138.4V464C0 472.8 7.164 480 16 480h32C56.84 480 64 472.8 64 464V131.9c0-19.78 16.09-35.87 35.88-35.87c9.438 0 18.69 3.828 25.38 10.5l16.61 16.61C121.5 160.9 124.3 207.6 150.6 242.7L144 249.4c-6.248 6.248-6.248 16.38 0 22.63l11.31 11.31c6.248 6.25 16.38 6.25 22.63 0l169.4-169.4C353.6 107.7 353.6 97.56 347.3 91.31z"/>
                                    </svg>
                                    <div class="house-details">
                                        {{ houseDetails.specs.bathroom }}
                                    </div>
                                </div>
                            </div>
                            <div class="col">
                                <p class="custom-divider">Kitchen</p>
                                <div class="house-details-part d-flex">
                                    <svg class="icon" style="width:24px;height:24px" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
                                        <path fill="currentColor" d="M55,23h0a3.511,3.511,0,0,0-2.963-3.467L36,17H28L11.963,19.532A3.511,3.511,0,0,0,9,23H9" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M25,1c0,1.333-2,1.333-2,2.667S25,5,25,6.333,23,7.667,23,9" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M33,1c0,1.333-2,1.333-2,2.667S33,5,33,6.333,31,7.667,31,9" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M41,1c0,1.333-2,1.333-2,2.667S41,5,41,6.333,39,7.667,39,9" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <polyline points="60 60 63 60 63 63 1 63 1 60 4 60" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="6" x2="58" y1="60" y2="60"/>
                                        <path fill="currentColor" d="M36,55a4,4,0,0,1-8,0c0-2.209,3-8,4-8S36,52.791,36,55Z" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M52,55a4,4,0,0,1-4,4c-2.209,0-4-.791-4-3s5-9,6-9S52,52.791,52,55Z" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M12,55a4,4,0,0,0,4,4c2.209,0,4-.791,4-3s-5-9-6-9S12,52.791,12,55Z" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M51,57a4,4,0,0,0,4-4V23H9V53a4,4,0,0,0,4,4" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="35" x2="44" y1="57" y2="57"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="20" x2="29" y1="57" y2="57"/>
                                        <path fill="currentColor" d="M58,27h4a1,1,0,0,1,1,1v2a1,1,0,0,1-1,1H55V27" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M60,31l-1.447,2.894A2,2,0,0,1,56.764,35H55" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M6,27H2a1,1,0,0,0-1,1v2a1,1,0,0,0,1,1H9V27" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <path fill="currentColor" d="M4,31l1.447,2.894A2,2,0,0,0,7.236,35H9" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="12" x2="9" y1="27" y2="27"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="16" x2="14" y1="27" y2="27"/>
                                        <line style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px" x1="55" x2="18" y1="27" y2="27"/>
                                        <path fill="currentColor" d="M32,11h0a4,4,0,0,1,4,4v2a0,0,0,0,1,0,0H28a0,0,0,0,1,0,0V15A4,4,0,0,1,32,11Z" style="fill:none;stroke:#000;stroke-linejoin:round;stroke-width:2px"/>
                                    </svg>
                                    <div class="house-details">
                                        <i v-if="houseDetails.specs.kitchen" class="fa-solid fa-check"></i>
                                        <i v-else class="fa-solid fa-xmark"></i>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <v-time-picker v-model="picker" :landscape="landscape"></v-time-picker>
                </div>
            </div>
            
        </div>
        <div id="house-details" class="container pt-5" v-else>
            <v-skeleton-loader type="card, paragraph"></v-skeleton-loader>
        </div>
    </div>
    
</template>

<script setup>
import { useHouseStore } from '@/store/houseStore';
import { ref, onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';

const houseStore = useHouseStore();
const houseDetails = ref(null);
const selectedDate = ref([]);
let bookedDateStrings = [];
let minDate = '';
let maxDate = '';

const backEndServer = "http://127.0.0.1:5000/"

onMounted(async () => {
    const route = useRoute();
    const houseName = route.params.houseName;

    await houseStore.fetchHouseDetails();
    houseDetails.value = houseStore.houseDetails.find(detail => detail.name === houseName);

    // Check if houseDetails.value has a booked_dates property and if it is an array
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
    console.log(bookedDateStrings);
    console.log(houseDetails.value)
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
    const encodedMessage = encodeURIComponent(`Hello! I'm interested in booking on ${formattedDate} for ${transformName(houseDetails.value.name)}. Can you provide more information?`);

    return `https://wa.me/+60179402337?text=${encodedMessage}`;
  } else {
    const encodedMessage = encodeURIComponent(`Hello! I'm interested in booking your ${transformName(houseDetails.value.name)} homestay. Can you provide more information which one is available?`);
    
    return `https://wa.me/+60179402337?text=${encodedMessage}`;
  }
});

</script>

<style scoped>
    .main-page {
        background: linear-gradient(to bottom, #A890FE, #EA8D8D);
        min-height: 100vh;
    }

    .house-details {
        margin-left: 30px;
        height: 100%;
    }
</style>