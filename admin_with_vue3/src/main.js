import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import pinia from './store/pinia'
import i18n from './i18n'
import installElementPlus from './plugins/element'
import installFilters from './plugins/filter'
// import installIcons from './icons'
import installDirectives from './directives'
import './styles/index.scss'
import './permission'
import 'virtual:svg-icons-register'

const app = createApp(App)
installElementPlus(app)
// installIcons(app)
installFilters(app)
installDirectives(app)
app.use(pinia).use(router).use(i18n).mount('#app')
