import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'
import { LANG, TAGS_VIEW } from '@/constant'

export const appStore = defineStore('app', {
  state: () => ({
    sidebarOpened: true,
    language: getItem(LANG) || 'cn',
    tagsView: getItem(TAGS_VIEW) || []
  }),
  getters: {},
  actions: {
    triggerSidebarOpened() {
      this.sidebarOpened = !this.sidebarOpened
    },
    setLanguage(language) {
      this.language = language
      setItem(LANG, language)
    },
    addTag(tag) {
      const isFind = this.tagsView.find((item) => item.path === tag.path)
      if (!isFind) {
        this.tagsView.push(tag)
        setItem(TAGS_VIEW, this.tagsView)
      }
    },
    changeTagsView({ index, tag }) {
      this.tagsView[index] = tag
      setItem(TAGS_VIEW, this.tagsView)
    },
    removeTagsView(payload) {
      if (payload.type === 'other') {
        this.tagsView = [this.tagsView[payload.index]]
      } else if (payload.type === 'right') {
        this.tagsView = this.tagsView.slice(0, payload.index + 1)
      } else if (payload.type === 'index') {
        this.tagsView.splice(payload.index, 1)
      }
      setItem(TAGS_VIEW, this.tagsView)
    }
  }
})
