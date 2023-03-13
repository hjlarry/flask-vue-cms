<template>
  <div class="bg-zinc-200 fixed h-screen w-screen">
    <m-navbar :sticky="true" v-if="isMobileDevice">精选会员</m-navbar>

    <div class="bg-white px-1 mx-auto xl:w-5/6">
      <h1 class="text-center text-yellow-500 font-bold pt-2">精选VIP</h1>
      <h4 class="text-center text-lg text-yellow-400 mt-0.5">
        升级精选VIP，畅想所有内容
      </h4>
      <div
        class="flex overflow-x-auto mt-5 space-x-2 py-2 xl:space-x-8 scrollbar-thin scrollbar-thumb-rounded-md scrollbar-thumb-zinc-200 scrollbar-track-transparent"
      >
        <div
          class="flex-none relative flex flex-col items-center cursor-pointer border rounded-md w-[100px] py-3 hover:bg-orange-50"
          v-for="(item, index) in vipPayListData"
          :key="item.id"
          :class="
            item.id === currentPayItem.id
              ? 'bg-orange-50 border-orange-300'
              : ''
          "
          @click="selectPayItem(index)"
        >
          <span class="text-base text-yellow-800">{{ item.title }}</span>
          <span
            class="text-[32px] tracking-tighter font-sans font-bold text-yellow-800"
            ><span class="text-base">￥</span> {{ item.price }}</span
          >
          <span class="text-xs text-yellow-500 line-through"
            >￥{{ item.oldPrice }}</span
          >
          <div
            v-if="item.isHot"
            class="absolute right-[-1px] top-[-12px] h-[22px] w-[48px] leading-[22px] text-center text-yellow-700 bg-gradient-to-r from-orange-300 to-orange-100 text-[12px] rounded-tr-[10px] rounded-bl-[10px]"
          >
            热销
          </div>
        </div>
      </div>
      <div class="text-sm text-zinc-400 mt-1 pb-5">
        {{ currentPayItem.desc }}
      </div>

      <div v-if="!isMobileDevice" class="py-1">
        <Discount />
        <div class="mt-1 rounded-md border text-center py-3">
          <p class="text-base">
            支付金额:
            <span class="text-xl text-red-500"
              >￥{{ currentPayItem.price }}</span
            >
          </p>
          <div
            class="w-20 border rounded-sm px-2 py-1 flex items-center mx-auto mt-2 cursor-pointer hover:bg-zinc-100"
          >
            <img src="@/assets/images/alipay.png" class="w-4 h-4" />
            <span class="text-xl ml-2">支付宝</span>
          </div>
        </div>
      </div>
    </div>

    <div class="fixed bottom-0 w-full" v-if="isMobileDevice">
      <Discount />
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
import { ref } from 'vue'

import { isMobileDevice } from '@/utils/flexiable'
import { getVipPayList } from '@/api/home'
import Discount from './discount.vue'

const vipPayListData = ref<any>([])
const currentPayItem = ref<any>({})
const getVipPayListData = async () => {
  const res = await getVipPayList()
  vipPayListData.value = res
  currentPayItem.value = res[0]
}
getVipPayListData()

const selectPayItem = (index: number) => {
  currentPayItem.value = vipPayListData.value[index]
}
</script>

<style scoped></style>
