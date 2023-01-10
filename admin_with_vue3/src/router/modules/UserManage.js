import layout from '@/layout/index.vue'

export default {
  path: '/user',
  component: layout,
  redirect: '/user/manage',
  name: 'userManage',
  meta: {
    title: 'user',
    icon: 'personal'
  },
  children: [
    {
      path: '/user/manage',
      component: () => import('@/views/user-manage/index.vue'),
      meta: {
        title: 'userManage',
        icon: 'personal-manage'
      }
    },
    {
      path: '/user/info/:id',
      name: 'userInfo',
      props: true,
      component: () => import('@/views/user-info/index.vue'),
      meta: {
        title: 'userInfo'
      }
    },
    {
      path: '/user/import',
      name: 'userImport',
      component: () => import('@/views/import/index.vue'),
      meta: {
        title: 'excelImport'
      }
    }
  ]
}
