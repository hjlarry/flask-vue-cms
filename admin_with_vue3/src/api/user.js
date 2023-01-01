import request from '@/utils/request'

export const getFeature = () => {
  return request({
    url: '/user/feature',
    method: 'get'
  })
}
