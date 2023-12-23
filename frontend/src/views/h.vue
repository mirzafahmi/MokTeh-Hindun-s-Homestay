<AppModal
    modalId="exampleModal"
    ariaLabel="exampleModalLabel"
    ariaHidden="true"
    title="Select Time of Check-in/out"
    confirmButtonText="Check Homestay Availability"
    @close="handleModalClose"
    @cancel="handleModalCancel"
    @confirm="handleModalConfirm"
>   
    <div class="row">
        <div class="col d-flex flex-column">
            <h6>Select Check-in time</h6>
            <vue-timepicker
                v-model="checkedIn"
                format="HH:mm"
                :minute-interval="30"
                :hour-range="allowedHourRange"
                :minute-range="allowedMinuteRange"
                close-on-complete
            >
            </vue-timepicker>
        </div>
        <div class="col d-flex flex-column">
            <h6>Select Check-out time</h6>
            <vue-timepicker
                v-model="checkedOut"
                format="HH:mm"
                :minute-interval="30"
                :hour-range="allowedHourRange"
                :minute-range="allowedMinuteRange"
                close-on-complete
                :confirmButtonClick="whatsappLink"
            >
            </vue-timepicker>
        </div>
    </div>
</AppModal>