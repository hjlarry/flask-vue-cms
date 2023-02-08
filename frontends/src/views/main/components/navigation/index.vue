<template>
  <mobileNavigationVue
    v-if="isMoibleDevice"
    :data="categoriesData"
  ></mobileNavigationVue>
</template>

<script setup lang="ts">
import { isMoibleDevice } from '@/utils/flexiable'
import mobileNavigationVue from './mobile/index.vue'
import { getCategories } from '@/api/home'
import { ref } from 'vue'

const categoriesData = ref([] as any)
const getCategoriesData = async () => {
  const { categories } = await getCategories()
  categoriesData.value = categories
  categoriesData.value.unshift({ id: 'all', name: '全部' })
}
getCategoriesData()
</script>

<style scoped></style>
