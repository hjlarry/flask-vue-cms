<template>
  <div>
    <svg-icon icon='change-theme' @click='openDialog'></svg-icon>
    <select-color v-model='dialogVisible'></select-color>
  </div>

</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import SelectColor from './components/SelectColor.vue'
import { ref } from 'vue'

const dialogVisible = ref(false)
const openDialog = () => {
  dialogVisible.value = true
}
</script>

<style scoped>

</style>
