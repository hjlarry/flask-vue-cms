import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'virtual:svg-icons-register'

import App from './App.vue'
import router from './router'
import mLibs from './libs'
import mDirectives from './directives'
import { useREM } from './utils/flexiable'
import { useTheme } from './utils/theme'
import './permission'
import './assets/main.css'

const app = createApp(App)

useREM()

app.use(createPinia())
app.use(router)
app.use(mLibs)
app.use(mDirectives)
useTheme()

app.mount('#app')
