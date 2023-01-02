import request from '@/utils/request'

export const getFeature = () => {
  return request({
    url: '/user/feature',
    method: 'get'
  })
}

export const getChapter = () => {
  return request({
    url: '/user/chapter',
    method: 'get'
  })
}
