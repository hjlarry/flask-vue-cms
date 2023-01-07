import request from '@/utils/request'

export const getRoles = () => {
  return request({
    url: '/role/list',
    method: 'get'
  })
}

export const getPermissions = () => {
  return request({
    url: '/permission/list',
    method: 'get'
  })
}
