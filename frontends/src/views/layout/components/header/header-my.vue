<template>
  <m-popover>
    <template #target>
      <div class="flex items-center relative p-0.5 cursor-pointer">
        <img
          src="https://m.imooc.com/static/wap/static/common/img/logo-small@2x.png"
          class="w-3 h-3 rounded-sm"
        />
        <m-svg-icon name="down-arrow" class="w-1 h-1 ml-0.5" />
        <m-svg-icon
          name="vip"
          class="absolute bottom-[2px] right-[16px] w-1 h-1"
        />
      </div>
    </template>
    <template #dropdown>
      <div class="flex flex-col w-[140px]">
        <div
          class="flex items-center space-x-1 p-1 rounded-sm cursor-pointer hover:bg-zinc-100/60"
          v-for="item in dropdownMenu"
          :key="item.id"
        >
          <m-svg-icon :name="item.icon" class="w-1.5 h-1.5" />
          <span class="text-sm text-zinc-800">{{ item.title }}</span>
        </div>
      </div>
    </template>
  </m-popover>
</template>

<script setup lang="ts">
const dropdownMenu = [
  {
    id: 0,
    title: '个人资料',
    icon: 'profile',
    path: '/profile'
  },
  {
    id: 1,
    title: '升级 VIP',
    icon: 'vip-profile',
    path: '/member'
  },
  {
    id: 2,
    title: '退出登录',
    icon: 'logout',
    path: ''
  }
]
</script>

<style scoped></style>
