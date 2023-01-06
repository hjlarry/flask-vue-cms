<template>
  <div class="navbar">
    <div class="navbar-left">
      <hambuger class="hambuger-container" />
      <breadcrumb />
    </div>
    <div class="right-menu">
      <guide class="right-menu-item"></guide>
      <header-search class="right-menu-item"></header-search>
      <screen-full class="right-menu-item"></screen-full>
      <theme-select class="right-menu-item"></theme-select>
      <lang-select class="right-menu-item"></lang-select>
      <el-dropdown trigger="click" class="avatar-container">
        <div class="avatar-wrapper">
          <el-avatar
            :src="uStore.userInfo.avatar"
            :size="40"
            shape="square"
            class="avatar"
          ></el-avatar>
        </div>
        <template #dropdown>
          <el-dropdown-menu class="user-dropdown">
            <el-dropdown-item
              ><router-link to="/"
                >{{ $t('msg.navBar.home') }}
              </router-link></el-dropdown-item
            >
            <el-dropdown-item
              ><a target="_blank" href="http://www.baidu.com">{{
                $t('msg.navBar.otherPage')
              }}</a></el-dropdown-item
            >
            <el-dropdown-item @click="handleLogout" divided>{{
              $t('msg.navBar.logout')
            }}</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script setup>
import Hambuger from '@/components/Hambuger/index.vue'
import Breadcrumb from '@/components/Breadcrumb/index.vue'
import LangSelect from '@/components/LangSelect/index.vue'
import ThemeSelect from '@/components/ThemeSelect/index.vue'
import ScreenFull from '@/components/ScreenFull/index.vue'
import HeaderSearch from '@/components/HeaderSearch/index.vue'
import Guide from '@/components/Guide/index.vue'
import { userStore } from '@/store/user_store'

const uStore = userStore()
const handleLogout = () => {
  uStore.logout()
}
</script>

<style lang="scss" scoped>
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
      margin-right: 16px;
    }

    :deep(.avatar-container) {
      cursor: pointer;
    }
  }
}

.user-dropdown a {
  margin: 0 auto;
}
</style>
