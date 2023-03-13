<template>
  <div class="tags-view-container">
    <el-scrollbar>
      <div class="tags-view-wrapper">
        <router-link
          class="tags-view-item"
          :class="isActive(tag) ? 'active' : ''"
          :style="{
            backgroundColor: isActive(tag) ? tStore.cssVar.menuBg : '',
            borderColor: isActive(tag) ? tStore.cssVar.menuBg : ''
          }"
          v-for="(tag, index) in aStore.tagsView"
          :key="tag.fullPath"
          :to="tag.fullPath"
          @contextmenu.prevent="openMenu($event, index)"
        >
          {{ tag.title }}
          <SvgIcon
            icon="close"
            class="icon-close"
            v-show="isShowCloseIcon(tag)"
            @click.prevent="onCloseClick(index)"
          ></SvgIcon>
        </router-link>
      </div>
    </el-scrollbar>
    <context-menu
      :index="selectIndex"
      v-show="isShow"
      :style="menuPos"
    ></context-menu>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { reactive, ref, watch } from 'vue'

import SvgIcon from '@/components/SvgIcon/index.vue'
import { themeStore } from '@/store/theme_store'
import { appStore } from '@/store/app_store'
import ContextMenu from './ContextMenu.vue'

const route = useRoute()
const tStore = themeStore()
const aStore = appStore()

function isActive(tag) {
  return tag.path === route.path
}

function isShowCloseIcon(tag) {
  return isActive(tag) && aStore.tagsView.length > 1
}

const router = useRouter()
function onCloseClick(index) {
  aStore.removeTagsView({
    index: index,
    type: 'index'
  })
  router.push(aStore.tagsView[0].fullPath)
}

const selectIndex = ref(0)
const isShow = ref(false)
const menuPos = reactive({
  left: 0,
  top: 0
})

function openMenu(event, index) {
  const { clientX, clientY } = event
  menuPos.left = clientX + 'px'
  menuPos.top = clientY + 'px'
  selectIndex.value = index
  isShow.value = true
}

function closeMenu() {
  isShow.value = false
}

watch(isShow, (val) => {
  if (val) {
    document.body.addEventListener('click', closeMenu)
  } else {
    document.body.removeEventListener('click', closeMenu)
  }
})
</script>

<style lang="scss" scoped>
.tags-view-container {
  height: 34px;
  width: 100%;
  border-bottom: 1px solid #d8dce5;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 0 3px 0 rgba(0, 0, 0, 0.04);

  .tags-view-wrapper {
    display: flex;

    .tags-view-item {
      cursor: pointer;
      margin: 2px 5px;
      padding: 0 8px;
      color: #495060;
      border: 1px solid #d8dce5;
      font-size: 12px;
      line-height: 28px;
      height: 28px;
      display: flex;
      flex-shrink: 0;
      align-items: center;
      justify-content: center;

      &:first-of-type {
        margin-left: 15px;
      }

      &:last-of-type {
        margin-right: 15px;
      }

      &.active {
        color: #fff;

        &::before {
          content: '';
          background: #ffffff;
          display: inline-block;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          position: relative;
          margin-right: 4px;
        }
      }

      .icon-close {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        vertical-align: 2px;
        line-height: 10px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
        transform-origin: 100% 50%;
        margin-left: 2px;

        &:hover {
          color: #fff;
          background-color: #b4bccc;
        }

        &::before {
          vertical-align: -2px;
          transform: scale(0.8);
          display: inline-block;
        }
      }
    }
  }
}
</style>
