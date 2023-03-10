<template>
  <div
    class="h-full dark:bg-zinc-800 overflow-auto top-0 left-0 w-screen fixed md:static scrollbar-thin scrollbar-thumb-rounded-md scrollbar-thumb-zinc-200 dark:scrollbar-thumb-zinc-500 scrollbar-track-transparent"
    ref="containerTarget"
  >
    <navigationVue />
    <div class="max-w-screen-xl mx-auto relative bg-white m-1 xl:mt-4">
      <listVue />
    </div>
    <div
      v-if="isMobileDevice"
      class="fixed mx-auto left-0 right-0 w-[220px] bottom-6 bg-white rounded-full shadow flex items-center justify-between px-2 py-1"
    >
      <div class="flex flex-col items-center w-5" @click="router.push('/')">
        <m-svg-icon name="home" class="w-2 h-2" fillClass="fill-zinc-900" />
        <span class="text-sm mt-0.5">首页</span>
      </div>
      <div
        class="flex flex-col items-center w-5"
        v-if="uStore.token"
        @click="onVipClick"
      >
        <m-svg-icon name="vip" class="w-2 h-2" fillClass="fill-zinc-400" />
        <span class="text-sm mt-0.5">VIP</span>
      </div>
      <div class="flex flex-col items-center w-5" @click="onMyClick">
        <m-svg-icon name="profile" class="w-2 h-2" fillClass="fill-zinc-400" />
        <span class="text-sm mt-0.5">{{ uStore.token ? '我的' : '登录' }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'home'
}
</script>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref, onActivated } from 'vue'
import { useScroll } from '@vueuse/core'

import { isMobileDevice } from '@/utils/flexiable'
import { userStore } from '@/stores/user'
import { appStore } from '@/stores/app'
import navigationVue from './components/navigation/index.vue'
import listVue from './components/list/index.vue'

const router = useRouter()
const uStore = userStore()
const aStore = appStore()
const onMyClick = () => {
  if (uStore.token) {
    aStore.changeRouterType('push')
    router.push('/profile')
  } else {
    router.push('/login')
  }
}

const onVipClick = () => {
  aStore.changeRouterType('push')
  router.push('/vip')
}

const containerTarget = ref()
const { y: containerScrollTop } = useScroll(containerTarget)
onActivated(() => {
  if (!containerScrollTop.value) return
  containerTarget.value.scrollTop = containerScrollTop.value
})
</script>

<style scoped>
.scrollbar-thin {
  overflow: auto;
}
</style>
