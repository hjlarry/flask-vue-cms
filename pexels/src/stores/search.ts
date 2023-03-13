import { defineStore } from 'pinia'
import { getItem, setItem } from '@/utils/storage'

export const searchStore = defineStore('search', {
  state: () => ({
    searchHistory: getItem('searchHistories') || [],
    currentSearch: ''
  }),
  actions: {
    addHistory(word: string) {
      const existIndex = this.searchHistory.findIndex((item) => item === word)
      if (existIndex !== -1) {
        this.searchHistory.splice(existIndex, 1)
      }
      this.searchHistory.unshift(word)
      setItem('searchHistories', this.searchHistory)
    },
    removeHistory(index: number) {
      this.searchHistory.splice(index, 1)
      setItem('searchHistories', this.searchHistory)
    },
    clearHistory() {
      this.searchHistory = []
      setItem('searchHistories', this.searchHistory)
    },
    changeCurrentSearch(word: string) {
      this.currentSearch = word
    }
  }
})
