<script>
  import { api } from '../api.js'
  import { GEAR_SLOTS, GEAR_WEIGHTS, GEAR_TRAITS, GEAR_QUALITY } from './constants.js'
  import SkillBar             from './SkillBar.svelte'
  import TraitTracker         from './TraitTracker.svelte'
  import ChampionPointsEditor from './ChampionPointsEditor.svelte'

  let { build, character, onback } = $props()

  let activeTab = $state('gear')   // 'gear' | 'skills' | 'traits' | 'cp'

  // ── Gear tab state ──────────────────────────────────────────────────────────
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

  async function loadGear() {
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
      form = blankForm(); showForm = false
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

  async function toggleStickerbook(item) {
    const next = item.stickerbook_unlocked ? 0 : 1
    gear = gear.map(g => g.id === item.id ? { ...g, stickerbook_unlocked: next } : g)
  }

  async function deleteGear(id) {
    try {
      await api.deleteGear(id)
      gear = gear.filter(g => g.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  loadGear()
</script>

<div class="page">
  <!-- Header -->
  <div class="flex-between" style="margin-bottom:.75rem">
    <div>
      <button class="btn-ghost back-btn" onclick={onback}>‹ Builds</button>
      <h1>{build.name}</h1>
      <div style="font-size:.85rem;color:var(--text-dim)">
        {build.class_name} · {build.role}
        {#if build.patch_version} · {build.patch_version}{/if}
      </div>
    </div>
    {#if activeTab === 'gear'}
      <button class="btn-primary" onclick={() => { showForm = !showForm }}>
        {showForm ? 'Cancel' : '+ Add Piece'}
      </button>
    {/if}
  </div>

  <!-- Tabs -->
  <div class="tabs">
    <button class:active={activeTab === 'gear'}   onclick={() => activeTab = 'gear'}>Gear</button>
    <button class:active={activeTab === 'skills'} onclick={() => activeTab = 'skills'}>Skills</button>
    <button class:active={activeTab === 'traits'} onclick={() => activeTab = 'traits'}>Traits</button>
    <button class:active={activeTab === 'cp'}     onclick={() => activeTab = 'cp'}>Champion Points</button>
  </div>

  <!-- ── GEAR TAB ─────────────────────────────────────────────────────────── -->
  {#if activeTab === 'gear'}
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
              <div class="progress-wrap" style="width:80px">
                <div class="progress-bar" class:full={setPercent === 100}
                     style="width:{setPercent}%"></div>
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
                    <th title="Obtained">Got</th>
                    <th title="Stickerbook unlocked">SB</th>
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
                        <span class="badge"
                              class:badge-gold={item.quality === 'Legendary'}
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
                        <button class="check-wrap"
                                onclick={() => toggleStickerbook(item)}
                                title={item.stickerbook_unlocked ? 'Remove from stickerbook' : 'Add to stickerbook'}>
                          <span class="check-box sb-box" class:checked={item.stickerbook_unlocked}></span>
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

  <!-- ── SKILLS TAB ────────────────────────────────────────────────────────── -->
  {:else if activeTab === 'skills'}
    <div style="margin-top:.75rem">
      <SkillBar {build} />
    </div>

  <!-- ── TRAITS TAB ────────────────────────────────────────────────────────── -->
  {:else if activeTab === 'traits'}
    <div style="margin-top:.75rem">
      <TraitTracker {character} />
    </div>

  <!-- ── CHAMPION POINTS TAB ──────────────────────────────────────────────── -->
  {:else if activeTab === 'cp'}
    <div style="margin-top:.75rem">
      <ChampionPointsEditor {build} />
    </div>
  {/if}
</div>

<style>
  .back-btn { margin-bottom: .25rem; font-size: .85rem; }

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

  .summary-card { margin-top: 1rem; }
  .summary-top { font-size: .9rem; color: var(--text-dim); }
  .summary-top .done { color: var(--green); font-weight: 600; }

  .gear-groups { display: flex; flex-direction: column; gap: 1rem; }
  .set-group { padding: .875rem 1rem; }
  .set-header { flex-wrap: wrap; gap: .5rem; }
  .set-name { font-weight: 600; font-size: 1rem; }
  .set-count { font-size: .75rem; }

  tr.obtained td:not(:last-child):not(:nth-last-child(2)):not(:nth-last-child(3)) {
    opacity: .45;
    text-decoration: line-through;
  }

  button.check-wrap {
    background: transparent;
    padding: 0;
    border: none;
  }
  button.check-wrap:disabled { opacity: .6; cursor: wait; }

  /* Blue tint for stickerbook checkbox */
  .sb-box { border-color: var(--blue) !important; }
  .sb-box.checked { background: var(--blue) !important; border-color: var(--blue) !important; }

  @media (max-width: 640px) {
    .tabs button { padding: .35rem .6rem; font-size: .8rem; }
  }
</style>
