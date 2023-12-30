<template>
    <div id="container">
        <div id="map"></div>
        <div id="markerList">
            <h3 class="title custom-margin">Visit Here:</h3>
            <ul v-if="markerOptionsArray">
                <li 
                    class="sub-title"
                    v-for="(marker, index) in markerOptionsArray.slice(1)" 
                    :key="index" 
                    :class="{ 'active-title': marker.id === activeMarker }"
                    @click="calculateAndDisplayRoute(marker.id, marker.position)">
                    {{ marker.title }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, defineProps } from 'vue';

const transformName = (name) => {
  return name.replace(/_/g, ' ').replace(/\b\w/g, (match) => match.toUpperCase());
};

const props = defineProps(
    [
        'houseDetails',
        'markerId'
    ]
);
const map = ref(null);
const markers = ref(null);
let originMarker = ref({
    id: 1,
    position: { lat: 0, lng: 0 },
    title: transformName(props.houseDetails.name),
});

const directionsService = ref(null);
const directionsRenderer = ref(null);
const activeMarker = ref(null);

const markerOptionsArray = [
    originMarker.value,
    { id: 2, position: { lat: 5.256772150894725, lng: 103.13298678885047 }, title: 'Nasi Dagang Atas Tol' },
    { id: 3, position: { lat: 5.31875215629569, lng: 103.10290529383204 }, title: 'Muzium Terengganu' },
    { id: 4, position: { lat: 5.339704495910074, lng: 103.14508055006151 }, title: 'Jabatan Angkat Kuala Terengganu' },
    { id: 5, position: { lat: 5.336807545997662, lng: 103.1367742544134 }, title: 'Pasar Payang' },
];

onMounted(async () => {

    originMarker.value.position = props.houseDetails.coordinate;

    const mapOptions = {
        center: originMarker.value.position,
        zoom: 17,
        mapTypeId: 'roadmap', 
        mapTypeControl: true, 
        mapTypeControlOptions: {
        style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
        position: google.maps.ControlPosition.TOP_LEFT,
        },
    };

    map.value = new google.maps.Map(document.getElementById('map'), mapOptions);

    directionsService.value = new google.maps.DirectionsService();
    directionsRenderer.value = new google.maps.DirectionsRenderer({
        map: map.value,
        polylineOptions: {
            strokeColor: 'red',
            strokeWeight: 8,
        },
    });

    markers.value = markerOptionsArray.map(options => {
        const marker = new google.maps.Marker({
            position: options.position,
            map: map.value,
        });

        const infoWindow = new google.maps.InfoWindow({
            content: `<div>${options.title}</div>`,
        });

        marker.addListener('click', () => {
        
        calculateAndDisplayRoute(options.id, options.position);
        });

        marker.setMap(map.value);
        return marker;
    });

    if (props.markerId) {
        const selectedMarker = markerOptionsArray.find(marker => marker.id.toString() === props.markerId);
        calculateAndDisplayRoute(selectedMarker.id, selectedMarker.position)
        const windowWidth = window.innerWidth;

        if (windowWidth >= 992) {
            // Larger screens: Scroll to the bottom
            window.scrollTo(0, document.body.scrollHeight);
        } else {
            // Smaller screens: Scroll to a specific height from the bottom
            const specificHeight = 1300; // Set your specific height value
            window.scrollTo(0, document.body.scrollHeight - specificHeight);
        }
    }
});

// Create a global info window variable
let infoWindow = null;

function calculateAndDisplayRoute(index, destination) {
  const request = {
    origin: originMarker.value.position,
    destination: destination,
    travelMode: google.maps.TravelMode.DRIVING,
  };
    activeMarker.value = index;
  directionsService.value.route(request, (result, status) => {
    if (status === 'OK') {
      // Set new directions
      directionsRenderer.value.setDirections(result);

      const route = result.routes[0];

      if (route) {
        const path = route.overview_path;

        // Calculate the midpoint index
        const midpointIndex = Math.floor(path.length / 2);

        // Create or update the info window
        if (!infoWindow) {
          infoWindow = new google.maps.InfoWindow();
        }

        // Set the content dynamically
        infoWindow.setContent(getDirectionsInfoContent(route));

        // Position the info window at the midpoint
        infoWindow.setPosition(path[midpointIndex]);

        // Open the info window on the map
        infoWindow.open(map.value);
      }
    } else {
      console.error('Directions request failed due to ' + status);
    }
  });
}

// Function to get the content for the info window
function getDirectionsInfoContent(route) {
  // Customize this based on your needs
  const distance = route.legs[0].distance.text;
  const duration = route.legs[0].duration.text;

    return `
        <div class="distance-details p-1 overflow-hidden">
            <strong>Distance:</strong> ${distance}
            <br>
            <strong>Duration:</strong> ${duration}
        </div>
        `;
}
</script>
    
<style scoped>
#container {
    position: relative;
    width: 100%;
    height: 100%;
}

.title {
    font-size: 23px;
    padding: 3px
}

.sub-title {
    font-size: 11px;
}

#map {
    width: 100%;
    min-height: 532px;
}

#markerList {
    position: absolute;
    top: 60px;
    right: 10px;
    max-width: 40%;
    background-color: white;
    padding: 10px;
    border-radius: 5px;
    z-index: 1000;
}

#markerList h2 {
    text-align: center;
    margin-bottom: 10px;
}

#markerList ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

#markerList li {
    cursor: pointer;
    margin: 5px;
    padding: 5px;
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.distance-details {
    padding: 5px;
}

.active-title {
    background-color: rgb(7, 238, 7) !important;
    color: black;
}

@media (max-width: 1200px) {
    #markerList {
        max-width: 50%;
        padding: 3px;
    }
    .title {
        font-size: 23px;
    }

    .sub-title {
        font-size: 11px;
    }
}

@media (max-width: 992px) {
    #markerList {
        max-width: 50%;
        padding: 5px;
    }
    .title {
        font-size: 25px;
    }

    .sub-title {
        font-size: 12px;
    }
}

@media (max-width: 768px) {
    #markerList {
        max-width: 50%;
        padding: 3px;
    }
    .title {
        font-size: 22px;
    }

    .sub-title {
        font-size: 10px;
    }
}

@media (max-width: 576px) {
    #markerList {
        max-width: 35%;
        padding: 3px;
    }
    .title {
        font-size: 18px;
    }

    .sub-title {
        font-size: 9px;
    }

}


</style>
      