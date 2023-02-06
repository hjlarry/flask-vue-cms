<template>
  <div>
    <ul>
      <li v-for="item in data" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
defineProps({
  data: {
    type: Array,
    required: true
  }
})
</script>

<style scoped></style>
