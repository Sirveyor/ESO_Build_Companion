<script>
  import { api } from '../api.js'

  let allSets    = $state([])
  let compared   = $state([])   // full set objects returned by /compare
  let loading    = $state(false)
  let loadingSets = $state(true)
  let error      = $state('')
  let selected   = $state([])   // ids chosen in the picker

  const MAX = 4

  async function loadAllSets() {
    try {
      allSets = (await api.getGearSets()).sort((a, b) => a.name.localeCompare(b.name))
    } catch (e) {
      error = e.message
    } finally {
      loadingSets = false
    }
  }

  async function compare() {
    if (selected.length < 2) return
    loading = true; error = ''
    try {
      compared = await api.compareGearSets(selected)
    } catch (e) {
      error = e.message
      compared = []
    } finally {
      loading = false
    }
  }

  function toggleSelect(id) {
    if (selected.includes(id)) {
      selected = selected.filter(s => s !== id)
    } else if (selected.length < MAX) {
      selected = [...selected, id]
    }
  }

  // All unique piece counts that appear in ANY compared set's bonuses
  let allPieces = $derived.by(() => {
    const nums = new Set()
    for (const s of compared) {
      for (const b of (s.bonuses || [])) nums.add(b.pieces_required)
    }
    return [...nums].sort((a, b) => a - b)
  })

  function getBonusFor(gearSet, pieces) {
    return (gearSet.bonuses || []).filter(b => b.pieces_required === pieces)
  }

  loadAllSets()
</script>

<div class="page">
  <h1 style="margin-bottom:.25rem">Set Comparison</h1>
  <p style="margin-bottom:1.25rem">Select 2–{MAX} sets to compare their bonuses side by side.</p>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  <!-- Set picker -->
  {#if loadingSets}
    <p>Loading sets…</p>
  {:else if allSets.length === 0}
    <div class="notice notice-info">No gear sets in the database yet. Add some in the Gear Sets page first.</div>
  {:else}
    <div class="card picker-card">
      <div class="flex-between" style="margin-bottom:.75rem">
        <h3>Choose Sets</h3>
        <span class="badge">{selected.length}/{MAX} selected</span>
      </div>
      <div class="picker-grid">
        {#each allSets as s (s.id)}
          {@const isSelected = selected.includes(s.id)}
          {@const isDisabled = !isSelected && selected.length >= MAX}
          <button class="picker-btn" class:selected={isSelected} class:disabled={isDisabled}
                  onclick={() => toggleSelect(s.id)} disabled={isDisabled}>
            <span class="pick-name">{s.name}</span>
            <span class="badge badge-blue" style="font-size:.65rem">{s.set_type}</span>
          </button>
        {/each}
      </div>
      <div style="margin-top:.75rem">
        <button class="btn-primary" onclick={compare} disabled={selected.length < 2 || loading}>
          {loading ? 'Comparing…' : 'Compare Selected'}
        </button>
        {#if selected.length > 0}
          <button class="btn-ghost" style="margin-left:.5rem" onclick={() => { selected = []; compared = [] }}>
            Clear
          </button>
        {/if}
      </div>
    </div>

    <!-- Comparison table -->
    {#if compared.length >= 2}
      <div style="margin-top:1.5rem">
        <h2 style="margin-bottom:1rem">Side-by-Side Comparison</h2>

        <!-- Summary row -->
        <div class="compare-cols" style="--cols:{compared.length}">
          {#each compared as s (s.id)}
            <div class="card compare-header">
              <div class="cset-name">{s.name}</div>
              <span class="badge badge-blue">{s.set_type}</span>
              {#if s.location}
                <div style="font-size:.8rem;color:var(--text-dim);margin-top:.25rem">{s.location}</div>
              {/if}
            </div>
          {/each}
        </div>

        <!-- Bonuses by piece count -->
        {#each allPieces as pc}
          <div class="piece-row">
            <div class="piece-label badge badge-gold">{pc}-piece</div>
            <div class="compare-cols" style="--cols:{compared.length};margin-top:.5rem">
              {#each compared as s (s.id)}
                {@const bonuses = getBonusFor(s, pc)}
                <div class="bonus-cell" class:empty-cell={bonuses.length === 0}>
                  {#if bonuses.length === 0}
                    <span class="no-bonus">—</span>
                  {:else}
                    {#each bonuses as b}
                      <div class="bonus-entry">
                        <span class="bonus-desc">{b.bonus_description}</span>
                        {#if b.stat_type}
                          <span class="badge badge-green" style="margin-top:.25rem;font-size:.7rem">
                            {b.stat_type}{b.stat_value ? ` +${b.stat_value}` : ''}
                          </span>
                        {/if}
                      </div>
                    {/each}
                  {/if}
                </div>
              {/each}
            </div>
          </div>
        {/each}

        {#if allPieces.length === 0}
          <div class="notice notice-info" style="margin-top:.75rem">
            None of the selected sets have bonuses entered yet. Add them in the Gear Sets page.
          </div>
        {/if}
      </div>
    {/if}
  {/if}
</div>

<style>
  .picker-card { margin-bottom: 1rem; }

  .picker-grid {
    display: flex;
    flex-wrap: wrap;
    gap: .4rem;
  }

  .picker-btn {
    display: flex;
    align-items: center;
    gap: .4rem;
    padding: .35rem .7rem;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text-dim);
    font-size: .85rem;
    transition: border-color .15s, color .15s, background .15s;
  }
  .picker-btn:hover:not(.disabled) { border-color: var(--gold-dim); color: var(--text); }
  .picker-btn.selected { border-color: var(--gold); color: var(--gold); background: var(--gold-dim); }
  .picker-btn.disabled { opacity: .4; cursor: not-allowed; }
  .pick-name { font-weight: 500; }

  .compare-cols {
    display: grid;
    grid-template-columns: repeat(var(--cols), 1fr);
    gap: .75rem;
  }

  .compare-header { text-align: center; }
  .cset-name { font-weight: 700; font-size: 1rem; margin-bottom: .3rem; }

  .piece-row { margin-top: 1.25rem; }
  .piece-label { font-size: .85rem; font-weight: 700; margin-bottom: .25rem; display: inline-block; }

  .bonus-cell {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .65rem .75rem;
    min-height: 60px;
    display: flex;
    flex-direction: column;
  }
  .empty-cell { opacity: .35; }

  .bonus-entry { display: flex; flex-direction: column; gap: .2rem; }
  .bonus-desc  { font-size: .875rem; line-height: 1.4; }
  .no-bonus    { color: var(--text-dim); font-size: .85rem; align-self: center; margin: auto; }

  @media (max-width: 640px) {
    .compare-cols { grid-template-columns: 1fr; }
    .picker-btn { font-size: .8rem; }
  }
</style>
