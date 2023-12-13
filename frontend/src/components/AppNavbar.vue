<script setup>
import { ref, onMounted } from 'vue';
import Axios from 'axios';

const responseData = ref(null);

onMounted(async () => {
  try {
    const path = 'http://127.0.0.1:5000/';
    const res = await Axios.get(path);
    responseData.value = res.data;
    console.log(res.data)
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="#">Mokteh Hindun™</a>
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
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Homestays List
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Place to Visit</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact Us</a>
          </li>  
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>

nav {
  background-color: var(--primary);
  box-shadow: rgba(0, 0, 0, 0.45) 0px 20px 20px -20px;
}

</style>
