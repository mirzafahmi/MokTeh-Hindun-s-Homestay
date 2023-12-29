<template>
<div class="col-lg-4 col">
	<ul class="d-flex align-items-center justify-content-center">
		<li 
		class="booking-card" 
		:style="{ backgroundImage: 'url(' + props.houseImage + ')' }">
			<div class="book-container">
			<div class="content">
				<router-link 
				class="nav-link btn" 
				:to="props.houseUrl"
				>
					View Details
				</router-link>
			</div>
			</div>
			<div class="informations-container">
			<h2 class="title text-center">{{ props.houseName }}</h2>
			<p class="sub-title">{{ props.houseRecommendation }}</p>
			<p class="price">
				<svg class="icon" style="width:24px;height:24px" viewBox="0 0 24 24">
					<path fill="currentColor" d="M3,6H21V18H3V6M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9M7,8A2,2 0 0,1 5,10V14A2,2 0 0,1 7,16H17A2,2 0 0,1 19,14V10A2,2 0 0,1 17,8H7Z" />
				</svg>
				RM {{props.housePricing}} per night
			</p>
			<p class="price">
				<svg class="icon" id="Layer_1" style="enable-background:new 0 0 512 512;width:24px;height:24px" version="1.1" viewBox="0 0 512 512" width="512px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
					<path fill="currentColor" d="M256,111.9C256,111.9,256,111.9,256,111.9L256,111.9z"/>
					<path fill="currentColor" d="M349.2,334.8c-11.2-3.9-29.5-5.1-37.5-8.2c-5.6-2.2-14.5-4.5-17.3-8c-2.9-3.4-2.9-28.1-2.9-28.1s7-6.5,9.9-13.8    c2.9-7.3,4.8-27.1,4.8-27.1s0.6,0.2,1.5,0.2c2.1,0,5.9-1.4,7.7-10.6c2.2-11.3,6.4-17.2,5.3-25.5c-0.8-5.6-3.2-6.5-4.6-6.5    c-0.7,0-1.2,0.2-1.2,0.2s5.7-8.4,5.7-37c0-29.4-22.7-58.4-64.6-58.5c-42,0.1-64.6,29.1-64.6,58.5c0,28.5,5.7,37,5.7,37    s-0.5-0.2-1.2-0.2c-1.5,0-3.9,0.9-4.6,6.5c-1.1,8.3,3,14.3,5.3,25.5c1.8,9.2,5.6,10.6,7.7,10.6c0.9,0,1.5-0.2,1.5-0.2    s1.9,19.9,4.8,27.1c2.9,7.3,9.9,13.8,9.9,13.8s0,24.7-2.9,28.1c-2.9,3.4-11.7,5.8-17.3,8c-8,3.1-26.3,4.3-37.5,8.2    c-11.2,3.9-45.8,20.2-45.8,65.2H395C395,355,360.5,338.7,349.2,334.8z"/>
					<path fill="currentColor" d="M144.1,322c9-4.5,17.8-4.5,24.6-5.4c0,0,3.8-6.2-8.7-8.4c0,0-17.1-4.3-19.1-6.7c-2-2.4-0.8-15.7-0.8-15.7   s23.9-0.8,33.4-9.2c-15.5-23.2-7.2-50.3-10.4-75.6C160,175.8,144.9,160,116,160c-0.1,0,0,0-1,0v0c-28,0-42.4,15.8-45.6,41.1   c-3.2,25.3,6,55.4-9.9,75.7c8.9,7.9,30.9,8.3,33.4,8.3c0.2,0,0.2,0,0.2,0c0,0,0.1-0.1,0.1-0.1s1,14.2-1,16.6   c-2,2.4-7.9,4.6-11.9,5.5c-8.8,1.9-18.1,5-25.8,7.7C46.8,317.4,32,333,32,352h80.2C114.4,344,129.5,329.4,144.1,322z"/>
					<path fill="currentColor" d="M399.8,352H480c0-19-14.8-34.6-22.5-37.3c-7.7-2.7-17.1-5.8-25.8-7.7c-4.1-0.9-9.9-3.1-11.9-5.5c-2-2.4-1-16.6-1-16.6   s0.1,0.1,0.1,0.1c0,0,0.1,0,0.2,0c2.5,0,24.6-0.3,33.5-8.3c-15.9-20.3-6.8-50.4-10-75.7C439.4,175.8,425,160,397,160v0   c-1,0-1,0-1,0c-28.9,0-44.1,15.8-47.2,41.1c-3.2,25.3,5.1,52.4-10.4,75.6c9.5,8.4,33.4,9.2,33.4,9.2s1.2,13.3-0.8,15.7   s-19.1,6.7-19.1,6.7c-12.5,2.2-8.7,8.4-8.7,8.4c6.8,0.9,15.7,0.9,24.6,5.4C382.5,329.4,397.6,344,399.8,352z"/>
				</svg>
				From {{props.housePax}} pax
			</p>
			<div class="specs">
				<div class="row">
					<p class="price col">
						<svg class="icon" data-name="Layer 1" id="Layer_1" style="width:24px;height:24px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
							<path fill="currentColor" d="M43.93,307.53V423.77H74.7V347.55H437.3v76.22h30.77V307.53a38.67,38.67,0,0,0-38.67-38.67H82.6A38.67,38.67,0,0,0,43.93,307.53Z"/>
							<path fill="currentColor" d="M82.6,244h34.71V174.23a10.55,10.55,0,0,1,10.54-10.55H234.9a10.55,10.55,0,0,1,10.54,10.55V244h21.12V174.23a10.56,10.56,0,0,1,10.55-10.55h107a10.56,10.56,0,0,1,10.55,10.55V244H429.4a62.35,62.35,0,0,1,7.9.8V139.24a51,51,0,0,0-51-51H125.7a51,51,0,0,0-51,51V244.77A62.35,62.35,0,0,1,82.6,244Z"/>
						</svg>
						{{ props.houseBedroom }}
					</p>
					<p class="price col">
						<svg class="icon" style="width:24px;height:24px" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
							<path fill="currentColor" d="M288 384c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C320 398.3 305.7 384 288 384zM416 256c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C448 270.3 433.7 256 416 256zM480 192c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C512 206.3 497.7 192 480 192zM288 320c0-17.67-14.33-32-32-32s-32 14.33-32 32c0 17.67 14.33 32 32 32S288 337.7 288 320zM320 224c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C352 238.3 337.7 224 320 224zM384 224c17.67 0 32-14.33 32-32c0-17.67-14.33-32-32-32s-32 14.33-32 32C352 209.7 366.3 224 384 224zM352 320c-17.67 0-32 14.33-32 32c0 17.67 14.33 32 32 32s32-14.33 32-32C384 334.3 369.7 320 352 320zM347.3 91.31l-11.31-11.31c-6.248-6.248-16.38-6.248-22.63 0l-6.631 6.631c-35.15-26.29-81.81-29.16-119.6-8.779L170.5 61.25C132.2 22.95 63.65 18.33 21.98 71.16C7.027 90.11 0 114.3 0 138.4V464C0 472.8 7.164 480 16 480h32C56.84 480 64 472.8 64 464V131.9c0-19.78 16.09-35.87 35.88-35.87c9.438 0 18.69 3.828 25.38 10.5l16.61 16.61C121.5 160.9 124.3 207.6 150.6 242.7L144 249.4c-6.248 6.248-6.248 16.38 0 22.63l11.31 11.31c6.248 6.25 16.38 6.25 22.63 0l169.4-169.4C353.6 107.7 353.6 97.56 347.3 91.31z"/>
						</svg>
						{{ props.houseBathroom }}
					</p>
				</div>
				<div class="row">
					<div class="price col">
						<svg class="icon" style="width:24px;height:24px" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
							<path fill="currentColor" d="M55,23h0a3.511,3.511,0,0,0-2.963-3.467L36,17H28L11.963,19.532A3.511,3.511,0,0,0,9,23H9" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M25,1c0,1.333-2,1.333-2,2.667S25,5,25,6.333,23,7.667,23,9" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M33,1c0,1.333-2,1.333-2,2.667S33,5,33,6.333,31,7.667,31,9" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M41,1c0,1.333-2,1.333-2,2.667S41,5,41,6.333,39,7.667,39,9" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<polyline points="60 60 63 60 63 63 1 63 1 60 4 60" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="6" x2="58" y1="60" y2="60"/>
							<path fill="currentColor" d="M36,55a4,4,0,0,1-8,0c0-2.209,3-8,4-8S36,52.791,36,55Z" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M52,55a4,4,0,0,1-4,4c-2.209,0-4-.791-4-3s5-9,6-9S52,52.791,52,55Z" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M12,55a4,4,0,0,0,4,4c2.209,0,4-.791,4-3s-5-9-6-9S12,52.791,12,55Z" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M51,57a4,4,0,0,0,4-4V23H9V53a4,4,0,0,0,4,4" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="35" x2="44" y1="57" y2="57"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="20" x2="29" y1="57" y2="57"/>
							<path fill="currentColor" d="M58,27h4a1,1,0,0,1,1,1v2a1,1,0,0,1-1,1H55V27" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M60,31l-1.447,2.894A2,2,0,0,1,56.764,35H55" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M6,27H2a1,1,0,0,0-1,1v2a1,1,0,0,0,1,1H9V27" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<path fill="currentColor" d="M4,31l1.447,2.894A2,2,0,0,0,7.236,35H9" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="12" x2="9" y1="27" y2="27"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="16" x2="14" y1="27" y2="27"/>
							<line style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px" x1="55" x2="18" y1="27" y2="27"/>
							<path fill="currentColor" d="M32,11h0a4,4,0,0,1,4,4v2a0,0,0,0,1,0,0H28a0,0,0,0,1,0,0V15A4,4,0,0,1,32,11Z" style="fill:none;stroke:#0a4870;stroke-linejoin:round;stroke-width:2px"/>
						</svg>
						<div>
							<i v-if="houseKitchen" class="fa-solid fa-check"></i>
							<i v-else class="fa-solid fa-xmark"></i>
						</div>
					</div>
					<div class="price col">
						<svg class="icon" style="width:24px;height:24px" enable-background="new 0 0 64 64" id="Layer_1" version="1.1" viewBox="0 0 64 64" width="64px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
							<path fill="currentColor" d="M50.219,0.163H13.782c-2.459,0-4.454,2.138-4.454,4.775v16.559h45.343V4.938   C54.672,2.301,52.678,0.163,50.219,0.163z M19.936,14.043c0,0.771-0.691,1.395-1.545,1.395c-0.853,0-1.544-0.624-1.544-1.395V7.784   c0-0.771,0.691-1.395,1.544-1.395c0.854,0,1.545,0.624,1.545,1.395V14.043z"/>
							<path fill="currentColor" d="M9.329,59.727c0,2.271,1.995,4.111,4.454,4.111h36.438c2.457,0,4.451-1.84,4.451-4.111V24.593H9.329V59.727   z M16.847,34.061c0-1.02,0.691-1.847,1.544-1.847c0.854,0,1.545,0.827,1.545,1.847v8.287c0,1.02-0.691,1.846-1.545,1.846   c-0.853,0-1.544-0.826-1.544-1.846V34.061z"/>
						</svg>
						<div>
							<i v-if="houseFridge" class="fa-solid fa-check"></i>
							<i v-else class="fa-solid fa-xmark"></i>
						</div>
					</div>
				</div>
				<div class="row">
					<div class="price col">
						<svg class="icon" style="width:24px;height:24px" data-name="Layer 1" id="Layer_1" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
							<path fill="currentColor" d="M27,4.87C26.64,3.58,25.72,3,24,3H6V3.5A7.61,7.61,0,0,0,7.47,7.12l-0.11.65A78,78,0,0,0,6,20.5V23a2,2,0,0,0,2,2H23a2,2,0,0,0,2-2V20.5c0-.49,0-1.07,0-1.7l1.31-.88A3.67,3.67,0,0,0,28,15.25,48.56,48.56,0,0,0,27,4.87ZM8.35,7.93L8.53,6.87,8.4,6.7A8.33,8.33,0,0,1,7.06,4H21.47c0.92,0.55,2.46,8.5,2.53,16H17V7.5a1.5,1.5,0,0,0-3,0V20H7A79.65,79.65,0,0,1,8.35,7.93ZM16,7.5v13a0.5,0.5,0,0,1-1,0V7.5A0.5,0.5,0,0,1,16,7.5ZM23,24H8a1,1,0,0,1-1-1V21h7.09a1.49,1.49,0,0,0,2.82,0H24v2A1,1,0,0,1,23,24Zm2.73-6.92-0.81.54c-0.24-4.56-1-11.15-2.3-13.62H24c1.59,0,1.86.53,2,1.13a47.35,47.35,0,0,1,1,10.12A2.76,2.76,0,0,1,25.73,17.08Z"/>
							<path fill="currentColor" d="M23,26H8a2,2,0,0,0-2,2v1H25V28A2,2,0,0,0,23,26ZM7,28a1,1,0,0,1,1-1H23a1,1,0,0,1,1,1H7Z"/>
						</svg>
						<div>
							<i v-if="houseKettle" class="fa-solid fa-check"></i>
							<i v-else class="fa-solid fa-xmark"></i>
						</div>
					</div>
					<div class="price col">
						<svg class="icon" style="width:24px;height:24px" data-name="Layer 1" id="Layer_1" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
							<path fill="currentColor" class="cls-1" d="M15.73,4.36L13.36,1l-7,21.89,2.82,1a1.91,1.91,0,0,1,1.48,2.34L9.3,31h13l0.15-.25A22.05,22.05,0,0,0,25,21C25,13.22,22.23,8.24,15.73,4.36ZM7.62,22.26l6.09-19,1.13,1.59L9,22.76ZM21.71,30H10.63l1-3.52A2.77,2.77,0,0,0,10,23.14L15.67,5.5C21.49,9.14,24,13.8,24,21A21.19,21.19,0,0,1,21.71,30Z"/>
							<rect fill="currentColor" class="cls-1" height="1" transform="translate(-9.9 32.49) rotate(-73.14)" width="5.33" x="14.28" y="22.42"/>
							<path fill="currentColor" class="cls-1" d="M17.65,12.91l-0.58-.45L12.1,29h8.24l0.13-.31A20.07,20.07,0,0,0,22,22C22,17.77,20.9,15.47,17.65,12.91Zm2,15.09H13.44L17.6,14.17C20.16,16.34,21,18.34,21,22A18.49,18.49,0,0,1,19.66,28Z"/>
						</svg>
						<div>
							<i v-if="houseIron" class="fa-solid fa-check"></i>
							<i v-else class="fa-solid fa-xmark"></i>
						</div>
					</div>
				</div>

			</div>
			<div class="more-information">
				<div class="info-and-date-container">
				<div class="box info">
					<svg class="icon" style="width:24px;height:24px" viewBox="0 0 24 24">
						<path fill="currentColor" d="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" />
					</svg>
					<p>Centre Pompidou at PARIS</p>
				</div>
				<div class="box date">
					<svg class="icon" style="width:24px;height:24px" viewBox="0 0 24 24">
						<path fill="currentColor" d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z" />
					</svg>
					<p>From October to December 2020</p>
				</div>
				</div>
				<p class="disclaimer">Lorem ipsum </p>
				</div>
			</div>
		</li>
	</ul>
