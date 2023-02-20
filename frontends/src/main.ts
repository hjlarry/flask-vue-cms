import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'virtual:svg-icons-register'

import App from './App.vue'
import router from './router'
import mLibs from './libs'
import useDirectives from './directives'
import { useREM } from './utils/flexiable'
import { useTheme } from './utils/theme'

import './assets/main.css'

const app = createApp(App)

useREM()

app.use(createPinia())
app.use(router)
app.use(mLibs)
useDirectives(app)
useTheme()

app.mount('#app')
