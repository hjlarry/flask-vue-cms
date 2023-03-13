<template>
  <el-dialog
    :model-value="modelValue"
    @close="closed"
    :title="$t('msg.excel.roleDialogTitle')"
  >
    <el-tree
      :data="allPermissions"
      :props="defaultProps"
      ref="treeRef"
      show-checkbox
      node-key="id"
      default-expand-all
      check-strictly
    >
    </el-tree>
    <template #footer>
      <span>
        <el-button @click="closed">{{ $t('msg.universal.cancel') }}</el-button>
        <el-button @click="onConfirm" type="primary">{{
          $t('msg.universal.confirm')
        }}</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'

import {
  getPermissions,
  getRolePermission,
  setRolePermission
} from '@/api/role'

const props = defineProps({
  modelValue: {
    required: true,
    type: Boolean
  },
  roleId: {
    required: true,
    type: Number
  }
})
const emits = defineEmits(['update:modelValue'])

function closed() {
  emits('update:modelValue', false)
}

const i18n = useI18n()

async function onConfirm() {
  await setRolePermission(props.roleId, {
    permissions: treeRef.value.getCheckedKeys()
  })
  ElMessage.success(i18n.t('msg.role.updateRoleSuccess'))
  treeRef.value.setCheckedKeys([])
  closed()
}

const defaultProps = ref({
  children: 'children',
  label: 'permission_name'
})

const allPermissions = ref([])
const treeRef = ref(null)

async function getPermissionData() {
  allPermissions.value = (await getPermissions()).data
  const res = await getRolePermission(props.roleId)
  treeRef.value.setCheckedKeys(res.data)
}

watch(
  () => props.roleId,
  (value) => {
    if (value) getPermissionData()
  }
)
</script>

<style scoped></style>
