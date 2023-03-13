<template>
  <Transition name="down" @after-leave="props.onClose">
    <div
      v-show="isVisiable"
      class="fixed min-w-[420px] top-[20px] left-[50%] -translate-x-1/2 z-50 flex items-center rounded-sm px-3 py-1.5 border cursor-pointer"
      :class="messageTypes[props.type].containerClass"
    >
      <m-svg-icon
        :name="messageTypes[props.type].icon"
        :fillClass="messageTypes[props.type].fillClass"
        class="w-1.5 h-1.5"
      />
      <span
        class="text-sm ml-1.5"
        :class="messageTypes[props.type].textClass"
        >{{ props.content }}</span
      >
    </div>
  </Transition>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

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
    fillClass: 'fill-yellow-500',
    textClass: 'text-yellow-500',
    containerClass:
      'bg-yellow-100 border-yellow-200 hover:shadow-lg hover:shadow-yellow-100'
  },
  error: {
    icon: 'error',
    fillClass: 'fill-red-500',
    textClass: 'text-red-500',
    containerClass:
      'bg-red-100 border-red-200 hover:shadow-lg hover:shadow-red-100'
  }
}

interface Props {
  type: keyof typeof messageTypes
  content: string
  duration: number
  onClose: () => void
}
const props = defineProps<Props>()
const isVisiable = ref(false)
onMounted(() => {
  isVisiable.value = true
  setTimeout(() => {
    isVisiable.value = false
    props.onClose()
  }, props.duration)
})
</script>

<style scoped>
.down-enter-active,
.down-leave-active {
  transition: all 0.5s ease;
}

.down-enter-from,
.down-leave-to {
  transform: translate3d(-50%, -100px, 0);
}
</style>
