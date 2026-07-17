<script>
  import { api } from '../api.js'

  let activeTab = $state('enchantments')  // enchantments | traits | mundus

  // ── Enchantments ──────────────────────────────────────────────────────────
  let enchantments    = $state([])
  let enchLoading     = $state(true)
  let enchSlotFilter  = $state('All')

  async function loadEnchantments() {
    enchLoading = true
    try {
      enchantments = await api.getRefEnchantments()
    } finally {
      enchLoading = false
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

  async function loadTraits() {
    traitsLoading = true
    try {
      traits = await api.getRefTraits()
    } finally {
      traitsLoading = false
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

  async function loadStones() {
    stonesLoading = true
    try {
      stones = await api.getRefMundusStones()
    } finally {
      stonesLoading = false
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

  <!-- ── GLYPHS TAB ──────────────────────────────────────────────────────── -->
  {#if activeTab === 'enchantments'}
    <div class="toolbar">
      <input bind:value={enchSearch} placeholder="Search glyphs…" class="search" />
      <div class="slot-filter">
        {#each ['All', 'Armor', 'Weapon', 'Jewelry'] as s}
          <button class:active={enchSlotFilter === s}
                  onclick={() => enchSlotFilter = s}>{s}</button>
        {/each}
      </div>
      <span class="badge count-badge">{visibleEnch.length}</span>
    </div>

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
            </tr>
          </thead>
          <tbody>
            {#each visibleEnch as e (e.id)}
              <tr>
                <td class="name-cell">{e.name}</td>
                <td>
                  <span class="slot-badge" style="color:{SLOT_COLORS[e.slot_type]}">{e.slot_type}</span>
                </td>
                <td>{e.effect || '—'}</td>
                <td><span class="rune-chip">{e.essence_rune || '—'}</span></td>
                <td class="notes-cell">{e.notes || ''}</td>
              </tr>
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
        {#each ['All', 'Armor', 'Weapon', 'Jewelry'] as s}
          <button class:active={traitSlotFilter === s}
                  onclick={() => traitSlotFilter = s}>{s}</button>
        {/each}
      </div>
    </div>

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
                  </tr>
                </thead>
                <tbody>
                  {#each items as t (t.id)}
                    <tr>
                      <td class="name-cell">{t.name}</td>
                      <td>{t.effect || '—'}</td>
                      <td><span class="rune-chip">{t.trait_material || '—'}</span></td>
                      <td class="notes-cell">{t.notes || ''}</td>
                    </tr>
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
    </div>

    {#if stonesLoading}
      <p class="loading">Loading…</p>
    {:else if visibleStones.length === 0}
      <div class="empty"><p>No stones match your filter.</p></div>
    {:else}
      <div class="mundus-grid">
        {#each visibleStones as s (s.id)}
          <div class="card mundus-card">
            <div class="mundus-name">{s.name}</div>
            <div class="mundus-effect">{s.effect || '—'}</div>
            {#if s.stat_type}
              <span class="badge badge-blue mundus-stat">{s.stat_type}</span>
            {/if}
            {#if s.location}
              <div class="mundus-location">📍 {s.location}</div>
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
  .mundus-name     { font-weight: 700; font-size: 1rem; color: var(--gold); margin-bottom: .35rem; }
  .mundus-effect   { font-size: .88rem; margin-bottom: .45rem; }
  .mundus-stat     { font-size: .72rem; margin-bottom: .45rem; }
  .mundus-location { font-size: .75rem; color: var(--text-dim); margin-top: .35rem; }

  @media (max-width: 640px) {
    .tabs button { padding: .35rem .6rem; font-size: .8rem; }
    .mundus-grid { grid-template-columns: 1fr; }
  }
</style>
