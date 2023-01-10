import router from '@/router'
import { userStore } from '@/store/user_store'
import { permissionStore } from '@/store/permission_store'

const whiteList = ['/login']

router.beforeEach(async (to, from, next) => {
  const uStore = userStore()
  const pStore = permissionStore()
  if (uStore.token) {
    if (to.path === '/login') {
      next('/')
    } else {
      if (!uStore.hasUserInfo) {
        // 1. 获取当前登录用户信息； 2.拿到其权限数据
        const { permissions } = await uStore.getUserInfo()
        const routes = pStore.filterRoutes(permissions.menus)
        routes.forEach((route) => {
          router.addRoute(route)
        })
        // 添加动态路由后，需要再进行一次主动跳转，否则刷新页面就空白
        return next(to.path)
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
