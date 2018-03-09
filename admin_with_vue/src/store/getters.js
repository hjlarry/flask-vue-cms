const getters = {
  sidebar: state => state.app.sidebar,
  token: state => state.user.token,
  avatar: state => process.env.SITE_URL + state.user.avatar,
  name: state => state.user.name,
  roles: state => state.user.roles,
  visitedViews: state => state.tagsView.visitedViews,
  cachedViews: state => state.tagsView.cachedViews
}
export default getters
