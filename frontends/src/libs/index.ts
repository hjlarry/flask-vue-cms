import { defineAsyncComponent } from 'vue'

export default {
  install(app) {
    // 遍历libs文件夹下所有的文件夹中的index.vue文件，动态注册为全局组件
    const components = import.meta.glob('./*/index.vue')
    for (const [key, value] of Object.entries(components)) {
      const componentName = 'm-' + key.split('/')[1]
      app.component(componentName, defineAsyncComponent(value))
    }
  }
}
