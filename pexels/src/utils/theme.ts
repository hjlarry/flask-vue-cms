import { watch } from 'vue'

import { appStore } from '@/stores/app'
import { THEME_LIGHT, THEME_DARK, THEME_SYSTEM } from '@/constants'

const changeTheme = (theme: string) => {
  let themeClassName = ''
  switch (theme) {
    case THEME_LIGHT:
      themeClassName = 'light'
      break
    case THEME_DARK:
      themeClassName = 'dark'
      break
    case THEME_SYSTEM:
      watchSystemThemeChange()
      themeClassName = matchMedia.matches ? 'dark' : 'light'
      break
  }
  document.body.className = themeClassName
}

// 监听系统主题变化
let matchMedia
const watchSystemThemeChange = () => {
  // 仅初始化一次
  if (matchMedia) return
  matchMedia = window.matchMedia('(prefers-color-scheme: dark)')
  matchMedia.onchange = function () {
    changeTheme(THEME_SYSTEM)
  }
}

export function useTheme() {
  const aStore = appStore()
  watch(() => aStore.theme, changeTheme, { immediate: true })
}
