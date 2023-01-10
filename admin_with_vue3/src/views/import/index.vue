<template>
  <el-upload
    class="upload"
    drag
    :auto-upload="false"
    :show-file-list="false"
    :on-change="handleUpload"
    v-loading="loading"
  >
    <SvgIcon icon="cloud-upload"></SvgIcon>
    <div class="el-upload__text">
      {{ $t('msg.uploadExcel.upload') }}
    </div>
  </el-upload>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { read, utils } from 'xlsx'
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'

import SvgIcon from '@/components/SvgIcon/index.vue'
import { userBatchImport } from '@/api/user'

const loading = ref(false)
const i18n = useI18n()
const router = useRouter()

function isExcel(file) {
  return /\.(xlsx|xls|csv)$/.test(file.name)
}

function handleUpload(file) {
  if (!isExcel(file)) {
    ElMessage.error('文件类型错误')
    return false
  }
  readData(file.raw)
}

function readData(file) {
  loading.value = true
  // 异步读取数据
  new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = (e) => {
      const data = e.target.result
      const workbook = read(data, { type: 'binary' })
      const sheetNames = workbook.SheetNames
      const worksheet = workbook.Sheets[sheetNames[0]]
      const json = utils.sheet_to_json(worksheet)
      resolve(json)
    }
    reader.readAsBinaryString(file)
  }).then(async (res) => {
    loading.value = false
    await userBatchImport({ users: res })
    ElMessage({
      message: res.length + i18n.t('msg.excel.importSuccess'),
      type: 'success'
    })
    await router.push('/user/manage')
  })
}
</script>

<style lang="scss" scoped>
.upload {
  width: 50%;
  margin: 50px auto;
  font-size: 18px;

  svg {
    width: 8em;
    height: 8em;
  }
}
</style>
