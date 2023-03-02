<template>
  <div class="h-screen">
    <headerVue />
    <div class="h-main">
      <!-- 二级路由出口 -->
      <RouterView />
    </div>
    <floatVue />
  </div>
</template>

<script setup lang="ts">
import headerVue from './components/header/index.vue'
import floatVue from './components/float.vue'
</script>

<style scoped></style>
