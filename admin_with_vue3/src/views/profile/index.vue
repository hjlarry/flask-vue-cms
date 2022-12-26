<template>
  <div class=''>
    {{ $t('msg.route.profile') }}
  </div>
  <el-pagination
    v-model:current-page='currentPage1'
    :page-size='100'
    layout='total, prev, pager, next'
    :total='1000'
  />
</template>

<script setup>
import { ref } from 'vue'

const currentPage1 = ref(5)
</script>

<style lang='scss' scoped></style>
