import { createStore } from 'vuex'
import getters from './getters'
import user from './modules/user'
import app from './modules/app'

export default createStore({
  state: {},
  getters: getters,
  mutations: {},
  actions: {},
  modules: {
    user,
    app
  }
})
