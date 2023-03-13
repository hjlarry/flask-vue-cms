import path from 'path'

function getChildren(routes) {
  const result = []
  routes.forEach((route) => {
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
  routes.forEach((route) => {
    if (!children.find((item) => item.path === route.path)) {
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
  routes.forEach((item) => {
    // 不存在 children && 不存在 meta 返回
    if (isNull(item.meta) && isNull(item.children)) return
    // 存在 children 不存在 meta，递归
    if (isNull(item.meta) && !isNull(item.children)) {
      result.push(...genMenus(item.children))
      return
    }
    const routePath = path.resolve(basePath, item.path)
    // 例如RoleList和UserMange都是 `/user`下的子页面，如果已添加过一个，另一个应该作为user的children
    let route = result.find((item) => item.path === routePath)
    if (!route) {
      route = {
        ...item,
        path: routePath,
        children: []
      }
      // 如果没有icon，也不会放到menu里去
      if (route.meta.title && route.meta.icon) {
        result.push(route)
      }
    }

    if (item.children) {
      route.children.push(...genMenus(item.children, route.path))
    }
  })
  return result
}
