<script>
  import { api } from '../api.js'
  import { ESO_CLASSES, ESO_RACES, ESO_ROLES, ESO_ALLIANCES, ALLIANCE_COLORS, CLASS_COLORS, ROLE_ICONS } from './constants.js'
  import OnboardingTour from './OnboardingTour.svelte'

  let { user, onselect, onback } = $props()

  let characters   = $state([])
  let loading      = $state(true)
  let error        = $state('')
  let showForm     = $state(false)
  let saving       = $state(false)
  let editId       = $state(null)
  let showCharTour = $state(false)
  let newCharId    = $state(null)

  const newChar = $derived(characters.find(c => c.id === newCharId))
  const charTourSteps = $derived([
    {
      title: `${newChar?.name ?? 'Your character'} is on the roster!`,
      text: 'A couple of quick pointers.',
    },
    {
      selector: '[data-tour="new-char-card"]',
      title: 'Your character',
      text: 'Click the card to manage builds and track gear. Hover it for edit and delete options.',
    },
    {
      selector: '[data-tour="new-char-btn"]',
      title: 'Add more',
      text: 'Add as many characters as you like from here.',
    },
  ])

  function finishCharTour() {
    localStorage.setItem(`eso_char_tour_seen:${user.id}`, '1')
    showCharTour = false
    newCharId = null
  }

  let form = $state(blankForm())

  function blankForm() {
    return {
      name: '', class_name: ESO_CLASSES[0], race: ESO_RACES[0],
      role: ESO_ROLES[0], alliance: ESO_ALLIANCES[0], level: 50, champion_points: 0, notes: '',
      custom_portrait: '',
    }
  }

  async function load() {
    try {
      characters = await api.getCharacters(user.id)
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function saveCharacter() {
    if (!form.name.trim()) return
    saving = true; error = ''
    try {
      const payload = {
        ...form,
        name: form.name.trim(),
        level: Number(form.level) || 50,
        champion_points: Number(form.champion_points) || 0,
        alliance: form.alliance || null,
        user_id: user.id,
        active_build_id: null,
        last_updated: new Date().toISOString(),
        custom_portrait: form.custom_portrait.trim() || null,
      }
      if (editId) {
        const updated = await api.updateCharacter(editId, { ...payload, id: editId })
        characters = characters.map(c => c.id === editId ? updated : c)
        editId = null
      } else {
        const created = await api.createCharacter({ ...payload, id: crypto.randomUUID() })
        characters = [...characters, created]
        newCharId = created.id
        if (!localStorage.getItem(`eso_char_tour_seen:${user.id}`)) showCharTour = true
      }
      form = blankForm(); showForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEdit(c) {
    editId = c.id
    form = {
      name: c.name, class_name: c.class_name, race: c.race,
      role: c.role, alliance: c.alliance || ESO_ALLIANCES[0],
      level: c.level, champion_points: c.champion_points, notes: c.notes || '',
      custom_portrait: c.custom_portrait || '',
    }
    showForm = true
  }

  async function deleteCharacter(id) {
    if (!confirm('Delete this character? This cannot be undone.')) return
    try {
      await api.deleteCharacter(id)
      characters = characters.filter(c => c.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  function cancelForm() {
    showForm = false; editId = null; form = blankForm(); error = ''
  }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1.5rem">
    <div>
      <button class="btn-ghost back-btn" onclick={onback}>‹ Profiles</button>
      <h1>{user.display_name || user.name}'s Characters</h1>
    </div>
    <button class="btn-primary" data-tour="new-char-btn"
            onclick={() => { showForm = !showForm; if (!showForm) cancelForm() }}>
      {showForm && !editId ? 'Cancel' : '+ New Character'}
    </button>
  </div>

  <div class="class-key">
    {#each ESO_CLASSES as c}
      <span class="class-key-item">
        <span class="class-key-dot" style="background:{CLASS_COLORS[c]}"></span>
        {c}
      </span>
    {/each}
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if showForm}
    <div class="inline-form" style="margin-bottom:1.5rem">
      <h3 style="margin-bottom:.75rem">{editId ? 'Edit Character' : 'New Character'}</h3>
      <div class="form-grid">
        <div class="form-row">
          <label>Name *</label>
          <input bind:value={form.name} placeholder="Character name" />
        </div>
        <div class="form-row">
          <label>Class</label>
          <select bind:value={form.class_name}>
            {#each ESO_CLASSES as c}<option>{c}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Race</label>
          <select bind:value={form.race}>
            {#each ESO_RACES as r}<option>{r}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Role</label>
          <select bind:value={form.role}>
            {#each ESO_ROLES as r}<option>{r}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Alliance</label>
          <select bind:value={form.alliance}>
            {#each ESO_ALLIANCES as a}<option>{a}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Level</label>
          <input type="number" bind:value={form.level} min="1" max="50" />
        </div>
        <div class="form-row">
          <label>Champion Points</label>
          <input type="number" bind:value={form.champion_points} min="0" />
        </div>
      </div>
      <div class="form-row">
        <label>Portrait URL</label>
        <input bind:value={form.custom_portrait} placeholder="https://…  (optional, falls back to class color)" />
      </div>
      <div class="form-row">
        <label>Notes</label>
        <textarea bind:value={form.notes} placeholder="Optional notes…"></textarea>
      </div>
      <div class="flex" style="gap:.5rem">
        <button class="btn-primary" onclick={saveCharacter} disabled={saving || !form.name.trim()}>
          {saving ? 'Saving…' : editId ? 'Save Changes' : 'Create Character'}
        </button>
        <button class="btn-ghost" onclick={cancelForm}>Cancel</button>
      </div>
    </div>
  {/if}

  {#if loading}
    <p>Loading characters…</p>
  {:else if characters.length === 0}
    <div class="empty">
      <div class="empty-icon">🧙</div>
      <h2>No characters yet</h2>
      <p>Add your first character to start tracking builds.</p>
    </div>
  {:else}
    <div class="grid-2">
      {#each characters as c (c.id)}
        <div class="card card-clickable char-card"
             data-tour={c.id === newCharId ? 'new-char-card' : undefined}
             onclick={() => onselect(c)}>
          {#if c.custom_portrait}
            <img class="char-avatar" src={c.custom_portrait} alt="{c.name} portrait" />
          {:else}
            <div class="char-avatar char-avatar-fallback" style="background:{CLASS_COLORS[c.class_name] || '#666'}"></div>
          {/if}
          <div class="char-info">
            <div class="char-name">{c.name}</div>
            <div class="char-meta">
              <span class="badge">{c.class_name}</span>
              <span class="badge">{ROLE_ICONS[c.role]} {c.role}</span>
              <span class="badge">{c.race}</span>
              {#if c.alliance}
                <span class="badge alliance-badge"
                      style="border-color:{ALLIANCE_COLORS[c.alliance]};color:{ALLIANCE_COLORS[c.alliance]}">
                  {c.alliance}
                </span>
              {/if}
            </div>
            <div class="char-level">Lv {c.level} · {c.champion_points} CP</div>
          </div>
          <div class="char-actions" onclick={(e) => e.stopPropagation()}>
            <button class="btn-icon" onclick={() => startEdit(c)} title="Edit">✎</button>
            <button class="btn-icon" onclick={() => deleteCharacter(c.id)} title="Delete">✕</button>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

{#if showCharTour}
  <OnboardingTour steps={charTourSteps} onfinish={finishCharTour} />
{/if}

<style>
  .back-btn { margin-bottom: .25rem; font-size: .85rem; }

  .class-key {
    display: flex;
    flex-wrap: wrap;
    gap: .3rem .9rem;
    margin-bottom: 1.25rem;
    padding: .5rem .75rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
  }
  .class-key-item {
    display: flex;
    align-items: center;
    gap: .35rem;
    font-size: .75rem;
    color: var(--text-dim);
  }
  .class-key-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .char-card {
    display: flex;
    align-items: flex-start;
    gap: .75rem;
    position: relative;
  }

  .char-avatar {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    flex-shrink: 0;
    object-fit: cover;
    border: 1px solid var(--border);
  }
  .char-avatar-fallback { border: none; }

  .char-info { flex: 1; min-width: 0; }
  .char-name { font-weight: 600; font-size: 1.05rem; margin-bottom: .35rem; }
  .char-meta { display: flex; flex-wrap: wrap; gap: .3rem; margin-bottom: .3rem; }
  .char-level { font-size: .8rem; color: var(--text-dim); }

  .char-actions {
    display: flex;
    gap: .2rem;
    opacity: 0;
    transition: opacity .15s;
  }
  .char-card:hover .char-actions { opacity: 1; }
</style>
