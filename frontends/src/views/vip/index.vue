<template>
  <div class="bg-zinc-200 fixed h-screen w-screen">
    <m-navbar :sticky="true" v-if="isMobileDevice">精选会员</m-navbar>

    <div class="bg-white px-1">
      <h1 class="text-center text-yellow-500 font-bold pt-2">精选VIP</h1>
      <h4 class="text-center text-lg text-yellow-400 mt-0.5">
        升级精选VIP，畅想所有内容
      </h4>
      <div
        class="flex overflow-x-auto mt-5 space-x-2 py-2 scrollbar-thin scrollbar-thumb-rounded-md scrollbar-thumb-zinc-200 scrollbar-track-transparent"
      >
        <div
          class="flex-none relative flex flex-col items-center cursor-pointer border rounded-md w-[100px] py-3 bg-orange-50 border-orange-300"
        >
          <span class="text-base text-yellow-800">连续包月</span>
          <span
            class="text-[32px] tracking-tighter font-sans font-bold text-yellow-800"
            ><span class="text-base">￥</span> 9</span
          >
          <span class="text-xs text-yellow-500 line-through">￥29</span>
        </div>

        <div
          class="flex-none relative flex flex-col items-center cursor-pointer border rounded-md w-[100px] py-3"
        >
          <span class="text-base text-yellow-800">连续包月</span>
          <span
            class="text-[32px] tracking-tighter font-sans font-bold text-yellow-800"
            ><span class="text-base">￥</span> 9</span
          >
          <span class="text-xs text-yellow-500 line-through">￥29</span>
        </div>

        <div
          class="flex-none relative flex flex-col items-center cursor-pointer border rounded-md w-[100px] py-3"
        >
          <span class="text-base text-yellow-800">连续包月</span>
          <span
            class="text-[32px] tracking-tighter font-sans font-bold text-yellow-800"
            ><span class="text-base">￥</span> 9</span
          >
          <span class="text-xs text-yellow-500 line-through">￥29</span>
        </div>

        <div
          class="flex-none relative flex flex-col items-center cursor-pointer border rounded-md w-[100px] py-3"
        >
          <span class="text-base text-yellow-800">连续包月</span>
          <span
            class="text-[32px] tracking-tighter font-sans font-bold text-yellow-800"
            ><span class="text-base">￥</span> 9</span
          >
          <span class="text-xs text-yellow-500 line-through">￥29</span>
        </div>
      </div>
      <div class="text-sm text-zinc-400 mt-1 pb-5">
        次月￥19续费，可随时取消
      </div>
    </div>

    <div class="fixed bottom-0 w-full">
      <div
        class="bg-orange-100 text-red-500 font-bold text-xs text-center py-0.5 flex items-center justify-center"
      >
        <m-svg-icon
          name="countdown"
          class="w-1.5 h-1.5 mr-1"
          fillClass="fill-red-600"
        ></m-svg-icon>
        <span>限时特惠 | 距离优惠结束仅剩 00:40:31</span>
      </div>
      <div class="flex items-center justify-between bg-white p-1">
        <div class="text-sm flex flex-col">
          <span>卷后合计: <span class="text-lg text-red-500">￥9</span></span>
          <span class="text-red-500">优惠券: 限时立减￥10</span>
        </div>
        <m-button class="w-1/3" type="main">立即开通</m-button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { isMobileDevice } from '@/utils/flexiable'
</script>

<style scoped></style>
