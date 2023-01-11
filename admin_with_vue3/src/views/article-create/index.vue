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
          <Markdown></Markdown>
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

const title = ref('')
const activeName = ref('markdown')
</script>

<style lang="scss" scoped>
.container {
  margin-top: 20px;
}
.title-input {
  margin-bottom: 20px;
}
</style>
