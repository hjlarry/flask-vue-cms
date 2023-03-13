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
export const getPexel = (params) => {
  return request.get('/getPexel', { params: params })
}

type CommonResult = {
  result: Array<any>
}
export const getHint = (params): CommonResult => {
  return request.get('/hint', { params: params })
}

export const getHot = (): CommonResult => {
  return request.get('/hot')
}

export const getVipPayList = (): CommonResult => {
  return request.get('/getVipPayList')
}
