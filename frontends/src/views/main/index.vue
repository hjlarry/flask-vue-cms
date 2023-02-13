<template>
  <div class="h-full dark:bg-zinc-800">
    <navigationVue />
  </div>
</template>

<script setup lang="ts">
import navigationVue from './components/navigation/index.vue'
import { getPexels } from '@/api/home'

getPexels().then((res) => {
  console.log(res, 456)
})
</script>
