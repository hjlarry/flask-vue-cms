<template>
  <div
    class="relative"
    ref="containerTarget"
    :style="{ height: containerHeight + 'px' }"
  >
    <template v-if="data.length">
      <div
        class="m-waterfall-item absolute duration-500"
        v-for="(item, index) in data"
        :style="{
          width: columnWidth + 'px',
          left: item._style?.left + 'px',
          top: item._style?.top + 'px'
        }"
        :key="nodeKey ? item[nodeKey] : index"
      >
        <slot :item="item" :width="columnWidth" :index="index" />
      </div>
    </template>
    <div v-else>loading...</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getMinHeightColumn, getMinHeight, getMaxHeight } from './helper'

interface Props {
  data: Array<any>
  nodeKey?: string
  column?: number
  columnSpacing?: number
  rowSpacing?: number
  picturePreload?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  column: 5,
  columnSpacing: 20,
  rowSpacing: 20,
  picturePreload: true
})

const containerTarget = ref<HTMLElement>() // 容器对象
const containerHeight = ref(0) // 容器总高度
const containerWidth = ref(0) // 容器不含padding,margin,border的宽度,
const containerLeft = ref(0) // 容器的左边距，用于计算item的left
const columnWidth = ref(0) // 每列宽度
const columnHeightObj = ref({}) // 记录每列高度的容器，{key: val}, key是第几列, val是高度

const initColumnHeightObj = () => {
  for (let i = 0; i < props.column; i++) {
    columnHeightObj.value[i] = 0
  }
}

const getContainerWidth = () => {
  const { paddingLeft, paddingRight } = getComputedStyle(
    containerTarget.value!,
    null
  )
  containerLeft.value = parseFloat(paddingLeft)
  containerWidth.value =
    containerTarget.value?.offsetWidth! -
    parseFloat(paddingLeft) -
    parseFloat(paddingRight)
}

const getColumnWidth = () => {
  // 计算每列宽度，就是把容器的宽度算出来，然后减去所有的间距，再除以列数
  getContainerWidth()
  const columnSpaceTotal = (props.column - 1) * props.columnSpacing
  columnWidth.value = (containerWidth.value - columnSpaceTotal) / props.column
}

onMounted(() => {
  getColumnWidth()
  initColumnHeightObj()
  getItemHeight()
})

// 所有item高度的集合
let itemHeights: any[] = []
const getItemHeight = () => {
  itemHeights = []
  let itemElements = [...document.getElementsByClassName('m-waterfall-item')]
  itemElements.forEach((el: any) => {
    itemHeights.push(el.offsetHeight)
  })
  setItemLocation()
  containerHeight.value = getMaxHeight(columnHeightObj.value)
}

const setItemLocation = () => {
  props.data.forEach((item, index) => {
    if (item._style) return
    item._style = {}
    item._style.left = nextItemLeft()
    item._style.top = nextItemTop()
    increseHeight(index)
  })
}

const nextItemLeft = () => {
  const column = getMinHeightColumn(columnHeightObj.value)
  return (
    column * (columnWidth.value + props.columnSpacing) + containerLeft.value
  )
}
const nextItemTop = () => getMinHeight(columnHeightObj.value)
const increseHeight = (index: number) => {
  const column = getMinHeightColumn(columnHeightObj.value)
  columnHeightObj.value[column] += itemHeights[index] + props.rowSpacing
}
</script>

<style scoped></style>
