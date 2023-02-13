<template>
  <ul
    class="mx-auto max-w-[800px] mt-2 px-[10px] flex flex-wrap justify-left items-start relative text-base text-zinc-900 font-bold overflow-hidden duration-500"
    :class="isOpenCategories ? 'h-[186px]' : 'h-[40px]'"
  >
    <li
      v-for="(item, index) in cStore.categoriesData"
      :key="item.id"
      class="hover:bg-zinc-200 rounded-sm p-1 mx-1 cursor-pointer"
    >
      {{ item.name }}
    </li>
    <div
      class="absolute right-1 bg-white p-1 rounded cursor-pointer hover:bg-zinc-200 duration-500"
      :class="isOpenCategories ? 'bottom-[10px]' : 'bottom-[3px]'"
      @click="isOpenCategories = !isOpenCategories"
    >
      <m-svg-icon
        :name="isOpenCategories ? 'fold' : 'unfold'"
        class="h-1 w-1"
      ></m-svg-icon>
    </div>
  </ul>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { categoryStore } from '@/stores/category'

const isOpenCategories = ref(false)
const cStore = categoryStore()
</script>

<style scoped></style>
