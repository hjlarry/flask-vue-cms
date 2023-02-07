import { createApp } from 'vue'
import { createPinia } from 'pinia'
import 'virtual:svg-icons-register'

import App from './App.vue'
import router from './router'
import mLibs from './libs'
import { useREM } from './utils/flexiable'

import './assets/main.css'

const app = createApp(App)

useREM()

app.use(createPinia())
app.use(router)
app.use(mLibs)

app.mount('#app')
