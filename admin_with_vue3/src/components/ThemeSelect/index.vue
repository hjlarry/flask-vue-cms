<template>
  <div>
    <el-tooltip :content="$t('msg.navBar.themeChange')">
      <SvgIcon
        id="guide-theme"
        icon="change-theme"
        @click="openDialog"
      ></SvgIcon>
    </el-tooltip>
    <select-color v-model:dialogVisable="dialogVisable"></select-color>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import SvgIcon from '@/components/SvgIcon/index.vue'
import SelectColor from './SelectColor.vue'

const dialogVisable = ref(false)
const openDialog = () => {
  dialogVisable.value = true
}
</script>

<style scoped></style>
