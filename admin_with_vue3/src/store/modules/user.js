import { login, getInfo } from '@/api/login'
import { getItem, setItem } from '@/utils/storage'
import { TOKEN } from '@/constant'

export default {
  namespaced: true,
  state: () => ({
    token: getItem(TOKEN),
    userinfo: {}
  }),
  mutations: {
    setToken(state, token) {
      state.token = token
      setItem(TOKEN, token)
    },
    setUserInfo(state, userinfo) {
      state.userinfo = userinfo
    }
  },
  actions: {
    login(context, userinfo) {
      const { username, password } = userinfo
      return new Promise((resolve, reject) => {
        login({ username: username.trim(), password: password })
          .then((response) => {
            console.log(response)
            this.commit('user/setToken', response.data.token)
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
    async getUserInfo(context) {
      const response = await getInfo(context.state.token)
      this.commit('user/setUserInfo', response.data)
      return response.data
    }
  }
}
