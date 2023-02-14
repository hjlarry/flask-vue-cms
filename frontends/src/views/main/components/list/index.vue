<template>
  <div>
    <m-waterfall :data="pexelsList">
      <template v-slot="{ item }">
        <itemVue :data="item" />
      </template>
    </m-waterfall>
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
