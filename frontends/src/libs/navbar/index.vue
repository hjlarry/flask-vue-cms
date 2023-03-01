<template>
  <div
    class="flex items-center h-5 border-b bg-white dark:bg-zinc-800 border-b-zinc-200 dark:border-b-zinc-700"
    :class="sticky ? 'sticky top-0 left-0 z-10' : 'relative'"
  >
    <div class="w-5 flex justify-center" @click="onBackClick">
      <m-svg-icon
        name="back"
        class="h-2 w-2"
        fillClass="fill-zinc-900 dark:fill-zinc-200"
      ></m-svg-icon>
    </div>
    <div
      class="flex-1 text-center text-base font-bold text-zinc-900 dark:text-zinc-200"
    >
      <slot></slot>
    </div>

    <div class="w-5 flex items-center justify-center" @click="onRightClick">
      <slot name="right"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const props = defineProps<{ sticky?: boolean; clickRight?: Function }>()
const router = useRouter()
const onBackClick = () => {
  router.back()
}
const onRightClick = () => {
  if (props.clickRight) props.clickRight()
}
</script>

<style scoped></style>
