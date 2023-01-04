<template>
  <div>
    <el-card shadow="hover" class="head-container">
      <div class="excel-btn">
        <el-button type="primary" @click="goImport">{{
          $t('msg.excel.importExcel')
        }}</el-button>
        <el-button type="success">{{ $t('msg.excel.exportExcel') }}</el-button>
      </div>
    </el-card>
    <el-card class="table-container" shadow="never">
      <el-table :data="tableData" border>
        <el-table-column
          label="#"
          type="index"
          width="50"
          align="center"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.excel.name')"
          prop="username"
        ></el-table-column>
        <el-table-column :label="$t('msg.excel.avatar')" align="center">
          <template #default="{ row }">
            <el-avatar :src="row.avatar" size="default"></el-avatar>
          </template>
        </el-table-column>
        <el-table-column
          :label="$t('msg.excel.role')"
          prop="role"
          align="center"
        >
          <template #default="{ row }">
            <el-tag v-for="item in row.roles" :key="item.id" size="small">
              {{ item.name }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column
          :label="$t('msg.excel.openTime')"
          prop="openTime"
          align="center"
        >
          <template #default="{ row }">
            {{ $filters.dateFilter(row.openTime) }}
          </template>
        </el-table-column>
        <el-table-column :label="$t('msg.excel.action')" align="center">
          <template #default>
            <el-button type="primary" size="small">{{
              $t('msg.excel.show')
            }}</el-button>
            <el-button type="info" size="small">{{
              $t('msg.excel.showRole')
            }}</el-button>
            <el-button type="danger" size="small">{{
              $t('msg.excel.remove')
            }}</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <el-pagination
      class="pagination"
      v-model:current-page="page"
      v-model:page-size="size"
      :page-sizes="[2, 10, 30]"
      layout="sizes, prev, pager, next, total"
      :total="total"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getUsers } from '@/api/user'
import { useRouter } from 'vue-router'

const tableData = ref([])
const page = ref(1)
const total = ref(0)
const size = ref(20)

async function getUsersList() {
  const res = await getUsers({ page: page.value, per_page: size.value })
  tableData.value = res.data.users
  total.value = res.data.pagination.total
}
getUsersList()

function handleSizeChange(val) {
  size.value = val
  getUsersList()
}

function handleCurrentChange(val) {
  page.value = val
  getUsersList()
}

const router = useRouter()
function goImport() {
  router.push('/user/import')
}
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

.pagination {
  margin: 20px auto;
  display: flex;
  justify-content: center;
}
</style>
