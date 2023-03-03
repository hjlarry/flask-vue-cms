import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'
import { toLogin, getInfo } from '@/api/login'
import { message } from '@/libs/message'

export const userStore = defineStore('user', {
  state: () => ({
    token: getItem('token') || '',
    userInfo: getItem('userInfo') || {}
  }),
  actions: {
    setToken(token) {
      this.token = token
      setItem('token', token)
    },
    setUserInfo(info) {
      this.userInfo = info
      setItem('userInfo', info)
    },
    async login(data) {
      const res = await toLogin(data)
      this.setToken(res.token)
      this.getInfo()
    },
    async getInfo() {
      const res = await getInfo()
      this.setUserInfo(res)
      message(
        'success',
        `欢迎您 ${
          res.vipLevel
            ? '尊贵的 VIP' + res.vipLevel + ' 用户 ' + res.nickname
            : res.nickname
        } `,
        3000
      )
    },
    logOut() {
      this.setToken('')
      this.setUserInfo({})
    }
  }
})
