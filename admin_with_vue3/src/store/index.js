import { createStore } from 'vuex'
import user from './modules/user'
import getters from './getters'

export default createStore({
  state: {},
  getters: getters,
  mutations: {},
  actions: {},
  modules: {
    user
  }
})
