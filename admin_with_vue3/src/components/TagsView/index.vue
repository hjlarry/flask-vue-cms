<template>
  <div class='tags-view-container'>
    <router-link
      class='tags-view-item'
      :class='isActive(tag) ? "active" : ""'
      :style='{
        backgroundColor: isActive(tag) ? $store.getters.cssVar.menuBg : "",
        borderColor: isActive(tag) ? $store.getters.cssVar.menuBg : ""
      }'
      v-for='(tag, index) in $store.getters.tagsViewList'
      :key='tag.fullPath'
      :to='tag.fullPath'>
      {{ tag.title }}
      <i class='el-icon-close' @click.prevent='onCloseClick(index)'></i>
    </router-link>
  </div>
</template>

<script setup>

import { useRoute } from 'vue-router'

const route = useRoute()

function isActive(tag) {
  return tag.path === route.path
}

function onCloseClick(index) {
  // $store.commit('app/deleteTag', index)
  console.log(index)
}

</script>

<style lang='scss' scoped>
.tags-view-container {
  height: 34px;
  border-bottom: 1px solid #d8dce5;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 0 3px 0 rgba(0, 0, 0, 0.04);

  .tags-view-item {
    display: inline-block;
    cursor: pointer;
    margin: 2px 5px;
    padding: 0 8px;
    color: #495060;
    border: 1px solid #d8dce5;
    font-size: 12px;
    line-height: 28px;

    &:first-of-type {
      margin-left: 15px;
    }

    &:last-of-type {
      margin-right: 15px;
    }

    &.active {
      color: #fff;
      &::before{
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

    .el-icon-close {
      width: 16px;
      height: 16px;
      border-radius: 50%;
      vertical-align: 2px;
      line-height: 10px;
      text-align: center;
      transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
      transform-origin: 100% 50%;

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

</style>
