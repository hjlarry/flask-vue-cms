<template>
  <div>
    <el-card shadow="hover" class="head-container">
      <div class="excel-btn">
        <el-button
          type="primary"
          @click="goImport"
          v-permission="['importUser']"
          >{{ $t('msg.excel.importExcel') }}</el-button
        >
        <el-button type="success" @click="onExport">{{
          $t('msg.excel.exportExcel')
        }}</el-button>
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
          prop="roles"
          align="center"
        >
          <template #default="{ row }">
            <el-tag v-for="item in row.roles" :key="item.id" size="small">
              {{ item.title }}
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
          <template #default="{ row }">
            <el-button type="primary" size="small" @click="onShowClick(row)">{{
              $t('msg.excel.show')
            }}</el-button>
            <el-button
              type="info"
              size="small"
              @click="onShowRole(row)"
              v-permission="['distributeRole']"
              >{{ $t('msg.excel.showRole') }}</el-button
            >
            <el-button
              type="danger"
              size="small"
              @click="onRemoveClick(row)"
              v-permission="['removeUser']"
              >{{ $t('msg.excel.remove') }}</el-button
            >
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
    <Export2Excel
      v-model:dialog-visable="export2ExcelVisiable"
      :table-data="tableData"
    ></Export2Excel>
    <show-role
      v-model="roleDialogVisible"
      :user-id="selectUserId"
      @updateRole="getUsersList"
    ></show-role>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useI18n } from 'vue-i18n'

import { getUsers, userDelete } from '@/api/user'
import Export2Excel from '@/views/user-manage/Export2Excel.vue'
import ShowRole from './showRole.vue'

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

const i18n = useI18n()
function onRemoveClick(row) {
  ElMessageBox.confirm(
    i18n.t('msg.excel.dialogTitle1') +
      row.username +
      i18n.t('msg.excel.dialogTitle2'),
    {
      type: 'warning'
    }
  )
    .then(async () => {
      await userDelete(row.id)
      ElMessage.success(i18n.t('msg.excel.removeSuccess'))
      await getUsersList()
    })
    .catch(() => {})
}

function onShowClick(row) {
  router.push({ name: 'userInfo', params: { id: row.id } })
}

const export2ExcelVisiable = ref(false)
function onExport() {
  export2ExcelVisiable.value = true
}

const roleDialogVisible = ref(false)
const selectUserId = ref(NaN)
function onShowRole(row) {
  roleDialogVisible.value = true
  selectUserId.value = row.id
}

// 确保关闭弹窗再次打开时仍然能去获取一次数据
watch(roleDialogVisible, (val) => {
  if (!val) selectUserId.value = NaN
})
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
