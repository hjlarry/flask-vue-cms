import request from '@/utils/request'

type CategoryResult = {
  categories: Array<any>
}
export const getCategories = (): CategoryResult => {
  return request.get('/getCategories')
}

type PexelsResult = {
  list: Array<any>
  total: number
}
export const getPexels = (params): PexelsResult => {
  return request.get('/getPexels', { params: params })
}

type HintResult = {
  result: Array<any>
}
export const getHint = (params): HintResult => {
  return request.get('/hint', { params: params })
}
