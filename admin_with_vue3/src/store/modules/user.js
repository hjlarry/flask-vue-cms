import { login } from '@/api/login'
import { getItem, setItem } from '@/utils/storage'
import { TOKEN } from '@/constant'

export default {
  namespaced: true,
  state: () => ({
    token: getItem(TOKEN)
  }),
  mutations: {
    setToken(state, token) {
      state.token = token
      setItem(TOKEN, token)
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
    }
  }
}
