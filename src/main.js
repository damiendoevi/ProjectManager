import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from '../src/stores/index'
import axiosInterceptor from './services/axios-interceptor'
import { createPinia } from 'pinia'

try {
  await store.dispatch('auth/editProfile')
} catch (e) {
  //
}

axiosInterceptor(store)
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(store)

app.mount('#app')
