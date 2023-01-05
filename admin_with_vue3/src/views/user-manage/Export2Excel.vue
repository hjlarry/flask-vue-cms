<template>
  <el-dialog
    :title="$t('msg.excel.title')"
    width="30%"
    :model-value="dialogVisable"
    @close="close"
  >
    <el-input
      v-model="fileName"
      :placeholder="$t('msg.excel.placeholder')"
      clearable
    ></el-input>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="close">{{ $t('msg.excel.close') }}</el-button>
        <el-button type="primary" @click="export2Excel" :loading="loading">
          {{ $t('msg.excel.confirm') }}
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { utils, writeFileXLSX } from 'xlsx'

const props = defineProps({
  dialogVisable: {
    type: Boolean,
    required: true
  },
  tableData: {
    type: Array,
    required: true
  }
})

const i18n = useI18n()
const fileName = ref('')
fileName.value = i18n.t('msg.excel.defaultName')
const emits = defineEmits(['update:dialogVisable'])
function close() {
  emits('update:dialogVisable', false)
}

const loading = ref(false)
function export2Excel() {
  loading.value = true
  const ws = utils.json_to_sheet(props.tableData)
  const wb = utils.book_new()
  utils.book_append_sheet(wb, ws, 'Data')
  writeFileXLSX(wb, fileName.value + '.xlsx')
  loading.value = false
  close()
}
</script>

<style scoped></style>
