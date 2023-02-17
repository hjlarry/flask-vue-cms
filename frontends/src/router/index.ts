import { createRouter, createWebHistory } from 'vue-router'
import { isMobileDevice } from '@/utils/flexiable'
import mobileRoutes from './mobile-routes'
import pcRoutes from './pc-routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: isMobileDevice.value ? mobileRoutes : pcRoutes
})

export default router
