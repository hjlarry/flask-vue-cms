<template>
  <el-timeline>
    <el-timeline-item
      v-for="item in chapterData"
      :key="item.id"
      :timestamp="item.timestamp"
      placement="top"
    >
      <el-card>
        <h4>{{ item.content }}</h4>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</template>

<script setup>
import { ref } from 'vue'
import { getChapter } from '@/api/user'

const chapterData = ref([])
const getChapterData = async () => {
  const res = await getChapter()
  chapterData.value = res.data
}
getChapterData()
</script>

<style scoped></style>
