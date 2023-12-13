<script setup>
import ChildComponent from './AppHouseCard.vue';


</script>

<template>
    <div id="page-1">
        <div class="container">
            <div class="row w-100">
                <div id="welcome-text" class="col-7">
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
            <div class="row w-100">
                <ChildComponent/>
            </div>
        </div>
    </div>        
</template>
<style>
    #welcome-text {
        margin-top: 300px;
        min-height: calc(100vh - 300px);
    }

    #page-1 {
        margin-top: 56px;
        min-height: calc(100vh - 56px);
        background-color: var(--primary);
    }

    #page-2 {
        min-height: calc(100vh - 56px);
        background-color: var(--accent);
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

    @media (max-width: 1000px) {
        #welcome-text {
        margin-top: 100px;
        min-height: calc(100vh - 300px);
        }

        #welcome-pic-list {
            margin-top: 0px;
        }

        .welcome-pic {
            rotate: 0deg !important;
            margin: 0px !important;
        }

    }
</style>