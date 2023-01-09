import { createRouter, createWebHashHistory } from 'vue-router'
import layout from '@/layout/index.vue'
import UserManageRouter from './modules/UserManage'
import RoleListRouter from './modules/RoleList'
import PermissionListRouter from './modules/PermissionList'
import ArticleRankingRouter from './modules/ArticleRanking'
import ArticleCreateRouter from './modules/ArticleCreate'
import { userStore } from '@/store/user_store'

export const publicRoutes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login/index')
  },
  {
    path: '/',
    redirect: '/profile',
    component: layout,
    children: [
      {
        path: '/profile',
        name: 'Profile',
        component: () => import('@/views/profile/index'),
        meta: {
          title: 'profile',
          icon: 'user'
        }
      },
      {
        path: '/404',
        name: '404',
        component: () => import('@/views/error-page/404')
      },
      {
        path: '/401',
        name: '401',
        component: () => import('@/views/error-page/401')
      }
    ]
  }
]

export const privateRoutes = [
  UserManageRouter,
  RoleListRouter,
  PermissionListRouter,
  ArticleRankingRouter,
  ArticleCreateRouter
]

const router = createRouter({
  history: createWebHashHistory(),
  routes: publicRoutes
})

export function resetRouter() {
  const uStore = userStore()
  if (
    uStore.userInfo &&
    uStore.userInfo.permissions &&
    uStore.userInfo.permissions.menus
  ) {
    const menus = uStore.userInfo.permissions.menus
    menus.forEach((menu) => router.removeRoute(menu))
  }
}

export default router
