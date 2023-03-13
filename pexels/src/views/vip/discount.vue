<template>
  <div
    v-if="isCountDown"
    class="bg-orange-100 text-red-500 font-bold text-xs text-center py-0.5 flex items-center justify-center xl:border-t border-orange-600"
  >
    <m-svg-icon
      name="countdown"
      class="w-1.5 h-1.5 mr-1"
      fillClass="fill-red-600"
    ></m-svg-icon>
    <span
      >限时特惠 | 距离优惠结束仅剩
      <m-count-down
        :time="60 * 60 - 1"
        class="inline-block"
        @finish="timeCountDown"
      ></m-count-down
    ></span>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isCountDown = ref(true)
const timeCountDown = () => {
  isCountDown.value = false
}
</script>

<style scoped></style>
