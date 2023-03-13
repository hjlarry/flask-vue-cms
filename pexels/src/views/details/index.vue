<template>
  <div v-if="data.loaded" class="bg-zinc-200 dark:bg-zinc-800 h-full w-full">
    <bigPictureVue :data="data"></bigPictureVue>
  </div>
</template>

<script setup lang="ts">
// 仅刷新时进入该页面
import { useRoute } from 'vue-router'
import { ref } from 'vue'

import { getPexel } from '@/api/home'
import bigPictureVue from './picture.vue'

const route = useRoute()
const data = ref({ loaded: false })
const getData = async () => {
  const res = await getPexel({ id: route.params.id })
  data.value = res as any
  data.value.loaded = true
}
getData()
</script>

<style scoped></style>
