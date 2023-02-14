<template>
  <div>
    <itemVue v-for="item in pexelsList" :key="item.id" :data="item" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { getPexels } from '@/api/home'
import itemVue from './item.vue'

const pexelsList = ref([])

getPexels().then((res: any) => {
  pexelsList.value = res.list
})
</script>

<style scoped></style>
