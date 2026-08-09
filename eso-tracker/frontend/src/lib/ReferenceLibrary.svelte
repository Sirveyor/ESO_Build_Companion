<script>
  import { api } from '../api.js'

  let activeTab = $state('enchantments')  // enchantments | traits | mundus
  let error = $state('')
  let saving = $state(false)

  const SLOT_TYPES = ['Armor', 'Weapon', 'Jewelry']

  // ── Enchantments ──────────────────────────────────────────────────────────
  let enchantments    = $state([])
  let enchLoading     = $state(true)
  let enchSlotFilter  = $state('All')

  let showEnchForm  = $state(false)
  let enchForm      = $state(blankEnchForm())
  let editingEnchId = $state(null)
  let editEnchForm  = $state(blankEnchForm())

  function blankEnchForm() {
    return { name: '', slot_type: SLOT_TYPES[0], effect: '', essence_rune: '', notes: '' }
  }

  async function loadEnchantments() {
    enchLoading = true
    try {
      enchantments = await api.getRefEnchantments()
    } finally {
      enchLoading = false
    }
  }

  async function createEnchantment() {
    if (!enchForm.name.trim()) return
    saving = true; error = ''
    try {
      const created = await api.createRefEnchantment({
        id: crypto.randomUUID(),
        name: enchForm.name.trim(),
        slot_type: enchForm.slot_type,
        effect: enchForm.effect || null,
        essence_rune: enchForm.essence_rune || null,
        notes: enchForm.notes || null,
      })
      enchantments = [...enchantments, created]
      enchForm = blankEnchForm()
      showEnchForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEditEnch(item) {
    editingEnchId = item.id
    editEnchForm = {
      name: item.name,
      slot_type: item.slot_type,
      effect: item.effect || '',
      essence_rune: item.essence_rune || '',
      notes: item.notes || '',
    }
  }

  async function saveEnchantment(id) {
    if (!editEnchForm.name.trim()) return
    saving = true; error = ''
    try {
      const updated = await api.updateRefEnchantment(id, {
        id,
        name: editEnchForm.name.trim(),
        slot_type: editEnchForm.slot_type,
        effect: editEnchForm.effect || null,
        essence_rune: editEnchForm.essence_rune || null,
        notes: editEnchForm.notes || null,
      })
      enchantments = enchantments.map(e => e.id === id ? updated : e)
      editingEnchId = null
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function deleteEnchantment(id) {
    if (!confirm('Delete this glyph?')) return
    try {
      await api.deleteRefEnchantment(id)
      enchantments = enchantments.filter(e => e.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  let filteredEnch = $derived.by(() => {
    if (enchSlotFilter === 'All') return enchantments
    return enchantments.filter(e => e.slot_type === enchSlotFilter)
  })

  // ── Traits ────────────────────────────────────────────────────────────────
  let traits         = $state([])
  let traitsLoading  = $state(true)
  let traitSlotFilter = $state('All')

  let showTraitForm  = $state(false)
  let traitForm      = $state(blankTraitForm())
  let editingTraitId = $state(null)
  let editTraitForm  = $state(blankTraitForm())

  function blankTraitForm() {
    return { name: '', slot_type: SLOT_TYPES[0], effect: '', trait_material: '', notes: '' }
  }

  async function loadTraits() {
    traitsLoading = true
    try {
      traits = await api.getRefTraits()
    } finally {
      traitsLoading = false
    }
  }

  async function createTrait() {
    if (!traitForm.name.trim()) return
    saving = true; error = ''
    try {
      const created = await api.createRefTrait({
        id: crypto.randomUUID(),
        name: traitForm.name.trim(),
        slot_type: traitForm.slot_type,
        effect: traitForm.effect || null,
        trait_material: traitForm.trait_material || null,
        notes: traitForm.notes || null,
      })
      traits = [...traits, created]
      traitForm = blankTraitForm()
      showTraitForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEditTrait(item) {
    editingTraitId = item.id
    editTraitForm = {
      name: item.name,
      slot_type: item.slot_type,
      effect: item.effect || '',
      trait_material: item.trait_material || '',
      notes: item.notes || '',
    }
  }

  async function saveTrait(id) {
    if (!editTraitForm.name.trim()) return
    saving = true; error = ''
    try {
      const updated = await api.updateRefTrait(id, {
        id,
        name: editTraitForm.name.trim(),
        slot_type: editTraitForm.slot_type,
        effect: editTraitForm.effect || null,
        trait_material: editTraitForm.trait_material || null,
        notes: editTraitForm.notes || null,
      })
      traits = traits.map(t => t.id === id ? updated : t)
      editingTraitId = null
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function deleteTrait(id) {
    if (!confirm('Delete this trait?')) return
    try {
      await api.deleteRefTrait(id)
      traits = traits.filter(t => t.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  let filteredTraits = $derived.by(() => {
    if (traitSlotFilter === 'All') return traits
    return traits.filter(t => t.slot_type === traitSlotFilter)
  })

  // Group traits by slot_type for display
  let groupedTraits = $derived.by(() => {
    const map = new Map()
    for (const t of filteredTraits) {
      if (!map.has(t.slot_type)) map.set(t.slot_type, [])
      map.get(t.slot_type).push(t)
    }
    return [...map.entries()].sort(([a], [b]) => a.localeCompare(b))
  })

  // ── Mundus Stones ─────────────────────────────────────────────────────────
  let stones        = $state([])
  let stonesLoading = $state(true)

  let showStoneForm  = $state(false)
  let stoneForm      = $state(blankStoneForm())
  let editingStoneId = $state(null)
  let editStoneForm  = $state(blankStoneForm())

  function blankStoneForm() {
    return { name: '', effect: '', stat_type: '', location: '' }
  }

  async function loadStones() {
    stonesLoading = true
    try {
      stones = await api.getRefMundusStones()
    } finally {
      stonesLoading = false
    }
  }

  async function createStone() {
    if (!stoneForm.name.trim()) return
    saving = true; error = ''
    try {
      const created = await api.createRefMundusStone({
        id: crypto.randomUUID(),
        name: stoneForm.name.trim(),
        effect: stoneForm.effect || null,
        stat_type: stoneForm.stat_type || null,
        location: stoneForm.location || null,
      })
      stones = [...stones, created]
      stoneForm = blankStoneForm()
      showStoneForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  function startEditStone(item) {
    editingStoneId = item.id
    editStoneForm = {
      name: item.name,
      effect: item.effect || '',
      stat_type: item.stat_type || '',
      location: item.location || '',
    }
  }

  async function saveStone(id) {
    if (!editStoneForm.name.trim()) return
    saving = true; error = ''
    try {
      const updated = await api.updateRefMundusStone(id, {
        id,
        name: editStoneForm.name.trim(),
        effect: editStoneForm.effect || null,
        stat_type: editStoneForm.stat_type || null,
        location: editStoneForm.location || null,
      })
      stones = stones.map(s => s.id === id ? updated : s)
      editingStoneId = null
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function deleteStone(id) {
    if (!confirm('Delete this mundus stone?')) return
    try {
      await api.deleteRefMundusStone(id)
      stones = stones.filter(s => s.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  // ── Enchantment search ────────────────────────────────────────────────────
  let enchSearch = $state('')
  let traitSearch = $state('')
  let stoneSearch = $state('')

  let visibleEnch = $derived.by(() => {
    const q = enchSearch.trim().toLowerCase()
    if (!q) return filteredEnch
    return filteredEnch.filter(e =>
      e.name.toLowerCase().includes(q) ||
      (e.effect || '').toLowerCase().includes(q) ||
      (e.essence_rune || '').toLowerCase().includes(q)
    )
  })

  let visibleTraits = $derived.by(() => {
    const q = traitSearch.trim().toLowerCase()
    if (!q) return groupedTraits
    const filtered = filteredTraits.filter(t =>
      t.name.toLowerCase().includes(q) ||
      (t.effect || '').toLowerCase().includes(q) ||
      (t.trait_material || '').toLowerCase().includes(q)
    )
    const map = new Map()
    for (const t of filtered) {
      if (!map.has(t.slot_type)) map.set(t.slot_type, [])
      map.get(t.slot_type).push(t)
    }
    return [...map.entries()].sort(([a], [b]) => a.localeCompare(b))
  })

  let visibleStones = $derived.by(() => {
    const q = stoneSearch.trim().toLowerCase()
    if (!q) return stones
    return stones.filter(s =>
      s.name.toLowerCase().includes(q) ||
      (s.effect || '').toLowerCase().includes(q) ||
      (s.stat_type || '').toLowerCase().includes(q)
    )
  })

  // ── Load on first tab visit ───────────────────────────────────────────────
  $effect(() => {
    if (activeTab === 'enchantments' && enchantments.length === 0) loadEnchantments()
    if (activeTab === 'traits'       && traits.length === 0)       loadTraits()
    if (activeTab === 'mundus'       && stones.length === 0)        loadStones()
  })

  const SLOT_COLORS = { Armor: 'var(--gold)', Weapon: '#e07040', Jewelry: '#70a0e0' }
</script>

<div class="page">
  <h1 style="margin-bottom:1rem">Reference Library</h1>

  <div class="tabs">
    <button class:active={activeTab === 'enchantments'} onclick={() => activeTab = 'enchantments'}>
      Glyphs / Enchantments
    </button>
    <button class:active={activeTab === 'traits'} onclick={() => activeTab = 'traits'}>
      Traits
    </button>
    <button class:active={activeTab === 'mundus'} onclick={() => activeTab = 'mundus'}>
      Mundus Stones
    </button>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  <!-- ── GLYPHS TAB ──────────────────────────────────────────────────────── -->
  {#if activeTab === 'enchantments'}
    <div class="toolbar">
      <input bind:value={enchSearch} placeholder="Search glyphs…" class="search" />
      <div class="slot-filter">
        {#each ['All', ...SLOT_TYPES] as s}
          <button class:active={enchSlotFilter === s}
                  onclick={() => enchSlotFilter = s}>{s}</button>
        {/each}
      </div>
      <span class="badge count-badge">{visibleEnch.length}</span>
      <button class="btn-secondary" onclick={() => { showEnchForm = !showEnchForm }}>
        {showEnchForm ? 'Cancel' : '+ Add Glyph'}
      </button>
    </div>

    {#if showEnchForm}
      <div class="inline-form" style="margin-bottom:1rem">
        <h3 style="margin-bottom:.75rem">New Glyph</h3>
        <div class="form-grid">
          <div class="form-row">
            <label>Name *</label>
            <input bind:value={enchForm.name} placeholder="e.g. Glyph of Weakening" />
          </div>
          <div class="form-row">
            <label>Slot</label>
            <select bind:value={enchForm.slot_type}>
              {#each SLOT_TYPES as t}<option>{t}</option>{/each}
            </select>
          </div>
          <div class="form-row">
            <label>Essence Rune</label>
            <input bind:value={enchForm.essence_rune} placeholder="e.g. Kuta" />
          </div>
        </div>
        <div class="form-row">
          <label>Effect</label>
          <input bind:value={enchForm.effect} placeholder="What the glyph does" />
        </div>
        <div class="form-row">
          <label>Notes</label>
          <textarea bind:value={enchForm.notes} placeholder="Optional notes…"></textarea>
        </div>
        <button class="btn-primary" onclick={createEnchantment} disabled={saving || !enchForm.name.trim()}>
          {saving ? 'Adding…' : 'Add Glyph'}
        </button>
      </div>
    {/if}

    {#if enchLoading}
      <p class="loading">Loading…</p>
    {:else if visibleEnch.length === 0}
      <div class="empty"><p>No glyphs match your filter.</p></div>
    {:else}
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Glyph</th>
              <th>Slot</th>
              <th>Effect</th>
              <th>Essence Rune</th>
              <th>Notes</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {#each visibleEnch as e (e.id)}
              {#if editingEnchId === e.id}
                <tr class="edit-row">
                  <td><input bind:value={editEnchForm.name} class="cell-input" /></td>
                  <td>
                    <select bind:value={editEnchForm.slot_type} class="cell-input">
                      {#each SLOT_TYPES as t}<option>{t}</option>{/each}
                    </select>
                  </td>
                  <td><input bind:value={editEnchForm.effect} class="cell-input" /></td>
                  <td><input bind:value={editEnchForm.essence_rune} class="cell-input" /></td>
                  <td><input bind:value={editEnchForm.notes} class="cell-input" /></td>
                  <td class="actions-cell">
                    <button class="btn-primary" style="font-size:.75rem;padding:.2rem .6rem"
                            onclick={() => saveEnchantment(e.id)}
                            disabled={saving || !editEnchForm.name.trim()}>
                      Save
                    </button>
                    <button class="btn-ghost" style="font-size:.75rem;padding:.2rem .5rem"
                            onclick={() => editingEnchId = null}>
                      ✕
                    </button>
                  </td>
                </tr>
              {:else}
                <tr>
                  <td class="name-cell">{e.name}</td>
                  <td>
                    <span class="slot-badge" style="color:{SLOT_COLORS[e.slot_type]}">{e.slot_type}</span>
                  </td>
                  <td>{e.effect || '—'}</td>
                  <td><span class="rune-chip">{e.essence_rune || '—'}</span></td>
                  <td class="notes-cell">{e.notes || ''}</td>
                  <td class="actions-cell">
                    <button class="btn-icon" onclick={() => startEditEnch(e)} title="Edit glyph">✎</button>
                    <button class="btn-icon" onclick={() => deleteEnchantment(e.id)} title="Delete glyph">✕</button>
                  </td>
                </tr>
              {/if}
            {/each}
          </tbody>
        </table>
      </div>
    {/if}

  <!-- ── TRAITS TAB ───────────────────────────────────────────────────────── -->
  {:else if activeTab === 'traits'}
    <div class="toolbar">
      <input bind:value={traitSearch} placeholder="Search traits…" class="search" />
      <div class="slot-filter">
        {#each ['All', ...SLOT_TYPES] as s}
          <button class:active={traitSlotFilter === s}
                  onclick={() => traitSlotFilter = s}>{s}</button>
        {/each}
      </div>
      <button class="btn-secondary" style="margin-left:auto" onclick={() => { showTraitForm = !showTraitForm }}>
        {showTraitForm ? 'Cancel' : '+ Add Trait'}
      </button>
    </div>

    {#if showTraitForm}
      <div class="inline-form" style="margin-bottom:1rem">
        <h3 style="margin-bottom:.75rem">New Trait</h3>
        <div class="form-grid">
          <div class="form-row">
            <label>Name *</label>
            <input bind:value={traitForm.name} placeholder="e.g. Divines" />
          </div>
          <div class="form-row">
            <label>Slot</label>
            <select bind:value={traitForm.slot_type}>
              {#each SLOT_TYPES as t}<option>{t}</option>{/each}
            </select>
          </div>
          <div class="form-row">
            <label>Trait Material</label>
            <input bind:value={traitForm.trait_material} placeholder="e.g. Seducer's Stone" />
          </div>
        </div>
        <div class="form-row">
          <label>Effect</label>
          <input bind:value={traitForm.effect} placeholder="What the trait does" />
        </div>
        <div class="form-row">
          <label>Notes</label>
          <textarea bind:value={traitForm.notes} placeholder="Optional notes…"></textarea>
        </div>
        <button class="btn-primary" onclick={createTrait} disabled={saving || !traitForm.name.trim()}>
          {saving ? 'Adding…' : 'Add Trait'}
        </button>
      </div>
    {/if}

    {#if traitsLoading}
      <p class="loading">Loading…</p>
    {:else if visibleTraits.length === 0}
      <div class="empty"><p>No traits match your filter.</p></div>
    {:else}
      <div class="trait-groups">
        {#each visibleTraits as [slotType, items] (slotType)}
          <div class="card trait-group">
            <h3 class="group-heading" style="color:{SLOT_COLORS[slotType]}">{slotType} Traits</h3>
            <div class="table-wrap">
              <table>
                <thead>
                  <tr>
                    <th>Trait</th>
                    <th>Effect</th>
                    <th>Trait Material</th>
                    <th>Notes</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  {#each items as t (t.id)}
                    {#if editingTraitId === t.id}
                      <tr class="edit-row">
                        <td><input bind:value={editTraitForm.name} class="cell-input" /></td>
                        <td><input bind:value={editTraitForm.effect} class="cell-input" /></td>
                        <td><input bind:value={editTraitForm.trait_material} class="cell-input" /></td>
                        <td><input bind:value={editTraitForm.notes} class="cell-input" /></td>
                        <td class="actions-cell">
                          <button class="btn-primary" style="font-size:.75rem;padding:.2rem .6rem"
                                  onclick={() => saveTrait(t.id)}
                                  disabled={saving || !editTraitForm.name.trim()}>
                            Save
                          </button>
                          <button class="btn-ghost" style="font-size:.75rem;padding:.2rem .5rem"
                                  onclick={() => editingTraitId = null}>
                            ✕
                          </button>
                        </td>
                      </tr>
                    {:else}
                      <tr>
                        <td class="name-cell">{t.name}</td>
                        <td>{t.effect || '—'}</td>
                        <td><span class="rune-chip">{t.trait_material || '—'}</span></td>
                        <td class="notes-cell">{t.notes || ''}</td>
                        <td class="actions-cell">
                          <button class="btn-icon" onclick={() => startEditTrait(t)} title="Edit trait">✎</button>
                          <button class="btn-icon" onclick={() => deleteTrait(t.id)} title="Delete trait">✕</button>
                        </td>
                      </tr>
                    {/if}
                  {/each}
                </tbody>
              </table>
            </div>
          </div>
        {/each}
      </div>
    {/if}

  <!-- ── MUNDUS STONES TAB ─────────────────────────────────────────────────── -->
  {:else if activeTab === 'mundus'}
    <div class="toolbar">
      <input bind:value={stoneSearch} placeholder="Search stones…" class="search" />
      <button class="btn-secondary" style="margin-left:auto" onclick={() => { showStoneForm = !showStoneForm }}>
        {showStoneForm ? 'Cancel' : '+ Add Stone'}
      </button>
    </div>

    {#if showStoneForm}
      <div class="inline-form" style="margin-bottom:1rem">
        <h3 style="margin-bottom:.75rem">New Mundus Stone</h3>
        <div class="form-grid">
          <div class="form-row">
            <label>Name *</label>
            <input bind:value={stoneForm.name} placeholder="e.g. The Thief" />
          </div>
          <div class="form-row">
            <label>Stat Type</label>
            <input bind:value={stoneForm.stat_type} placeholder="e.g. Critical Chance" />
          </div>
          <div class="form-row">
            <label>Location</label>
            <input bind:value={stoneForm.location} placeholder="Where to find the stone" />
          </div>
        </div>
        <div class="form-row">
          <label>Effect</label>
          <input bind:value={stoneForm.effect} placeholder="What the stone does" />
        </div>
        <button class="btn-primary" onclick={createStone} disabled={saving || !stoneForm.name.trim()}>
          {saving ? 'Adding…' : 'Add Stone'}
        </button>
      </div>
    {/if}

    {#if stonesLoading}
      <p class="loading">Loading…</p>
    {:else if visibleStones.length === 0}
      <div class="empty"><p>No stones match your filter.</p></div>
    {:else}
      <div class="mundus-grid">
        {#each visibleStones as s (s.id)}
          <div class="card mundus-card">
            {#if editingStoneId === s.id}
              <div class="form-row">
                <label>Name</label>
                <input bind:value={editStoneForm.name} class="cell-input" />
              </div>
              <div class="form-row">
                <label>Effect</label>
                <input bind:value={editStoneForm.effect} class="cell-input" />
              </div>
              <div class="form-row">
                <label>Stat Type</label>
                <input bind:value={editStoneForm.stat_type} class="cell-input" />
              </div>
              <div class="form-row">
                <label>Location</label>
                <input bind:value={editStoneForm.location} class="cell-input" />
              </div>
              <div class="flex" style="gap:.5rem">
                <button class="btn-primary" style="font-size:.75rem;padding:.2rem .6rem"
                        onclick={() => saveStone(s.id)}
                        disabled={saving || !editStoneForm.name.trim()}>
                  Save
                </button>
                <button class="btn-ghost" style="font-size:.75rem;padding:.2rem .5rem"
                        onclick={() => editingStoneId = null}>
                  Cancel
                </button>
              </div>
            {:else}
              <div class="mundus-card-header">
                <div class="mundus-name">{s.name}</div>
                <div class="mundus-actions">
                  <button class="btn-icon" onclick={() => startEditStone(s)} title="Edit stone">✎</button>
                  <button class="btn-icon" onclick={() => deleteStone(s.id)} title="Delete stone">✕</button>
                </div>
              </div>
              <div class="mundus-effect">{s.effect || '—'}</div>
              {#if s.stat_type}
                <span class="badge badge-blue mundus-stat">{s.stat_type}</span>
              {/if}
              {#if s.location}
                <div class="mundus-location">📍 {s.location}</div>
              {/if}
            {/if}
          </div>
        {/each}
      </div>
    {/if}
  {/if}
</div>

<style>
  h1 { font-size: 1.4rem; }

  .tabs {
    display: flex;
    gap: .15rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
  }
  .tabs button {
    background: transparent;
    color: var(--text-dim);
    padding: .45rem 1rem;
    border-radius: var(--radius) var(--radius) 0 0;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    font-size: .875rem;
  }
  .tabs button:hover  { color: var(--text); background: var(--surface-2); }
  .tabs button.active { color: var(--gold); border-bottom-color: var(--gold); background: var(--surface); }

  .toolbar {
    display: flex;
    align-items: center;
    gap: .75rem;
    margin-bottom: .875rem;
    flex-wrap: wrap;
  }
  .search { max-width: 240px; }

  .slot-filter { display: flex; gap: .2rem; }
  .slot-filter button {
    padding: .25rem .65rem;
    font-size: .8rem;
    background: var(--surface-2);
    color: var(--text-dim);
    border-radius: var(--radius);
  }
  .slot-filter button:hover { color: var(--text); }
  .slot-filter button.active { background: var(--gold); color: #111; }

  .count-badge { margin-left: auto; }

  .loading { color: var(--text-dim); margin-top: 1rem; }

  /* Shared table */
  .name-cell  { font-weight: 600; white-space: nowrap; }
  .notes-cell { font-size: .78rem; color: var(--text-dim); max-width: 220px; }

  .slot-badge { font-weight: 600; font-size: .8rem; }

  .rune-chip {
    display: inline-block;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .1rem .45rem;
    font-size: .78rem;
    white-space: nowrap;
  }

  .actions-cell { white-space: nowrap; text-align: right; }
  .edit-row { background: var(--surface-2); }
  .cell-input { width: 100%; font-size: .82rem; padding: .25rem .4rem; }

  /* Traits */
  .trait-groups { display: flex; flex-direction: column; gap: 1rem; }
  .trait-group  { padding: .875rem 1rem; }
  .group-heading { font-size: .95rem; font-weight: 700; margin-bottom: .6rem; }

  /* Mundus grid */
  .mundus-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: .75rem;
  }
  .mundus-card     { padding: .875rem 1rem; }
  .mundus-card-header { display: flex; align-items: flex-start; justify-content: space-between; gap: .5rem; margin-bottom: .35rem; }
  .mundus-actions  { display: flex; gap: .1rem; flex-shrink: 0; }
  .mundus-name     { font-weight: 700; font-size: 1rem; color: var(--gold); }
  .mundus-effect   { font-size: .88rem; margin-bottom: .45rem; }
  .mundus-stat     { font-size: .72rem; margin-bottom: .45rem; }
  .mundus-location { font-size: .75rem; color: var(--text-dim); margin-top: .35rem; }

  @media (max-width: 640px) {
    .tabs button { padding: .35rem .6rem; font-size: .8rem; }
    .mundus-grid { grid-template-columns: 1fr; }
  }
</style>
