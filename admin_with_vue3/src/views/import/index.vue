<template>
  <el-upload
    class="upload"
    drag
    :auto-upload="false"
    :limit="1"
    :show-file-list="false"
    :on-change="handleUpload"
  >
    <SvgIcon icon="cloud-upload"></SvgIcon>
    <div class="el-upload__text">
      {{ $t('msg.uploadExcel.upload') }}
    </div>
  </el-upload>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon'
import { ElMessage } from 'element-plus'

function handleUpload(file) {
  console.log(file)
  if (!(file.name.endsWith('.xlsx') || file.name.endsWith('.xls'))) {
    ElMessage.error('文件类型错误')
    return false
  }
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
