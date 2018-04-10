<template>
  <div class="app-container">
    <div class="filter-container">

    </div>

    <el-table :data="list" v-loading.body="listLoading" element-loading-text="Loading" border fit highlight-current-row>
      <el-table-column align="center" label='ID' width="95">
        <template slot-scope="scope">
          {{scope.$index}}
        </template>
      </el-table-column>
      <el-table-column label="顺序" width="95" align="center">
        <template slot-scope="scope">
          <span>{{scope.row.order}}</span>
        </template>
      </el-table-column>
      <el-table-column label="标题">
        <template slot-scope="scope">
          {{scope.row.title}}
        </template>
      </el-table-column>
      <el-table-column label="缩略图" width="200" align="center">
        <template slot-scope="scope">
          <img :src="scope.row.thumb_pic" alt="" width="100" height="50">
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="模块" width="110" align="center">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.module_name">{{scope.row.module_name}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="更新时间" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time"></i>
          <span>{{scope.row.updated_at}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="操作" width="200" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="pagination-container">
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange"
      :current-page="listQuery.page" :page-sizes="[5,10,20,30,50]" :page-size="listQuery.limit" layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { fetchList, deleteArticle } from '@/api/article'

export default {
  name: 'ArticleList',
  props: {
    module: {
      type: String,
      default: '1'
    }
  },
  data() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        module: this.module
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false
        for (let index = 0; index < this.list.length; index++) {
          if (this.list[index].thumb_pic) {
            this.list[index].thumb_pic = process.env.SITE_URL + this.list[index].thumb_pic
          }
        }
      })
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.getList()
    },
    handleUpdate(row) {
      this.$router.push({
        path: '/article/edit',
        query: { 'id': row.id }
      })
    },
    handleDelete(row) {
      const index = this.list.indexOf(row)
      const confirm = this.$confirm(`确定移除` + row.title + '?')
      confirm.then(() => {
        deleteArticle(row.id).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.list.splice(index, 1)
        })
      }).catch(() => {

      })
    }
  }
}
</script>



