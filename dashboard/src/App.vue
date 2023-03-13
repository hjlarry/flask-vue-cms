<template>
  <el-config-provider :locale="aStore.language === 'en' ? en : zhCn">
    <router-view></router-view>
  </el-config-provider>
</template>

<script setup>
import { ElConfigProvider } from 'element-plus'
import zhCn from 'element-plus/lib/locale/lang/zh-cn'
import en from 'element-plus/lib/locale/lang/en'

import { genNewStyle, writeNewStyle } from '@/utils/theme'
import { themeStore } from '@/store/theme_store'
import { appStore } from '@/store/app_store'

const tStore = themeStore()
const aStore = appStore()
genNewStyle(tStore.mainColor).then((newStyle) => writeNewStyle(newStyle))
</script>
