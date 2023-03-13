<template>
  <div class="navbar">
    <div class="navbar-left">
      <Hambuger class="hambuger-container" />
      <Breadcrumb />
    </div>
    <div class="right-menu">
      <Guide class="right-menu-item"></Guide>
      <HeaderSearch class="right-menu-item"></HeaderSearch>
      <ScreenFull class="right-menu-item"></ScreenFull>
      <ThemeSelect class="right-menu-item"></ThemeSelect>
      <LangSelect class="right-menu-item"></LangSelect>
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
              ><a target="_blank" href="https://www.baidu.com">{{
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
import { userStore } from '@/store/user_store'
import Hambuger from '@/components/Hambuger/index.vue'
import Breadcrumb from '@/components/Breadcrumb/index.vue'
import LangSelect from '@/components/LangSelect/index.vue'
import ThemeSelect from '@/components/ThemeSelect/index.vue'
import ScreenFull from '@/components/ScreenFull/index.vue'
import HeaderSearch from '@/components/HeaderSearch/index.vue'
import Guide from '@/components/Guide/index.vue'

const uStore = userStore()
function handleLogout() {
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
