import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'
import { toLogin } from '@/api/login'

export const userStore = defineStore('user', {
  state: () => ({
    token: getItem('token') || '',
    userInfo: getItem('userInfo') || {}
  }),
  actions: {
    async login(data) {
      const res = await toLogin(data)
      this.token = res.token
      setItem('token', this.token)
    }
  }
})
