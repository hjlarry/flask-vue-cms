<template>
  <svg aria-hidden="true">
    <use :xlink:href="symbolId" :class="fillClass" :fill="color" />
  </svg>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  name: string
  color?: string
  fillClass?: string
}
const props = defineProps<Props>()
const symbolId = computed(() => `#icon-${props.name}`)
</script>
