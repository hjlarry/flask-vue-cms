<template>
  <div class="fixed top-0 left-0 z-50 w-full h-full bg-white">
    {{ data.id }}
  </div>
</template>

<script setup lang="ts">
defineProps<{ data: any }>()
</script>

<style scoped></style>
