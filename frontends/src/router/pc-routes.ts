export default [
  {
    path: '/',
    name: 'main',
    component: () => import('@/views/pc-layout/index.vue'),
    children: [
      {
        path: '',
        name: 'home',
        component: () => import('@/views/main/index.vue')
      },
      {
        path: '/pictures/:id',
        name: 'picture',
        component: () => import('@/views/details/index.vue')
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
      }
    ]
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
  }
]
