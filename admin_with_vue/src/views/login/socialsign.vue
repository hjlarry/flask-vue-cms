<template>
  <div class="social-signup-container">
    <div class="sign-btn" @click="githubHandleClick('github')">
      <span class="github-svg-container"><svg-icon icon-class="github" class="icon"></svg-icon>Github</span>
    </div>
  </div>
</template>

<script>
  import openWindow from '@/utils/openWindow'

  export default {
    name: 'social-signin',
    methods: {
      githubHandleClick(thirdpart) {
        const client_id = '9f24e95ba9507c804669'
        const url = 'https://github.com/login/oauth/authorize?client_id=' + client_id + '&scope=user:email'
        openWindow(url, thirdpart, 540, 540)
      }
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
  .social-signup-container {
    margin: 20px 0;
    .sign-btn {
      display: inline-block;
      cursor: pointer;
    }
    .icon {
      font-size: 60px;
      width: 100%;
    }
    .github-svg-container {
      display: inline-block;
      width: 80px;
      height: 80px;
      line-height: 40px;
      text-align: center;
      padding-top: 1px;
      border-radius: 4px;
      margin-bottom: 20px;
      margin-right: 5px;
    }
  }
</style>
