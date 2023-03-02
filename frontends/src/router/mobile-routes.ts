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
  }
]
