import variables from '@/styles/variables.scss'

const getters = {
  userInfo: (state) => state.user.userInfo,
  token: (state) => state.user.token,
  hasUserInfo: (state) => {
    return JSON.stringify(state.user.userInfo) !== '{}'
  },
  cssVar: (state) => variables,
  sidebarOpened: (state) => state.app.sidebarOpened,
  lang: (state) => state.app.language,
  mainColor: (state) => state.theme.mainColor
}

export default getters
