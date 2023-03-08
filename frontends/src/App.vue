<template>
  <!-- 一级路由出口 -->
  <m-transition-router-view :routerType="aStore.routerType" />
</template>

<script setup lang="ts">
import { appStore } from './stores/app'

const aStore = appStore()
</script>
<style scoped></style>
