<template>
  <div class="app-container">
    <el-form ref="user" :model="user" :rules="rules">
      <el-form-item style="margin-bottom: 40px;" prop="username">
          <MDinput v-model="user.username" :maxlength="100" :disabled="isEdit">
            用户名
          </MDinput>
      </el-form-item>

      <el-form-item style="margin-bottom: 40px;" prop="password">
          <MDinput type="password" v-model="user.password" :maxlength="100">
            密码
          </MDinput>
      </el-form-item>

      <el-form-item style="margin-bottom: 40px;" prop="name">
          <MDinput name="name" v-model="user.name" required :maxlength="100">
            姓名
          </MDinput>
      </el-form-item>

      <el-form-item>
        <div class="label">
          头像
        </div>
          <pan-thumb :image="image"></pan-thumb>

          <el-button type="primary" icon="upload" style="position: absolute;bottom: 15px;margin-left: 40px;" @click="imagecropperShow=true">更换
          </el-button>

          <image-crop :width="300" :height="300" :url="upload_url" @close='close' @crop-upload-success="cropSuccess"
            :key="imagecropperKey" v-show="imagecropperShow"></image-crop>
      </el-form-item>


      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onClear">清空</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import MDinput from '@/components/MDinput'
import ImageCrop from '@/components/ImageCrop'
import PanThumb from '@/components/PanThumb'
import { createUser, editUser, fetchUser } from '@/api/user'
import { getToken } from '@/utils/auth'

const defaultForm = {
  username: '',
  password: '',
  name: '',
  avatar: ''
}

export default {
  name: 'UserDetail',
  components: { MDinput, PanThumb, ImageCrop },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    const validateRequire = (rule, value, callback) => {
      if (value === '') {
        this.$message({
          message: rule.field + '为必传项',
          type: 'error'
        })
        callback(null)
      } else {
        callback()
      }
    }
    return {
      user: Object.assign({}, defaultForm),
      module: {},
      fileList: [],
      rules: {
        username: [{ validator: validateRequire }],
        password: [{ validator: validateRequire }]
      },
      upload_url: process.env.BASE_API + '/upload_avatar',
      upload_header: {
        'Authorization': getToken()
      },
      imagecropperShow: false,
      imagecropperKey: 0,
      image: process.env.SITE_URL + 'static/img/logo.png'
    }
  },
  created() {
    if (this.isEdit) {
      this.fetchData()
    }
  },
  methods: {
    onSubmit() {
      if (this.isEdit) {
        editUser(this.user).then(response => {
          if (response.code === 0) {
            this.$notify({
              title: '成功',
              message: '已编辑',
              type: 'success',
              duration: 2000
            })
          }
        })
      } else {
        this.$refs.user.validate(valid => {
          if (valid) {
            console.log('correct submit!!')
          } else {
            console.log('error submit!!')
          }
        })
        createUser(this.user).then(response => {
          if (response.code === 0) {
            this.$notify({
              title: '成功',
              message: '已创建',
              type: 'success',
              duration: 2000
            })
            Object.assign(this.user, defaultForm)
          }
        })
      }
    },
    onClear() {
      Object.assign(this.user, defaultForm)
    },
    fetchData() {
      fetchUser(this.$route.query.id).then(response => {
        const user = response.data
        Object.assign(this.user, user)
        if (user.avatar) {
          this.image = process.env.SITE_URL + user.avatar
        }
      })
    },
    cropSuccess(resData) {
      this.imagecropperShow = false
      this.imagecropperKey = this.imagecropperKey + 1
      this.image = process.env.SITE_URL + resData.fileurl
      this.user.avatar = resData.fileurl
    },
    close() {
      this.imagecropperShow = false
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>

.label {
  font-size: 18px;
  color: #9E9E9E;
}


</style>

