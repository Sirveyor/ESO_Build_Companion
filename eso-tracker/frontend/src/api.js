// Points at port 8000 on whatever host served this page, so LAN devices work automatically.
const BASE = `http://${window.location.hostname}:8000`
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
  addSetBonus:    (setId, data)   => req('POST',   `/gear-sets/${setId}/bonuses`, data),
  deleteSetBonus: (setId, bonId)  => req('DELETE', `/gear-sets/${setId}/bonuses/${bonId}`),
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

  // UESP Scraper
  scraperSearch:  (q)              => req('GET',    `/scraper/search?q=${encodeURIComponent(q)}`),
  scraperPreview: (url)            => req('POST',   '/scraper/preview', { url }),
  scraperImport:  (url, overwrite) => req('POST',   '/scraper/import',  { url, overwrite: overwrite ?? false }),
}
