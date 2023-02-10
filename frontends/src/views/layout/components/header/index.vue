<template>
  <div
    class="h-header flex items-center px-2 py-1 border-b border-b-zinc-200 bg-white"
  >
    <img
      class="h-4 cursor-pointer mr-2"
      src="https://sponsors.vuejs.org/images/chrome_frameworks_fund.png"
      alt="logo"
    />
    <header-search class="mr-1 flex-1" />
    <header-theme class="mr-1" />
    <header-my />
  </div>
</template>

<script setup lang="ts">
import HeaderTheme from './header-theme.vue'
import HeaderMy from './header-my.vue'
import HeaderSearch from './header-search/index.vue'
</script>

<style scoped></style>
