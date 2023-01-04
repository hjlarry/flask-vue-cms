<template>
  <div>
    <el-card shadow="never" class="head-container">
      <div class="excel-btn">
        <el-button type="primary">{{ $t('msg.excel.importExcel') }}</el-button>
        <el-button type="success">{{ $t('msg.excel.exportExcel') }}</el-button>
      </div>
    </el-card>
    <el-card class="table-container">
      <el-table :data="tableData" border>
        <el-table-column label="#" type="index" width="50"></el-table-column>
        <el-table-column
          :label="$t('msg.excel.name')"
          prop="username"
        ></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getUsers } from '@/api/user'

const tableData = ref([])
const page = ref(1)
const total = ref(0)
const size = ref(2)

async function getUsersList() {
  const res = await getUsers({ page: page.value, size: size.value })
  tableData.value = res.data.users
  total.value = res.total
}
getUsersList()
</script>

<style lang="scss" scoped>
:deep(.head-container) .el-card__body {
  display: flex;
  .excel-btn {
    margin-left: auto;
  }
}
.table-container {
  margin-top: 20px;
}
</style>
