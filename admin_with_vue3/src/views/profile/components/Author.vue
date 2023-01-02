<template>
  <div class="author-container">
    <div class="header">
      <PanThumb
        :image="$store.getters.userInfo.avatar"
        height="60px"
        width="60px"
      >
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
