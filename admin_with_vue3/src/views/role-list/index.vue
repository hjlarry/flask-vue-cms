<template>
  <div class="">
    <el-card shadow="never">
      <el-table :data="rolesData" border>
        <el-table-column
          :label="$t('msg.role.index')"
          type="index"
          width="120"
          align="center"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.role.name')"
          prop="title"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.role.desc')"
          prop="description"
        ></el-table-column>
        <el-table-column
          :label="$t('msg.role.action')"
          prop="action"
          align="center"
        >
          <el-button type="primary" size="small">{{
            $t('msg.role.assignPermissions')
          }}</el-button>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { getRoles } from '@/api/role'

const rolesData = ref([])
async function getRoleList() {
  rolesData.value = await (await getRoles()).data
}
getRoleList()
</script>

<style lang="scss" scoped></style>
