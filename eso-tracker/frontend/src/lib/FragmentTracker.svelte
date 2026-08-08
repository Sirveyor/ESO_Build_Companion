<script>
  import { api } from '../api.js'

  let { character } = $props()

  const CATEGORIES = [
    'All', 'Public Dungeon', 'Event', 'Prologue Quest', 'Tales of Tribute', 'Infinite Archive', 'Skill Style',
  ]
  const CATEGORY_CLASS = {
    'Public Dungeon': 'badge-blue', Event: 'badge-special', 'Prologue Quest': 'badge-green',
    'Tales of Tribute': 'badge-gold', 'Infinite Archive': 'badge-hm', 'Skill Style': 'badge-hs',
  }

  let allSets       = $state([])
  let learned        = $state([])   // LearnedFragment rows
  let loading        = $state(true)
  let error          = $state('')
  let filterCategory = $state('All')
  let search         = $state('')
  let showComplete   = $state(true)
  let showIncomplete = $state(true)
  let expandedId     = $state(null)

  let learnedIds = $derived(new Set(learned.map(l => l.fragment_id)))

  function setProgress(s) {
    const total = s.items.length
    const known = s.items.filter(it => learnedIds.has(it.id)).length
    return { total, known }
  }

  let filtered = $derived.by(() => {
    let list = allSets
    if (filterCategory !== 'All') list = list.filter(s => s.category === filterCategory)
    if (search.trim()) {
      const q = search.trim().toLowerCase()
      list = list.filter(s =>
        s.name.toLowerCase().includes(q) ||
        s.items.some(it => it.name.toLowerCase().includes(q))
      )
    }
    list = list.filter(s => {
      const { total, known } = setProgress(s)
      const complete = known === total
      return complete ? showComplete : showIncomplete
    })
    return [...list].sort((a, b) => a.name.localeCompare(b.name))
  })

  let stats = $derived.by(() => {
    const totalPieces = allSets.reduce((sum, s) => sum + s.items.length, 0)
    const knownPieces  = learned.length
    const totalSets    = allSets.length
    const completeSets = allSets.filter(s => {
      const { total, known } = setProgress(s)
      return total > 0 && known === total
    }).length
    const byCat = {}
    for (const c of CATEGORIES.slice(1)) {
      const catSets = allSets.filter(s => s.category === c)
      const tot = catSets.reduce((sum, s) => sum + s.items.length, 0)
      const kn  = catSets.reduce((sum, s) => sum + setProgress(s).known, 0)
      byCat[c] = { total: tot, known: kn }
    }
    return { totalPieces, knownPieces, totalSets, completeSets, byCat }
  })

  async function load() {
    try {
      ;[allSets, learned] = await Promise.all([
        api.getRefFragments(),
        api.getLearnedFragments(character.id),
      ])
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function toggleItem(item) {
    const existing = learned.find(l => l.fragment_id === item.id)
    if (existing) {
      await api.unlearnFragment(existing.id)
      learned = learned.filter(l => l.id !== existing.id)
    } else {
      const row = await api.learnFragment({
        id: crypto.randomUUID(),
        character_id: character.id,
        fragment_id: item.id,
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
      <h1>Fragment Tracker</h1>
      <p style="font-size:.85rem;color:var(--text-dim)">
        {stats.knownPieces} / {stats.totalPieces} pieces collected
        &middot; {stats.completeSets} / {stats.totalSets} collections complete for {character.name}
      </p>
    </div>
    <div class="progress-wrap" style="width:200px">
      <div class="progress-bar {stats.knownPieces === stats.totalPieces ? 'full' : ''}"
           style="width:{stats.totalPieces ? Math.round(stats.knownPieces/stats.totalPieces*100) : 0}%"></div>
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
    <input bind:value={search} placeholder="Search collections or pieces…" style="max-width:240px" />
    <select bind:value={filterCategory} style="max-width:170px">
      {#each CATEGORIES as c}<option>{c}</option>{/each}
    </select>
    <label class="check-wrap">
      <span class="check-box {showComplete ? 'checked' : ''}"
            onclick={() => showComplete = !showComplete}
            role="checkbox" aria-checked={showComplete} tabindex="0"></span>
      <span style="font-size:.85rem">Complete</span>
    </label>
    <label class="check-wrap">
      <span class="check-box {showIncomplete ? 'checked' : ''}"
            onclick={() => showIncomplete = !showIncomplete}
            role="checkbox" aria-checked={showIncomplete} tabindex="0"></span>
      <span style="font-size:.85rem">Incomplete</span>
    </label>
    <span class="badge" style="margin-left:auto">{filtered.length} shown</span>
  </div>

  {#if loading}
    <p>Loading fragments…</p>
  {:else if filtered.length === 0}
    <div class="empty">
      <div class="empty-icon">🧩</div>
      <h2>No collections match your filter</h2>
    </div>
  {:else}
    <div class="sets-list">
      {#each filtered as s (s.id)}
        {@const { total, known } = setProgress(s)}
        <div class="card set-card">
          <div class="set-header" onclick={() => expandedId = expandedId === s.id ? null : s.id}>
            <div class="set-title">
              <span class="set-name">{s.name}</span>
              <span class="badge {CATEGORY_CLASS[s.category] ?? ''}" style="margin-left:.5rem">{s.category}</span>
            </div>
            <div class="set-right">
              <span class="badge {known === total ? 'badge-green' : ''}">{known}/{total}</span>
              <span class="expand-icon">{expandedId === s.id ? '▲' : '▼'}</span>
            </div>
          </div>

          {#if expandedId === s.id}
            <div class="set-body">
              <div class="item-list">
                {#each s.items as it (it.id)}
                  {@const isLearned = learnedIds.has(it.id)}
                  <div class="item-row" class:learned={isLearned} onclick={() => toggleItem(it)}>
                    <span class="check-box {isLearned ? 'checked' : ''}"></span>
                    <span class="item-name">{it.name}</span>
                    <span class="item-source">{it.source ?? 'Source not documented'}</span>
                  </div>
                {/each}
              </div>
            </div>
          {/if}
        </div>
      {/each}
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

  .sets-list { display: flex; flex-direction: column; gap: .6rem; }
  .set-card { padding: 0; overflow: hidden; }

  .set-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .75rem 1rem;
    cursor: pointer;
    gap: .75rem;
  }
  .set-header:hover { background: var(--surface-2); }

  .set-title { display: flex; align-items: center; flex-wrap: wrap; }
  .set-name  { font-weight: 600; }

  .set-right { display: flex; align-items: center; gap: .5rem; flex-shrink: 0; }
  .expand-icon { color: var(--text-dim); font-size: .75rem; }

  .set-body { padding: 0 1rem 1rem; border-top: 1px solid var(--border); }
  .item-list { display: flex; flex-direction: column; gap: .3rem; padding-top: .75rem; }

  .item-row {
    display: flex;
    align-items: center;
    gap: .6rem;
    padding: .35rem .5rem;
    border-radius: var(--radius);
    background: var(--bg);
    cursor: pointer;
  }
  .item-row:hover { background: var(--surface-2); }
  .item-row.learned { opacity: .55; }
  .item-row.learned .check-box { background: var(--green); border-color: var(--green); }
  .item-name   { font-weight: 500; white-space: nowrap; }
  .item-source { font-size: .82rem; color: var(--text-dim); }

  /* Category badge colours */
  :global(.badge-hm)      { background: rgba(180,100,200,.15); color: #c070e0; border-color: rgba(180,100,200,.3); }
  :global(.badge-hs)      { background: rgba(200,100,80,.15);  color: #d07060; border-color: rgba(200,100,80,.3);  }
  :global(.badge-special) { background: rgba(255,140,0,.15);   color: #ff8c00;     border-color: rgba(255,140,0,.3); }
</style>
