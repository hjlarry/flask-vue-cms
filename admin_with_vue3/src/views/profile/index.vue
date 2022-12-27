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
  <el-row>
    <el-button>Default</el-button>
    <el-button type="primary">Primary</el-button>
    <el-button type="success">Success</el-button>
    <el-button type="info">Info</el-button>
    <el-button type="warning">Warning</el-button>
    <el-button type="danger">Danger</el-button>
  </el-row>
</template>

<script setup>
import { ref } from 'vue'

const currentPage1 = ref(5)
</script>

<style lang='scss' scoped></style>
