import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'
import { DEFAULT_COLOR, MAIN_COLOR } from '@/constant'
// import variables from '@/styles/variables.scss'
import { genNewColor } from '@/utils/theme'

const variables = {
  menuBg: '#304156',
  menuHover: '#263445',
  subMenuBg: '#1f2d3d'
}
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
