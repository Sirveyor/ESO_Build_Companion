<script>
  import { api } from '../api.js'

  let { character } = $props()

  const CATEGORIES = [
    'All', 'Racial', 'Crafted', 'Crown Store', 'Dungeon/Trial', 'Overland', 'Event', 'PvP/Imperial City',
  ]
  const CATEGORY_CLASS = {
    Racial: 'badge-gold', Crafted: 'badge-green', 'Crown Store': 'badge-gourmet',
    'Dungeon/Trial': 'badge-hm', Overland: 'badge-blue', Event: 'badge-special', 'PvP/Imperial City': 'badge-hs',
  }

  let allMotifs      = $state([])
  let learned        = $state([])   // LearnedMotif rows
  let loading        = $state(true)
  let error          = $state('')
  let filterCategory = $state('All')
  let search         = $state('')
  let showUnlearned  = $state(true)
  let showLearned    = $state(true)
  let sortBy         = $state('number') // 'number' | 'name' | 'category'

  let learnedIds = $derived(new Set(learned.map(l => l.motif_id)))
  let batchBusy  = $state(false)

  let filtered = $derived.by(() => {
    let list = allMotifs
    if (filterCategory !== 'All') list = list.filter(m => m.category === filterCategory)
    if (!showLearned)   list = list.filter(m => !learnedIds.has(m.id))
    if (!showUnlearned) list = list.filter(m =>  learnedIds.has(m.id))
    if (search.trim()) {
      const q = search.trim().toLowerCase()
      list = list.filter(m => m.name.toLowerCase().includes(q))
    }
    return [...list].sort((a, b) => {
      if (sortBy === 'category') {
        const cc = a.category.localeCompare(b.category)
        return cc !== 0 ? cc : a.name.localeCompare(b.name)
      }
      if (sortBy === 'number') {
        if ((a.motif_number ?? 0) !== (b.motif_number ?? 0)) return (a.motif_number ?? 0) - (b.motif_number ?? 0)
        return a.name.localeCompare(b.name)
      }
      return a.name.localeCompare(b.name)
    })
  })

  let stats = $derived.by(() => {
    const total  = allMotifs.length
    const known  = learned.length
    const byCat  = {}
    for (const c of CATEGORIES.slice(1)) {
      const tot = allMotifs.filter(m => m.category === c).length
      const kn  = learned.filter(l => {
        const m = allMotifs.find(x => x.id === l.motif_id)
        return m?.category === c
      }).length
      byCat[c] = { total: tot, known: kn }
    }
    return { total, known, byCat }
  })

  async function load() {
    try {
      ;[allMotifs, learned] = await Promise.all([
        api.getRefMotifs(),
        api.getLearnedMotifs(character.id),
      ])
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  let shownUnlearned = $derived(filtered.filter(m => !learnedIds.has(m.id)))
  let shownLearned   = $derived(filtered.filter(m =>  learnedIds.has(m.id)))

  async function markAllShown() {
    batchBusy = true
    try {
      if (shownUnlearned.length > 0) {
        const newRows = await Promise.all(
          shownUnlearned.map(m => api.learnMotif({
            id: crypto.randomUUID(),
            character_id: character.id,
            motif_id: m.id,
            learned_at: new Date().toISOString(),
          }))
        )
        learned = [...learned, ...newRows]
      } else {
        const toRemove = learned.filter(l => shownLearned.some(m => m.id === l.motif_id))
        await Promise.all(toRemove.map(l => api.unlearnMotif(l.id)))
        const removeIds = new Set(toRemove.map(l => l.id))
        learned = learned.filter(l => !removeIds.has(l.id))
      }
    } finally {
      batchBusy = false
    }
  }

  async function toggleLearned(motif) {
    const existing = learned.find(l => l.motif_id === motif.id)
    if (existing) {
      await api.unlearnMotif(existing.id)
      learned = learned.filter(l => l.id !== existing.id)
    } else {
      const row = await api.learnMotif({
        id: crypto.randomUUID(),
        character_id: character.id,
        motif_id: motif.id,
        learned_at: new Date().toISOString(),
      })
      learned = [...learned, row]
    }
  }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1rem">
    <div>
      <h1>Motif Tracker</h1>
      <p style="font-size:.85rem;color:var(--text-dim)">
        {stats.known} / {stats.total} motifs learned for {character.name}
      </p>
    </div>
    <div class="progress-wrap" style="width:200px">
      <div class="progress-bar {stats.known === stats.total ? 'full' : ''}"
           style="width:{stats.total ? Math.round(stats.known/stats.total*100) : 0}%"></div>
    </div>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  <!-- Summary by category -->
  <div class="cat-summary" style="margin-bottom:1rem">
    {#each CATEGORIES.slice(1) as c}
      {@const s = stats.byCat[c]}
      {#if s?.total}
        <div class="cat-pill {s?.known === s?.total ? 'done' : ''}"
             role="button" tabindex="0"
             onclick={() => filterCategory = filterCategory === c ? 'All' : c}
             onkeydown={(e) => e.key === 'Enter' && (filterCategory = filterCategory === c ? 'All' : c)}>
          <span class="badge {CATEGORY_CLASS[c]}">{c}</span>
          <span class="pill-count">{s?.known ?? 0}/{s?.total ?? 0}</span>
        </div>
      {/if}
    {/each}
  </div>

  <!-- Filters -->
  <div class="flex" style="flex-wrap:wrap;gap:.5rem;margin-bottom:1rem">
    <input bind:value={search} placeholder="Search motifs…" style="max-width:240px" />
    <select bind:value={filterCategory} style="max-width:170px">
      {#each CATEGORIES as c}<option>{c}</option>{/each}
    </select>
    <select bind:value={sortBy} style="max-width:130px">
      <option value="number">Sort: Number</option>
      <option value="name">Sort: Name</option>
      <option value="category">Sort: Category</option>
    </select>
    <label class="check-wrap">
      <span class="check-box {showLearned ? 'checked' : ''}"
            onclick={() => showLearned = !showLearned}
            role="checkbox" aria-checked={showLearned} tabindex="0"></span>
      <span style="font-size:.85rem">Learned</span>
    </label>
    <label class="check-wrap">
      <span class="check-box {showUnlearned ? 'checked' : ''}"
            onclick={() => showUnlearned = !showUnlearned}
            role="checkbox" aria-checked={showUnlearned} tabindex="0"></span>
      <span style="font-size:.85rem">Not yet</span>
    </label>
    <div style="display:flex;align-items:center;gap:.5rem;margin-left:auto">
      <span class="badge">{filtered.length} shown</span>
      {#if filtered.length > 0}
        <button class="btn-batch" onclick={markAllShown} disabled={batchBusy}>
          {#if batchBusy}
            Working…
          {:else if shownUnlearned.length > 0}
            Mark all shown ({shownUnlearned.length})
          {:else}
            Unlearn all shown ({shownLearned.length})
          {/if}
        </button>
      {/if}
    </div>
  </div>

  {#if loading}
    <p>Loading motifs…</p>
  {:else if filtered.length === 0}
    <div class="empty">
      <div class="empty-icon">📖</div>
      <h2>No motifs match your filter</h2>
    </div>
  {:else}
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th></th>
            <th>Motif</th>
            <th>Category</th>
            <th>Chapter</th>
            <th>Source</th>
          </tr>
        </thead>
        <tbody>
          {#each filtered as m (m.id)}
            {@const isLearned = learnedIds.has(m.id)}
            <tr class:learned={isLearned} onclick={() => toggleLearned(m)}>
              <td class="check-cell">
                <span class="check-box {isLearned ? 'checked' : ''}"></span>
              </td>
              <td class="motif-name">
                {m.name}
                {#if m.motif_number}<span class="motif-num">#{m.motif_number}</span>{/if}
              </td>
              <td>
                <span class="badge {CATEGORY_CLASS[m.category] ?? ''}">{m.category}</span>
              </td>
              <td style="font-size:.8rem;color:var(--text-dim)">{m.chapter ?? '—'}</td>
              <td class="source-cell">{m.source ?? ''}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  {/if}
</div>

<style>
  .cat-summary {
    display: flex;
    flex-wrap: wrap;
    gap: .4rem;
  }
  .cat-pill {
    display: flex;
    align-items: center;
    gap: .3rem;
    cursor: pointer;
    padding: .2rem .4rem;
    border-radius: var(--radius);
    border: 1px solid transparent;
    transition: border-color .15s;
  }
  .cat-pill:hover { border-color: var(--border); }
  .cat-pill.done .pill-count { color: var(--green); }
  .pill-count { font-size: .75rem; color: var(--text-dim); }

  .btn-batch {
    font-size: .8rem;
    padding: .25rem .6rem;
    background: var(--surface-2);
    color: var(--text);
    border-radius: var(--radius);
    white-space: nowrap;
  }
  .btn-batch:hover:not(:disabled) { background: var(--gold-dim); color: var(--gold); }
  .btn-batch:disabled { opacity: .45; cursor: default; }

  tr { cursor: pointer; }
  tr.learned td { opacity: .55; }
  tr.learned .check-box { background: var(--green); border-color: var(--green); }

  .check-cell { width: 28px; }
  .motif-name { font-weight: 500; }
  .motif-num  { font-size: .75rem; color: var(--text-dim); margin-left: .35rem; }
  .source-cell { font-size: .8rem; color: var(--text-dim); }
</style>
