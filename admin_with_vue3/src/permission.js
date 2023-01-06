import router from '@/router'
import { userStore } from '@/store/user_store'

const whiteList = ['/login']

router.beforeEach(async (to, from, next) => {
  const uStore = userStore()
  if (uStore.token) {
    if (to.path === '/login') {
      next('/')
    } else {
      if (!uStore.hasUserInfo) {
        await uStore.getUserInfo()
      }
      next()
    }
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next('/login')
    }
  }
})
