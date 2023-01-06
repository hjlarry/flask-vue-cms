<template>
  <div class="app-main">
    <router-view v-slot="{ Component, route }">
      <transition name="fade-transform" mode="out-in">
        <component :is="Component" :key="route.path"></component>
      </transition>
    </router-view>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { watch } from 'vue'
import { generateRouteTitle, watchSwitchLang } from '@/i18n'
import { shouldInTagsView } from '@/utils/tags'
import { appStore } from '@/store/app_store'

const route = useRoute()
const aStore = appStore()

function getTitle(route) {
  let title
  if (!route.meta) {
    const pathArr = route.path.split('/')
    title = pathArr[pathArr.length - 1]
  } else {
    title = generateRouteTitle(route.meta.title)
  }
  return title
}

watch(
  route,
  (to, from) => {
    if (!shouldInTagsView(to.path)) return
    const { fullPath, path, query, params, meta, name } = to
    aStore.addTag({
      fullPath,
      path,
      query,
      params,
      meta,
      name,
      title: getTitle(to)
    })
  },
  {
    immediate: true
  }
)

watchSwitchLang(() => {
  aStore.tagsView.forEach((route, index) => {
    aStore.changeTagsView({
      index,
      tag: {
        ...route,
        title: getTitle(route)
      }
    })
  })
})
</script>

<style scoped>
.app-main {
  min-height: calc(100vh - 93px);
  width: 100%;
  overflow: hidden;
  padding: 104px 20px 20px 20px;
  box-sizing: border-box;
}
</style>
