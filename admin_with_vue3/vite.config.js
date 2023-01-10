import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { createSvgIconsPlugin } from 'vite-plugin-svg-icons'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    createSvgIconsPlugin({
      // 指定需要缓存的图标文件夹
      iconDirs: [fileURLToPath(new URL('./src/icons/svg', import.meta.url))],
      // 指定symbolId格式
      symbolId: 'icon-[name]'
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      path: 'path-browserify'
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
              @import "./src/styles/variables.scss";
            `
      }
    }
  },
  server: {
    host: '127.0.0.1',
    port: 3000,
    proxy: {
      '/admin': {
        target: 'http://127.0.0.1:5000', //实际请求地址
        changeOrigin: true
      }
    }
  }
})
