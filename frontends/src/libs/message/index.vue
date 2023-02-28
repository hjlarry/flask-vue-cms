<template>
  <div
    class="fixed min-w-[420px] top-[20px] left-[50%] -translate-x-1/2 z-50 flex items-center rounded-sm px-3 py-1.5 border cursor-pointer"
    :class="messageTypes[props.type].containerClass"
  >
    <m-svg-icon :name="messageTypes[props.type].icon" class="w-1.5 h-1.5" />
    <span class="text-sm">{{ props.content }}</span>
  </div>
</template>

<script setup lang="ts">
import mSvgIcon from '@/libs/svg-icon/index.vue'

const messageTypes = {
  success: {
    icon: 'success',
    fillClass: 'fill-green-500',
    textClass: 'text-green-500',
    containerClass:
      'bg-green-100 border-green-200 hover:shadow-lg hover:shadow-green-100'
  },
  warn: {
    icon: 'warn',
    fillClass: 'fill-green-500',
    textClass: 'text-green-500',
    containerClass:
      'bg-green-100 border-green-200 hover:shadow-lg hover:shadow-green-100'
  },
  error: {
    icon: 'error',
    fillClass: 'fill-green-500',
    textClass: 'text-green-500',
    containerClass:
      'bg-green-100 border-green-200 hover:shadow-lg hover:shadow-green-100'
  }
}

interface Props {
  type: keyof typeof messageTypes
  content: string
  duration: number
  onClose: () => void
}
const props = defineProps<Props>()
</script>

<style scoped></style>
