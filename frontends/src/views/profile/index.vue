<template>
  <div class="bg-zinc-200 h-full xl:py-2">
    <m-navbar :sticky="true" v-if="isMobileDevice">个人资料</m-navbar>
    <div class="max-w-sm bg-white h-full mx-auto text-sm p-1 xl:rounded-sm">
      <h1 v-if="!isMobileDevice" class="text-center text-lg font-bold">
        个人资料
      </h1>
      <div class="flex flex-col xl:flex-row-reverse">
        <div id="pc-right" class="py-2 xl:before:w-1/3 xl:pt-5">
          <div class="flex flex-col items-center">
            <img
              class="w-10 h-10 bg-gray-200 rounded-full"
              :src="userInfo.avatar"
              @click="onAvatarClick"
            />
            <span class="text-xs text-zinc-400 mt-0.5 w-[80%] text-center"
              >支持 jpg、png、gif 格式大小 5M 以内的图片</span
            >
            <input
              type="file"
              ref="fileInput"
              class="hidden"
              accept=".png,.jpeg"
              @change="onSelectImgHandler"
            />
          </div>
        </div>
        <div id="pc-left" class="flex-1">
          <div class="my-2 xl:flex items-center">
            <span class="font-bold w-[10%] xl:text-right mr-2">昵称</span>
            <m-input
              v-model="userInfo.nickname"
              :maxlength="20"
              class="mx-auto my-1 flex-1"
            ></m-input>
          </div>
          <div class="my-2 xl:flex items-center">
            <span class="font-bold w-[10%] xl:text-right mr-2">职位</span>
            <m-input
              v-model="userInfo.company"
              class="mx-auto my-1 flex-1"
            ></m-input>
          </div>
          <div class="my-2 xl:flex items-center">
            <span class="font-bold w-[10%] xl:text-right mr-2">个人主页</span>
            <m-input
              v-model="userInfo.homePage"
              class="mx-auto my-1 flex-1"
            ></m-input>
          </div>
          <div class="my-2 xl:flex items-center">
            <span class="font-bold w-[10%] xl:text-right mr-2">个人介绍</span>
            <m-input
              v-model="userInfo.introduction"
              type="textarea"
              class="mx-auto my-2 flex-1"
              :maxlength="50"
            ></m-input>
          </div>
          <div class="mt-4">
            <m-button class="w-full xl:w-1/3 mx-auto" @click="onSubmitClick"
              >保存修改</m-button
            >
          </div>
          <div class="my-2" v-if="isMobileDevice">
            <m-button class="w-full" type="info">退出登录</m-button>
          </div>
        </div>
      </div>

      <m-popup v-model="isVisiable" v-if="isMobileDevice">
        <changeAvatar
          :blob="currentBlob"
          @close="isVisiable = false"
        ></changeAvatar>
      </m-popup>
      <m-dialog v-model="isVisiable" v-else>
        <changeAvatar
          :blob="currentBlob"
          @close="isVisiable = false"
        ></changeAvatar>
      </m-dialog>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

import { isMobileDevice } from '@/utils/flexiable'
import { userStore } from '@/stores/user'
import { setInfo } from '@/api/login'
import { message } from '@/libs/message/index'
import changeAvatar from './change-avatar.vue'

const uStore = userStore()
const userInfo = ref({ ...uStore.userInfo })
const onSubmitClick = () => {
  setInfo(userInfo.value).then(() => {
    message('success', '用户信息修改成功')
    uStore.setUserInfo(userInfo.value)
  })
}

const fileInput = ref<HTMLInputElement>()
const isVisiable = ref(false)
const currentBlob = ref()
const onAvatarClick = () => {
  fileInput.value?.click()
}
const onSelectImgHandler = () => {
  const file = fileInput.value?.files?.[0]
  currentBlob.value = URL.createObjectURL(file as File)
  isVisiable.value = true
}
watch(isVisiable, (val) => {
  if (!val) {
    ;(fileInput.value as HTMLInputElement).value = ''
  }
})
</script>

<style scoped></style>
