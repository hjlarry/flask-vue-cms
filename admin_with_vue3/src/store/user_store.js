import { defineStore } from 'pinia'
import { clear, getItem, setItem } from '@/utils/storage'
import { TOKEN } from '@/constant'
import { getInfo, toLogin } from '@/api/login'
import router from '@/router'

export const userStore = defineStore('user', {
  state: () => ({
    token: getItem(TOKEN),
    userInfo: {}
  }),
  getters: {
    hasUserInfo(state) {
      return JSON.stringify(state.userInfo) !== '{}'
    }
  },
  actions: {
    login(userinfo) {
      const { username, password } = userinfo
      return new Promise((resolve, reject) => {
        toLogin({ username: username.trim(), password: password })
          .then((response) => {
            this.token = response.data.token
            setItem(TOKEN, response.data.token)
            resolve()
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
    async getUserInfo() {
      const response = await getInfo(this.token)
      this.userInfo = response.data
      return response.data
    },
    logout() {
      this.token = ''
      this.userInfo = {}
      clear()
      router.push('/login')
    }
  }
})
