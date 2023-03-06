<template>
  <div
    class="h-header flex items-center px-2 py-1 border-b border-b-zinc-200 bg-white dark:bg-zinc-800 dark:border-b-zinc-700"
  >
    <m-svg-icon
      name="wei-bo"
      class="h-4 w-4 cursor-pointer mr-2"
      @click="router.push('/')"
    ></m-svg-icon>
    <header-search class="mr-1 flex-1" />
    <header-theme class="mr-1" />
    <header-my />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

import HeaderTheme from './header-theme.vue'
import HeaderMy from './header-my.vue'
import HeaderSearch from './header-search/index.vue'

const router = useRouter()
</script>

<style scoped></style>
