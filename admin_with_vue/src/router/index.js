import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirct in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
  }
**/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/authredirect', component: () => import('@/views/login/authredirect'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard/index',
    name: 'Home',
    hidden: true
  },

  {
    path: '/dashboard',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index'),
        meta: { title: '主页', icon: 'home' }
      }
    ]
  },

  {
    path: '/article',
    component: Layout,
    redirect: '/article/all',
    name: 'article',
    meta: { title: '内容管理', icon: 'content' },
    children: [
      {
        path: 'all',
        name: 'article-all',
        component: () => import('@/views/article/index'),
        meta: { title: '资讯管理', icon: 'table' }
      },
      {
        path: 'create',
        component: () => import('@/views/article/create'),
        name: 'article-create',
        meta: { title: '创建资讯', icon: 'form' }
      },
      {
        path: 'edit',
        component: () => import('@/views/article/edit'),
        name: 'article-edit',
        hidden: true,
        meta: { title: '编辑资讯' }
      }
    ]
  },

  {
    path: '/system',
    component: Layout,
    redirect: '/system/user',
    name: 'system',
    meta: { title: '系统管理', icon: 'system' },
    children: [
      {
        path: 'user',
        name: 'user-all',
        component: () => import('@/views/user/index'),
        meta: { title: '系统用户管理', icon: 'user' }
      },
      {
        path: 'user_create',
        component: () => import('@/views/user/create'),
        name: 'user-create',
        meta: { title: '创建管理员', icon: 'user_add' }
      },
      {
        path: 'operation_log',
        component: () => import('@/views/sysinfo/OperationLog'),
        name: 'operation-log',
        meta: { title: '操作日志', icon: 'log' }
      },
      {
        path: 'user_edit',
        component: () => import('@/views/user/edit'),
        name: 'user-edit',
        hidden: true,
        meta: { title: '编辑管理员' }
      }
    ]
  },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

