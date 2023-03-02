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
      }
    ]
  }
]
