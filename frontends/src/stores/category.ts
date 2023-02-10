import { defineStore } from 'pinia'
import { getCategories } from '@/api/home'
import { getItem, setItem } from '@/utils/storage'

export const categoryStore = defineStore('category', {
  state: () => ({
    categories: getItem('categories') || []
  }),
  getters: {
    categoriesData(state) {
      if (state.categories.length === 0) {
        this.fetchCategories()
      }
      return state.categories
    }
  },
  actions: {
    async fetchCategories() {
      const res = await getCategories()
      this.categories = res.categories
      this.categories.unshift({ id: 'all', name: '全部' })
      setItem('categories', this.categories)
    }
  }
})
