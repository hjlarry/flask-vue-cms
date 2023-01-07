<template>
  <el-dialog
    :model-value="modelValue"
    @close="closed"
    :title="$t('msg.excel.roleDialogTitle')"
  >
    <el-checkbox-group v-model="currentUserRoles">
      <el-checkbox
        v-for="item in allRoles"
        :key="item.id"
        :label="item.title"
      ></el-checkbox>
    </el-checkbox-group>
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
import { getRoles } from '@/api/role'
import { userRole, updateUserRole } from '@/api/user'
import { ElMessage } from 'element-plus'

const props = defineProps({
  modelValue: {
    required: true,
    type: Boolean
  },
  userId: {
    type: Number,
    required: true
  }
})
const emits = defineEmits(['update:modelValue', 'updateRole'])

function closed() {
  emits('update:modelValue', false)
}

async function onConfirm() {
  const roles = currentUserRoles.value.map((title) => {
    return allRoles.value.find((role) => role.title === title)
  })
  await updateUserRole(props.userId, roles)
  ElMessage.success('更新成功')
  closed()
  emits('updateRole')
}

const allRoles = ref([])
const currentUserRoles = ref([])

async function getRoleData() {
  allRoles.value = (await getRoles()).data
  const res = (await userRole(props.userId)).data
  currentUserRoles.value = res.role.map((item) => item.title)
}

// 组件初始状态时，useId为null，监听到其有值时再获取数据
watch(
  () => props.userId,
  (val) => {
    if (val) {
      getRoleData()
    }
  }
)
</script>

<style scoped></style>
