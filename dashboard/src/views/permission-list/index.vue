<template>
  <div class="">
    <el-card shadow="never">
      <el-table
        :data="permissonData"
        border
        row-key="id"
        default-expand-all
        :tree-props="{ children: 'children', hasChildren: 'hasChildren' }"
      >
        <el-table-column
          :label="$t('msg.permission.name')"
          prop="permission_name"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.permission.mark')"
          prop="permission_mark"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.permission.desc')"
          prop="permission_desc"
        ></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import { getPermissions } from '@/api/role'

const permissonData = ref([])
async function getPermissionList() {
  permissonData.value = await (await getPermissions()).data
}
getPermissionList()
</script>

<style lang="scss" scoped></style>
