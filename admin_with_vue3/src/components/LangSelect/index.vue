<template>
  <el-dropdown trigger="click" class="lang-select" @command="SwitchLang">
    <span>
      <el-tooltip :content="$t('msg.navBar.lang')">
        <SvgIcon id="guide-lang" icon="language"></SvgIcon>
      </el-tooltip>
    </span>

    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item command="en" :disabled="lang === 'en'">
          English
        </el-dropdown-item>
        <el-dropdown-item command="cn" :disabled="lang === 'cn'">
          中文
        </el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { ElMessage } from 'element-plus'

import { appStore } from '@/store/app_store'
import SvgIcon from '@/components/SvgIcon/index.vue'

const aStore = appStore()
const lang = computed(() => aStore.language)
const i18n = useI18n()

function SwitchLang(command) {
  aStore.setLanguage(command)
  i18n.locale.value = command
  ElMessage.success(i18n.t('msg.toast.switchLangSuccess'))
}
</script>

<style scoped></style>
