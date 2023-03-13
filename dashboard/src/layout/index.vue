<template>
  <div
    class="app-wrapper"
    :class="[aStore.sidebarOpened ? 'default' : 'hide-sidebar']"
  >
    <Sidebar
      class="sidebar-container"
      :style="{ backgroundColor: tStore.cssVar.menuBg }"
    />
    <div class="main-container">
      <div class="fix-header">
        <Navbar />
        <TagsView></TagsView>
      </div>
      <AppMain />
    </div>
  </div>
</template>

<script setup>
import { themeStore } from '@/store/theme_store'
import { appStore } from '@/store/app_store'
import TagsView from '@/components/TagsView/index.vue'
import Navbar from './components/Navbar.vue'
import Sidebar from './components/Sidebar/index.vue'
import AppMain from './components/AppMain.vue'

const tStore = themeStore()
const aStore = appStore()
</script>

<style lang="scss" scoped>
.hide-sidebar {
  .sidebar-container {
    width: #{$hideSideBarWidth} !important;
  }

  .main-container {
    margin-left: #{$hideSideBarWidth} !important;
  }

  .fix-header {
    width: calc(100% - #{$hideSideBarWidth}) !important;
    transition: width #{$sideBarDuration};
  }
}
</style>
