import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const path = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  optimizeDeps: {
    exclude: ["oh-vue-icons/icons"]
  },
  server: {
    host: "localhost",
    port: 81,
  },
  logLevel: "error"
})