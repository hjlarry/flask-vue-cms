<template>
  <div
    class="h-full dark:bg-zinc-800 overflow-auto top-0 left-0 w-screen fixed md:static"
  >
    <navigationVue />
    <div class="max-w-screen-xl mx-auto relative m-1 xl:mt-4">
      <listVue />
    </div>
  </div>
</template>

<script setup lang="ts">
import navigationVue from './components/navigation/index.vue'
import listVue from './components/list/index.vue'
</script>
