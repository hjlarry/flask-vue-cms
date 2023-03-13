const whiteList = ['/login', '/register', '/404', '/401']

export function shouldInTagsView(path) {
  return !whiteList.includes(path)
}
