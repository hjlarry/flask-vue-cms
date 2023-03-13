import request from '@/utils/request'

export const getArticles = (data) => {
  return request({
    url: '/article/list',
    method: 'get',
    params: data
  })
}

export const articleDelete = (id) => {
  return request({
    url: '/article/delete/' + id,
    method: 'post'
  })
}

export const articleDetail = (id) => {
  return request({
    url: '/article/' + id
  })
}

export const createArticle = (data) => {
  return request({
    url: '/article',
    method: 'post',
    data
  })
}

export const editArticle = (id, data) => {
  return request({
    url: '/article/' + id,
    method: 'post',
    data
  })
}
