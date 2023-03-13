<template>
  <div class="sticky top-0 left-0 bg-white z-20 dark:bg-zinc-900">
    <ul
      class="relative flex overflow-x-auto text-xs overflow-hidden p-1 text-zinc-600"
      ref="ulTarget"
    >
      <!-- hamburger -->
      <li
        class="z-20 fixed top-0 right-[-1px] h-4 px-1 flex items-center bg-white dark:bg-zinc-900 shadow-l-white dark:shadow-l-zinc"
        @click="isOpenPopup = true"
      >
        <m-svg-icon class="w-1.5 h-1.5" name="hamburger" />
      </li>
      <!-- slide item -->
      <li
        class="absolute bg-zinc-900 dark:bg-zinc-700 h-[22px] rounded-lg duration-300"
        :style="sliderStyle"
      ></li>
      <!-- categories -->
      <li
        v-for="(item, index) in cStore.categoriesData"
        :key="item.id"
        class="shrink-0 px-1.5 py-0.5 z-10 duration-200 last:mr-4"
        :class="currentCategoryIndex === index ? 'text-white' : ''"
        ref="itemRef"
        @click="onItemClick(item, index)"
      >
        {{ item.name }}
      </li>
    </ul>
  </div>
  <m-popup v-model="isOpenPopup">
    <popMenus
      :data="cStore.categoriesData"
      @onItemClick="onItemClick"
    ></popMenus>
  </m-popup>
</template>

<script setup lang="ts">
import { useScroll } from '@vueuse/core'
import { ref, watch } from 'vue'

import popMenus from './popMenu.vue'
import { categoryStore } from '@/stores/category'

const cStore = categoryStore()

// 给滑块一个初始样式
const sliderStyle = ref({
  width: '52px',
  transform: 'translateX(0px)'
})
const ulTarget = ref(null)
const currentCategoryIndex = ref(0)
const itemRef = ref([])
// 拿到整个ul的滚动距离
const { x: ulTargetLeft } = useScroll(ulTarget)

const onItemClick = (item: any, index: number) => {
  currentCategoryIndex.value = index
  isOpenPopup.value = false
  cStore.setCurrentCategory(item)
}

watch(currentCategoryIndex, (val) => {
  // 计算滑块的实际位置，就是ul的滚动距离+当前li距离屏幕左侧的距离-ul的padding-left
  const currentCategoryLi: any = itemRef.value[val]
  const { left, width } = currentCategoryLi.getBoundingClientRect()
  sliderStyle.value = {
    width: `${width}px`,
    transform: `translateX(${ulTargetLeft.value + left - 10}px)`
  }
})

const isOpenPopup = ref(false)
</script>

<style scoped></style>
