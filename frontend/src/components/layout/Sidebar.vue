<template>
  <aside class="w-64 mt-2" aria-label="Sidebar">
    <div class="overflow-y-auto py-4 px-3 bg-gray-50 rounded-md dark:bg-gray-800">
      <ul class="space-y-2">
        <li>
          <router-link to="/" class="flex items-center p-2 text-base font-normal text-gray-900 hover:text-white rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
            <!-- <svg class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path><path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path></svg> -->
            <v-icon name="md-spacedashboard-twotone" scale="1.25" />
            <span class="ml-3">Dashboard</span>
          </router-link>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 hover:text-white rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
            <!-- <svg class="flex-shrink-0 w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg> -->
            <v-icon name="la-address-book-solid" scale="1.25" />
            <span class="flex-1 ml-3 whitespace-nowrap">Address Book</span>
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 hover:text-white rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
            <v-icon name="md-businesscenter-twotone" scale="1.25" />
            <span class="flex-1 ml-3 whitespace-nowrap">Company Directory</span>
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 hover:text-white rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
            <v-icon name="la-file-invoice-dollar-solid" scale="1.25" />
            <span class="flex-1 ml-3 whitespace-nowrap">Invoices</span>
          </a>
        </li>
        <li>
          <a href="#" class="flex items-center p-2 text-base font-normal text-gray-900 hover:text-white rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
            <v-icon name="oi-project" scale="1.25" />
            <span class="flex-1 ml-3 whitespace-nowrap">Projects</span>
          </a>
        </li>
      </ul>
    </div>
  </aside>
</template>
<script setup>
const props = defineProps({
  children: {
    type: Array,
    default() {
      return []
    },
  },
  collapseBehavior: {
    type: String, // 'collapse' | 'hide';
    default: 'collapse',
  },
  collapsed: {
    type: Boolean,
    default: false,
  },
})
</script>