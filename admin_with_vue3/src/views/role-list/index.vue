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
          #default="{ row }"
        >
          <el-button
            type="primary"
            size="small"
            @click="onShowDialog(row)"
            v-permission="['distributePermission']"
            >{{ $t('msg.role.assignPermissions') }}</el-button
          >
        </el-table-column>
      </el-table>
    </el-card>
    <show-permission
      v-model="permissionDialog"
      :role-id="selectRoleId"
    ></show-permission>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { getRoles } from '@/api/role'
import ShowPermission from './showPermission.vue'

const rolesData = ref([])
async function getRoleList() {
  rolesData.value = await (await getRoles()).data
}
getRoleList()

const permissionDialog = ref(false)
const selectRoleId = ref(NaN)
function onShowDialog(row) {
  permissionDialog.value = true
  selectRoleId.value = row.id
}
watch(permissionDialog, (val) => {
  if (!val) selectRoleId.value = NaN
})
</script>

<style lang="scss" scoped></style>
