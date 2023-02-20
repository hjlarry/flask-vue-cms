export default {
  async install(app) {
    // glob默认懒加载，eager为true则直接引入所有模块
    const directives = import.meta.glob('./modules/*.ts', { eager: true })
    for (const [key, value] of Object.entries(directives)) {
      const name = key.replace(/\.\/modules\/(.*)\.ts/, '$1')
      app.directive(name, value.default)
    }
  }
}
