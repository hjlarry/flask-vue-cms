<template>
  <div class="">
    <h2 class="title">{{ detail.title }}</h2>
    <div class="header">
      <span class="author"
        >{{ $t('msg.article.author') }}: {{ detail.author }}</span
      >
      <span class="time"
        >{{ $t('msg.article.publicDate') }}:
        {{ $filters.relativeTime(detail.publicDate) }}</span
      >
      <el-button class="edit" type="primary" link @click="onEdit">{{
        $t('msg.article.edit')
      }}</el-button>
    </div>
    <div class="content" v-html="detail.content"></div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'
import { articleDetail } from '@/api/article'

const detail = ref({})
const route = useRoute()
const articleId = route.params.id

async function getArticle() {
  detail.value = (await articleDetail(articleId)).data
}

getArticle()

const router = useRouter()
function onEdit() {
  router.push(`/article/edit/${articleId}`)
}
</script>

<style lang="scss" scoped>
.title {
  font-size: 22px;
  text-align: center;
  padding: 12px 0;
}
.header {
  padding: 26px 0;
  font-size: 14px;
  .author {
    color: #555666;
    margin-right: 20px;
  }
  .time {
    color: #999aaa;
    margin-right: 20px;
  }
  .edit {
    float: right;
  }
}

.content {
  font-size: 14px;
  padding: 20px 0;
  border-top: 1px solid #d4d4d4;
}
</style>
