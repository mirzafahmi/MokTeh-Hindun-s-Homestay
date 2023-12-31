import { defineStore } from 'pinia';
import Axios from 'axios';

export const useHouseStore = defineStore({
    id: 'house',
    state: () => ({
      houseDetails: null,
    }),
    actions: {
      async fetchHouseDetails(path) {
        try {
          const res = await Axios.get(path);
          this.houseDetails = res.data.house_details;
        } catch (error) {
          console.error(error);
        }
      },
    },
  });

export const useServerStore = defineStore({
  id: 'server',
  state: () => ({
    backEndServer: 'https://homestay-backend-kali.onrender.com/',
  }),
});