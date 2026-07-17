<script>
  import { api } from '../api.js'
  import { ESO_CLASSES, ESO_ROLES, ROLE_ICONS, ALLIANCE_COLORS } from './constants.js'

  let { character, onselect, onback } = $props()

  let builds      = $state([])
  let completions = $state({})
  let loading     = $state(true)
  let error       = $state('')
  let showForm    = $state(false)
  let saving      = $state(false)
  let editId      = $state(null)

  let form = $state(blankForm())

  function blankForm() {
    return {
      name: '',
      class_name: character?.class_name ?? ESO_CLASSES[0],
      role: character?.role ?? ESO_ROLES[0],
      patch_version: '',
      notes: '',
    }
  }

  async function load() {
    try {
      builds = await api.getCharacterBuilds(character.id)
      // Fetch completion for each build in parallel
      const results = await Promise.all(builds.map(b => api.getBuildCompletion(b.id).catch(() => null)))
      completions = Object.fromEntries(builds.map((b, i) => [b.id, results[i]]))
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function saveBuild() {
    if (!form.name.trim()) return
    saving = true; error = ''
    try {
      const payload = {
        name: form.name.trim(),
        class_name: form.class_name,
        role: form.role,
        patch_version: form.patch_version || null,
        notes: form.notes || null,
        source_link_id: null,
        last_updated: new Date().toISOString(),
        favorite: 0,
        tags: null,
      }
      if (editId) {
        const updated = await api.updateBuild(editId, { ...payload, id: editId })
        builds = builds.map(b => b.id === editId ? updated : b)
        editId = null
      } else {
        const created = await api.createBuild(character.id, { ...payload, id: crypto.randomUUID() })
        builds = [...builds, created]
        completions = { ...completions, [created.id]: { total_pieces: 0, obtained: 0, percent: 0 } }
      }
      form = blankForm(); showForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEdit(b) {
    editId = b.id
    form = {
      name: b.name, class_name: b.class_name, role: b.role,
      patch_version: b.patch_version || '', notes: b.notes || '',
    }
    showForm = true
  }

  async function deleteBuild(id) {
    if (!confirm('Delete this build and all its gear? This cannot be undone.')) return
    try {
      await api.deleteBuild(id)
      builds = builds.filter(b => b.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  async function duplicateBuild(b) {
    try {
      const copy = await api.duplicateBuild(b.id)
      builds = [...builds, copy]
      completions = { ...completions, [copy.id]: { total_pieces: 0, obtained: 0, percent: 0 } }
    } catch (e) {
      error = e.message
    }
  }

  function cancelForm() { showForm = false; editId = null; form = blankForm(); error = '' }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1.5rem">
    <div>
      <button class="btn-ghost back-btn" onclick={onback}>‹ Characters</button>
      <h1>{character.name}</h1>
      <div class="char-meta flex" style="margin-top:.25rem">
        <span class="badge">{character.class_name}</span>
        <span class="badge">{ROLE_ICONS[character.role]} {character.role}</span>
        <span class="badge">{character.race}</span>
        {#if character.alliance}
          <span class="badge"
                style="border-color:{ALLIANCE_COLORS[character.alliance]};color:{ALLIANCE_COLORS[character.alliance]}">
            {character.alliance}
          </span>
        {/if}
        <span style="color:var(--text-dim);font-size:.85rem">Lv {character.level} · {character.champion_points} CP</span>
      </div>
    </div>
    <button class="btn-primary" onclick={() => { showForm = !showForm; if (!showForm) cancelForm() }}>
      {showForm && !editId ? 'Cancel' : '+ New Build'}
    </button>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if showForm}
    <div class="inline-form" style="margin-bottom:1.5rem">
      <h3 style="margin-bottom:.75rem">{editId ? 'Edit Build' : 'New Build'}</h3>
      <div class="form-grid">
        <div class="form-row">
          <label>Build Name *</label>
          <input bind:value={form.name} placeholder="e.g. Oakensoul Mag Sorc" />
        </div>
        <div class="form-row">
          <label>Class</label>
          <select bind:value={form.class_name}>
            {#each ESO_CLASSES as c}<option>{c}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Role</label>
          <select bind:value={form.role}>
            {#each ESO_ROLES as r}<option>{r}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Patch Version</label>
          <input bind:value={form.patch_version} placeholder="e.g. U42" />
        </div>
      </div>
      <div class="form-row">
        <label>Notes</label>
        <textarea bind:value={form.notes} placeholder="Build notes, source URL, etc."></textarea>
      </div>
      <div class="flex" style="gap:.5rem">
        <button class="btn-primary" onclick={saveBuild} disabled={saving || !form.name.trim()}>
          {saving ? 'Saving…' : editId ? 'Save Changes' : 'Create Build'}
        </button>
        <button class="btn-ghost" onclick={cancelForm}>Cancel</button>
      </div>
    </div>
  {/if}

  {#if loading}
    <p>Loading builds…</p>
  {:else if builds.length === 0}
    <div class="empty">
      <div class="empty-icon">📋</div>
      <h2>No builds yet</h2>
      <p>Create a build to start tracking gear for {character.name}.</p>
    </div>
  {:else}
    <div class="builds-list">
      {#each builds as b (b.id)}
        {@const comp = completions[b.id]}
        <div class="card card-clickable build-row" onclick={() => onselect(b)}>
          <div class="build-main">
            <div class="build-name">{b.name}</div>
            <div class="build-meta flex">
              <span class="badge">{ROLE_ICONS[b.role]} {b.role}</span>
              <span class="badge">{b.class_name}</span>
              {#if b.patch_version}<span class="badge badge-blue">{b.patch_version}</span>{/if}
              {#if b.favorite}<span class="badge badge-gold">★ Favourite</span>{/if}
            </div>
            {#if b.notes}
              <p style="font-size:.8rem;margin-top:.3rem;color:var(--text-dim)">{b.notes}</p>
            {/if}
          </div>
          <div class="build-progress">
            {#if comp}
              <div class="progress-label">
                <span>{comp.obtained}/{comp.total_pieces} pieces</span>
                <span class:full={comp.percent === 100}>{comp.percent}%</span>
              </div>
              <div class="progress-wrap">
                <div class="progress-bar" class:full={comp.percent === 100}
                     style="width:{comp.percent}%"></div>
              </div>
            {:else}
              <span style="color:var(--text-dim);font-size:.8rem">No gear added</span>
            {/if}
          </div>
          <div class="build-actions" onclick={(e) => e.stopPropagation()}>
            <button class="btn-icon" onclick={() => startEdit(b)} title="Edit">✎</button>
            <button class="btn-icon" onclick={() => duplicateBuild(b)} title="Duplicate">⧉</button>
            <button class="btn-icon" onclick={() => deleteBuild(b.id)} title="Delete">✕</button>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .back-btn { margin-bottom: .25rem; font-size: .85rem; }
  .char-meta { flex-wrap: wrap; }

  .builds-list { display: flex; flex-direction: column; gap: .75rem; }

  .build-row {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .build-main { flex: 1; min-width: 0; }
  .build-name { font-weight: 600; font-size: 1.05rem; margin-bottom: .3rem; }
  .build-meta { flex-wrap: wrap; }

  .build-progress { width: 180px; flex-shrink: 0; }
  .progress-label {
    display: flex;
    justify-content: space-between;
    font-size: .75rem;
    color: var(--text-dim);
    margin-bottom: .3rem;
  }
  .progress-label .full { color: var(--green); }

  .build-actions { display: flex; gap: .2rem; opacity: 0; transition: opacity .15s; }
  .build-row:hover .build-actions { opacity: 1; }

  @media (max-width: 640px) {
    .build-row { flex-wrap: wrap; }
    .build-progress { width: 100%; }
  }
</style>
