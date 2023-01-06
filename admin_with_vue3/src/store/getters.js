const getters = {
  userInfo: (state) => state.user.userInfo,
  token: (state) => state.user.token,
  hasUserInfo: (state) => {
    return JSON.stringify(state.user.userInfo) !== '{}'
  },
  sidebarOpened: (state) => state.app.sidebarOpened,
  lang: (state) => state.app.language,
  tagsViewList: (state) => state.app.tagsView
}

export default getters
