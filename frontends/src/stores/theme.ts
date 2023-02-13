import { defineStore } from 'pinia'
import { THEME_LIGHT } from '@/constants'
import { getItem, setItem } from '@/utils/storage'

export const themeStore = defineStore('theme', {
  state: () => ({
    theme: getItem('theme') || THEME_LIGHT
  }),
  actions: {
    setTheme(theme: string) {
      this.theme = theme
      setItem('theme', theme)
    }
  }
})
