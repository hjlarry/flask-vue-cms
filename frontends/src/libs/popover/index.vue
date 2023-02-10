<template>
  <div class="relative" @mouseenter="onMouseEnter" @mouseleave="onMouseLeave">
    <!-- 悬浮目标 -->
    <div ref="targetRef">
      <slot name="target"></slot>
    </div>
    <!-- 浮层 -->
    <div
      class="absolute z-20 p-1 rounded border text-base bg-white"
      :style="positionStyle"
      v-show="isOpen"
      ref="dropdownRef"
    >
      <slot name="dropdown"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Prop {
  placement?: 'left' | 'left-bottom' | 'right' | 'right-bottom'
}

const props = withDefaults(defineProps<Prop>(), {
  placement: 'left-bottom'
})

const targetRef = ref<HTMLElement>()
const dropdownRef = ref<HTMLElement>()
const positionStyle = ref({
  left: '0',
  top: '0'
})

onMounted(() => {
  const targetWidth = targetRef.value?.offsetWidth
  const targetHeight = targetRef.value?.offsetHeight
  const dropdownWidth = dropdownRef.value?.offsetWidth
  switch (props.placement) {
    case 'left':
      positionStyle.value.top = '0'
      positionStyle.value.left = `-${dropdownWidth}px`
      break
    case 'left-bottom':
      positionStyle.value.top = `${targetHeight}px`
      positionStyle.value.left = `-${dropdownWidth}px`
      break
    case 'right':
      positionStyle.value.top = '0'
      positionStyle.value.left = `${targetWidth}px`
      break
    case 'right-bottom':
      positionStyle.value.top = `${targetHeight}px`
      positionStyle.value.left = `${targetWidth}px`
      break
  }
  isOpen.value = false
})
// 先让isOpen为true，才能在onMounted中获取到dropdownRef正确的宽度
const isOpen = ref(true)
// 控制延迟关闭
let timeout = 0
const DELAY_TIME = 100
const onMouseEnter = () => {
  isOpen.value = true
  // 再次触发时，清理延时装置
  if (timeout) {
    clearTimeout(timeout)
  }
}

const onMouseLeave = () => {
  timeout = setTimeout(() => {
    isOpen.value = false
    timeout = 0
  }, DELAY_TIME)
}
</script>

<style scoped></style>
