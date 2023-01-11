<template>
  <div>
    <div id="markdown-box"></div>
    <div class="bottom">
      <el-button type="primary" @click="onSubmit">{{
        $t('msg.article.commit')
      }}</el-button>
    </div>
  </div>
</template>

<script setup>
import MkEditor from '@toast-ui/editor'
import '@toast-ui/editor/dist/i18n/zh-cn'
import '@toast-ui/editor/dist/toastui-editor.css'

import { appStore } from '@/store/app_store'
import { onMounted } from 'vue'

let mkEditor
let el
const aStore = appStore()
function initEditor() {
  mkEditor = new MkEditor({
    el,
    height: '500px',
    previewStyle: 'vertical',
    language: aStore.language === 'cn' ? 'zh-CN' : 'en'
  })
  mkEditor.getMarkdown()
}

onMounted(() => {
  el = document.querySelector('#markdown-box')
  initEditor()
})

function onSubmit() {}
</script>

<style lang="scss" scoped>
.bottom {
  margin-top: 20px;
  text-align: right;
}
</style>
