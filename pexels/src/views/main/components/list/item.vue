<template>
  <div class="bg-white dark:bg-zinc-900 xl:dark:bg-zinc-800 rounded pb-1">
    <div
      class="relative w-full rounded cursor-zoom-in group"
      :style="{ 'background-color': randomColor() }"
      @click="onItemClick"
    >
      <img
        v-lazy
        class="w-full rounded bg-transparent"
        ref="imgTarget"
        :src="data.photo"
        :style="{ height: (width / data.photoWidth) * data.photoHeight + 'px' }"
      />
      <div
        class="hidden opacity-0 w-full h-full bg-zinc-900/50 absolute top-0 left-0 rounded duration-300 group-hover:opacity-100 xl:block"
      >
        <m-button class="absolute top-1.5 left-1.5">分享</m-button>
        <m-button
          class="absolute top-1.5 right-1.5 bg-zinc-100/70"
          type="info"
          size="small"
          icon="heart"
          iconClass="fill-zinc-900 dark:fill-zinc-200"
        ></m-button>
        <m-button
          class="absolute bottom-1.5 left-1.5 bg-zinc-100/70"
          type="info"
          size="small"
          icon="download"
          iconClass="fill-zinc-900 dark:fill-zinc-200"
          @click="onDownloadClick"
        ></m-button>
        <m-button
          class="absolute bottom-1.5 right-1.5 bg-zinc-100/70"
          type="info"
          size="small"
          icon="full"
          iconClass="fill-zinc-900 dark:fill-zinc-200"
          @click="onFullClick"
        ></m-button>
      </div>
    </div>
    <p class="text-sm mt-1 font-bold text-zinc-900 dark:text-zinc-300 px-1">
      {{ data.title }}
    </p>
    <div class="flex items-center mt-1 px-1">
      <img class="w-2 h-2 rounded-full" :src="data.avatar" />
      <span class="text-sm text-zinc-500 ml-1">{{ data.author }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { saveAs } from 'file-saver'
import { ref } from 'vue'
import { useFullscreen } from '@vueuse/core'

import { message } from '@/libs/message/index'

const props = defineProps<{
  data: any
  width: number
}>()

const emits = defineEmits(['click'])

const randomColor = () => {
  return (
    '#' +
    Math.floor(Math.random() * 0xffffff)
      .toString(16)
      .padEnd(6, '0')
  )
}

const imgTarget = ref<HTMLElement>()
const getImgCenterPos = () => {
  if (!imgTarget.value) return
  const { top, left, width, height } = imgTarget.value.getBoundingClientRect()
  return {
    top: top + height / 2,
    left: left + width / 2
  }
}

const onItemClick = () => {
  emits('click', { data: props.data, location: getImgCenterPos() })
}

const onDownloadClick = () => {
  message('success', '图片开始下载')
  setTimeout(() => {
    saveAs(props.data.photoDownLink, props.data.title)
  }, 1000)
}

const onFullClick = () => {
  const { toggle } = useFullscreen(imgTarget)
  toggle()
}
</script>

<style scoped></style>
