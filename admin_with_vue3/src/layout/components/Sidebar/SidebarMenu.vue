<template>
  <el-menu :unique-opened='true'
           :background-color='$store.getters.cssVar.menuBg'
           :text-color='$store.getters.cssVar.menuText'
           :active-text-color='$store.getters.cssVar.$menuActiveText'
           :default-active='activeMenu'
           :collapse='!$store.getters.sidebarOpened'
           router>
    <sidebar-item v-for='item in routes' :route='item' :key='item.path'></sidebar-item>
  </el-menu>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { filterRoutes, genMenus } from '@/utils/route'
import { computed } from 'vue'
import SidebarItem from './SidebarItem.vue'

const router = useRouter()
const routes = computed(() => genMenus(filterRoutes(router.getRoutes())))
const activeMenu = router.currentRoute.value.path
</script>

<style scoped>

</style>
