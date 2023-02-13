import request from '@/utils/request'

type Result = {
  categories: Array<any>
}
export const getCategories = (): Result => {
  return request.get('/getCategories')
}

export const getPexels = () => {
  return request.get('/getPexels')
}
