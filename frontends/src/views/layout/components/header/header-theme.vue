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
          v-for="item in itemsData"
          :key="item.id"
        >
          <m-svg-icon :name="item.icon" class="w-1.5 h-1.5" />
          <span class="text-sm">{{ item.text }}</span>
        </div>
      </div>
    </template>
  </m-popover>
</template>

<script setup lang="ts">
const itemsData = [
  {
    id: 1,
    icon: 'theme-light',
    text: '极简白'
  },
  {
    id: 2,
    icon: 'theme-dark',
    text: '极夜黑'
  },
  {
    id: 3,
    icon: 'theme-system',
    text: '跟随系统'
  }
]
</script>

<style scoped></style>
