import request from '@/utils/request'

export const getCategories = () => {
  return request({
    url: '/getCategories',
    method: 'get'
  })
}
