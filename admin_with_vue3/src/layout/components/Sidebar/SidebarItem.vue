<template>
  <el-submenu v-if='route.children.length > 0' :index='route.path'>
    <template #title>
      <menu-item :title='route.meta.title' :icon='route.meta.icon'></menu-item>
    </template>
    <sidebar-item v-for='item in route.children' :key='item.path' :route='item' />
  </el-submenu>
  <el-menu-item v-else :index='route.path'>
    <menu-item :title='route.meta.title' :icon='route.meta.icon'></menu-item>
  </el-menu-item>
</template>

<script setup>
import { defineProps } from 'vue'
import MenuItem from './MenuItem.vue'

defineProps({
  route: {
    type: Object,
    required: true
  }
})

</script>

<style scoped>

</style>
