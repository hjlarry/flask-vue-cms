<template>
  <div class='navbar'>
    <div class='navbar-left'>
      <hambuger class='hambuger-container' />
      <breadcrumb />
    </div>
    <div class='right-menu'>
      <theme-select class='right-menu-item'></theme-select>
      <lang-select class='right-menu-item'></lang-select>
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
              <el-dropdown-item>{{ $t('msg.navBar.home')}} </el-dropdown-item>
            </router-link>
            <el-dropdown-item><a target='_blank' href='http://www.baidu.com'>{{ $t('msg.navBar.otherPage')}}</a></el-dropdown-item>
            <el-dropdown-item @click='handleLogout' divided>{{ $t('msg.navBar.logout')}}</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup>
import { useStore } from 'vuex'
import Hambuger from '@/components/Hambuger/index.vue'
import Breadcrumb from '@/components/Breadcrumb/index.vue'
import LangSelect from '@/components/LangSelect/index.vue'
import ThemeSelect from '@/components/ThemeSelect/index.vue'

const store = useStore()
const handleLogout = () => {
  store.dispatch('user/logout')
}

</script>

<style lang='scss' scoped>
.navbar {
  display: flex;
  padding: 10px;

  .navbar-left {
    display: flex;
    align-items: center;

    .hambuger-container {
      cursor: pointer;
      transition: background 0.5s;

      &:hover {
        background: rgba(0, 0, 0, 0.1);
      }
    }
  }

  .right-menu {
    margin-left: auto;
    display: flex;
    align-items: center;

    :deep(.right-menu-item) {
      font-size: 24px;
      cursor: pointer;
      color: #5a5e66;
    }

    :deep(.avatar-container) {
      cursor: pointer;
    }
  }
}

.user-dropdown {
  width: 120px;
  text-align: center;
}

</style>
