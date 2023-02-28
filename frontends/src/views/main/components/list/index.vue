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
          <itemVue :data="item" :width="width" @click="onItemClick" />
        </template>
      </m-waterfall>
    </m-infinite-scroll-down>
    <bigPictureVue v-if="isBigVisible" :data="currentPicData"></bigPictureVue>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

import { getPexels } from '@/api/home'
import { isMobileDevice } from '@/utils/flexiable'
import { categoryStore } from '@/stores/category'
import { searchStore } from '@/stores/search'
import itemVue from './item.vue'
import bigPictureVue from '../../details/picture.vue'
import { useEventListener } from '@vueuse/core'

const pexelsList = ref<any>([])
const isLoading = ref(false)
const isFinished = ref(false)
const cStore = categoryStore()
const sStore = searchStore()
let query = {
  page: 0,
  pageSize: 15,
  id: cStore.currentCategory.id,
  searchText: ''
}

const loadMore = async () => {
  if (isFinished.value) return
  query.page += 1

  const res = await getPexels(query)
  pexelsList.value.push(...res.list)

  if (pexelsList.value.length === res.total) {
    isFinished.value = true
  }
  isLoading.value = false
}

const resetQuery = (newQuery: any) => {
  query = { ...query, ...newQuery }
  isFinished.value = false
  pexelsList.value = []
}

const currentPicData = ref({})
const isBigVisible = ref(false)
const onItemClick = (item: any) => {
  console.log(item, 121)
  history.pushState(null, '', `/pins/${item.id}`)
  currentPicData.value = item
  isBigVisible.value = true
}

useEventListener('popstate', () => {
  isBigVisible.value = false
})

watch(
  () => cStore.currentCategory,
  (val) => {
    resetQuery({ id: val.id, page: 0 })
  }
)

watch(
  () => sStore.currentSearch,
  (val) => {
    resetQuery({ searchText: val, page: 0 })
  }
)
</script>

<style scoped></style>
