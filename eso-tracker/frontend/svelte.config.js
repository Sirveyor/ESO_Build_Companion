/** @type {import("@sveltejs/vite-plugin-svelte").SvelteConfig} */

// Suppress a11y warnings that are purely academic for a private household app.
const SUPPRESSED = new Set([
  'a11y_label_has_associated_control',
  'a11y_click_events_have_key_events',
  'a11y_no_static_element_interactions',
])

export default {
  onwarn(warning, defaultHandler) {
    if (SUPPRESSED.has(warning.code)) return
    defaultHandler(warning)
  },
}
