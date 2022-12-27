<template>
  <el-config-provider :locale='$store.getters.lang === "en" ? en : zhCn'>
    <router-view></router-view>
  </el-config-provider>
</template>

<script setup>
import { ElConfigProvider } from 'element-plus'
import zhCn from 'element-plus/lib/locale/lang/zh-cn'
import en from 'element-plus/lib/locale/lang/en'
import { genNewStyle, writeNewStyle } from '@/utils/theme'
import { useStore } from 'vuex'

const store = useStore()
genNewStyle(store.getters.mainColor).then(newStyle => writeNewStyle(newStyle))

</script>

<style></style>
