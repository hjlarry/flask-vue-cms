<template>
  <el-card>
    <template #header>
      <span>Project card</span>
    </template>
    <template #default>
      <PanThumb
        :image="$store.getters.userInfo.avatar"
        :height="'100px'"
        :width="'100px'"
      >
        <span>Hello World!</span>
      </PanThumb>
    </template>
  </el-card>
</template>

<script setup>
import PanThumb from '@/components/PanThumb/index.vue'
</script>

<style scoped></style>
