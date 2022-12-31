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
    },
    removeTagsView(state, payload) {
      if (payload.type === 'other') {
        state.tagsView = [state.tagsView[payload.index]]
      } else if (payload.type === 'right') {
        state.tagsView = state.tagsView.slice(0, payload.index + 1)
      } else if (payload.type === 'index') {
        state.tagsView.splice(payload.index, 1)
      }
      setItem(TAGS_VIEW, state.tagsView)
    }
  },
  actions: {}
}
