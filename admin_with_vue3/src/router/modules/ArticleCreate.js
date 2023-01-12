import layout from '@/layout/index.vue'

export default {
  path: '/article',
  component: layout,
  redirect: '/articles',
  name: 'articleCreate',
  meta: {
    title: 'article',
    icon: 'article'
  },
  children: [
    {
      path: '/article/create',
      component: () => import('@/views/article-create/index.vue'),
      meta: {
        title: 'articleCreate',
        icon: 'article-create'
      }
    },
    {
      path: '/article/edit/:id',
      component: () => import('@/views/article-create/index.vue'),
      meta: {
        title: 'articleEdit'
      }
    }
  ]
}
