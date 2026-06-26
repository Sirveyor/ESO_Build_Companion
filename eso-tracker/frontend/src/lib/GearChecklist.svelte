<script>
  import { api } from '../api.js'
  import { GEAR_SLOTS, GEAR_WEIGHTS, GEAR_TRAITS, GEAR_QUALITY } from './constants.js'

  let { build, onback } = $props()

  let gear     = $state([])
  let loading  = $state(true)
  let error    = $state('')
  let showForm = $state(false)
  let saving   = $state(false)
  let toggling = $state(new Set())

  let form = $state(blankForm())

  function blankForm() {
    return {
      set_name: '', slot: GEAR_SLOTS[0], weight: GEAR_WEIGHTS[0],
      trait: GEAR_TRAITS[0], quality: GEAR_QUALITY[3], notes: '',
    }
  }

  // Group gear by set_name for display
  let grouped = $derived.by(() => {
    const map = new Map()
    for (const g of gear) {
      if (!map.has(g.set_name)) map.set(g.set_name, [])
      map.get(g.set_name).push(g)
    }
    return [...map.entries()].sort(([a], [b]) => a.localeCompare(b))
  })

  let totalPieces   = $derived(gear.length)
  let obtainedCount = $derived(gear.filter(g => g.obtained).length)
  let percent       = $derived(totalPieces ? Math.round(obtainedCount / totalPieces * 100) : 0)

  async function load() {
    try {
      gear = await api.getBuildGear(build.id)
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function addGear() {
    if (!form.set_name.trim()) return
    saving = true; error = ''
    try {
      const created = await api.addGearToBuild(build.id, {
        id: crypto.randomUUID(),
        set_name: form.set_name.trim(),
        set_id: null,
        slot: form.slot,
        weight: form.weight,
        trait: form.trait,
        quality: form.quality,
        obtained: 0,
        stickerbook_unlocked: 0,
        location: null,
        source_notes: form.notes || null,
        craftable: 0,
        transmute_cost: null,
        notes: null,
        last_updated: new Date().toISOString(),
        custom_icon: null,
        enchantment: null,
      })
      gear = [...gear, created]
      form = blankForm()
      showForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function toggleObtained(item) {
    if (toggling.has(item.id)) return
    toggling = new Set([...toggling, item.id])
    try {
      const result = await api.toggleGearObtained(item.id)
      gear = gear.map(g => g.id === item.id ? { ...g, obtained: result.obtained } : g)
    } catch (e) {
      error = e.message
    } finally {
      toggling = new Set([...toggling].filter(id => id !== item.id))
    }
  }

  async function deleteGear(id) {
    try {
      await api.deleteGear(id)
      gear = gear.filter(g => g.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  load()
</script>

<div class="page">
  <!-- Header -->
  <div class="flex-between" style="margin-bottom:1rem">
    <div>
      <button class="btn-ghost back-btn" onclick={onback}>‹ Builds</button>
      <h1>{build.name}</h1>
      <div style="font-size:.85rem;color:var(--text-dim)">
        {build.class_name} · {build.role}
        {#if build.patch_version} · {build.patch_version}{/if}
      </div>
    </div>
    <button class="btn-primary" onclick={() => { showForm = !showForm }}>
      {showForm ? 'Cancel' : '+ Add Piece'}
    </button>
  </div>

  <!-- Overall progress -->
  {#if totalPieces > 0}
    <div class="card summary-card">
      <div class="summary-top flex-between">
        <span>Overall Progress</span>
        <span class:done={percent === 100}>
          {obtainedCount} / {totalPieces} pieces · {percent}%
        </span>
      </div>
      <div class="progress-wrap" style="margin-top:.5rem">
        <div class="progress-bar" class:full={percent === 100} style="width:{percent}%"></div>
      </div>
    </div>
  {/if}

  {#if error}
    <div class="notice notice-error" style="margin-top:.75rem">{error}</div>
  {/if}

  <!-- Add gear form -->
  {#if showForm}
    <div class="inline-form" style="margin-top:.75rem">
      <h3 style="margin-bottom:.75rem">Add Gear Piece</h3>
      <div class="form-grid">
        <div class="form-row">
          <label>Set Name *</label>
          <input bind:value={form.set_name} placeholder="e.g. Mother's Sorrow" />
        </div>
        <div class="form-row">
          <label>Slot</label>
          <select bind:value={form.slot}>
            {#each GEAR_SLOTS as s}<option>{s}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Weight / Type</label>
          <select bind:value={form.weight}>
            {#each GEAR_WEIGHTS as w}<option>{w}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Trait</label>
          <select bind:value={form.trait}>
            {#each GEAR_TRAITS as t}<option>{t}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Quality</label>
          <select bind:value={form.quality}>
            {#each GEAR_QUALITY as q}<option>{q}</option>{/each}
          </select>
        </div>
        <div class="form-row">
          <label>Notes / Where to get</label>
          <input bind:value={form.notes} placeholder="e.g. Deshaan overland" />
        </div>
      </div>
      <button class="btn-primary" onclick={addGear} disabled={saving || !form.set_name.trim()}>
        {saving ? 'Adding…' : 'Add Piece'}
      </button>
    </div>
  {/if}

  <!-- Gear list grouped by set -->
  {#if loading}
    <p style="margin-top:1rem">Loading gear…</p>
  {:else if gear.length === 0}
    <div class="empty">
      <div class="empty-icon">⚔</div>
      <h2>No gear pieces yet</h2>
      <p>Add the gear pieces you need to complete this build.</p>
    </div>
  {:else}
    <div class="gear-groups" style="margin-top:1rem">
      {#each grouped as [setName, pieces] (setName)}
        {@const setObtained = pieces.filter(p => p.obtained).length}
        {@const setPercent = Math.round(setObtained / pieces.length * 100)}
        <div class="card set-group">
          <div class="set-header flex-between">
            <div>
              <span class="set-name">{setName}</span>
              <span class="set-count badge" style="margin-left:.5rem">
                {setObtained}/{pieces.length}
              </span>
            </div>
            <div class="set-mini-progress">
              <div class="progress-wrap" style="width:80px">
                <div class="progress-bar" class:full={setPercent === 100}
                     style="width:{setPercent}%"></div>
              </div>
            </div>
          </div>

          <div class="table-wrap" style="margin-top:.75rem">
            <table>
              <thead>
                <tr>
                  <th>Slot</th>
                  <th>Weight</th>
                  <th>Trait</th>
                  <th>Quality</th>
                  <th>Notes</th>
                  <th>Obtained</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {#each pieces as item (item.id)}
                  <tr class:obtained={item.obtained}>
                    <td>{item.slot}</td>
                    <td><span class="badge">{item.weight}</span></td>
                    <td>{item.trait || '—'}</td>
                    <td>
                      <span class="badge" class:badge-gold={item.quality === 'Legendary'}
                            class:badge-blue={item.quality === 'Epic'}>
                        {item.quality || '—'}
                      </span>
                    </td>
                    <td style="color:var(--text-dim);font-size:.8rem">{item.source_notes || ''}</td>
                    <td>
                      <button class="check-wrap"
                              onclick={() => toggleObtained(item)}
                              disabled={toggling.has(item.id)}
                              title={item.obtained ? 'Mark as needed' : 'Mark as obtained'}>
                        <span class="check-box" class:checked={item.obtained}></span>
                      </button>
                    </td>
                    <td>
                      <button class="btn-icon" onclick={() => deleteGear(item.id)} title="Remove">✕</button>
                    </td>
                  </tr>
                {/each}
              </tbody>
            </table>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .back-btn { margin-bottom: .25rem; font-size: .85rem; }

  .summary-card { margin-top: 1rem; }
  .summary-top { font-size: .9rem; color: var(--text-dim); }
  .summary-top .done { color: var(--green); font-weight: 600; }

  .gear-groups { display: flex; flex-direction: column; gap: 1rem; }

  .set-group { padding: .875rem 1rem; }
  .set-header { flex-wrap: wrap; gap: .5rem; }
  .set-name { font-weight: 600; font-size: 1rem; }
  .set-count { font-size: .75rem; }

  tr.obtained td:not(:last-child):not(:nth-last-child(2)) {
    opacity: .45;
    text-decoration: line-through;
  }
  tr.obtained .check-box { background: var(--green); border-color: var(--green); }

  button.check-wrap {
    background: transparent;
    padding: 0;
    border: none;
  }
  button.check-wrap:disabled { opacity: .6; cursor: wait; }
</style>
