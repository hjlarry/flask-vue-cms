<template>
  <div class='navbar'>
    <div class='navbar-left'>
        <hambuger class='hambuger-container'/>
    </div>
    <div class='right-menu'>
      <el-dropdown trigger='click' class='avatar-container'>
        <div class='avatar-wrapper'>
          <el-avatar
            :src='$store.getters.userInfo.avatar'
            :size='40'
            shape='square'
            class='avatar'
          ></el-avatar>
        </div>
        <template #dropdown>
          <el-dropdown-menu class='user-dropdown'>
            <router-link to='/'>
              <el-dropdown-item>首页</el-dropdown-item>
            </router-link>
            <el-dropdown-item><a target='_blank' href='http://www.baidu.com'>其他页面</a></el-dropdown-item>
            <el-dropdown-item @click='handleLogout' divided>退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup>
import { useStore } from 'vuex'
import Hambuger from '@/components/Hambuger/index.vue'

const store = useStore()
const handleLogout = () => {
  store.dispatch('user/logout')
}

</script>

<style lang='scss' scoped>
.navbar {
  display: flex;
  padding: 10px;
  .hambuger-container{
    line-height: 46px;
    cursor: pointer;
    transition: background 0.5s;
    &:hover{
      background: rgba(0,0,0,0.1);
    }
  }

  .right-menu {
    margin-left: auto;
    display: flex;
    align-items: center;

    :deep(.avatar-container) {
      cursor: pointer;
    }
  }
}

.user-dropdown {
  width: 100px;
  text-align: center;
}

</style>
