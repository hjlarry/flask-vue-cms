<template>
  <m-popover>
    <template #target>
      <div
        v-if="uStore.token"
        class="flex items-center relative p-0.5 cursor-pointer rounded-sm hover:bg-zinc-100 dark:hover:bg-zinc-400"
      >
        <img :src="uStore.userInfo.avatar" class="w-3 h-3 rounded-sm" />
        <m-svg-icon
          name="down-arrow"
          class="w-1 h-1 ml-0.5"
          fillClass="fill-zinc-900 dark:fill-zinc-300"
        />
        <m-svg-icon
          v-if="uStore.userInfo.vipLevel"
          name="vip"
          class="absolute bottom-[2px] right-[16px] w-1 h-1"
        />
      </div>
      <div v-else>
        <m-button
          icon="profile"
          iconColor="#fff"
          @click="router.push('/login')"
        ></m-button>
      </div>
    </template>
    <template #dropdown v-if="uStore.token">
      <div class="flex flex-col w-[140px]">
        <div
          class="flex items-center space-x-1 p-1 rounded-sm cursor-pointer hover:bg-zinc-100/60 dark:hover:bg-zinc-700"
          v-for="item in dropdownMenu"
          :key="item.id"
          @click="onItemClick(item)"
        >
          <m-svg-icon
            :name="item.icon"
            class="w-1.5 h-1.5"
            fillClass="fill-zinc-900 dark:fill-zinc-300"
          />
          <span class="text-sm text-zinc-800 dark:text-zinc-300">{{
            item.title
          }}</span>
        </div>
      </div>
    </template>
  </m-popover>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { userStore } from '@/stores/user'

import { confirm } from '@/libs/confirm'

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

const uStore = userStore()
const router = useRouter()

const onItemClick = (item: any) => {
  if (item.id === 2) {
    confirm('确定退出登录吗？').then(() => {
      uStore.logOut()
    })
  } else {
    router.push(item.path)
  }
}
</script>

<style scoped></style>
