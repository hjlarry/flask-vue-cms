import router from '@/router'
import store from '@/store'

const whiteList = ['/login']

router.beforeEach(async (to, from, next) => {
  if (store.state.user.token) {
    if (to.path === '/login') {
      next('/')
    } else {
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
