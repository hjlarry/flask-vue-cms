<template>
  <el-menu
    :unique-opened="true"
    :background-color="store.cssVar.menuBg"
    :text-color="store.cssVar.menuText"
    :active-text-color="store.cssVar.$menuActiveText"
    :default-active="activeMenu"
    :collapse="!$store.getters.sidebarOpened"
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

const router = useRouter()
const routes = computed(() => genMenus(filterRoutes(router.getRoutes())))
const route = useRoute()
const activeMenu = computed(() => route.path)
const store = themeStore()
</script>

<style scoped></style>
