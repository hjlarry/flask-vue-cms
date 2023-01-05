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

export const getUsers = (data) => {
  return request({
    url: '/user/list',
    method: 'get',
    params: data
  })
}

export const userBatchImport = (data) => {
  return request({
    url: '/user/batchImport',
    method: 'post',
    data
  })
}

export const userDelete = (id) => {
  return request({
    url: '/user/delete/' + id,
    method: 'post'
  })
}
