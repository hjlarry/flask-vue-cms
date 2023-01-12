import request from '@/utils/request'

export const getFeature = () => {
  return request({
    url: '/feature',
    method: 'get'
  })
}

export const getTimeline = () => {
  return request({
    url: '/timeline',
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

export const userDetail = (id) => {
  return request({
    url: '/user/' + id
  })
}

export const userRole = (id) => {
  return request({
    url: '/user/role/' + id
  })
}

export const updateUserRole = (id, data) => {
  return request({
    url: '/user/role/' + id,
    method: 'post',
    data
  })
}
