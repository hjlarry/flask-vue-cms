<template>
  <Teleport to="body">
    <Transition name="fade">
      <div
        v-if="isOpen"
        @click="isOpen = false"
        class="w-screen h-screen fixed top-0 left-0 z-30 bg-zinc-900/80"
      ></div>
    </Transition>

    <Transition name="popup-down-up">
      <div
        class="fixed bottom-0 w-screen bg-white dark:bg-zinc-800 z-40"
        v-if="isOpen"
      >
        <slot></slot>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { useScrollLock, useVModel } from '@vueuse/core'
import { watch } from 'vue'

const props = defineProps<{
  modelValue: boolean
}>()

const isOpen = useVModel(props)
const isLocked = useScrollLock(document.body)
watch(
  isOpen,
  (val) => {
    isLocked.value = val
  },
  { immediate: true }
)
</script>

<style scoped>
.fade-enter-active {
  transition: all 0.3s;
}

.fade-leave-active {
  transition: all 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.popup-down-up-enter-active {
  transition: all 0.3s;
}

.popup-down-up-leave-active {
  transition: all 0.3s;
}

.popup-down-up-enter-from,
.popup-down-up-leave-to {
  transform: translateY(100%);
}
</style>
