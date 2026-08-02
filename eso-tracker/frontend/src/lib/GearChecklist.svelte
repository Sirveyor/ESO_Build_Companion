<script>
  import { api } from '../api.js'
  import { GEAR_SLOTS, GEAR_WEIGHTS, GEAR_TRAITS, GEAR_QUALITY,
           ARMOR_GLYPHS, WEAPON_GLYPHS, JEWELRY_GLYPHS } from './constants.js'
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
    try {
      await api.toggleGearStickerbook(item.id)
    } catch (e) {
      // rollback optimistic update
      gear = gear.map(g => g.id === item.id ? { ...g, stickerbook_unlocked: item.stickerbook_unlocked } : g)
      error = e.message
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

  // ── Gear item editing ─────────────────────────────────────────────────────
  let editGear     = $state(null)
  let editGearForm = $state({ set_name: '', slot: GEAR_SLOTS[0], weight: GEAR_WEIGHTS[0], trait: GEAR_TRAITS[0], quality: GEAR_QUALITY[3], notes: '' })
  let savingEdit   = $state(false)

  function openGearEdit(item) {
    editGearForm = {
      set_name: item.set_name,
      slot:     item.slot,
      weight:   item.weight   || GEAR_WEIGHTS[0],
      trait:    item.trait    || GEAR_TRAITS[0],
      quality:  item.quality  || GEAR_QUALITY[3],
      notes:    item.source_notes || '',
    }
    editGear    = item.id
    editEnchant = null
  }

  async function saveGearEdit(item) {
    if (!editGearForm.set_name.trim()) return
    savingEdit = true; error = ''
    try {
      const updated = await api.updateGear(item.id, {
        ...item,
        set_name:     editGearForm.set_name.trim(),
        slot:         editGearForm.slot,
        weight:       editGearForm.weight,
        trait:        editGearForm.trait,
        quality:      editGearForm.quality,
        source_notes: editGearForm.notes || null,
        last_updated: new Date().toISOString(),
      })
      gear    = gear.map(g => g.id === item.id ? { ...updated, enchantment: item.enchantment } : g)
      editGear = null
    } catch (e) {
      error = e.message
    } finally {
      savingEdit = false
    }
  }

  // ── Enchantment editing ───────────────────────────────────────────────────
  let editEnchant = $state(null)
  let enchantForm = $state({ type: '', quality: GEAR_QUALITY[3], obtained: false, source: '' })
  let savingEnch  = $state(false)

  const JEWELRY_SLOTS = new Set(['Neck', 'Ring 1', 'Ring 2'])
  const WEAPON_SLOTS  = new Set(['Main Hand', 'Off Hand', 'Main Hand Backup', 'Off Hand Backup'])

  // Weapon types that occupy both hands — no off-hand can be paired with these
  const TWO_HANDED_TYPES = new Set([
    'Battle Axe', 'Greatsword', 'Maul',
    'Bow',
    'Flame Staff', 'Frost Staff', 'Lightning Staff',
    'Restoration Staff',
  ])
  const OFFHAND_TO_MAINHAND = { 'Off Hand': 'Main Hand', 'Off Hand Backup': 'Main Hand Backup' }
  const MAINHAND_TO_OFFHAND = { 'Main Hand': 'Off Hand', 'Main Hand Backup': 'Off Hand Backup' }

  function twoHandedConflict(slot, weight, gearList) {
    // Adding an off-hand when the paired main hand holds a 2H weapon
    const mhSlot = OFFHAND_TO_MAINHAND[slot]
    if (mhSlot) {
      const mh = gearList.find(g => g.slot === mhSlot)
      if (mh && TWO_HANDED_TYPES.has(mh.weight))
        return `${mhSlot} has a ${mh.weight} (two-handed) — an off-hand cannot be equipped on the same bar.`
    }
    // Adding/changing a main hand to a 2H weapon when the paired off-hand already exists
    const ohSlot = MAINHAND_TO_OFFHAND[slot]
    if (ohSlot && TWO_HANDED_TYPES.has(weight)) {
      const oh = gearList.find(g => g.slot === ohSlot)
      if (oh)
        return `${weight} is two-handed — remove the ${ohSlot} piece (${oh.set_name}) first, or it cannot be equipped.`
    }
    return null
  }

  function duplicateSlotConflict(slot, gearList) {
    const existing = gearList.find(g => g.slot === slot)
    if (existing)
      return `The ${slot} slot is already filled by ${existing.set_name} in this build.`
    return null
  }

  function slotType(slot) {
    if (JEWELRY_SLOTS.has(slot)) return 'Jewelry'
    if (WEAPON_SLOTS.has(slot))  return 'Weapon'
    return 'Armor'
  }

  // ── Reference data for dropdowns ─────────────────────────────────────────
  let allGearSets     = $state([])
  let refEnchantList  = $state([])
  let refTraitList    = $state([])
  let refWeaponTypes  = $state([])

  // Leaf weapon types: those that are NOT a parent of any other entry
  let weaponLeafTypes = $derived.by(() => {
    const parentIds = new Set(refWeaponTypes.filter(w => w.parent_id != null).map(w => w.parent_id))
    return refWeaponTypes.filter(w => !parentIds.has(w.id))
  })

  async function loadRefData() {
    try {
      const [sets, enchs, traits, wtypes] = await Promise.all([
        api.getGearSets(),
        api.getRefEnchantments(),
        api.getRefTraits(),
        api.getRefWeaponTypes(),
      ])
      allGearSets    = sets
      refEnchantList = enchs
      refTraitList   = traits
      refWeaponTypes = wtypes
    } catch (e) { /* non-fatal; forms fall back to static constants */ }
  }

  function glyphSuggestions(slot) {
    const st = slotType(slot)
    const filtered = refEnchantList.filter(e => e.slot_type === st)
    if (filtered.length) return filtered.map(e => e.name)
    if (JEWELRY_SLOTS.has(slot)) return JEWELRY_GLYPHS
    if (WEAPON_SLOTS.has(slot))  return WEAPON_GLYPHS
    return ARMOR_GLYPHS
  }

  let addTraitOptions = $derived.by(() => {
    const filtered = refTraitList.filter(t => t.slot_type === slotType(form.slot))
    return filtered.length ? filtered.map(t => t.name) : GEAR_TRAITS
  })

  let editTraitOptions = $derived.by(() => {
    const filtered = refTraitList.filter(t => t.slot_type === slotType(editGearForm.slot))
    return filtered.length ? filtered.map(t => t.name) : GEAR_TRAITS
  })

  let addConflict  = $derived.by(() =>
    duplicateSlotConflict(form.slot, gear) ||
    twoHandedConflict(form.slot, form.weight, gear)
  )
  let editConflict = $derived.by(() => {
    const others = gear.filter(g => g.id !== editGear)
    return duplicateSlotConflict(editGearForm.slot, others) ||
           twoHandedConflict(editGearForm.slot, editGearForm.weight, others)
  })

  // Auto-fill "where to get" from the matched gear set's location
  $effect(() => {
    const match = allGearSets.find(s => s.name.toLowerCase() === form.set_name.toLowerCase())
    if (match?.location && !form.notes) form.notes = match.location
  })

  $effect(() => {
    const match = allGearSets.find(s => s.name.toLowerCase() === editGearForm.set_name.toLowerCase())
    if (match?.location && !editGearForm.notes) editGearForm.notes = match.location
  })

  function openEnchantEdit(item) {
    enchantForm = {
      type:     item.enchantment?.type    ?? '',
      quality:  item.enchantment?.quality ?? GEAR_QUALITY[3],
      obtained: !!(item.enchantment?.obtained),
      source:   item.enchantment?.source  ?? '',
    }
    editEnchant = item.id
    editGear    = null
  }

  async function saveEnchantment(item) {
    savingEnch = true
    try {
      const updated = await api.updateGearEnchantment(item.id, {
        gear_id:  item.id,
        type:     enchantForm.type    || null,
        quality:  enchantForm.quality || null,
        obtained: enchantForm.obtained ? 1 : 0,
        source:   enchantForm.source  || null,
        level:    null,
      })
      gear = gear.map(g => g.id === item.id ? { ...g, enchantment: updated } : g)
      editEnchant = null
    } catch (e) {
      error = e.message
    } finally {
      savingEnch = false
    }
  }

  loadGear()
  loadRefData()
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
    <datalist id="gear-set-names">
      {#each allGearSets as s}<option value={s.name}></option>{/each}
    </datalist>

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
            <input bind:value={form.set_name} list="gear-set-names" placeholder="e.g. Mother's Sorrow" />
          </div>
          <div class="form-row">
            <label>Slot</label>
            <select bind:value={form.slot}>
              {#each GEAR_SLOTS as s}<option>{s}</option>{/each}
            </select>
          </div>
          <div class="form-row">
            <label>{WEAPON_SLOTS.has(form.slot) ? 'Weapon Type' : 'Weight'}</label>
            <select bind:value={form.weight}>
              {#if WEAPON_SLOTS.has(form.slot)}
                {#each weaponLeafTypes as wt}<option value={wt.name}>{wt.name}</option>{/each}
              {:else if JEWELRY_SLOTS.has(form.slot)}
                <option>Jewelry</option>
              {:else}
                <option>Heavy</option>
                <option>Medium</option>
                <option>Light</option>
              {/if}
            </select>
          </div>
          <div class="form-row">
            <label>Trait</label>
            <select bind:value={form.trait}>
              {#each addTraitOptions as t}<option>{t}</option>{/each}
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
        {#if addConflict}
          <div class="notice notice-warn" style="margin-bottom:.5rem">{addConflict}</div>
        {/if}
        <button class="btn-primary" onclick={addGear} disabled={saving || !form.set_name.trim() || !!addConflict}>
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
                    <th>Weight / Type</th>
                    <th>Trait</th>
                    <th>Quality</th>
                    <th>Enchant</th>
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
                      <td>
                        {#if WEAPON_SLOTS.has(item.slot)}
                          <span class="badge badge-weapon-type">{item.weight || '—'}</span>
                        {:else if JEWELRY_SLOTS.has(item.slot)}
                          <span class="badge badge-jewelry-type">{item.weight || '—'}</span>
                        {:else}
                          <span class="badge">{item.weight || '—'}</span>
                        {/if}
                      </td>
                      <td>{item.trait || '—'}</td>
                      <td>
                        <span class="badge"
                              class:badge-gold={item.quality === 'Legendary'}
                              class:badge-blue={item.quality === 'Epic'}>
                          {item.quality || '—'}
                        </span>
                      </td>
                      <td>
                        {#if item.enchantment?.type}
                          <button class="enchant-btn" onclick={() => openEnchantEdit(item)}>
                            <span class="enchant-name">{item.enchantment.type}</span>
                            {#if item.enchantment.obtained}
                              <span class="enchant-got">✓</span>
                            {/if}
                          </button>
                        {:else}
                          <button class="btn-ghost enchant-add" onclick={() => openEnchantEdit(item)}>+ Glyph</button>
                        {/if}
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
                      <td class="actions-cell">
                        <button class="btn-icon" onclick={() => openGearEdit(item)} title="Edit">✎</button>
                        <button class="btn-icon" onclick={() => deleteGear(item.id)} title="Remove">✕</button>
                      </td>
                    </tr>
                    {#if editGear === item.id}
                      <tr class="gear-edit-row">
                        <td colspan="9">
                          <div class="gear-edit-form">
                            <div class="form-grid gear-edit-grid">
                              <div class="form-row">
                                <label>Set Name *</label>
                                <input bind:value={editGearForm.set_name} list="gear-set-names" />
                              </div>
                              <div class="form-row">
                                <label>Slot</label>
                                <select bind:value={editGearForm.slot}>
                                  {#each GEAR_SLOTS as s}<option>{s}</option>{/each}
                                </select>
                              </div>
                              <div class="form-row">
                                <label>{WEAPON_SLOTS.has(editGearForm.slot) ? 'Weapon Type' : 'Weight'}</label>
                                <select bind:value={editGearForm.weight}>
                                  {#if WEAPON_SLOTS.has(editGearForm.slot)}
                                    {#each weaponLeafTypes as wt}<option value={wt.name}>{wt.name}</option>{/each}
                                  {:else if JEWELRY_SLOTS.has(editGearForm.slot)}
                                    <option>Jewelry</option>
                                  {:else}
                                    <option>Heavy</option>
                                    <option>Medium</option>
                                    <option>Light</option>
                                  {/if}
                                </select>
                              </div>
                              <div class="form-row">
                                <label>Trait</label>
                                <select bind:value={editGearForm.trait}>
                                  {#each editTraitOptions as t}<option>{t}</option>{/each}
                                </select>
                              </div>
                              <div class="form-row">
                                <label>Quality</label>
                                <select bind:value={editGearForm.quality}>
                                  {#each GEAR_QUALITY as q}<option>{q}</option>{/each}
                                </select>
                              </div>
                              <div class="form-row">
                                <label>Notes / Where to get</label>
                                <input bind:value={editGearForm.notes} placeholder="e.g. Deshaan overland" />
                              </div>
                            </div>
                            {#if editConflict}
                              <div class="notice notice-warn" style="margin:.4rem 0 .25rem">{editConflict}</div>
                            {/if}
                            <div class="flex" style="gap:.4rem;margin-top:.5rem">
                              <button class="btn-primary" style="padding:.25rem .75rem;flex-shrink:0"
                                      onclick={() => saveGearEdit(item)}
                                      disabled={savingEdit || !editGearForm.set_name.trim() || !!editConflict}>
                                {savingEdit ? '…' : 'Save'}
                              </button>
                              <button class="btn-ghost" style="padding:.25rem .75rem;flex-shrink:0"
                                      onclick={() => editGear = null}>Cancel</button>
                            </div>
                          </div>
                        </td>
                      </tr>
                    {/if}
                    {#if editEnchant === item.id}
                      <tr class="enchant-edit-row">
                        <td colspan="9">
                          <div class="enchant-form">
                            <input class="enchant-type-input"
                                   list="glyphs-{item.id}"
                                   bind:value={enchantForm.type}
                                   placeholder="Glyph type…" />
                            <datalist id="glyphs-{item.id}">
                              {#each glyphSuggestions(item.slot) as g}
                                <option value={g}></option>
                              {/each}
                            </datalist>
                            <select bind:value={enchantForm.quality} style="width:auto">
                              {#each GEAR_QUALITY as q}<option>{q}</option>{/each}
                            </select>
                            <button class="check-wrap enchant-got-btn"
                                    onclick={() => enchantForm.obtained = !enchantForm.obtained}
                                    title={enchantForm.obtained ? 'Have glyph' : 'Need glyph'}>
                              <span class="check-box" class:checked={enchantForm.obtained}></span>
                              <span class="enchant-got-label">Got it</span>
                            </button>
                            <input bind:value={enchantForm.source}
                                   placeholder="Source / notes…"
                                   style="flex:1;min-width:80px" />
                            <button class="btn-primary" style="padding:.25rem .75rem;flex-shrink:0"
                                    onclick={() => saveEnchantment(item)} disabled={savingEnch}>
                              {savingEnch ? '…' : 'Save'}
                            </button>
                            <button class="btn-ghost" style="padding:.25rem .75rem;flex-shrink:0"
                                    onclick={() => editEnchant = null}>Cancel</button>
                          </div>
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

  :global(.badge-weapon-type)  { border-color: #7a4a2a; color: #c4845a; }
  :global(.badge-jewelry-type) { border-color: #5a4a7a; color: #9a8ac0; }

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

  tr.obtained td:not(:last-child):not(:nth-last-child(2)):not(:nth-last-child(3)):not(:nth-last-child(5)) {
    opacity: .45;
    text-decoration: line-through;
  }

  /* Enchantment column */
  .enchant-btn {
    background: none; border: none; padding: 0; text-align: left; cursor: pointer;
    color: var(--gold); display: flex; align-items: center; gap: .25rem; font-size: .8rem;
  }
  .enchant-btn:hover { opacity: .75; }
  .enchant-name {
    white-space: normal; word-break: break-word; display: block;
  }
  .enchant-got { color: var(--green); font-size: .7rem; flex-shrink: 0; }
  .enchant-add { font-size: .72rem; padding: .1rem .35rem; color: var(--text-dim); }

  .actions-cell { white-space: nowrap; }

  .gear-edit-row td { padding: .6rem .75rem; background: var(--surface-2); border-top: none; }
  .gear-edit-form { }
  .gear-edit-grid { grid-template-columns: 1fr 1fr 1fr; }

  .enchant-edit-row td { padding: .4rem .75rem; background: var(--surface-2); border-top: none; }
  .enchant-form { display: flex; align-items: center; gap: .4rem; flex-wrap: wrap; }
  .enchant-type-input { width: 180px; }
  .enchant-got-btn { display: flex; align-items: center; gap: .3rem; }
  .enchant-got-label { font-size: .8rem; color: var(--text-dim); white-space: nowrap; }

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
