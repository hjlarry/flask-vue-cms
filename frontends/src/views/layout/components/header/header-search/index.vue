<template>
  <div>
    <searchPanel v-model="searchValue">
      <template #dropdown>
        <div>
          <hintVue
            v-show="searchValue"
            :userInput="searchValue"
            @click="onHintClickHandler"
          ></hintVue>
          <historyVue v-show="!searchValue"></historyVue>
        </div>
      </template>
    </searchPanel>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { searchStore } from '@/stores/search'
import searchPanel from './search-panel.vue'
import hintVue from './hint.vue'
import historyVue from './history.vue'

const sStore = searchStore()

const searchValue = ref('')
const onHintClickHandler = (item: string) => {
  searchValue.value = item
  sStore.addHistory(item)
}
</script>

<style scoped></style>
