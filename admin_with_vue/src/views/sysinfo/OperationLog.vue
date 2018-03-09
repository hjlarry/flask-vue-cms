<template>
  <div class="app-container">
    <div class="filter-container">
      <el-button type="primary" icon="el-icon-delete" @click="handleBatchDelete" :disabled="isEmptySelection">Delete
      </el-button>
      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" v-model="listQuery.path" placeholder="path">
      </el-input>
      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" v-model="listQuery.input" placeholder="input">
      </el-input>
      <el-date-picker v-model="listQuery.date" type="date" placeholder="选择日期" value-format="yyyy-MM-dd"></el-date-picker>
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">Search</el-button>
    </div>

    <el-table :data="list" v-loading.body="listLoading" element-loading-text="Loading" border fit highlight-current-row
              @selection-change="handleSelectionChange">
      <el-table-column align="center" type="selection" width="50"></el-table-column>
      <el-table-column align="center" label='ID' width="60">
        <template slot-scope="scope">
          {{scope.row.id}}
        </template>
      </el-table-column>
      <el-table-column label="user" width="100" align="center">
        <template slot-scope="scope">
          {{scope.row.user}}
        </template>
      </el-table-column>
      <el-table-column label="path" width="300">
        <template slot-scope="scope">
          {{scope.row.path}}
        </template>
      </el-table-column>
      <el-table-column label="method" width="100" align="center">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.method == 'GET'">{{scope.row.method}}</el-tag>
          <el-tag v-else type="success">{{scope.row.method}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="input" align="center">
        <template slot-scope="scope">
          {{scope.row.input_summary}}
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" v-if="scope.row.created_at"></i>
          <span>{{scope.row.created_at}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="" width="80" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="pagination-container">
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange"
                     :current-page="listQuery.page" :page-sizes="[5,10,20,30,50]" :page-size="listQuery.limit"
                     layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import { fetchLogList, deleteLog } from '@/api/sysinfo'

  export default {
    data() {
      return {
        list: null,
        total: null,
        listLoading: true,
        listQuery: {
          page: 1,
          limit: 10,
          path: '',
          input: '',
          date: ''
        },
        multipleSelection: []
      }
    },
    computed: {
      isEmptySelection: function() {
        return this.multipleSelection.length === 0
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        this.listLoading = true
        fetchLogList(this.listQuery).then(response => {
          this.list = response.data.items
          this.total = response.data.total
          this.listLoading = false
        })
      },
      handleFilter() {
        this.listQuery.page = 1
        this.getList()
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
          path: '/user/edit',
          query: { 'id': row.id }
        })
      },
      handleSelectionChange(val) {
        this.multipleSelection = val
      },
      handleDelete(row) {
        const index = this.list.indexOf(row)
        const confirm = this.$confirm(`确定移除` + row.id + '?')
        const del_data = [{ 'id': row.id }]
        this.LogDelete(confirm, del_data).then(() => {
          this.list.splice(index, 1)
        })
      },
      handleBatchDelete() {
        const confirm = this.$confirm('确定删除这些log?')
        const del_data = []
        let item = {}
        for (item in this.multipleSelection) {
          del_data.push({ 'id': this.multipleSelection[item].id })
        }
        this.LogDelete(confirm, del_data).then(() => {
          this.getList()
        })
      },
      LogDelete(confirm, del_data) {
        return confirm.then(() => {
          return deleteLog(del_data)
        }).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
        }).catch(() => {
          console.log('456')
          this.$notify({
            title: '失败',
            message: '删除失败',
            type: 'fail',
            duration: 2000
          })
          return Promise.reject('')
        })
      }
    }
  }
</script>



