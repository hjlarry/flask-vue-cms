import { MAIN_COLOR, DEFAULT_COLOR } from '@/constant'
import { getItem, setItem } from '@/utils/storage'
import variables from '@/styles/variables.scss'

export default {
  namespaced: true,
  state: () => ({
    mainColor: getItem(MAIN_COLOR) || DEFAULT_COLOR,
    variables
  }),
  mutations: {
    setColor(state, color) {
      state.mainColor = color
      state.variables.menuBg = color
      setItem(MAIN_COLOR, color)
    }
  },
  actions: {}
}
