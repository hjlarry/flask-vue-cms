import { MAIN_COLOR, DEFAULT_COLOR } from '@/constant'
import { getItem, setItem } from '@/utils/storage'

export default {
  namespaced: true,
  state: () => ({
    mainColor: getItem(MAIN_COLOR) || DEFAULT_COLOR
  }),
  mutations: {
    setColor(state, color) {
      state.mainColor = color
      setItem(MAIN_COLOR, color)
    }
  },
  actions: {}
}
