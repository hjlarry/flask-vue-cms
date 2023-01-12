<template>
  <el-timeline>
    <el-timeline-item
      v-for="item in timelineData"
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

import { getTimeline } from '@/api/user'

const timelineData = ref([])
const getTimelineData = async () => {
  const res = await getTimeline()
  timelineData.value = res.data
}
getTimelineData()
</script>

<style scoped></style>
