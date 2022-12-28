<template>
  <div class='app-wrapper'
       :class="[$store.getters.sidebarOpened ? 'default' : 'hide-sidebar']">
    <sidebar
      class='sidebar-container'
      :style='{ backgroundColor: $store.getters.cssVar.menuBg }'
    />
    <div class='main-container'>
      <div class='fix-header'>
        <navbar />
      </div>
      <app-main />
    </div>
  </div>
</template>

<script setup>
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'
import AppMain from './components/AppMain'
</script>

<style lang='scss' scoped>
@import '~@/styles/variables.scss';

.hide-sidebar {
  .sidebar-container {
    width: #{ $hideSideBarWidth } !important;
  }

  .main-container {
    margin-left: #{ $hideSideBarWidth } !important;
  }

  .fix-header {
    width: calc(100% - #{ $hideSideBarWidth }) !important;
    transition: width #{$sideBarDuration};
  }
}
</style>
