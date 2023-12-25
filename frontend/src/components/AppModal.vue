<template>
    <div 
        class="modal fade" 
        :id="modalId" 
        tabindex="-1" 
        :aria-labelledby="ariaLabel" 
        :aria-hidden="ariaHidden"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" :id="ariaLabel">{{ title }}</h1>
            <button 
                type="button" 
                class="btn-close" 
                data-bs-dismiss="modal"
                aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <slot></slot>
          </div>
          <div class="modal-footer">
            <button 
                type="button" 
                class="btn btn-secondary" 
                data-bs-dismiss="modal"
            >
                Cancel
            </button>
            <a
                class="btn btn-primary"
                :href="confirmButtonClick"
                target="_blank"
                rel="noopener noreferrer"
            >
                {{ confirmButtonText }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(
    [
        'modalId',
        'ariaLabel',
        'ariaHidden',
        'title',
        'confirmButtonText',
        'confirmButtonClick'
    ]
);
</script>

<style scoped>
#exampleModal {
background-color: transparent;
}

button {
    color: white;
}
</style>
  