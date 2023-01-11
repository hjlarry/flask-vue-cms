<template>
  <div class="container">
    <el-card shadow="never">
      <el-input
        class="title-input"
        :placeholder="$t('msg.article.titlePlaceholder')"
        v-model="title"
        clearable
      ></el-input>
      <el-tabs v-model="activeName">
        <el-tab-pane :label="$t('msg.article.markdown')" name="markdown">
          <Markdown
            :title="title"
            :detail="detail"
            @onSuccess="onSuccess"
          ></Markdown>
        </el-tab-pane>
        <el-tab-pane :label="$t('msg.article.richText')" name="richEditor">
          <RichEditor></RichEditor>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Markdown from './Markdown.vue'
import RichEditor from './RichEditor.vue'
import { useRoute } from 'vue-router'
import { articleDetail } from '@/api/article'

const detail = ref({})
const route = useRoute()
const articleId = route.params.id

async function getArticle() {
  detail.value = (await articleDetail(articleId)).data
  title.value = detail.value.title
}

if (articleId) {
  getArticle()
}

const title = ref('')
const activeName = ref('markdown')

function onSuccess() {
  title.value = ''
}
</script>

<style lang="scss" scoped>
.container {
  margin-top: 20px;
}

.title-input {
  margin-bottom: 20px;
}
</style>
