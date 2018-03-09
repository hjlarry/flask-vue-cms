<template>
  <article-detail :is-edit='true'></article-detail>
</template>

<script>
  import ArticleDetail from './ArticleDetail'
  export default {
    name: 'editForm',
    components: { ArticleDetail }
  }
</script>
