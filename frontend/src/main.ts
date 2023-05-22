import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import "flowbite/dist/flowbite.css"
import "@/assets/main.css"

import { OhVueIcon, addIcons } from "oh-vue-icons"
import { MdSpacedashboardTwotone, LaAddressBookSolid, MdBusinesscenterTwotone, LaFileInvoiceDollarSolid, OiProject, MdPentagonTwotone } from "oh-vue-icons/icons"

addIcons(MdSpacedashboardTwotone, LaAddressBookSolid, MdBusinesscenterTwotone, LaFileInvoiceDollarSolid, OiProject, MdPentagonTwotone)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.component("v-icon", OhVueIcon)
app.use(store).use(router, axios).mount('#app')