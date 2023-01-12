import layout from '@/layout/index.vue'

export default {
  path: '/article',
  component: layout,
  redirect: '/articles',
  name: 'articles',
  meta: {
    title: 'article',
    icon: 'article'
  },
  children: [
    {
      path: '/articles',
      component: () => import('@/views/article-list/index.vue'),
      meta: {
        title: 'articles',
        icon: 'article-list'
      }
    },
    {
      path: '/article/:id',
      component: () => import('@/views/article-detail/index.vue'),
      meta: {
        title: 'articleDetail'
      }
    }
  ]
}
