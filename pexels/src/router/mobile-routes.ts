export default [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/main/index.vue')
  },
  {
    path: '/pictures/:id',
    name: 'picture',
    component: () => import('@/views/details/index.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login/login.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/login/register.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/profile/index.vue'),
    meta: {
      needLogin: true
    }
  },
  {
    path: '/vip',
    name: 'vip',
    component: () => import('@/views/vip/index.vue'),
    meta: {
      needLogin: true
    }
  },
  {
    path: '/pay/result',
    name: 'payResult',
    component: () => import('@/views/vip/result.vue'),
    meta: {
      needLogin: true
    }
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/errors/404.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: 'error',
    redirect: '/404'
  }
]
