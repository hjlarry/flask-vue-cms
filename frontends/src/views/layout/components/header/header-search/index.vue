<template>
  <div>
    <searchPanel v-model="searchValue">
      <template #dropdown>
        <div class="p-2">dropdown</div>
      </template>
    </searchPanel>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

import searchPanel from './search-panel.vue'

const searchValue = ref('')
watch(searchValue, (val) => {
  console.log(val)
})
</script>

<style scoped></style>
