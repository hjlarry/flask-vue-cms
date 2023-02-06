import { createRouter, createWebHistory } from 'vue-router'
import { isMoibleDevice } from '@/utils/flexiable'
import mobileRoutes from './mobile-routes'
import pcRoutes from './pc-routes'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: isMoibleDevice.value ? mobileRoutes : pcRoutes
})

export default router
