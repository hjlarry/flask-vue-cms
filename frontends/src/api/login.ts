import request from '@/utils/request'

export const toLogin = (data) => {
  return request.post('/login', { data: data })
}
