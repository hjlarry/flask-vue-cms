<template>
  <div class="tab-container">
      <!--<router-link to="/article/create">-->
          <!--<el-button class="filter-item" type="primary" icon="el-icon-edit">添加新文章</el-button>-->
      <!--</router-link>-->
    <el-tabs style='margin-top:15px;' v-model="activeName" type="border-card">
      <el-tab-pane :label="default_module.title" :key='default_module.id'>
        <keep-alive>
          <article-list :module='default_module.id'></article-list>
        </keep-alive>
      </el-tab-pane>
      <el-tab-pane v-for="item in module" :label="item.title" :key='item.id'>
        <keep-alive>
          <article-list :module='item.id' v-if="activeName==item.id"></article-list>
        </keep-alive>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import ArticleList from './ArticleList'
import { fetchModule } from '@/api/article'
export default {
  name: 'index',
  components: { ArticleList },
  data() {
    return {
      activeName: '0',
      default_module: { title: '所有文章', id: 'all' },
      module: []
    }
  },
  created() {
    this.getModule()
  },
  methods: {
    getModule() {
      fetchModule().then(response => {
        for (let item = 0; item < response.data.length; item++) {
          response.data[item].id = String(response.data[item].id)
          this.module.push(response.data[item])
        }
      })
    }
  }
}
</script>

<style scoped>
  .tab-container{
    margin: 30px;
  }
</style>
