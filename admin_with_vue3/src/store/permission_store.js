import { publicRoutes, privateRoutes } from '@/router'
import { defineStore } from 'pinia'

export const permissionStore = defineStore('permission', {
  state: () => ({
    routes: publicRoutes
  }),
  actions: {
    setRoutes(newRoutes) {
      this.routes = [...publicRoutes, ...newRoutes]
    },
    filterRoutes(menus) {
      const routes = []
      menus.forEach((key) => {
        routes.push(...privateRoutes.filter((item) => item.name === key))
      })
      routes.push({
        path: '/:catchAll(.*)',
        redirect: '/404'
      })
      this.setRoutes(routes)
      return routes
    }
  }
})
