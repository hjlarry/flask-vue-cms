<template>
  <div class="dashboard-container" v-loading.body="listLoading">
    <el-row :gutter="10">
      <el-col :xs="16" :sm="16" :lg="8">
        <el-card class="box-card-component" >
          <div>
            <span class="card-title">System Info</span>
          </div>
          <div style="margin-top: 30px">

            <div v-for="value,key in sys" class="list-item"><span>{{key}}</span> <span class="des">{{value}}</span></div>

          </div>
        </el-card>
      </el-col>

      <el-col :xs="16" :sm="16" :lg="8">
        <el-card class="box-card-component" >
          <div>
            <span class="card-title">CPU Status</span>
          </div>
          <div style="margin-top: 30px">
            <div v-for="value,key in cpu" class='progress-item'>
              <span>{{key}}</span>
              <el-progress :percentage="value"></el-progress>
            </div>
          </div>
        </el-card>
      </el-col>

      <el-col :xs="16" :sm="16" :lg="8">
        <el-card class="box-card-component" >
          <div>
            <span class="card-title">Memery Status</span>
          </div>
          <div style="margin-top: 30px">
            <div class='progress-item'>
              <span>Total({{mem.total | sizeformat}}G)</span>
              <el-progress :percentage="100"></el-progress>
            </div>

            <div class='progress-item'>
              <span>Avaliable({{mem.available | sizeformat}}G)</span>
              <el-progress :percentage="mem_avaliable"></el-progress>
            </div>

            <div class='progress-item'>
              <span>Used(exclude cache & buffers {{ mem.total - mem.available | sizeformat}}G)</span>
              <el-progress :percentage="mem.percent"></el-progress>
            </div>

            <div class='progress-item'>
              <span>Used(include cache & buffers {{ mem.used | sizeformat}}G)</span>
              <el-progress :percentage="mem_used"></el-progress>
            </div>

            <div class='progress-item'>
              <span>Free({{ mem.free | sizeformat}}G)</span>
              <el-progress :percentage="mem_free"></el-progress>
            </div>

          </div>
        </el-card>
      </el-col>

    </el-row>

    <el-row :gutter="10">
      <el-col :xs="32" :sm="32" :lg="16">
        <el-card class="disk-card">
          <div>
            <span class="card-title">Disk Info</span>
          </div>
          <el-table :data="disk" style="width: 100%;padding-top: 15px;">
          <el-table-column label="Device" width="150" show-overflow-tooltip align="center">
            <template slot-scope="scope">
              {{scope.row.device}}
            </template>
          </el-table-column>
          <el-table-column label="Mountpoint" >
            <template slot-scope="scope">
              {{scope.row.mountpoint}}
            </template>
          </el-table-column>
          <el-table-column label="Space" width="140" align="center">
            <template slot-scope="scope">
              {{scope.row.space_total | sizeformat}}G
            </template>
          </el-table-column>
          <el-table-column label="Space Free" width="140" align="center">
            <template slot-scope="scope">
              {{scope.row.space_free | sizeformat}}G
            </template>
          </el-table-column>
          <el-table-column label="Space Used" width="140" align="center">
            <template slot-scope="scope">
              <el-progress :percentage="scope.row.space_used_percent" :show-text="false"></el-progress>
            </template>
          </el-table-column>
          <el-table-column label="Type" width="100" align="center">
            <template slot-scope="scope">
              <el-tag> {{scope.row.type}}</el-tag>
            </template>
          </el-table-column>
        </el-table>
        </el-card>
      </el-col>

      <el-col :xs="16" :sm="16" :lg="8">
        <el-card class="disk-card">
          <div>
            <span class="card-title">User Info</span>
          </div>
          <el-table :data="user" style="width: 100%;padding-top: 15px;">
          <el-table-column label="Name" width="150" show-overflow-tooltip align="center">
            <template slot-scope="scope">
              {{scope.row.name}}
            </template>
          </el-table-column>
          <el-table-column label="Session Started" >
            <template slot-scope="scope">
              {{scope.row.started}}
            </template>
          </el-table-column>

          <el-table-column label="Host" width="100" align="center">
            <template slot-scope="scope">
              {{scope.row.host}}
            </template>
          </el-table-column>
        </el-table>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { fetchInfo } from '@/api/sysinfo'

export default {
  name: 'dashboard',
  data() {
    return {
      cpu: {},
      sys: {},
      mem: {},
      listLoading: true,
      mem_avaliable: 0,
      mem_used: 0,
      mem_free: 0,
      disk: null,
      user: null
    }
  },
  created() {
    this.getInfo()
  },
  // mounted() {
  //   this.timer = -1 // 首次设置小于0，立马调用getDatas函数
  //   setInterval(() => {
  //     this.timer--
  //     if (this.timer < 0) {
  //       this.getInfo() // 调用getDatas函数
  //       this.timer = 3 // 重置变量，60s后才能调用getDatas函数
  //     }
  //   }, 1000)
  // },
  filters: {
    sizeformat: function(value) {
      return parseFloat(value / (1024 * 1024 * 1024)).toFixed(2)
    }
  },
  methods: {
    getInfo() {
      this.listLoading = true
      fetchInfo().then(response => {
        this.listLoading = false
        this.cpu = response.data.cpu
        this.sys = response.data.sys
        this.mem = response.data.mem
        this.mem_avaliable = Math.round(this.mem.available / this.mem.total * 100)
        this.mem_used = Math.round(this.mem.used / this.mem.total * 100)
        this.mem_free = Math.round(this.mem.free / this.mem.total * 100)
        this.disk = response.data.disk.slice(0, 5)
        this.user = response.data.user.slice(0, 7)
      })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
.progress-item {
  margin-bottom: 10px;
  font-size: 14px;
}

  .list-item{
    line-height: 25px;
  }
  .des{
    float: right;
  }
  .box-card-component{
    height: 300px;
    margin-top: 10px;
  }
  .disk-card{
    margin-top: 10px;
    height: 500px;
  }
  .card-title{
    font-weight: bold;
  }

</style>
