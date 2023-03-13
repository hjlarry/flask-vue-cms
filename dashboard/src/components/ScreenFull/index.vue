<template>
  <div>
    <el-tooltip :content="$t('msg.navBar.screenfull')">
      <SvgIcon
        id="guide-full"
        :icon="isFullScreen ? 'exit-fullscreen' : 'fullscreen'"
        @click="onToggle"
      ></SvgIcon>
    </el-tooltip>
  </div>
</template>

<script setup>
import screenfull from 'screenfull'
import { ref } from 'vue'

import SvgIcon from '@/components/SvgIcon/index.vue'

const isFullScreen = ref(false)

function onToggle() {
  isFullScreen.value = !isFullScreen.value
  screenfull.toggle()
}
</script>

<style scoped></style>
