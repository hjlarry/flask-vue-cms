<template>
  <div
    class="relative"
    ref="containerTarget"
    :style="{ height: containerHeight + 'px' }"
  >
    <template v-if="columnWidth && data.length">
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
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'
import { getMinHeightColumn, waitImgLoaded } from './helper'

interface Props {
  data: Array<any>
  nodeKey?: string
  column: number
  columnSpacing?: number
  rowSpacing?: number
  picturePreload?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  columnSpacing: 20,
  rowSpacing: 20,
  picturePreload: true
})

const containerTarget = ref<HTMLElement>() // 容器对象
const containerHeight = ref(0) // 容器总高度
const containerWidth = ref(0) // 容器不含padding,margin,border的宽度,
const containerLeft = ref(0) // 容器的左边距，用于计算item的left
const columnWidth = ref(0) // 每列宽度
const columnHeightArr = ref<Array<number>>([]) // 记录每列高度的容器, index是第几列, val是高度

const initColumnHeightObj = () => {
  for (let i = 0; i < props.column; i++) {
    columnHeightArr.value[i] = 0
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
})

// picturePreload为false时，应当在onMounted时渲染各个组件后，再去计算每个item的高度，否则item的高度计算不准确，会重叠起来
// picturePreload为true时，则可以不需要watch，直接在onMounted时computeItemHeight()即可
watch(
  () => props.data,
  () => {
    nextTick(() => {
      computeItemHeight()
    })
  },
  {
    immediate: true
  }
)

onUnmounted(() => {
  props.data.forEach((item) => {
    delete item._style
  })
})

// 所有item高度的集合
let itemHeights: any[] = []
const computeItemHeight = () => {
  itemHeights = []
  let itemElements = [...document.getElementsByClassName('m-waterfall-item')]
  const allImgs = itemElements.map((el: any) => {
    return el.getElementsByTagName('img')[0].src
  })

  function setLocation() {
    itemElements.forEach((el: any) => {
      itemHeights.push(el.offsetHeight)
    })
    setItemLocation()
    containerHeight.value = Math.max(...columnHeightArr.value)
  }

  if (props.picturePreload) {
    waitImgLoaded(allImgs).then(() => {
      setLocation()
    })
  } else {
    setLocation()
  }
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
  const column = getMinHeightColumn(columnHeightArr.value)
  return (
    column * (columnWidth.value + props.columnSpacing) + containerLeft.value
  )
}
const nextItemTop = () => Math.min(...columnHeightArr.value)
const increseHeight = (index: number) => {
  const column = getMinHeightColumn(columnHeightArr.value)
  columnHeightArr.value[column] += itemHeights[index] + props.rowSpacing
}
</script>

<style scoped></style>
