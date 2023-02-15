<template>
  <div class="h-screen">
    <headerVue />
    <mainVue />
    <floatVue />
  </div>
</template>

<script setup lang="ts">
import mainVue from './components/main.vue'
import headerVue from './components/header/index.vue'
import floatVue from './components/float.vue'
</script>

<style scoped></style>
