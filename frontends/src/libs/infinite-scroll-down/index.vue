<template>
  <div>
    <slot></slot>
    <div ref="bottomEl">
      <m-svg-icon
        v-if="isLoading"
        name="infinite-load"
        class="mx-auto h-6 animate-spin"
      />
      <p v-if="isFinished" class="text-center text-lg">没有更多数据了</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useIntersectionObserver, useVModel } from '@vueuse/core'

const props = defineProps<{ modelValue: boolean; isFinished: boolean }>()
const emits = defineEmits(['update:modelValue', 'loadMore'])

const isLoading = useVModel(props)
const bottomEl = ref<HTMLElement>()
const currentIsBottom = ref(false)

useIntersectionObserver(bottomEl, ([{ isIntersecting }]) => {
  currentIsBottom.value = isIntersecting
  if (currentIsBottom.value && !isLoading.value && !props.isFinished) {
    isLoading.value = true
    emits('loadMore')
  }
})
</script>

<style scoped></style>
