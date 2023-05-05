import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css"
import "@/assets/bootstrap.bundle.min.js"
import 'material-icons/iconfont/material-icons.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(router, axios).mount('#app')
