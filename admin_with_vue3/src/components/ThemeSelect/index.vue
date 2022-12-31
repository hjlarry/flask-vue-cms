<template>
  <div>
    <el-tooltip :content='$t("msg.navBar.themeChange")'>
      <svg-icon id='guide-theme' icon='change-theme' @click='openDialog'></svg-icon>
    </el-tooltip>
    <select-color v-model='dialogVisible'></select-color>
  </div>

</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import SelectColor from './SelectColor.vue'
import { ref } from 'vue'

const dialogVisible = ref(false)
const openDialog = () => {
  dialogVisible.value = true
}
</script>

<style scoped>

</style>
