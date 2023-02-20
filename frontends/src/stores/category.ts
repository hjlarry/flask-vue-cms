import { defineStore } from 'pinia'
import { getCategories } from '@/api/home'
import { getItem, setItem } from '@/utils/storage'

const CATEGORY_ALL_ITEM = { id: 'all', name: '全部' }

export const categoryStore = defineStore('category', {
  state: () => ({
    categories: getItem('categories') || [],
    currentCategory: CATEGORY_ALL_ITEM
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
      this.categories.unshift(CATEGORY_ALL_ITEM)
      setItem('categories', this.categories)
    },
    setCurrentCategory(category) {
      this.currentCategory = category
    }
  }
})
