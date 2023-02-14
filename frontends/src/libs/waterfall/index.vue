<template>
  <div
    class="relative"
    ref="containerTarget"
    :style="{ height: containerHeight + 'px' }"
  >
    <template v-if="columnWidth && data.length">
      <div
        class="absolute duration-500"
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

interface Props {
  data: Array<any>
  nodeKey?: string
  column?: number
  columnSpacing?: number
  rowSpacing?: number
  picturePreload?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  column: 2,
  columnSpacing: 20,
  rowSpacing: 20,
  picturePreload: true
})

const containerTarget = ref<HTMLElement>() // 容器对象
const containerHeight = ref(0) // 容器总高度
const containerWidth = ref(0) // 容器不含padding,margin,border的宽度,
const containerLeft = ref(0) // 容器的左边距，用于计算item的left
const columnWidth = ref(0) // 每列宽度
const columnHeightObj = ref<{ key: number; val: number }>() // 记录每列高度的容器，key是第几列, val是高度

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
})
</script>

<style scoped></style>
