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
import { onMounted, watch } from 'vue'
import { watchSwitchLang } from '@/i18n'
import { articleCreate, articleEdit } from '@/views/article-create/commit'

const props = defineProps({
  title: {
    required: true,
    type: String
  },
  detail: {
    type: Object
  }
})
const emits = defineEmits(['onSuccess'])

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

watchSwitchLang(() => {
  const htmlStr = mkEditor.getHTML()
  mkEditor.destroy()
  initEditor()
  mkEditor.setHTML(htmlStr)
})

watch(
  () => props.detail,
  (val) => {
    if (val && val.content) {
      mkEditor.setHTML(val.content)
    }
  }
)

async function onSubmit() {
  const data = {
    title: props.title,
    content: mkEditor.getHTML()
  }
  if (props.detail && props.detail.id) {
    await articleEdit(props.detail.id, data)
  } else {
    await articleCreate(data)
  }

  mkEditor.reset()
  emits('onSuccess')
}
</script>

<style lang="scss" scoped>
.bottom {
  margin-top: 20px;
  text-align: right;
}
</style>
