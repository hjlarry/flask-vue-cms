<template>
  <div class="sticky top-0 bg-white dark:bg-zinc-800 z-10">
    <ul
      class="mx-auto max-w-[800px] px-[10px] pt-1 relative flex flex-wrap justify-left items-start text-base text-zinc-900 dark:text-zinc-500 font-bold overflow-hidden duration-500 dark:bg-zinc-800"
      :class="isOpenCategories ? 'h-[186px]' : 'h-[50px]'"
    >
      <li
        v-for="(item, index) in cStore.categoriesData"
        :key="item.id"
        class="hover:bg-zinc-200 rounded-sm p-1 mx-1 cursor-pointer"
      >
        {{ item.name }}
      </li>
      <div
        class="absolute right-1 p-1 rounded cursor-pointer hover:bg-zinc-200 dark:hover:text-zinc-300 dark:hover:bg-zinc-200 duration-500"
        :class="isOpenCategories ? 'bottom-[10px]' : 'bottom-[5px]'"
        @click="isOpenCategories = !isOpenCategories"
      >
        <m-svg-icon
          :name="isOpenCategories ? 'fold' : 'unfold'"
          class="h-1 w-1"
          fillClass="fill-zinc-900 dark:fill-zinc-500"
        ></m-svg-icon>
      </div>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { categoryStore } from '@/stores/category'

const isOpenCategories = ref(false)
const cStore = categoryStore()
</script>

<style scoped></style>
