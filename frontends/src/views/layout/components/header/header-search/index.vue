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
        </div>
      </template>
    </searchPanel>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import searchPanel from './search-panel.vue'
import hintVue from './hint.vue'

const searchValue = ref('')
const onHintClickHandler = (item: string) => {
  searchValue.value = item
}
</script>

<style scoped></style>
