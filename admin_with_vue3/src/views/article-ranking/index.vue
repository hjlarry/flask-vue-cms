<template>
  <div>
    <el-card shadow="hover" class="header-container">
      <el-checkbox-group v-model="selectedDynamicLabel">
        <el-checkbox
          v-for="(item, index) in dynamicData"
          :key="index"
          :label="item.label"
        >
          {{ item.label }}
        </el-checkbox>
      </el-checkbox-group>
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
          v-for="(item, index) in tableColumns"
          :label="item.label"
          :prop="item.prop"
          :key="index"
        >
          <template #default="{ row }" v-if="item.prop === 'publicDate'">
            {{ $filters.relativeTime(row.publicDate) }}
          </template>
          <template #default="{ row }" v-else-if="item.prop === 'action'">
            <el-button type="primary" size="small" @click="onShowClick(row)"
              >{{ $t('msg.article.show') }}
            </el-button>
            <el-button type="danger" size="small" @click="onRemoveClick(row)"
              >{{ $t('msg.article.remove') }}
            </el-button>
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
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useI18n } from 'vue-i18n'

import { getArticles, articleDelete } from '@/api/article'
import { selectedDynamicLabel, dynamicData, tableColumns } from './dynamicTable'

const tableData = ref([])
const page = ref(1)
const total = ref(0)
const size = ref(20)

async function getArticleList() {
  const res = await getArticles({ page: page.value, per_page: size.value })
  tableData.value = res.data.articles
  total.value = res.data.pagination.total
}

getArticleList()

function handleSizeChange(val) {
  size.value = val
  getArticleList()
}

function handleCurrentChange(val) {
  page.value = val
  getArticleList()
}

const router = useRouter()
const i18n = useI18n()

function onRemoveClick(row) {
  ElMessageBox.confirm(
    i18n.t('msg.excel.dialogTitle1') +
      row.title +
      i18n.t('msg.excel.dialogTitle2'),
    {
      type: 'warning'
    }
  )
    .then(async () => {
      await articleDelete(row.id)
      ElMessage.success(i18n.t('msg.excel.removeSuccess'))
      await getArticleList()
    })
    .catch(() => {})
}

function onShowClick(row) {
  router.push(`/article/${row.id}`)
}
</script>

<style lang="scss" scoped>
.table-container {
  margin-top: 20px;
}

.pagination {
  margin: 20px auto;
  display: flex;
  justify-content: center;
}
</style>
