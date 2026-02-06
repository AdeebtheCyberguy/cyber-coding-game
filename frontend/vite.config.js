import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    base: '/cyber-coding-game/',
    plugins: [react()],
    server: {
        port: 5173,
        proxy: {
            // Proxy API requests to backend during development
            '/api': {
                target: 'http://localhost:8000',
                changeOrigin: true,
            },
        },
    },
    build: {
        outDir: 'dist',
        sourcemap: false, // Disable sourcemaps in production for security
    },
})
