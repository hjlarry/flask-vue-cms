import router from '@/router'
import { message } from '@/libs/message'
import { userStore } from '@/stores/user'

router.beforeEach((to, from) => {
  if (!to.meta.needLogin) {
    return
  }
  const uStore = userStore()
  if (uStore.token) {
    return true
  }

  message('error', '请先登录')
  return '/'
})
