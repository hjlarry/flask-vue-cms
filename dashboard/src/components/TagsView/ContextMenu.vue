<template>
  <ul class="context-menu-container">
    <li @click="onRefreshClick">{{ $t('msg.tagsView.refresh') }}</li>
    <li @click="onCloseRight">{{ $t('msg.tagsView.closeRight') }}</li>
    <li @click="onCloseOther">{{ $t('msg.tagsView.closeOther') }}</li>
  </ul>
</template>

<script setup>
import { useRouter } from 'vue-router'

import { appStore } from '@/store/app_store'

const props = defineProps({
  index: {
    type: Number,
    required: true
  }
})

const router = useRouter()
const aStore = appStore()
function onRefreshClick() {
  router.go(0)
}

function onCloseRight() {
  aStore.removeTagsView({
    index: props.index,
    type: 'right'
  })
  const last = aStore.tagsView.length - 1
  router.push(aStore.tagsView[last].fullPath)
}

function onCloseOther() {
  aStore.removeTagsView({
    index: props.index,
    type: 'other'
  })
  router.push(aStore.tagsView[0].fullPath)
}
</script>

<style lang="scss" scoped>
.context-menu-container {
  list-style: none;
  border: 1px solid #d8dce5;
  border-radius: 4px;
  background: #fff;
  padding: 5px;
  width: 100px;
  font-size: 12px;
  font-weight: 400;
  position: fixed;
  z-index: 999;
  box-shadow: 2px 2px 3px 0 rgba(0, 0, 0, 0.3);

  li {
    cursor: pointer;
    padding: 5px 10px;

    &:hover {
      background: #eee;
    }
  }
}
</style>
