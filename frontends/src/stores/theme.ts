import { defineStore } from 'pinia'
import { THEME_LIGHT } from '@/constants'

export const themeStore = defineStore('theme', {
  state: () => ({
    theme: THEME_LIGHT
  }),
  actions: {
    setTheme(theme: string) {
      this.theme = theme
    }
  }
})
