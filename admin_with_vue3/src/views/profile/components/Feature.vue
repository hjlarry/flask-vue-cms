<template>
  <el-collapse v-model="activeNames">
    <el-collapse-item
      v-for="item in features"
      :key="item.id"
      :title="item.title"
      :name="item.id"
    >
      <div v-html="item.content"></div>
    </el-collapse-item>
  </el-collapse>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  features: {
    type: Array,
    default: () => []
  }
})

const activeNames = ref('1')
</script>

<style lang="scss" scoped>
:deep(.el-collapse-item__header) {
  font-size: 16px;
  font-weight: bold;
  color: #303133;
}
.el-collapse-item {
  :deep(a) {
    color: #2d62f7;
    display: inline;
  }
}
</style>
