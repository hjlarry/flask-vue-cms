<template>
  <m-popover>
    <template #target>
      <m-svg-icon
        :name="currentThemeIcon"
        class="w-4 h-4 p-1 cursor-pointer hover:bg-zinc-100/60 dark:hover:bg-zinc-400 rounded-sm duration-500"
        fillClass="fill-zinc-900 dark:fill-zinc-300"
      />
    </template>
    <template #dropdown>
      <div class="flex flex-col w-[140px]">
        <div
          class="flex items-center space-x-1 p-1 rounded-sm cursor-pointer hover:bg-zinc-100/60 dark:hover:bg-zinc-700"
          v-for="item in dropdownMenu"
          :key="item.id"
          @click="itemClick(item)"
        >
          <m-svg-icon
            :name="item.icon"
            class="w-1.5 h-1.5"
            fillClass="fill-zinc-900 dark:fill-zinc-300"
          />
          <span class="text-sm text-zinc-800 dark:text-zinc-300">{{
            item.text
          }}</span>
        </div>
      </div>
    </template>
  </m-popover>
</template>

<script setup lang="ts">
import { computed } from 'vue'

import { themeStore } from '@/stores/theme'
import { THEME_LIGHT, THEME_DARK, THEME_SYSTEM } from '@/constants'

const dropdownMenu = [
  {
    id: 1,
    icon: 'theme-light',
    text: '极简白',
    type: THEME_LIGHT
  },
  {
    id: 2,
    icon: 'theme-dark',
    text: '极夜黑',
    type: THEME_DARK
  },
  {
    id: 3,
    icon: 'theme-system',
    text: '跟随系统',
    type: THEME_SYSTEM
  }
]

const tStore = themeStore()
const itemClick = (item: any) => {
  tStore.setTheme(item.type)
}
const currentThemeIcon = computed(() => {
  return dropdownMenu.find((item) => item.type === tStore.theme)?.icon
})
</script>

<style scoped></style>
