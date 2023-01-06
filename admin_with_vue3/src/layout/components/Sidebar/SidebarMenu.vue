<template>
  <el-menu
    :unique-opened="true"
    :background-color="tStore.cssVar.menuBg"
    :text-color="tStore.cssVar.menuText"
    :active-text-color="tStore.cssVar.$menuActiveText"
    :default-active="activeMenu"
    :collapse="!aStore.sidebarOpened"
    router
  >
    <sidebar-item
      v-for="item in routes"
      :route="item"
      :key="item.path"
    ></sidebar-item>
  </el-menu>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { filterRoutes, genMenus } from '@/utils/route'
import { computed } from 'vue'
import SidebarItem from './SidebarItem.vue'
import { themeStore } from '@/store/theme_store'
import { appStore } from '@/store/app_store'

const router = useRouter()
const routes = computed(() => genMenus(filterRoutes(router.getRoutes())))
const route = useRoute()
const activeMenu = computed(() => route.path)
const tStore = themeStore()
const aStore = appStore()
</script>

<style scoped></style>
