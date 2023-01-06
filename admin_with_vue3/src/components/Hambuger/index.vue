<template>
  <div class="hambuger-container" @click="toggerClick">
    <svg-icon id="guide-hamburger" class="hambuger" :icon="icon" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import SvgIcon from '@/components/SvgIcon/index.vue'
import { appStore } from '@/store/app_store'

const aStore = appStore()
const toggerClick = () => {
  aStore.triggerSidebarOpened()
}
const icon = computed(() =>
  aStore.sidebarOpened ? 'hamburger-opened' : 'hamburger-closed'
)
</script>

<style lang="scss" scoped>
.hambuger-container {
  padding: 0 16px;

  .hambuger {
    width: 20px;
    height: 20px;
    margin: 0 auto;
  }
}
</style>
