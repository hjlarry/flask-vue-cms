import i18n from '@/i18n'

export const fuseConfig = {
  // 是否按优先级进行排序
  shouldSort: true,
  // 匹配长度超过这个值的才会被认为是匹配的
  minMatchCharLength: 1,
  // 将被搜索的键列表。 这支持嵌套路径、加权搜索、在字符串和对象数组中搜索。
  // name：搜索的键
  // weight：对应的权重
  keys: [
    {
      name: 'title',
      weight: 0.7
    },
    {
      name: 'path',
      weight: 0.3
    }
  ]
}

export function genRoutes(routes, prefixTitle = []) {
  const result = []
  routes.forEach((route) => {
    const data = {
      path: route.path,
      title: [...prefixTitle]
    }
    // 通过判断是否有冒号来判断是否是动态路由
    const re = /.*\/:.*/
    if (route.meta && route.meta.title && !re.exec(route.path)) {
      const i18nTitle = i18n.global.t(`msg.route.${route.meta.title}`)
      data.title = [...data.title, i18nTitle]
      result.push(data)
    }
    if (route.children) {
      result.push(...genRoutes(route.children, data.title))
    }
  })
  return result
}
