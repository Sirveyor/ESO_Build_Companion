<script>
  import { api } from '../api.js'
  import { SET_TYPES } from './constants.js'

  let sets       = $state([])
  let loading    = $state(true)
  let error      = $state('')
  let showForm   = $state(false)
  let saving     = $state(false)
  let expandedId = $state(null)
  let search     = $state('')
  let filterType = $state('All')

  let bonusForm = $state({ setId: null, pieces_required: 2, bonus_description: '', stat_type: '', stat_value: '' })
  let showBonusForm  = $state(null)   // set.id when add-form open
  let editingBonusId = $state(null)   // bonus.id being edited
  let editBonusForm  = $state({ pieces_required: 2, bonus_description: '', stat_type: '', stat_value: '' })

  let setForm = $state(blankSetForm())

  function blankSetForm() {
    return { name: '', set_type: SET_TYPES[0], location: '', num_pieces: 5, notes: '' }
  }

  let filtered = $derived.by(() => {
    let list = sets
    if (filterType !== 'All') list = list.filter(s => s.set_type === filterType)
    if (search.trim()) {
      const q = search.trim().toLowerCase()
      list = list.filter(s => s.name.toLowerCase().includes(q) || (s.location || '').toLowerCase().includes(q))
    }
    return [...list].sort((a, b) => a.name.localeCompare(b.name))
  })

  async function load() {
    try {
      sets = await api.getGearSets()
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function createSet() {
    if (!setForm.name.trim()) return
    saving = true; error = ''
    try {
      const created = await api.createGearSet({
        id: crypto.randomUUID(),
        name: setForm.name.trim(),
        set_type: setForm.set_type,
        location: setForm.location || null,
        num_pieces: Number(setForm.num_pieces) || 5,
        notes: setForm.notes || null,
        last_updated: new Date().toISOString(),
        bonuses: [],
      })
      sets = [...sets, created]
      setForm = blankSetForm()
      showForm = false
      expandedId = created.id
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function addBonus() {
    if (!bonusForm.bonus_description.trim() || !bonusForm.setId) return
    saving = true
    try {
      const bonus = await api.addSetBonus(bonusForm.setId, {
        id: crypto.randomUUID(),
        set_id: bonusForm.setId,
        pieces_required: Number(bonusForm.pieces_required),
        bonus_description: bonusForm.bonus_description.trim(),
        stat_type: bonusForm.stat_type || null,
        stat_value: bonusForm.stat_value ? Number(bonusForm.stat_value) : null,
      })
      sets = sets.map(s => s.id === bonusForm.setId
        ? { ...s, bonuses: [...(s.bonuses || []), bonus].sort((a, b) => a.pieces_required - b.pieces_required) }
        : s
      )
      bonusForm = { ...bonusForm, bonus_description: '', stat_type: '', stat_value: '' }
      showBonusForm = null
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEditBonus(b) {
    editingBonusId = b.id
    editBonusForm = {
      pieces_required:  b.pieces_required,
      bonus_description: b.bonus_description,
      stat_type:  b.stat_type  || '',
      stat_value: b.stat_value ?? '',
    }
  }

  async function saveBonus(setId, bonusId) {
    if (!editBonusForm.bonus_description.trim()) return
    saving = true
    try {
      const updated = await api.updateSetBonus(setId, bonusId, {
        id: bonusId,
        set_id: setId,
        pieces_required: Number(editBonusForm.pieces_required),
        bonus_description: editBonusForm.bonus_description.trim(),
        stat_type:  editBonusForm.stat_type  || null,
        stat_value: editBonusForm.stat_value !== '' ? Number(editBonusForm.stat_value) : null,
      })
      sets = sets.map(s => s.id === setId
        ? { ...s, bonuses: s.bonuses.map(b => b.id === bonusId ? updated : b) }
        : s
      )
      editingBonusId = null
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function deleteBonus(setId, bonusId) {
    try {
      await api.deleteSetBonus(setId, bonusId)
      sets = sets.map(s => s.id === setId
        ? { ...s, bonuses: s.bonuses.filter(b => b.id !== bonusId) }
        : s
      )
    } catch (e) {
      error = e.message
    }
  }

  async function deleteSet(id) {
    if (!confirm('Delete this gear set and all its bonuses?')) return
    try {
      await api.deleteGearSet(id)
      sets = sets.filter(s => s.id !== id)
      if (expandedId === id) expandedId = null
    } catch (e) {
      error = e.message
    }
  }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1rem">
    <h1>Gear Sets</h1>
    <button class="btn-primary" onclick={() => { showForm = !showForm }}>
      {showForm ? 'Cancel' : '+ New Set'}
    </button>
  </div>

  <!-- Filters -->
  <div class="filters flex" style="margin-bottom:1rem;flex-wrap:wrap">
    <input class="search" bind:value={search} placeholder="Search sets…" style="max-width:220px" />
    <select bind:value={filterType} style="max-width:160px">
      <option>All</option>
      {#each SET_TYPES as t}<option>{t}</option>{/each}
    </select>
    <span class="badge" style="margin-left:auto">{filtered.length} set{filtered.length !== 1 ? 's' : ''}</span>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  <!-- New set form -->
  {#if showForm}
    <div class="inline-form" style="margin-bottom:1rem">
      <h3 style="margin-bottom:.75rem">New Gear Set</h3>
      <div class="form-grid">
        <div class="form-row">
          <label>Set Name *</label>
          <input bind:value={setForm.name} placeholder="e.g. Mother's Sorrow" />
        </div>
        <div class="form-row">
          <label>Type</label>
          <select bind:value={setForm.set_type}>
            {#each SET_TYPES as t}<option>{t}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Location</label>
          <input bind:value={setForm.location} placeholder="e.g. Deshaan overland" />
        </div>
        <div class="form-row">
          <label>Pieces in Set</label>
          <input type="number" bind:value={setForm.num_pieces} min="1" max="5" />
        </div>
      </div>
      <div class="form-row">
        <label>Notes</label>
        <textarea bind:value={setForm.notes} placeholder="Optional notes…"></textarea>
      </div>
      <button class="btn-primary" onclick={createSet} disabled={saving || !setForm.name.trim()}>
        {saving ? 'Creating…' : 'Create Set'}
      </button>
    </div>
  {/if}

  {#if loading}
    <p>Loading gear sets…</p>
  {:else if filtered.length === 0}
    <div class="empty">
      <div class="empty-icon">⚙</div>
      <h2>{search || filterType !== 'All' ? 'No sets match your filter' : 'No gear sets yet'}</h2>
      <p>Add sets manually or use the Compare tool to evaluate options.</p>
    </div>
  {:else}
    <div class="sets-list">
      {#each filtered as s (s.id)}
        <div class="card set-card">
          <div class="set-header" onclick={() => expandedId = expandedId === s.id ? null : s.id}>
            <div class="set-title">
              <span class="set-name">{s.name}</span>
              <span class="badge badge-blue" style="margin-left:.5rem">{s.set_type}</span>
              {#if s.location}
                <span class="badge" style="margin-left:.25rem">{s.location}</span>
              {/if}
            </div>
            <div class="set-actions" onclick={(e) => e.stopPropagation()}>
              <button class="btn-icon" onclick={() => deleteSet(s.id)} title="Delete">✕</button>
            </div>
            <span class="expand-icon">{expandedId === s.id ? '▲' : '▼'}</span>
          </div>

          {#if expandedId === s.id}
            <div class="set-body">
              <div class="bonus-list">
                {#each [...(s.bonuses || [])].sort((a, b) => a.pieces_required - b.pieces_required) as b (b.id)}
                  {#if editingBonusId === b.id}
                    <div class="bonus-edit-row">
                      <select bind:value={editBonusForm.pieces_required} class="pieces-select">
                        {#each [1,2,3,4,5] as n}<option value={n}>{n} pc</option>{/each}
                      </select>
                      <input bind:value={editBonusForm.bonus_description}
                             placeholder="Bonus description" class="desc-input" />
                      <input bind:value={editBonusForm.stat_type}
                             placeholder="Stat type" class="stat-input" />
                      <input type="number" bind:value={editBonusForm.stat_value}
                             placeholder="Value" class="val-input" />
                      <button class="btn-primary" style="font-size:.75rem;padding:.2rem .6rem"
                              onclick={() => saveBonus(s.id, b.id)}
                              disabled={saving || !editBonusForm.bonus_description.trim()}>
                        Save
                      </button>
                      <button class="btn-ghost" style="font-size:.75rem;padding:.2rem .5rem"
                              onclick={() => editingBonusId = null}>
                        ✕
                      </button>
                    </div>
                  {:else}
                    <div class="bonus-row">
                      <span class="piece-badge badge badge-gold">{b.pieces_required} pc</span>
                      <span class="bonus-text">{b.bonus_description}</span>
                      {#if b.stat_type}
                        <span class="badge badge-green">{b.stat_type}{b.stat_value ? ` +${b.stat_value}` : ''}</span>
                      {/if}
                      <button class="btn-icon" onclick={() => startEditBonus(b)} title="Edit bonus">✎</button>
                      <button class="btn-icon" onclick={() => deleteBonus(s.id, b.id)} title="Remove bonus">✕</button>
                    </div>
                  {/if}
                {:else}
                  <p style="font-size:.85rem;color:var(--text-dim)">No bonuses added yet.</p>
                {/each}
              </div>

              {#if showBonusForm === s.id}
                <div class="bonus-form">
                  <div class="form-grid" style="grid-template-columns:80px 1fr 140px 100px">
                    <div class="form-row">
                      <label>Pieces</label>
                      <select bind:value={bonusForm.pieces_required}>
                        {#each [1,2,3,4,5] as n}<option value={n}>{n}</option>{/each}
                      </select>
                    </div>
                    <div class="form-row">
                      <label>Bonus Description *</label>
                      <input bind:value={bonusForm.bonus_description}
                             placeholder="e.g. Adds 1096 Max Magicka" />
                    </div>
                    <div class="form-row">
                      <label>Stat Type</label>
                      <input bind:value={bonusForm.stat_type} placeholder="e.g. Max Magicka" />
                    </div>
                    <div class="form-row">
                      <label>Stat Value</label>
                      <input type="number" bind:value={bonusForm.stat_value} placeholder="1096" />
                    </div>
                  </div>
                  <div class="flex" style="gap:.5rem">
                    <button class="btn-primary" onclick={addBonus}
                            disabled={saving || !bonusForm.bonus_description.trim()}>
                      Add Bonus
                    </button>
                    <button class="btn-ghost" onclick={() => showBonusForm = null}>Cancel</button>
                  </div>
                </div>
              {:else}
                <button class="btn-secondary" style="margin-top:.75rem;font-size:.8rem"
                        onclick={() => { showBonusForm = s.id; bonusForm.setId = s.id }}>
                  + Add Bonus
                </button>
              {/if}
            </div>
          {/if}
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .sets-list { display: flex; flex-direction: column; gap: .75rem; }

  .set-card { padding: 0; overflow: hidden; }

  .set-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .875rem 1rem;
    cursor: pointer;
    gap: .75rem;
  }
  .set-header:hover { background: var(--surface-2); }

  .set-title { display: flex; align-items: center; flex-wrap: wrap; gap: .3rem; }
  .set-name  { font-weight: 600; font-size: 1rem; }

  .set-actions { display: flex; align-items: center; gap: .5rem; flex-shrink: 0; }
  .expand-icon { color: var(--text-dim); font-size: .75rem; }

  .set-body {
    padding: 0 1rem 1rem;
    border-top: 1px solid var(--border);
    margin-top: 0;
  }

  .bonus-list { display: flex; flex-direction: column; gap: .4rem; padding-top: .75rem; }

  .bonus-row {
    display: flex;
    align-items: center;
    gap: .5rem;
    flex-wrap: wrap;
    padding: .35rem .5rem;
    border-radius: var(--radius);
    background: var(--bg);
  }
  .piece-badge { font-weight: 700; }
  .bonus-text  { flex: 1; font-size: .9rem; min-width: 0; }

  .bonus-edit-row {
    display: flex;
    align-items: center;
    gap: .4rem;
    flex-wrap: wrap;
    padding: .3rem .5rem;
    border-radius: var(--radius);
    background: var(--surface-2);
    border: 1px solid var(--border);
  }
  .bonus-edit-row .pieces-select { width: 64px; padding: .2rem .3rem; font-size: .8rem; }
  .bonus-edit-row .desc-input    { flex: 1; min-width: 160px; font-size: .8rem; }
  .bonus-edit-row .stat-input    { width: 120px; font-size: .8rem; }
  .bonus-edit-row .val-input     { width: 72px; font-size: .8rem; }

  .bonus-form {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .75rem;
    margin-top: .75rem;
  }

  .filters { gap: .5rem; }
</style>
