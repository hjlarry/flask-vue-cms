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
    <Transition
      :css="false"
      @before-enter="beforeEnter"
      @enter="enter"
      @leave="leave"
    >
      <bigPictureVue v-if="isBigVisible" :data="currentPicData" />
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useEventListener } from '@vueuse/core'
import { gsap } from 'gsap'

import { getPexels } from '@/api/home'
import { isMobileDevice } from '@/utils/flexiable'
import { categoryStore } from '@/stores/category'
import { searchStore } from '@/stores/search'
import itemVue from './item.vue'
import bigPictureVue from '../../details/picture.vue'

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
const currentPicPos = ref({ left: 0, top: 0 })
const isBigVisible = ref(false)
const onItemClick = (item: any) => {
  history.pushState(null, '', `/pictures/${item.data.id}`)
  currentPicData.value = item.data
  currentPicPos.value = item.location
  isBigVisible.value = true
}

useEventListener('popstate', () => {
  isBigVisible.value = false
})

const beforeEnter = (el: HTMLElement) => {
  gsap.set(el, {
    translateX: currentPicPos.value.left,
    translateY: currentPicPos.value.top,
    scaleX: 0,
    scaleY: 0,
    transformOrigin: '0 0',
    opacity: 0
  })
}
const enter = (el: HTMLElement, done: any) => {
  gsap.to(el, {
    duration: 0.5,
    scaleX: 1,
    scaleY: 1,
    opacity: 1,
    translateX: 0,
    translateY: 0,
    onComplete: done
  })
}
const leave = (el: HTMLElement, done: any) => {
  gsap.to(el, {
    duration: 0.5,
    scaleX: 0,
    scaleY: 0,
    opacity: 0,
    translateX: currentPicPos.value.left,
    translateY: currentPicPos.value.top
  })
}

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
