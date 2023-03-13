<template>
  <div>
    <Transition name="fade">
      <div
        v-if="isOpen"
        class="w-screen h-screen fixed top-0 left-0 z-30 bg-zinc-900/80"
        @click="close"
      ></div>
    </Transition>
    <Transition name="up">
      <div
        v-if="isOpen"
        class="fixed w-[80%] top-1/3 left-1/2 -translate-x-1/2 z-40 px-2 py-1.5 rounded-sm bg-white dark:bg-zinc-800 border dark:border-zinc-600 xl:w-[35%]"
      >
        <div class="text-lg font-bold text-zinc-900 dark:text-zinc-200">
          {{ title }}
        </div>
        <div class="text-base text-zinc-900 dark:text-zinc-200 my-2">
          {{ content }}
        </div>
        <div class="flex justify-end">
          <m-button type="info" class="mr-2" @click="onCancelClick">{{
            cancelText
          }}</m-button>
          <m-button type="primary" @click="onOkClick">{{ okText }}</m-button>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import mButton from '@/libs/button/index.vue'

interface Props {
  title?: string
  content?: string
  okText: string
  cancelText: string
  okHandler?: () => void
  cancelHandler?: () => void
  closeHandler?: () => void
}

const props = defineProps<Props>()

const isOpen = ref(false)

onMounted(() => {
  isOpen.value = true
})

const close = () => {
  isOpen.value = false
  if (props.closeHandler) {
    props.closeHandler()
  }
}

const onCancelClick = () => {
  if (props.cancelHandler) {
    props.cancelHandler()
  }
  close()
}

const onOkClick = () => {
  if (props.okHandler) {
    props.okHandler()
  }
  close()
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 500ms;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.up-enter-active,
.up-leave-active {
  transition: all 500ms;
}

.up-enter-from,
.up-leave-to {
  opacity: 0;
  transform: translate3d(-50%, 100px, 0);
}
</style>
