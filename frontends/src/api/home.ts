import request from '@/utils/request'

type Result = {
  categories: Array<any>
}
export const getCategories = (): Result => {
  return request.get('/getCategories')
}
