<template>
  <div class="mt-1">
    <span class="text-zinc-400 text-xs">热门精选</span>
    <div class="flex h-[140px] mt-1">
      <div class="relative cursor-pointer w-[260px]">
        <img :src="hots.big.photo" class="h-full w-full rounded-sm" />
        <p class="absolute bottom-1 left-1 text-sm text-white">
          # {{ hots.big.title }}
        </p>
      </div>
      <div class="flex flex-wrap flex-1 max-w-[860px]">
        <div
          class="relative cursor-pointer h-[45%] w-[260px] ml-1.5 mb-1.5"
          v-for="item in hots.smalls"
        >
          <img
            :src="item.photo"
            class="rounded-sm w-full h-full object-cover"
          />
          <p
            class="absolute w-full h-full text-white text-sm top-0 left-0 backdrop-blur rounded-sm flex items-center px-1 cursor-pointer hover:backdrop-blur-none"
          >
            # {{ item.title }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { getHot } from '@/api/home'

interface Items {
  id: string
  title: string
  photo: string
}

const hots = ref({
  big: {} as Items,
  smalls: Array<Items>()
})

const fillHots = async () => {
  const res = await getHot()
  hots.value.big = res.result[0]
  hots.value.smalls = res.result.slice(1)
}

fillHots()
</script>

<style scoped></style>
