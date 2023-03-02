<template>
  <div
    class="fixed top-0 left-0 z-50 w-screen h-screen scrollbar-thin scrollbar-thumb-rounded-md scrollbar-thumb-zinc-200 dark:scrollbar-thumb-zinc-500 scrollbar-track-transparent bg-white backdrop-blur-4xl xl:bg-transparent xl:p-2"
  >
    <m-navbar v-if="isMobileDevice" sticky
      >{{ data.title }}
      <template #right>
        <m-svg-icon
          name="share"
          class="w-3 h-3"
          fillClass="fill-zinc-900 dark:fill-zinc-200"
        ></m-svg-icon>
      </template>
    </m-navbar>
    <m-svg-icon
      v-else
      name="close"
      class="absolute right-2 top-2 w-3 h-3 p-0.5 cursor-pointer rounded-sm hover:bg-zinc-100"
      fillClass="fill-zinc-400"
      @click="onClose"
    ></m-svg-icon>
    <div class="xl:w-[80%] xl:h-full xl:mx-auto xl:flex">
      <img
        class="xl:w-3/5 xl:h-full xl:rounded-tl-lg xl:rounded-bl-lg"
        :src="imgURL"
      />
      <div
        class="bg-white dark:bg-zinc-900 xl:w-2/5 xl:h-full xl:rounded-tr-lg xl:rounded-br-lg xl:p-3"
      >
        <div v-if="!isMobileDevice" class="flex justify-between">
          <m-svg-icon
            name="share"
            class="h-4 w-4 p-1 hover:bg-zinc-200 duration-500 rounded cursor-pointer dark:hover:bg-zinc-700"
            fillClass="fill-zinc-900 dark:fill-zinc-200"
          ></m-svg-icon>
          <m-button
            type="info"
            icon="heart"
            iconClass="fill-zinc-900 dark:fill-zinc-200"
          ></m-button>
        </div>

        <p
          class="text-base text-zinc-900 dark:text-zinc-200 ml-1 pt-2 font-bold xl:text-xl"
        >
          {{ data.title }}
        </p>

        <div class="flex items-center py-3 px-1">
          <img class="w-3 h-3 rounded-full" :src="data.avatar" />
          <span class="text-base text-zinc-900 dark:text-zinc-200 ml-1">{{
            data.author
          }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

import { isMobileDevice } from '@/utils/flexiable'

const props = defineProps<{ data: any }>()

const imgURL = props.data.photo.replace(/w=\d+/, 'w=1000')

const router = useRouter()
const onClose = () => {
  router.back()
}
</script>

<style scoped></style>
