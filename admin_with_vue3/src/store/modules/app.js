import { LANG, TAGS_VIEW } from '@/constant'
import { getItem, setItem } from '@/utils/storage'

export default {
  namespaced: true,
  state: () => ({
    sidebarOpened: true,
    language: getItem(LANG) || 'cn',
    tagsView: getItem(TAGS_VIEW) || []
  }),
  mutations: {
    triggerSidebarOpened(state) {
      state.sidebarOpened = !state.sidebarOpened
    },
    setLanguage(state, language) {
      state.language = language
      setItem(LANG, language)
    },
    addTag(state, tag) {
      const isFind = state.tagsView.find(item => item.path === tag.path)
      if (!isFind) {
        state.tagsView.push(tag)
        setItem(TAGS_VIEW, state.tagsView)
      }
    },
    changeTagsView(state, {
      index,
      tag
    }) {
      state.tagsView[index] = tag
      setItem(TAGS_VIEW, state.tagsView)
    }
  },
  actions: {}
}
