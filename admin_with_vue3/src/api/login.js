import request from '@/utils/request'

export const login = (data) => {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export const getInfo = (token) => {
  return request({
    url: '/info',
    method: 'get',
    params: { token }
  })
}