</div>
</template>

<script setup>
import { defineProps } from 'vue';

const props = defineProps([
	'houseUrl',
	'houseImage',
	'houseName',
	'houseRecommendation',
	'housePax',
	'housePricing',
	'houseBedroom',
	'houseBathroom',
	'houseKitchen',
	'houseFridge',
	'houseKettle',
	'houseIron'
]);
</script>

<style scoped>
* {
	 margin: 0;
	 padding: 0;
	 font-family: 'Sofia', sans-serif;
}
 h2 {
	 color: #0a4870;
	 font-weight: 500;
}
 ul {
	 display: flex;
	 flex-wrap: wrap;
	 list-style: none;
	 padding: 0;
}
 ul .booking-card {
	 position: relative;
	 height: 750px;
	 width: 300px;
	 margin-bottom: 20px;
	 display: flex;
	 flex: 0 0 300px;
	 flex-direction: column;
	 -webkit-border-radius: 10px;
	 -moz-border-radius: 10px;
	 border-radius: 10px;
	 overflow: hidden;
	 background-position: center center;
	 background-size: cover;
	 text-align: center;
	 color: #0a4870;
	 transition: 0.3s;
}
 ul .booking-card::before {
	 content: '';
	 position: absolute;
	 top: 0;
	 left: 0;
	 right: 0;
	 bottom: 0;
	 background: rgba(10, 72, 112, 0);
	 transition: 0.3s;
}
 ul .booking-card .book-container {
	 height: 200px;
}
 ul .booking-card .book-container .content {
	 position: relative;
	 opacity: 0;
	 display: flex;
	 align-items: center;
	 justify-content: center;
	 height: 100%;
	 width: 100%;
	 transform: translateY(-200px);
	 transition: 0.3s;
}
 ul .booking-card .book-container .content .btn {
	 border: 3px solid white;
	 padding: 10px 15px;
	 background: none;
	 text-transform: uppercase;
	 font-weight: bold;
	 font-size: 1.3em;
	 color: white;
	 cursor: pointer;
	 transition: 0.3s;
}
 ul .booking-card .book-container .content .btn:hover {
	 background: white;
	 border: 0px solid white;
	 color: #0a4870;
}
 ul .booking-card .informations-container {
	 flex: 1 0 auto;
	 padding: 20px;
	 background: #f0f0f0;
	 transform: translateY(300px);
	 transition: 0.3s;
}
 ul .booking-card .informations-container .title {
	 position: relative;
	 padding-bottom: 10px;
	 margin-bottom: 10px;
	 font-weight: bold;
	 font-size: 1.2em;
}
 ul .booking-card .informations-container .title::after {
	 content: '';
	 position: absolute;
	 bottom: 0;
	 left: 0;
	 right: 0;
	 height: 3px;
	 width: 50px;
	 margin: auto;
	 background: #0a4870;
}
 ul .booking-card .informations-container .price {
	 display: flex;
	 align-items: center;
	 justify-content: center;
	 margin-top: 10px;
}
 ul .booking-card .informations-container .price .icon {
	 margin: 0px 15px;
}
 ul .booking-card .informations-container .more-information {
	 opacity: 0;
	 transition: 0.3s;
}
 ul .booking-card .informations-container .more-information .info-and-date-container {
	 display: flex;
}
 ul .booking-card .informations-container .more-information .info-and-date-container .box {
	 flex: 1 0;
	 padding: 15px;
	 margin-top: 20px;
	 -webkit-border-radius: 10px;
	 -moz-border-radius: 10px;
	 border-radius: 10px;
	 background: white;
	 font-weight: bold;
	 font-size: 0.9em;
}
 ul .booking-card .informations-container .more-information .info-and-date-container .box .icon {
	 margin-bottom: 5px;
}
 ul .booking-card .informations-container .more-information .info-and-date-container .box.info {
	 color: #ec992c;
	 margin-right: 10px;
}
 ul .booking-card .informations-container .more-information .disclaimer {
	 margin-top: 20px;
	 font-size: 0.8em;
	 color: #7d7d7d;
}
 ul .booking-card:hover::before {
	 background: rgba(10, 72, 112, 0.6);
}
 ul .booking-card:hover .book-container .content {
	 opacity: 1;
	 transform: translateY(0px);
}
 ul .booking-card:hover .informations-container {
	 transform: translateY(0px);
}
 ul .booking-card:hover .informations-container .more-information {
	 opacity: 1;
}

hr {
	margin: 5px 0px
}

@media (min-width: 1400px) {
	ul .booking-card {
		flex: 0 0 350px;
	}
}
</style>