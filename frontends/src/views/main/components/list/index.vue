<template>
  <div>
    <m-infinite-scroll-down
      v-model="isLoading"
      :is-finished="isFinished"
      @loadMore="loadMore"
    >
      <m-waterfall
        :data="pexelsList"
        :column="isMobileDevice ? 2 : 5"
        :picture-preload="false"
        class="px-1"
      >
        <template v-slot="{ item, width }">
          <itemVue :data="item" :width="width" />
        </template>
      </m-waterfall>
    </m-infinite-scroll-down>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { getPexels } from '@/api/home'
import { isMobileDevice } from '@/utils/flexiable'
import itemVue from './item.vue'

const pexelsList = ref([])
const isLoading = ref(false)
const isFinished = ref(false)
let query = {
  page: 1,
  pageSize: 15
}

const loadMore = async () => {
  if (isFinished.value) return
  if (pexelsList.value.length) {
    query.page += 1
  }

  const res = await getPexels(query)
  if (query.page === 1) {
    pexelsList.value = res.list
  } else {
    pexelsList.value.push(...res.list)
  }
  console.log(pexelsList.value.length, 12321)
  if (pexelsList.value.length === res.total) {
    isFinished.value = true
  }
  isLoading.value = false
}
</script>

<style scoped></style>
