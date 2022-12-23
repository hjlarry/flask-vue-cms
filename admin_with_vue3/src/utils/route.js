import path from 'path'

function getChildren(routes) {
  const result = []
  routes.forEach(route => {
    if (route.children && route.children.length > 0) {
      result.push(...route.children)
    }
  })
  return result
}

// 只获取一级路由
export function filterRoutes(routes) {
  const children = getChildren(routes)
  const result = []
  routes.forEach(route => {
    if (!children.find(item => item.path === route.path)) {
      result.push(route)
    }
  })
  return result
}

function isNull(data) {
  if (!data) return true
  if (JSON.stringify(data) === '{}') return true
  if (JSON.stringify(data) === '[]') return true
  return false
}

export function genMenus(routes, basePath = '') {
  const result = []
  routes.forEach(route => {
    // 没有meta且没有children的直接跳过
    if (isNull(route.meta) && isNull(route.children)) return
    // 没有meta但有children的，递归
    if (isNull(route.meta) && !isNull(route.children)) {
      result.push(...genMenus(route.children))
      return
    }
    const routePath = path.resolve(basePath, route.path)
    const fRoute = {
      ...route,
      path: routePath,
      children: []
    }
    // 如果没有icon，也不会放到menu里去
    if (fRoute.meta.title && fRoute.meta.icon) {
      result.push(fRoute)
    }
    if (route.children) {
      fRoute.children.push(...genMenus(route.children, routePath))
    }
  })
  return result
}
