<GMapMap
    :center="houseDetails.coordinate"
    :zoom= "17"
    :options="{ mapTypeId: 'roadmap' }"
    style="width: 100%; height: 532px"
    @map-loaded="handleMapLoaded"
>
    <GMapCluster>
        <GMapMarker
            :position="originMarker.position"
        >
            <GMapInfoWindow 
                :position="originMarker.position" 
                :options="{ pixelOffset: { width: 0, height: -10 } }"
                @click="handleMarkerClick(originMarker)"
            >
                <h6>Go to from here:</h6>
                <div
                    class="direction-box"
                    v-for="(m, index) in markers.slice(1)"
                    :key="index"
                    @click="() => handleDirectionLinkClick(m.position)"
                >
                {{ m.legend }}
            </div>
            </GMapInfoWindow>
        </GMapMarker>
        <GMapMarker
            :key="index"
            v-for="(m, index) in markers.slice(1)"
            :position="m.position"
            @click="handleMarkerClick(m)"
        />
    </GMapCluster>
    <GMapPolyline :path="getPaths" ref="polyline" />
</GMapMap>