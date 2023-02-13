<template>
  <m-popover>
    <template #target>
      <m-svg-icon
        name="theme-light"
        class="w-4 h-4 p-1 cursor-pointer hover:bg-zinc-100/60 rounded-sm duration-500"
      />
    </template>
    <template #dropdown>
      <div class="flex flex-col w-[140px]">
        <div
          class="flex items-center space-x-1 p-1 rounded-sm cursor-pointer hover:bg-zinc-100/60"
          v-for="item in dropdownMenu"
          :key="item.id"
          @click="itemClick(item)"
        >
          <m-svg-icon :name="item.icon" class="w-1.5 h-1.5" />
          <span class="text-sm text-zinc-800">{{ item.text }}</span>
        </div>
      </div>
    </template>
  </m-popover>
</template>

<script setup lang="ts">
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
</script>

<style scoped></style>
