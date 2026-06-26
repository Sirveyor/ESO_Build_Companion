<script>
  import { api } from '../api.js'

  let { character } = $props()

  const STATUSES = ['unknown', 'in_progress', 'complete']
  const STATUS_LABEL = { unknown: 'Unknown', in_progress: 'Researching', complete: 'Complete' }
  const STATUS_CLASS = { unknown: '', in_progress: 'badge-blue', complete: 'badge-green' }

  // Trait categories for quick-fill suggestions
  const ARMOR_TRAITS   = ['Divines', 'Infused', 'Impenetrable', 'Reinforced', 'Well-Fitted', 'Sturdy', 'Training', 'Exploration', 'Nirnhoned']
  const WEAPON_TRAITS  = ['Powered', 'Charged', 'Precise', 'Infused', 'Defending', 'Training', 'Sharpened', 'Weighted', 'Nirnhoned']
  const JEWELRY_TRAITS = ['Arcane', 'Healthy', 'Robust', 'Infused', 'Bloodthirsty', 'Harmony', 'Protective', 'Swift', 'Triune']

  let traits   = $state([])
  let loading  = $state(true)
  let error    = $state('')
  let showForm = $state(false)
  let saving   = $state(false)
  let timerNow = $state(Date.now())

  let form = $state(blankForm())
  function blankForm() {
    return { trait_type: '', research_status: 'unknown', notes: '', research_end_time: '' }
  }

  // Tick every minute to update research timers
  $effect(() => {
    const t = setInterval(() => timerNow = Date.now(), 60_000)
    return () => clearInterval(t)
  })

  function timeRemaining(endTime) {
    if (!endTime) return null
    const diff = new Date(endTime).getTime() - timerNow
    if (diff <= 0) return 'Ready'
    const h = Math.floor(diff / 3_600_000)
    const m = Math.floor((diff % 3_600_000) / 60_000)
    return h > 0 ? `${h}h ${m}m` : `${m}m`
  }

  async function load() {
    try {
      traits = await api.getTraits(character.id)
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function addTrait() {
    if (!form.trait_type.trim()) return
    saving = true; error = ''
    try {
      const created = await api.createTrait({
        id: crypto.randomUUID(),
        trait_type: form.trait_type.trim(),
        character_id: character.id,
        research_status: form.research_status,
        research_end_time: form.research_status === 'in_progress' && form.research_end_time
          ? new Date(form.research_end_time).toISOString()
          : null,
        notes: form.notes || null,
        craftable: form.research_status === 'complete' ? 1 : 0,
      })
      traits = [...traits, created].sort((a, b) => a.trait_type.localeCompare(b.trait_type))
      form = blankForm(); showForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function markComplete(t) {
    try {
      const updated = await api.completeTrait(t.id)
      traits = traits.map(tr => tr.id === t.id
        ? { ...tr, research_status: updated.research_status, research_end_time: null, craftable: 1 }
        : tr
      )
    } catch (e) {
      error = e.message
    }
  }

  async function startResearch(t, endTime) {
    try {
      const updated = await api.startTraitResearch(t.id, new Date(endTime).toISOString())
      traits = traits.map(tr => tr.id === t.id
        ? { ...tr, research_status: 'in_progress', research_end_time: updated.research_end_time }
        : tr
      )
    } catch (e) {
      error = e.message
    }
  }

  async function deleteTrait(id) {
    try {
      await api.deleteTrait(id)
      traits = traits.filter(t => t.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  load()
</script>

<div class="trait-section">
  <div class="flex-between" style="margin-bottom:.75rem">
    <span style="font-size:.85rem;color:var(--text-dim)">
      {traits.filter(t => t.research_status === 'complete').length} / {traits.length} traits unlocked
    </span>
    <button class="btn-secondary" style="font-size:.8rem"
            onclick={() => { showForm = !showForm }}>
      {showForm ? 'Cancel' : '+ Add Trait'}
    </button>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if showForm}
    <div class="inline-form" style="margin-bottom:.75rem">
      <div class="form-grid">
        <div class="form-row">
          <label>Trait</label>
          <input bind:value={form.trait_type}
                 placeholder="e.g. Heavy Armor Head — Divines" list="trait-suggestions" />
          <datalist id="trait-suggestions">
            {#each ARMOR_TRAITS as t}<option value="Armor — {t}"></option>{/each}
            {#each WEAPON_TRAITS as t}<option value="Weapon — {t}"></option>{/each}
            {#each JEWELRY_TRAITS as t}<option value="Jewelry — {t}"></option>{/each}
          </datalist>
        </div>
        <div class="form-row">
          <label>Status</label>
          <select bind:value={form.research_status}>
            {#each STATUSES as s}<option value={s}>{STATUS_LABEL[s]}</option>{/each}
          </select>
        </div>
        {#if form.research_status === 'in_progress'}
          <div class="form-row">
            <label>Research Completes</label>
            <input type="datetime-local" bind:value={form.research_end_time} />
          </div>
        {/if}
        <div class="form-row">
          <label>Notes</label>
          <input bind:value={form.notes} placeholder="Optional notes" />
        </div>
      </div>
      <button class="btn-primary" onclick={addTrait}
              disabled={saving || !form.trait_type.trim()}>
        {saving ? 'Adding…' : 'Add Trait'}
      </button>
    </div>
  {/if}

  {#if loading}
    <p>Loading traits…</p>
  {:else if traits.length === 0}
    <div class="empty">
      <div class="empty-icon">🔬</div>
      <h3>No traits tracked yet</h3>
      <p>Add traits to track your research progress for {character.name}.</p>
    </div>
  {:else}
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Trait</th>
            <th>Status</th>
            <th>Time Left</th>
            <th>Notes</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {#each traits as t (t.id)}
            {@const remaining = t.research_end_time ? timeRemaining(t.research_end_time) : null}
            <tr class:complete={t.research_status === 'complete'}>
              <td class="trait-type">{t.trait_type}</td>
              <td>
                <span class="badge {STATUS_CLASS[t.research_status] || ''}">
                  {STATUS_LABEL[t.research_status] || t.research_status}
                </span>
              </td>
              <td>
                {#if remaining === 'Ready'}
                  <button class="btn-secondary" style="font-size:.75rem;padding:.2rem .6rem"
                          onclick={() => markComplete(t)}>
                    Mark Complete
                  </button>
                {:else if remaining}
                  <span style="color:var(--blue);font-size:.82rem">{remaining}</span>
                {:else if t.research_status === 'in_progress'}
                  <input type="datetime-local" style="font-size:.75rem;padding:.2rem"
                         onchange={(e) => startResearch(t, e.target.value)} />
                {:else if t.research_status !== 'complete'}
                  <button class="btn-ghost" style="font-size:.75rem;padding:.2rem .6rem"
                          onclick={() => startResearch(t, new Date(Date.now() + 21600000).toISOString())}>
                    Start (6h)
                  </button>
                {:else}
                  <span style="color:var(--green);font-size:.8rem">✓ Done</span>
                {/if}
              </td>
              <td style="font-size:.8rem;color:var(--text-dim)">{t.notes || ''}</td>
              <td>
                <button class="btn-icon" onclick={() => deleteTrait(t.id)} title="Delete">✕</button>
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>

    <!-- Quick-add common traits -->
    <details style="margin-top:.75rem">
      <summary style="font-size:.8rem;color:var(--text-dim);cursor:pointer">Quick-add common traits</summary>
      <div class="quick-add">
        {#each ['Divines', 'Infused', 'Impenetrable', 'Nirnhoned', 'Precise', 'Sharpened', 'Bloodthirsty'] as t}
          <button class="badge" style="cursor:pointer"
                  onclick={() => { form.trait_type = t; showForm = true }}>
            + {t}
          </button>
        {/each}
      </div>
    </details>
  {/if}
</div>

<style>
  .trait-section { }
  tr.complete td { opacity: .5; }
  .trait-type { font-weight: 500; }
  .quick-add { display: flex; flex-wrap: wrap; gap: .3rem; margin-top: .4rem; }
  .quick-add .badge { cursor: pointer; }
  .quick-add .badge:hover { border-color: var(--gold-dim); color: var(--gold); }
</style>
