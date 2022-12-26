<template>
  <el-breadcrumb class='breadcrumb'>
    <transition-group name='breadcrumb'>
      <el-breadcrumb-item v-for='(item,index) in breadcrumbData' :key='item.path'>
      <span v-if='index === breadcrumbData.length - 1' class='no-redirect'>
            {{ generateRouteTitle(item.meta.title) }}</span>
        <span v-else class='redirect' @click='onLinkClick(item)'>
            {{ generateRouteTitle(item.meta.title) }}</span>
      </el-breadcrumb-item>
    </transition-group>
  </el-breadcrumb>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ref, watch } from 'vue'
import store from '@/store'
import { generateRouteTitle } from '@/i18n'

const route = useRoute()
const breadcrumbData = ref([])

function updateBreadcrumbData() {
  breadcrumbData.value = route.matched.filter(
    item => item.meta && item.meta.title
  )
  console.log(breadcrumbData.value)
}

const router = useRouter()

function onLinkClick(item) {
  router.push(item.path)
}

watch(
  route,
  () => {
    updateBreadcrumbData()
  }, {
    immediate: true
  }
)

const linkHoverColor = ref(store.getters.cssVar.menuBg)

</script>

<style lang='scss' scoped>
.breadcrumb {
  font-size: 14px;

  .no-redirect {
    color: #97a8be;
  }

  .redirect {
    font-weight: 600;
    color: #666;

    &:hover {
      cursor: pointer;
      color: v-bind(linkHoverColor);
    }
  }
}
</style>
