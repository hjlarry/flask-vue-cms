import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'
import { DEFAULT_COLOR, MAIN_COLOR } from '@/constant'
import { genNewColor, variables } from '@/utils/theme'

export const themeStore = defineStore('theme', {
  state: () => ({
    mainColor: getItem(MAIN_COLOR) || DEFAULT_COLOR,
    variables
  }),
  getters: {
    cssVar(state) {
      return {
        ...state.variables,
        ...genNewColor(getItem(MAIN_COLOR))
      }
    }
  },
  actions: {
    setColor(color) {
      this.mainColor = color
      this.variables.menuBg = color
      setItem(MAIN_COLOR, color)
    }
  }
})
