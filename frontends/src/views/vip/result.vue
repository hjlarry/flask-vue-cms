<template>
  <div class="h-full bg-zinc-200 dark:bg-zinc-800 duration-400 xl:pt-1">
    <m-navbar :sticky="true" v-if="isMobileDevice">精选会员</m-navbar>
    <div
      class="mx-auto h-full pt-[50%] px-1 bg-white dark:bg-zinc-900 duration-400 xl:h-[360px] xl:rounded-sm xl:py-10 xl:border-zinc-200 xl:dark:border-zinc-600 xl:border-[1px] xl:px-4 xl:max-w-screen-lg"
    >
      <div class="flex justify-center items-center">
        <m-svg-icon name="pay-success" class="w-8 h-8 mr-4"></m-svg-icon>

        <p class="text-ml text-zinc-900 dark:text-zinc-200">支付成功</p>
      </div>

      <m-button
        class="w-full mt-8 mx-auto dark:bg-zinc-800 xl:w-[120px]"
        @click="onConfirm"
        >确定</m-button
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

import { isMobileDevice } from '@/utils/flexiable'

const router = useRouter()
const onConfirm = () => {
  router.push('/')
}
</script>

<style scoped></style>
