<template>
  <mobile-navigation-vue
    v-if="isMoibleDevice"
    :data="categoriesData"
  ></mobile-navigation-vue>
</template>

<script setup>
import { isMoibleDevice } from '@/utils/flexiable'
import mobileNavigationVue from './mobile/index.vue'
import { getCategories } from '@/api/home'
import { ref } from 'vue'

const categoriesData = ref([])
const getCategoriesData = async () => {
  const { categories } = await getCategories()
  categoriesData.value = categories
}
getCategoriesData()
</script>

<style scoped></style>
