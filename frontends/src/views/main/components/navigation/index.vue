<template>
  <mobileNavigationVue v-if="isMoibleDevice"></mobileNavigationVue>
  <pcNavigationVue v-else></pcNavigationVue>
</template>

<script setup lang="ts">
import { isMoibleDevice } from '@/utils/flexiable'
import mobileNavigationVue from './mobile/index.vue'
import pcNavigationVue from './pc/index.vue'
</script>

<style scoped></style>
