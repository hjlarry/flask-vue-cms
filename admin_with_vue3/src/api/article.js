import request from '@/utils/request'

export const getArticles = (data) => {
  return request({
    url: '/article/list',
    method: 'get',
    params: data
  })
}
