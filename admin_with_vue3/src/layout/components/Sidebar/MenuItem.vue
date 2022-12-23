<template>
  <svg-icon :icon='icon' />
  <span>{{ title }}</span>
</template>

<script setup>
import { defineProps } from 'vue'
import SvgIcon from '@/components/SvgIcon/index.vue'

defineProps({
  title: {
    type: String,
    required: true
  },
  icon: {
    type: String
  }
})
</script>

<style scoped>

</style>
