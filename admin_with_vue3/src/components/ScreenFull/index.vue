<template>
  <div>
    <el-tooltip :content='$t("msg.navBar.screenfull")'>
      <svg-icon id='guide-full' :icon='isFullScreen ? "exit-fullscreen": "fullscreen"' @click='onToggle'></svg-icon>
    </el-tooltip>
  </div>
</template>

<script setup>
import screenfull from 'screenfull'

import SvgIcon from '@/components/SvgIcon/index.vue'
import { ref } from 'vue'

const isFullScreen = ref(false)

function onToggle() {
  isFullScreen.value = !isFullScreen.value
  screenfull.toggle()
}

</script>

<style scoped>

</style>
