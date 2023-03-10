<template>
  <div class="bg-zinc-200 h-full xl:py-2">
    <m-navbar :sticky="true" v-if="isMobileDevice">精选会员</m-navbar>
  </div>
</template>

<script setup lang="ts">
import { isMobileDevice } from '@/utils/flexiable'
</script>

<style scoped></style>
