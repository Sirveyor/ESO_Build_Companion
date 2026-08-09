// Points at a backend port on whatever host served this page, so LAN devices work automatically.
// Defaults to 8000, but can be overridden per-visitor via ?api_port=8001 (e.g. for testers who
// each run against their own isolated backend instance/database) -- the choice is remembered in
// localStorage so it only needs to be set once per browser.
const API_PORT = (() => {
  const fromUrl = new URLSearchParams(window.location.search).get('api_port')
  if (fromUrl) {
    localStorage.setItem('eso_api_port', fromUrl)
    return fromUrl
  }
  return localStorage.getItem('eso_api_port') || '8000'
})()

const BASE = `http://${window.location.hostname}:${API_PORT}`
const HEADERS = { 'Content-Type': 'application/json' }

async function req(method, path, body) {
  const res = await fetch(`${BASE}${path}`, {
    method,
    headers: HEADERS,
    body: body !== undefined ? JSON.stringify(body) : undefined,
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(err.detail || `HTTP ${res.status}`)
  }
  return res.status === 204 ? null : res.json()
}

export const api = {
  // App version
  getVersion: () => req('GET', '/version'),

  // Users
  getUsers:    ()         => req('GET',    '/users/'),
  createUser:  (data)     => req('POST',   '/users/', data),
  deleteUser:  (id)       => req('DELETE', `/users/${id}`),

  // Characters (pass userId to filter by user)
  getCharacters:   (userId)       => req('GET',    `/characters/${userId ? `?user_id=${userId}` : ''}`),
  createCharacter: (data)         => req('POST',   '/characters/', data),
  updateCharacter: (id, data)     => req('PUT',    `/characters/${id}`, data),
  deleteCharacter: (id)           => req('DELETE', `/characters/${id}`),
  setActiveBuild:  (charId, bid)  => req('PUT',    `/characters/${charId}/active_build?build_id=${bid}`),

  // Builds (scoped to a character)
  getCharacterBuilds: (charId)        => req('GET',    `/characters/${charId}/builds`),
  createBuild:        (charId, data)  => req('POST',   `/characters/${charId}/builds`, data),
  updateBuild:        (id, data)      => req('PUT',    `/builds/${id}`, data),
  deleteBuild:        (id)            => req('DELETE', `/builds/${id}`),
  getBuildCompletion: (id)            => req('GET',    `/builds/${id}/completion`),

  // Gear (scoped to a build)
  getBuildGear:       (buildId)        => req('GET',    `/builds/${buildId}/gear`),
  addGearToBuild:     (buildId, data)  => req('POST',   `/builds/${buildId}/gear`, data),
  updateGear:            (id, data)  => req('PUT', `/gear/${id}`, data),
  toggleGearObtained:    (id)        => req('PUT', `/gear/${id}/obtained`),
  toggleGearStickerbook: (id)        => req('PUT', `/gear/${id}/stickerbook`),
  updateGearEnchantment: (id, data)  => req('PUT', `/gear/${id}/enchantment`, data),
  deleteGear:         (id)             => req('DELETE', `/gear/${id}`),

  // Gear Sets
  getGearSets:    ()              => req('GET',    '/gear-sets/'),
  createGearSet:  (data)          => req('POST',   '/gear-sets/', data),
  deleteGearSet:  (id)            => req('DELETE', `/gear-sets/${id}`),
  addSetBonus:    (setId, data)          => req('POST',   `/gear-sets/${setId}/bonuses`, data),
  updateSetBonus: (setId, bonId, data)   => req('PUT',    `/gear-sets/${setId}/bonuses/${bonId}`, data),
  deleteSetBonus: (setId, bonId)         => req('DELETE', `/gear-sets/${setId}/bonuses/${bonId}`),
  compareGearSets:(ids)           => req('GET',    `/gear-sets/compare?set_ids=${ids.join(',')}`),

  // Build skills
  getBuildSkills:    (buildId)              => req('GET',    `/builds/${buildId}/skills`),
  setBuildSkill:     (buildId, data)        => req('POST',   `/builds/${buildId}/skills`, data),
  clearSkillSlot:    (buildId, bar, pos)    => req('DELETE', `/builds/${buildId}/skills/${bar}/${pos}`),
  toggleSkillObtained: (skillId)           => req('PUT',    `/skills/${skillId}/obtained`),

  // Champion Points
  getBuildCP:  (buildId)       => req('GET', `/builds/${buildId}/champion-points`),
  saveBuildCP: (buildId, data) => req('PUT', `/builds/${buildId}/champion-points`, data),

  // Traits (per character)
  getTraits:   (characterId)  => req('GET',    `/traits/${characterId ? `?character_id=${characterId}` : ''}`),
  createTrait: (data)         => req('POST',   '/traits/', data),
  deleteTrait: (id)           => req('DELETE', `/traits/${id}`),
  startTraitResearch: (id, endTime) =>
    req('PUT', `/traits/${id}/research?research_end_time=${encodeURIComponent(endTime)}`),
  completeTrait: (id) => req('PUT', `/traits/${id}/complete`),

  // Build duplicate
  duplicateBuild: (buildId) => req('POST', `/builds/${buildId}/duplicate`),

  // Reference data (read-only game data)
  getRefEnchantments: (slotType)  => req('GET', `/reference/enchantments${slotType ? `?slot_type=${slotType}` : ''}`),
  getRefTraits:       (slotType)  => req('GET', `/reference/traits${slotType ? `?slot_type=${slotType}` : ''}`),
  getRefMundusStones: ()          => req('GET', '/reference/mundus-stones'),
  getRefSkillLines:      (className)      => req('GET', `/reference/skill-lines${className ? `?class_name=${encodeURIComponent(className)}` : ''}`),
  getRefSkills:          (skillLineId)    => req('GET', `/reference/skills${skillLineId  ? `?skill_line_id=${encodeURIComponent(skillLineId)}` : ''}`),
  getRefResearchTraits:  (slotCategory)   => req('GET', `/reference/research-traits${slotCategory ? `?slot_category=${encodeURIComponent(slotCategory)}` : ''}`),
  getRefFood:            (foodType)       => req('GET', `/reference/food${foodType ? `?food_type=${encodeURIComponent(foodType)}` : ''}`),
  getRefWeaponTypes:     ()               => req('GET', '/reference/weapon-types'),
  getRefMotifs:          (category)       => req('GET', `/reference/motifs${category ? `?category=${encodeURIComponent(category)}` : ''}`),
  getRefFragments:       (category)       => req('GET', `/reference/fragments${category ? `?category=${encodeURIComponent(category)}` : ''}`),

  // Learned Recipes (per character)
  getLearnedRecipes:  (charId) => req('GET',    `/recipes/${charId ? `?character_id=${charId}` : ''}`),
  learnRecipe:        (data)   => req('POST',   '/recipes/', data),
  unlearnRecipe:      (id)     => req('DELETE', `/recipes/${id}`),

  // Learned Motifs (per character)
  getLearnedMotifs: (charId) => req('GET',    `/motifs/${charId ? `?character_id=${charId}` : ''}`),
  learnMotif:       (data)   => req('POST',   '/motifs/', data),
  unlearnMotif:     (id)     => req('DELETE', `/motifs/${id}`),

  // Learned Fragments (per character)
  getLearnedFragments: (charId) => req('GET',    `/fragments/${charId ? `?character_id=${charId}` : ''}`),
  learnFragment:       (data)   => req('POST',   '/fragments/', data),
  unlearnFragment:     (id)     => req('DELETE', `/fragments/${id}`),

  // UESP Scraper
  scraperSearch:  (q)              => req('GET',    `/scraper/search?q=${encodeURIComponent(q)}`),
  scraperPreview: (url)            => req('POST',   '/scraper/preview', { url }),
  scraperImport:  (url, overwrite) => req('POST',   '/scraper/import',  { url, overwrite: overwrite ?? false }),
}
