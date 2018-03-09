<template>
  <article-detail :is-edit='false'></article-detail>
</template>

<script>
  import ArticleDetail from './ArticleDetail'
  export default {
    name: 'createForm',
    components: { ArticleDetail }
  }
</script>
