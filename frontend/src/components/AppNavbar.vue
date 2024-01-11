<template>
  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <router-link 
      class="navbar-brand"
      to="/"
      >
      Mokteh Hindun™
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link 
            @click="closeDropdown"
            class="nav-link" 
            :class="{ active: isRoute('/') }" 
            to="/"
            >
              Home
            </router-link>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle custom-dropdown-link"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              :class="{ active: isDropdownActive(['/rumah_kayu', '/rumah_batu', '/rumah_kecik']) }"
            >
              Homestays List
            </a>
            <ul class="dropdown-menu">
              <li @click="closeDropdown">
                <router-link 
                class="dropdown-item" 
                to="/rumah_kayu"
                >
                  Rumah Kayu
                </router-link>
              </li>
              <li @click="closeDropdown">
                <router-link 
                class="dropdown-item" 
                to="/rumah_batu"
                >
                  Rumah Batu
                </router-link>
              </li>
              <li @click="closeDropdown">
                <router-link 
                class="dropdown-item" 
                to="/rumah_kecik"
                >
                  Rumah Kecik
                </router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <router-link 
            class="nav-link" 
            :class="{ active: isRoute('/visit') }"
            to="/visit"
            >
              Places To Visit
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>


<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isDropdownOpen = ref(false);

function isRoute(path) {
  return route.path === path;
}

function isDropdownActive(routes) {
  return routes.some((route) => isRoute(route));
}

function toggleDropdown() {
  isDropdownOpen.value = !isDropdownOpen.value;
}

function closeDropdown() {
  isDropdownOpen.value = false;
}
</script>


<style scoped>
nav {
  background-color: var(--primary);
  box-shadow: rgba(0, 0, 0, 0.45) 0px 20px 20px -20px;
}

.custom-dropdown-link {
  color: rgba(var(--bs-emphasis-color-rgb), 0.65);
}

.active {
  border-bottom: 1px solid black
}
</style>
