<script>
  import { api } from '../api.js'

  let { character } = $props()

  const DISH_TYPES = [
    'All',
    'Meat', 'Fruit', 'Vegetable', 'Savoury', 'Ragout', 'Entremet', 'Gourmet', 'Special',
    'Alcohol', 'Tea', 'Tonic', 'Liqueur', 'Tincture', 'Cordial', 'Distillate',
  ]
  const DISH_LABEL = {
    Meat: 'Health', Fruit: 'Magicka', Vegetable: 'Stamina',
    Savoury: 'H+M', Ragout: 'H+S', Entremet: 'M+S', Gourmet: 'All Stats',
    Special: 'Event',
    Alcohol: 'HP Rec', Tea: 'Mag Rec', Tonic: 'Stam Rec',
    Liqueur: 'H+M Rec', Tincture: 'H+S Rec', Cordial: 'M+S Rec', Distillate: 'All Rec',
  }
  const DISH_CLASS = {
    Meat: 'badge-gold', Fruit: 'badge-blue', Vegetable: 'badge-green',
    Savoury: 'badge-hm', Ragout: 'badge-hs', Entremet: 'badge-ms', Gourmet: 'badge-gourmet',
    Special: 'badge-special',
    Alcohol: 'badge-gold', Tea: 'badge-blue', Tonic: 'badge-green',
    Liqueur: 'badge-hm', Tincture: 'badge-hs', Cordial: 'badge-ms', Distillate: 'badge-gourmet',
  }

  let allRecipes    = $state([])
  let learned       = $state([])   // LearnedRecipe rows
  let loading       = $state(true)
  let error         = $state('')
  let filterDish    = $state('All')
  let filterRi      = $state(0)     // 0 = all RI levels
  let search        = $state('')
  let showUnlearned = $state(true)
  let showLearned   = $state(true)
  let sortBy        = $state('name') // 'name' | 'level' | 'type'

  let learnedIds      = $derived(new Set(learned.map(l => l.recipe_id)))
  let batchBusy       = $state(false)

  let filtered = $derived.by(() => {
    let list = allRecipes
    if (filterDish !== 'All') list = list.filter(r => r.dish_type === filterDish)
    if (filterRi > 0)         list = list.filter(r => r.ri === filterRi)
    if (!showLearned)   list = list.filter(r => !learnedIds.has(r.id))
    if (!showUnlearned) list = list.filter(r => learnedIds.has(r.id))
    if (search.trim()) {
      const q = search.trim().toLowerCase()
      list = list.filter(r =>
        r.name.toLowerCase().includes(q) ||
        [r.ing_meat, r.ing_fruit, r.ing_veg, r.ing_med].filter(Boolean).join(' ').toLowerCase().includes(q)
      )
    }
    return [...list].sort((a, b) => {
      if (sortBy === 'level') {
        if (a.food_level !== b.food_level) return a.food_level - b.food_level
        if (a.ri !== b.ri) return a.ri - b.ri
        return a.name.localeCompare(b.name)
      }
      if (sortBy === 'type') {
        const tc = a.dish_type.localeCompare(b.dish_type)
        return tc !== 0 ? tc : a.name.localeCompare(b.name)
      }
      return a.name.localeCompare(b.name)
    })
  })

  let stats = $derived.by(() => {
    const total   = allRecipes.length
    const known   = learned.length
    const byDish  = {}
    for (const dt of DISH_TYPES.slice(1)) {
      const tot = allRecipes.filter(r => r.dish_type === dt).length
      const kn  = learned.filter(l => {
        const r = allRecipes.find(x => x.id === l.recipe_id)
        return r?.dish_type === dt
      }).length
      byDish[dt] = { total: tot, known: kn }
    }
    return { total, known, byDish }
  })

  async function load() {
    try {
      ;[allRecipes, learned] = await Promise.all([
        api.getRefFood(),
        api.getLearnedRecipes(character.id),
      ])
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  let shownUnlearned = $derived(filtered.filter(r => !learnedIds.has(r.id)))
  let shownLearned   = $derived(filtered.filter(r =>  learnedIds.has(r.id)))

  async function markAllShown() {
    batchBusy = true
    try {
      if (shownUnlearned.length > 0) {
        const newRows = await Promise.all(
          shownUnlearned.map(r => api.learnRecipe({
            id: crypto.randomUUID(),
            character_id: character.id,
            recipe_id: r.id,
            learned_at: new Date().toISOString(),
          }))
        )
        learned = [...learned, ...newRows]
      } else {
        const toRemove = learned.filter(l => shownLearned.some(r => r.id === l.recipe_id))
        await Promise.all(toRemove.map(l => api.unlearnRecipe(l.id)))
        const removeIds = new Set(toRemove.map(l => l.id))
        learned = learned.filter(l => !removeIds.has(l.id))
      }
    } finally {
      batchBusy = false
    }
  }

  async function toggleLearned(recipe) {
    const existing = learned.find(l => l.recipe_id === recipe.id)
    if (existing) {
      await api.unlearnRecipe(existing.id)
      learned = learned.filter(l => l.id !== existing.id)
    } else {
      const row = await api.learnRecipe({
        id: crypto.randomUUID(),
        character_id: character.id,
        recipe_id: recipe.id,
        learned_at: new Date().toISOString(),
      })
      learned = [...learned, row]
    }
  }

  function ingredientList(r) {
    return [r.ing_meat, r.ing_fruit, r.ing_veg, r.ing_med, r.ing_impr].filter(Boolean).join(', ')
  }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1rem">
    <div>
      <h1>Recipe Tracker</h1>
      <p style="font-size:.85rem;color:var(--text-dim)">
        {stats.known} / {stats.total} recipes learned for {character.name}
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

  <!-- Summary by dish type -->
  <div class="dish-summary" style="margin-bottom:1rem">
    {#each DISH_TYPES.slice(1) as dt}
      {@const s = stats.byDish[dt]}
      <div class="dish-pill {s?.known === s?.total ? 'done' : ''}"
           role="button" tabindex="0"
           onclick={() => filterDish = filterDish === dt ? 'All' : dt}
           onkeydown={(e) => e.key === 'Enter' && (filterDish = filterDish === dt ? 'All' : dt)}>
        <span class="badge {DISH_CLASS[dt]}">{dt}</span>
        <span class="pill-count">{s?.known ?? 0}/{s?.total ?? 0}</span>
      </div>
    {/each}
  </div>

  <!-- Filters -->
  <div class="flex" style="flex-wrap:wrap;gap:.5rem;margin-bottom:1rem">
    <input bind:value={search} placeholder="Search recipes or ingredients…" style="max-width:240px" />
    <select bind:value={filterDish} style="max-width:140px">
      {#each DISH_TYPES as dt}<option>{dt}</option>{/each}
    </select>
    <select bind:value={filterRi} style="max-width:140px">
      <option value={0}>All RI Levels</option>
      {#each [1,2,3,4,5,6] as n}<option value={n}>RI {n}</option>{/each}
    </select>
    <select bind:value={sortBy} style="max-width:130px">
      <option value="name">Sort: Name</option>
      <option value="level">Sort: Level</option>
      <option value="type">Sort: Type</option>
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
    <p>Loading recipes…</p>
  {:else if filtered.length === 0}
    <div class="empty">
      <div class="empty-icon">🍖</div>
      <h2>No recipes match your filter</h2>
    </div>
  {:else}
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th></th>
            <th>Recipe</th>
            <th>Type</th>
            <th>Stats</th>
            <th>Ingredients</th>
            <th>Dur</th>
            <th>RI / Lv</th>
          </tr>
        </thead>
        <tbody>
          {#each filtered as r (r.id)}
            {@const isLearned = learnedIds.has(r.id)}
            <tr class:learned={isLearned} onclick={() => toggleLearned(r)}>
              <td class="check-cell">
                <span class="check-box {isLearned ? 'checked' : ''}"></span>
              </td>
              <td class="recipe-name">{r.name}</td>
              <td>
                <span class="badge {DISH_CLASS[r.dish_type] ?? ''}">
                  {DISH_LABEL[r.dish_type] ?? r.dish_type}
                </span>
              </td>
              <td class="stats-cell">{r.stat_bonuses ?? ''}</td>
              <td class="ing-cell">{ingredientList(r)}</td>
              <td style="white-space:nowrap;font-size:.8rem;color:var(--text-dim)">{r.duration}m</td>
              <td style="white-space:nowrap;font-size:.8rem;color:var(--text-dim)">RI{r.ri} / Lv{r.food_level}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  {/if}
</div>

<style>
  .dish-summary {
    display: flex;
    flex-wrap: wrap;
    gap: .4rem;
  }
  .dish-pill {
    display: flex;
    align-items: center;
    gap: .3rem;
    cursor: pointer;
    padding: .2rem .4rem;
    border-radius: var(--radius);
    border: 1px solid transparent;
    transition: border-color .15s;
  }
  .dish-pill:hover { border-color: var(--border); }
  .dish-pill.done .pill-count { color: var(--green); }
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
  .recipe-name { font-weight: 500; }
  .stats-cell { font-size: .8rem; color: var(--text-dim); }
  .ing-cell   { font-size: .8rem; color: var(--text-dim); }

  /* Dish-type badge colours */
  :global(.badge-hm)      { background: rgba(180,100,200,.15); color: #c070e0; border-color: rgba(180,100,200,.3); }
  :global(.badge-hs)      { background: rgba(200,100,80,.15);  color: #d07060; border-color: rgba(200,100,80,.3);  }
  :global(.badge-ms)      { background: rgba(60,160,180,.15);  color: #40b0c8; border-color: rgba(60,160,180,.3);  }
  :global(.badge-gourmet) { background: rgba(201,168,76,.2);   color: var(--gold); border-color: var(--gold-dim);  }
  :global(.badge-special) { background: rgba(255,140,0,.15);   color: #ff8c00;     border-color: rgba(255,140,0,.3); }
</style>
