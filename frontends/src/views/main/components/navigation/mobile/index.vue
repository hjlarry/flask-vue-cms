<template>
  <div class="sticky top-0 left-0">
    <ul
      class="relative flex overflow-x-auto text-xs overflow-hidden p-1 text-zinc-600"
      ref="ulTarget"
    >
      <!-- hamburger -->
      <li
        class="z-20 fixed top-0 right-[-1px] h-4 px-1 flex items-center bg-white shadow-l-white"
      >
        <m-svg-icon class="w-1.5 h-1.5" name="hamburger" />
      </li>
      <!-- slide item -->
      <li
        class="absolute bg-zinc-900 h-[22px] rounded-lg duration-300"
        :style="sliderStyle"
      ></li>
      <!-- categories -->
      <li
        v-for="(item, index) in data"
        :key="item.id"
        class="shrink-0 px-1.5 py-0.5 z-10 duration-200 last:mr-4"
        :class="currentCategoryIndex === index ? 'text-white' : ''"
        ref="itemRef"
        @click="onItemClick(index)"
      >
        {{ item.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { useScroll } from '@vueuse/core'
import { ref, watch } from 'vue'

interface Props {
  data: Array<{ id: string; name: string }>
}
defineProps<Props>()

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

const onItemClick = (index: number) => {
  currentCategoryIndex.value = index
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
</script>

<style scoped></style>
