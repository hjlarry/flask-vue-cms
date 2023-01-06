<template>
  <div class="author-container">
    <div class="header">
      <PanThumb :image="uStore.userInfo.avatar" height="60px" width="60px">
        {{ $t('msg.profile.name') }}
      </PanThumb>
    </div>
    <div class="info">
      {{ $t('msg.profile.Introduction') }}
    </div>
  </div>
</template>

<script setup>
import PanThumb from '@/components/PanThumb/index.vue'
import { userStore } from '@/store/user_store'
const uStore = userStore()
</script>

<style scoped>
.author-container {
  display: flex;
  align-items: center;
}
.info {
  margin-left: 20px;
}
</style>
