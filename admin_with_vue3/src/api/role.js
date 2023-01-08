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

export const getRolePermission = (id) => {
  return request({
    url: '/role/' + id + '/permission',
    method: 'get'
  })
}

export const setRolePermission = (id, data) => {
  return request({
    url: '/role/' + id + '/permission',
    method: 'post',
    data
  })
}
