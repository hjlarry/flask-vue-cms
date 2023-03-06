<template>
  <div class="bg-zinc-200 h-full">
    <m-navbar :sticky="true">个人资料</m-navbar>
    <form class="max-w-sm bg-white h-full mx-auto text-sm px-1">
      <h1 v-if="!isMobileDevice" class="text-center text-lg font-bold">
        个人资料
      </h1>

      <div class="py-2">
        <div class="flex flex-col items-center">
          <div class="w-10 h-10 bg-gray-200 rounded-full"></div>
          <span class="text-xs text-zinc-400 mt-0.5"
            >支持 jpg、png、gif 格式大小 5M 以内的图片</span
          >
        </div>
      </div>
      <div class="my-2">
        <span class="font-bold">用户名</span>
        <m-input
          v-model="username"
          :maxlength="20"
          class="mx-auto my-1"
        ></m-input>
      </div>
      <div class="my-2">
        <span class="font-bold">职位</span>
        <m-input v-model="username" class="mx-auto my-1"></m-input>
      </div>
      <div class="my-2">
        <span class="font-bold">个人主页</span>
        <m-input v-model="username" class="mx-auto my-1"></m-input>
      </div>
      <div class="my-2">
        <span class="font-bold">个人介绍</span>
        <m-input
          v-model="username"
          type="textarea"
          class="mx-auto my-2"
          :maxlength="50"
        ></m-input>
      </div>
      <div class="mt-4">
        <m-button class="w-full">保存修改</m-button>
      </div>
      <div class="my-2" v-if="isMobileDevice">
        <m-button class="w-full" type="info">退出登录</m-button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { isMobileDevice } from '@/utils/flexiable'

const username = ref('')
</script>

<style scoped></style>
