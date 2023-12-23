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
              <li>
                <router-link 
                class="dropdown-item" 
                to="/rumah_kayu"
                >
                  Rumah Kayu
                </router-link>
              </li>
              <li>
                <router-link 
                class="dropdown-item" 
                to="/rumah_batu"
                >
                  Rumah Batu
                </router-link>
              </li>
              <li>
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
              Visit
            </router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact Us</a>
          </li>  
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();

function isRoute(path) {
  return route.path === path;
}

function isDropdownActive(routes) {
  return routes.some((route) => isRoute(route));
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

</style>
