import { defineStore } from 'pinia'
import { THEME_LIGHT } from '@/constants'
import { getItem, setItem } from '@/utils/storage'

export const appStore = defineStore('app', {
  state: () => ({
    theme: getItem('theme') || THEME_LIGHT,
    // 用于确定路由跳转时，执行哪种动画效果
    routerType: 'none'
  }),
  actions: {
    setTheme(theme: string) {
      this.theme = theme
      setItem('theme', theme)
    },
    changeRouterType(type: 'none' | 'push' | 'back') {
      this.routerType = type
    }
  }
})
