import { createRouter, createWebHistory } from "vue-router"

import ListCategory from "./pages/ListCategory"
import HelloWorld from "./components/HelloWorld"

const routes = [
    {
        name: 'list',
        path: '/',
        component: ListCategory
    },
    {
        name: 'hello-world',
        path: '/hello-world',
        component: HelloWorld
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router