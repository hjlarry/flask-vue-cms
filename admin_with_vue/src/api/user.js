import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/user',
    method: 'get',
    params: query
  })
}

export function deleteUser(id) {
  return request({
    url: '/user/delete/' + id,
    method: 'delete'
  })
}

export function createUser(data) {
  return request({
    url: '/user/create',
    method: 'post',
    data
  })
}

export function editUser(data) {
  return request({
    url: '/user/edit/' + data.id,
    method: 'put',
    data
  })
}

export function fetchUser(query) {
  return request({
    url: '/user/' + query,
    method: 'get'
  })
}
