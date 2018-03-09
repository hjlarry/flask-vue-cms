<template>
  <div class="app-container">
    <el-form ref="form" :model="article">
      <el-form-item style="margin-bottom: 40px;" prop="title">
              <MDinput name="name" v-model="article.title" required :maxlength="100">
                标题
              </MDinput>
      </el-form-item>

      <el-form-item style="margin-bottom: 40px;" prop="order" label="顺序">
        <el-input-number v-model="article.order" size="small" ></el-input-number>
      </el-form-item>

      <el-form-item style="margin-bottom: 40px;" prop="module" label="模块">
        <el-select v-model="article.module_id" clearable placeholder="请选择">
          <el-option
            v-for="item in module"
            :key="item.id"
            :label="item.title"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>

      <el-form-item style="margin-bottom: 40px;" label="头图">
        <el-upload class="upload" :action="upload_url" :limit="1" :file-list="fileList"
                   list-type="picture" :on-success="imgUploadSuccess" :on-remove="imgRemove" :headers="upload_header">
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
        </el-upload>
      </el-form-item>


      <div class="editor-container">
        <tinymce :height=800 ref="editor" v-model="article.content"></tinymce>
      </div>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onClear">清空</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Tinymce from '@/components/Tinymce'
import MDinput from '@/components/MDinput'
import { createArticle, fetchModule, fetchArticle, editArticle } from '@/api/article'
import { getToken } from '@/utils/auth'

const defaultForm = {
  title: '',
  content: '',
  order: '',
  module_id: '',
  thumb_pic: ''
}

export default {
  name: 'articleDetail',
  components: { Tinymce, MDinput },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      article: Object.assign({}, defaultForm),
      module: {},
      fileList: [],
      upload_url: process.env.BASE_API + '/upload',
      upload_header: {
        'Authorization': getToken()
      }
    }
  },
  created() {
    this.getModule()
    if (this.isEdit) {
      this.fetchData()
    }
  },
  methods: {
    onSubmit() {
      if (this.isEdit) {
        editArticle(this.article).then(response => {
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
        createArticle(this.article).then(response => {
          if (response.code === 0) {
            this.$notify({
              title: '成功',
              message: '已创建',
              type: 'success',
              duration: 2000
            })
            Object.assign(this.article, defaultForm)
          }
        })
      }
    },
    onClear() {
      Object.assign(this.article, defaultForm)
    },
    fetchData() {
      fetchArticle(this.$route.query.id).then(response => {
        const article = response.data
        Object.assign(this.article, article)
        this.fileList.push({ name: '已上传的缩略图', url: process.env.SITE_URL + article.thumb_pic })
      })
    },
    getModule() {
      fetchModule().then(response => {
        this.module = response.data
      })
    },
    imgUploadSuccess(response, file, fileList) {
      this.article.thumb_pic = response.data.fileurl
    },
    imgRemove(file, fileList) {
      this.article.thumb_pic = ''
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>

.editor-container {
  min-height: 300px;
  margin: 0 0 30px;
  .editor-upload-btn-container {
      text-align: right;
      margin-right: 10px;
      .editor-upload-btn {
          display: inline-block;
      }
  }
}
</style>

