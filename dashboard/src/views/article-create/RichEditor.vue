<template>
  <div>
    <div class="editor-box">
      <Toolbar
        :editor="editorRef"
        :defaultConfig="toolbarConfig"
        mode="simple"
        :key="menuKey"
      ></Toolbar>
      <Editor
        :defaultConfig="editorConfig"
        style="height: 500px; overflow-y: hidden"
        v-model="content"
        mode="simple"
        :key="menuKey"
        @onCreated="handleCreated"
      ></Editor>
    </div>
    <div class="bottom">
      <el-button type="primary" @click="onSubmit">{{
        $t('msg.article.commit')
      }}</el-button>
    </div>
  </div>
</template>

<script setup>
import '@wangeditor/editor/dist/css/style.css'
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
import { i18nChangeLanguage } from '@wangeditor/editor'

import { appStore } from '@/store/app_store'
import { onBeforeUnmount, ref, shallowRef, watch } from 'vue'
import { watchSwitchLang } from '@/i18n'
import { articleCreate, articleEdit } from '@/views/article-create/commit'

const editorRef = shallowRef()
const content = ref('')
const toolbarConfig = {}
const editorConfig = { placeholder: '请输入内容...' }
const menuKey = ref(0)
const aStore = appStore()

function handleCreated(editor) {
  const lang = aStore.language === 'cn' ? 'zh-CN' : 'en'
  i18nChangeLanguage(lang)
  editorRef.value = editor
  content.value = props.detail.content
}

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

// 组件销毁时，也及时销毁编辑器，重要！
onBeforeUnmount(() => {
  const editor = editorRef.value
  if (editor == null) return
  editor.destroy()
})

watchSwitchLang(() => {
  // 组件绑定了:key，则key值改变，重新创建组件
  ++menuKey.value
})

watch(
  () => props.detail,
  (val) => {
    if (val && val.content) {
      content.value = val.content
    }
  }
)

async function onSubmit() {
  const data = {
    title: props.title,
    content: content.value
  }
  if (props.detail && props.detail.id) {
    await articleEdit(props.detail.id, data)
  } else {
    await articleCreate(data)
  }
  content.value = ''
  emits('onSuccess')
}
</script>

<style lang="scss" scoped>
.bottom {
  margin-top: 20px;
  text-align: right;
}
</style>
