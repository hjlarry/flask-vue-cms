import { MAIN_COLOR } from '@/constant'
import { getItem } from '@/utils/storage'
import { genNewColor } from '@/utils/theme'

const getters = {
  userInfo: (state) => state.user.userInfo,
  token: (state) => state.user.token,
  hasUserInfo: (state) => {
    return JSON.stringify(state.user.userInfo) !== '{}'
  },
  cssVar: (state) => {
    return {
      ...state.theme.variables,
      ...genNewColor(getItem(MAIN_COLOR))
    }
  },
  sidebarOpened: (state) => state.app.sidebarOpened,
  lang: (state) => state.app.language,
  mainColor: (state) => state.theme.mainColor
}

export default getters
