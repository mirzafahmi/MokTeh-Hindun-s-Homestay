<script setup>
import AppHouseCard from './../components/AppHouseCard.vue';
import { ref, onMounted } from 'vue';
import Axios from 'axios';

const responseData = ref(null);

const transformName = (name) => {
  return name.replace(/_/g, ' ').replace(/\b\w/g, (match) => match.toUpperCase());
};

onMounted(async () => {
  try {
    const path = 'http://127.0.0.1:5000/';
    const res = await Axios.get(path);
      responseData.value = res.data;
    console.log(res.data[0].specs.room.length)
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
    <div id="scroll-container">
        <div id="page-1">
            <div class="container">
                <div class="row w-100">
                    <div id="welcome-text" class="col-md-12 col-lg-7">
                        <h1 class="title">
                            Welcome to Mokteh Hindun's Homestays
                        </h1>
                        <h3 id="tagline">
                            Experience the unparalleled beauty of Terengganu as you immerse yourself in the authentic charm of our Homestay, where every moment becomes a delightful journey into the heart of this enchanting destination. Embrace the rich cultural tapestry, indulge in the vibrant local flavors, and create lasting memories surrounded by the breathtaking landscapes that make your stay a truly unforgettable exploration of Terengganu's allure.
                        </h3>
                    </div>
                    <div id="welcome-pic-list" class="col w-100">
                        <img 
                        id="bridge-pic" 
                        class="welcome-pic" 
                        src="./../../public/welcome_pic.jpg" 
                        alt="Jambatan Gantung"
                        />

                        <img 
                        id="keropok-pic" 
                        class="welcome-pic" 
                        src="./../../public/keropok.jpg" 
                        alt="Jambatan Gantung"
                        />
                        
                        <img 
                        id="penyu-pic" 
                        class="welcome-pic" 
                        src="./../../public/penyu.jpg" 
                        alt="Jambatan Gantung"
                        />
                    </div>
                </div>
            </div>
        </div>
        <div id="page-2">
            <div class="container">
                <h1 class="title text-center pt-5">What we can offer to you?</h1>
                
            </div>
        </div>
        <div id="page-3">
            <div class="container">
                <h1 class="title text-center pt-5">Here are the list of our homestay</h1>
                <div id="card-list" class="row w-100" v-if="responseData">
                    <AppHouseCard 
                    v-for="(item, index) in responseData"
                    :key="index"
                    :houseName="transformName(item.name)"
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
            </div>
        </div>
    </div>     
</template>
<style>
    #welcome-text {
        margin-top: 300px;
        min-height: calc(100vh - 356px);
    }

    #page-1 {
        background-color: var(--primary);
        scroll-snap-align: start;
    }

    #page-2 {
        
        background-color: var(--accent);
    }

    #page-3 {
        min-height: calc(100vh);
        background-color: var(--primary);
    }
    
    #page-1, #page-2 {
        min-height: calc(100vh - var(--navbar));
    }
    .title{
        font-family: 'roboto', sans-serif;
        font-size: 72px;
        font-weight: 800;
        text-align: left;
    }

    #tagline{
        font-family: 'Montserrat', sans-serif;
        font-size: calc(58 / 1.618 * 0.6px);
        font-weight: 100;
        text-align: left;
        margin: 30px 0px;
    }

    #welcome-pic-list {
        margin-top: 180px;
    }

    .welcome-pic {
        height: 400px;
        width: 300px;
        border-radius: 50px;
    }

    .welcome-pic:not(:first-child) {
        margin: -60px 0px;
    }

    .welcome-pic:nth-child(odd) {
        float: right;
    }

    #bridge-pic {    
        rotate: 20deg;
        margin-bottom: -60px;
    }

    #keropok-pic {
        rotate: -25deg;
        margin-left: 30px
    }

    #penyu-pic {    
        rotate: 25deg;
    }

    #card-list {
        margin-top: 50px;
    }

    @media (max-width: 991px) {
        * {
            all: initial;
            all: inherit;
            all: unset;
            all: revert;
            all: revert-layer;
        }
        
        #welcome-text {
        margin-top: 100px;
        min-height: 0px;
        }

        #welcome-pic-list {
            margin-top: 0px;
            position: relative;
            margin-top: 80px;
        }

        .welcome-pic {
            position: absolute;
        }

        .welcome-pic:not(:first-child) {
            margin: 0px;
        }

        .welcome-pic:nth-child(odd) {
            float: none;
        }

        #bridge-pic {    
            rotate: -20deg;
        }

        #keropok-pic {
            right: 25%;
            rotate: 0deg;
        }

        #penyu-pic {    
            right: 0;
            rotate: 20deg;
        }
    }

    @media (min-width: 1001px) {
        html,
        body {
        height: 100vh;
        overflow: hidden;
        }

        #scroll-container {
        overflow: auto;
        height: 100vh;
        scroll-snap-points-y: repeat(100vh);
        scroll-snap-type: y mandatory;
        }

        #page-1, #page-2, #page-3 {
        scroll-snap-align: start;
        position: relative;
        will-change: transform;
        }
    }
</style>