<template>
  <div>
    <el-tooltip :content="$t('msg.navBar.themeChange')">
      <svg-icon
        id="guide-theme"
        icon="change-theme"
        @click="openDialog"
      ></svg-icon>
    </el-tooltip>
    <select-color v-model:dialogVisable="dialogVisable"></select-color>
  </div>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import SelectColor from './SelectColor.vue'
import { ref } from 'vue'

const dialogVisable = ref(false)
const openDialog = () => {
  dialogVisable.value = true
}
</script>

<style scoped></style>
