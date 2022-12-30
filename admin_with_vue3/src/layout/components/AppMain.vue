<template>
  <div class='app-main'>
    <router-view></router-view>
  </div>
</template>

<script setup>

import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import { watch } from 'vue'
import { generateRouteTitle } from '@/i18n'
import { shouldInTagsView } from '@/utils/tags'

const route = useRoute()
const store = useStore()

function getTitle(route) {
  let title = ''
  if (!route.meta) {
    const pathArr = route.path.split('/')
    title = pathArr[pathArr.length - 1]
  } else {
    title = generateRouteTitle(route.meta.title)
  }
  return title
}

watch(route, (to, from) => {
  if (!shouldInTagsView(to.path)) return
  const {
    fullPath,
    path,
    query,
    params,
    meta,
    name
  } = to
  store.commit('app/addTag', {
    fullPath,
    path,
    query,
    params,
    meta,
    name,
    title: getTitle(to)
  })
  console.log(store.getters.tagsViewList, 123)
}, {
  immediate: true
})

</script>

<style scoped>
.app-main {
  min-height: calc(100vh - 60px);
  width: 100%;
  overflow: hidden;
  padding: 95px 20px 20px 20px;
  box-sizing: border-box;
}
</style>
