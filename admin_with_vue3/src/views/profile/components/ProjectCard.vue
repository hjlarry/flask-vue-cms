<template>
  <el-card>
    <template #header>
      <div class="header">
        <span>{{ $t('msg.profile.introduce') }}</span>
      </div>
    </template>
    <template #default>
      <div class="user-info">
        <div class="box-center">
          <PanThumb
            :image="uStore.userInfo.avatar"
            :height="'100px'"
            :width="'100px'"
          >
            <span>Hello World!</span>
          </PanThumb>
        </div>
        <div class="box-center">
          <div class="user-name">
            <span>{{ uStore.userInfo.name }}</span>
          </div>
        </div>
      </div>
      <div class="project-bio">
        <div class="project-bio-header">
          <SvgIcon icon="introduce"></SvgIcon>
          <span>{{ $t('msg.profile.projectIntroduction') }}</span>
        </div>
        <div class="project-bio-body">
          <span>{{ $t('msg.profile.muted') }}</span>
        </div>
      </div>
      <div class="project-bio">
        <div class="project-bio-header">
          <SvgIcon icon="reward"></SvgIcon>
          <span>{{ $t('msg.profile.projectFunction') }}</span>
        </div>
        <div class="project-bio-body">
          <div class="progress-item" v-for="item in features" :key="item.id">
            <span>{{ item.title }}</span>
            <el-progress
              status="success"
              :percentage="item.percentage"
            ></el-progress>
          </div>
        </div>
      </div>
    </template>
  </el-card>
</template>

<script setup>
import PanThumb from '@/components/PanThumb/index.vue'
import SvgIcon from '@/components/SvgIcon/index.vue'
import { userStore } from '@/store/user_store'

const uStore = userStore()

defineProps({
  features: {
    type: Array,
    default: () => []
  }
})
</script>

<style lang="scss" scoped>
.box-center {
  text-align: center;
  .user-name {
    font-weight: bold;
    margin-top: 10px;
  }
}

.project-bio {
  margin-top: 20px;
  .project-bio-header {
    display: flex;
    align-items: center;
    margin: 0 20px 10px 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ebeef5;
    span {
      margin-left: 10px;
      font-size: 18px;
      font-weight: bold;
    }
  }
  .project-bio-body {
    color: #999;
    margin: 0 20px;
    .progress-item {
      margin: 20px 0;
      font-size: 14px;
    }
  }
}
</style>
