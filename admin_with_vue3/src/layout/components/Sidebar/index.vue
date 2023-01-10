<template>
  <div>
    <div class="logo-container">
      <el-avatar
        :size="logoHeight"
        shape="square"
        src="https://avatar.52pojie.cn/data/avatar/001/15/47/76_avatar_small.jpg"
      />
      <transition name="fade-transform">
        <h1 class="logo-title" v-if="aStore.sidebarOpened">My-Admin</h1>
      </transition>
    </div>
    <el-scrollbar>
      <SidebarMenu></SidebarMenu>
    </el-scrollbar>
  </div>
</template>

<script setup>
import { appStore } from '@/store/app_store'
import SidebarMenu from './SidebarMenu.vue'

const aStore = appStore()
const logoHeight = 50
const itemHeight = logoHeight + 'px'
</script>

<style lang="scss" scoped>
.logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px 0;

  .logo-title {
    font-size: 16px;
    color: #fff;
    white-space: nowrap;
    line-height: v-bind(itemHeight);
  }
}
</style>
