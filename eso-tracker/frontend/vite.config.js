import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  server: {
    host: true,   // bind to 0.0.0.0 so Deborah's iPad can reach it on LAN
    port: 5173,
  },
})
