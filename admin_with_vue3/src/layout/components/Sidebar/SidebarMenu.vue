<template>
  <el-menu :unique-opened='true' default-active='2' background-color='#545c64' text-color='#fff'
           active-text-color='#ffd04b'>
    <el-submenu index='1'>
      <template #title>
        <i class='el-icon-location'></i>
        <span>导航一</span>
      </template>
      <el-menu-item index='1-1'>选项1</el-menu-item>
      <el-menu-item index='1-2'>选项2</el-menu-item>
      <el-menu-item index='1-3'>选项3</el-menu-item>
    </el-submenu>
    <el-menu-item index='4'><i class='el-icon-setting'></i>
      <span>导航四</span></el-menu-item>
  </el-menu>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { filterRoutes, genMenus } from '@/utils/route'
import { computed } from 'vue'

const router = useRouter()
const routes = computed(() => genMenus(filterRoutes(router.getRoutes())))
console.log(genMenus(routes.value), 222)
</script>

<style scoped>

</style>
