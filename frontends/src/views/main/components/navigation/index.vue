<template>
  <mobileNavigationVue v-if="isMoibleDevice"></mobileNavigationVue>
</template>

<script setup lang="ts">
import { isMoibleDevice } from '@/utils/flexiable'
</script>

<style scoped></style>
