import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/article',
    method: 'get',
    params: query
  })
}

export function createArticle(data) {
  return request({
    url: '/article/create',
    method: 'post',
    data
  })
}

export function editArticle(data) {
  return request({
    url: '/article/edit/' + data.id,
    method: 'put',
    data
  })
}

export function fetchArticle(query) {
  return request({
    url: '/article/' + query,
    method: 'get'
  })
}

export function fetchModule() {
  return request({
    url: '/module',
    method: 'get'
  })
}

export function deleteArticle(id) {
  return request({
    url: '/article/delete/' + id,
    method: 'delete'
  })
}
