<template>
  <mobileNavigationVue v-if="isMobileDevice"></mobileNavigationVue>
  <pcNavigationVue v-else></pcNavigationVue>
</template>

<script setup lang="ts">
import { isMobileDevice } from '@/utils/flexiable'
import mobileNavigationVue from './mobile/index.vue'
import pcNavigationVue from './pc/index.vue'
</script>

<style scoped></style>
