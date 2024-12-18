/* eslint-disable */
import {defineConfig, loadEnv} from "vite"
import react from "@vitejs/plugin-react-swc"

// https://vitejs.dev/config/
export default defineConfig(({mode}) => {
  const env = loadEnv(mode, process.cwd(), "")
  return {
    plugins: [react()],
    preview: {
      port: env.VITE_CLIENT_PORT,
    },
    server: {
      port: env.VITE_CLIENT_PORT,
    },
  }
})