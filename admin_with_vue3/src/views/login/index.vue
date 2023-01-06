<template>
  <div class="login-container">
    <el-form
      autoComplete="on"
      :model="loginForm"
      :rules="loginRules"
      ref="loginFormRef"
      label-position="left"
      label-width="0px"
      class="card-box login-form"
    >
      <div class="title-container">
        <h3 class="title">flask-vue-cms</h3>
        <lang-select class="lang-select"></lang-select>
      </div>

      <el-form-item prop="username">
        <span class="svg-container svg-container_login">
          <svg-icon icon="user"></svg-icon>
        </span>
        <el-input
          name="username"
          type="text"
          v-model="loginForm.username"
          autoComplete="on"
          placeholder="username"
        />
      </el-form-item>
      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon="password"></svg-icon>
        </span>
        <el-input
          name="password"
          :type="pwdType"
          v-model="loginForm.password"
          autoComplete="on"
          placeholder="password"
        ></el-input>
        <span class="show-pwd" @click="showPwd">
          <svg-icon :icon="pwdType === 'password' ? 'eye' : 'eye-open'" />
        </span>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width: 100%" @click="handleLogin">
          {{ $t('msg.login.loginBtn') }}
        </el-button>
      </el-form-item>

      <div class="tips" v-html="$t('msg.login.desc')"></div>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import router from '@/router'
import LangSelect from '@/components/LangSelect/index.vue'
import { useI18n } from 'vue-i18n'
import { userStore } from '@/store/user_store'
import SvgIcon from '@/components/SvgIcon'

const loginForm = ref({
  username: 'admin',
  password: 'admin'
})

const i18n = useI18n()

const validatePass = (rule, value, callback) => {
  if (value.length < 3) {
    callback(new Error(i18n.t('msg.login.passwordRule')))
  } else {
    callback()
  }
}
const loginRules = ref({
  username: [
    {
      required: true,
      trigger: 'blur',
      message: i18n.t('msg.login.usernameRule')
    }
  ],
  password: [
    {
      required: true,
      trigger: 'blur',
      validator: validatePass
    }
  ]
})

const pwdType = ref('password')
const showPwd = () => {
  if (pwdType.value === 'password') {
    pwdType.value = ''
  } else {
    pwdType.value = 'password'
  }
}

const loading = ref(false)
const loginFormRef = ref(null)
const uStore = userStore()
const handleLogin = () => {
  loginFormRef.value.validate((valid) => {
    if (!valid) return
    loading.value = true
    uStore
      .login(loginForm.value)
      .then(() => {
        loading.value = false
        router.push('/')
      })
      .catch((error) => {
        console.log(error)
        loading.value = false
      })
  })
}
</script>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;
$cursor: #fff;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;

    :deep(.el-form-item) {
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.1);
      border-radius: 5px;
      color: #454545;
    }

    :deep(.el-input) {
      display: inline-block;
      height: 47px;
      width: 85%;

      .el-input__wrapper {
        background: transparent;
        width: 100%;
        box-shadow: none;
      }

      input {
        background: transparent;
        border: 0;
        border-radius: 0;
        padding: 12px 5px 12px 15px;
        color: $light_gray;
        height: 47px;
        caret-color: $cursor;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0 auto 40px auto;
      text-align: center;
      font-weight: bold;
    }

    :deep(.lang-select) {
      font-size: 26px;
      position: absolute;
      right: 0;
      top: 0;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
