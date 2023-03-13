<template>
  <el-icon><SvgIcon :icon="icon" /></el-icon>
  <span>{{ generateRouteTitle(title) }}</span>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon/index.vue'
import { generateRouteTitle } from '@/i18n'

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

<style scoped></style>
