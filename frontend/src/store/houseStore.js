import { defineStore } from 'pinia';
import Axios from 'axios';

export const useHouseStore = defineStore({
    id: 'house',
    state: () => ({
      houseDetails: null,
    }),
    actions: {
      async fetchHouseDetails() {
        try {
          const path = 'http://192.168.0.142:5000';
          const res = await Axios.get(path);
          this.houseDetails = res.data.house_details;
        } catch (error) {
          console.error(error);
        }
      },
    },
  });
