import { watch } from 'vue'

import { themeStore } from '@/stores/theme'
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
  }
  document.body.className = themeClassName
}

export function useTheme() {
  const tStore = themeStore()
  watch(() => tStore.$state.theme, changeTheme, { immediate: true })
}
