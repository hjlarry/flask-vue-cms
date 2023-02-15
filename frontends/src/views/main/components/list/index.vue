<template>
  <div>
    <m-waterfall
      :data="pexelsList"
      :column="isMoibleDevice ? 2 : 5"
      :picture-preload="false"
      class="px-1"
    >
      <template v-slot="{ item, width }">
        <itemVue :data="item" :width="width" />
      </template>
    </m-waterfall>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

import { getPexels } from '@/api/home'
import { isMoibleDevice } from '@/utils/flexiable'
import itemVue from './item.vue'

const pexelsList = ref([])

getPexels().then((res: any) => {
  pexelsList.value = res.list
})
</script>

<style scoped></style>
