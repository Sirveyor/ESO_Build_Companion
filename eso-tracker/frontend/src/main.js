import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

// crypto.randomUUID() requires a secure context (HTTPS/localhost).
// On LAN via plain HTTP it's missing — patch it with a Math.random fallback.
if (!crypto.randomUUID) {
  crypto.randomUUID = () => 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = Math.random() * 16 | 0
    return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16)
  })
}

const app = mount(App, {
  target: document.getElementById('app'),
})

export default app
