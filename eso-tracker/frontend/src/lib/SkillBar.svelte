<script>
  import { api } from '../api.js'

  let { build } = $props()

  // slots[bar][position] = assignment | null
  let slots = $state({ bar1: Array(6).fill(null), bar2: Array(6).fill(null) })
  let loading  = $state(true)
  let error    = $state('')
  let editing  = $state(null)   // { bar, position } currently open for editing
  let saving   = $state(false)

  let form = $state(blankForm())
  function blankForm() {
    return { name: '', skill_line: '', morph: '', obtained: false }
  }

  async function load() {
    try {
      const assignments = await api.getBuildSkills(build.id)
      const next = { bar1: Array(6).fill(null), bar2: Array(6).fill(null) }
      for (const a of assignments) {
        if (next[a.bar]) next[a.bar][a.position] = a
      }
      slots = next
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  function openSlot(bar, position) {
    const existing = slots[bar][position]
    if (existing) {
      form = {
        name: existing.skill.name,
        skill_line: existing.skill.skill_line,
        morph: existing.skill.morph || '',
        obtained: !!existing.skill.obtained,
      }
    } else {
      form = blankForm()
    }
    editing = { bar, position }
  }

  async function saveSlot() {
    if (!form.name.trim()) return
    saving = true; error = ''
    const { bar, position } = editing
    const isUlt = position === 5 ? 1 : 0
    try {
      const result = await api.setBuildSkill(build.id, {
        skill: {
          name: form.name.trim(),
          skill_line: form.skill_line.trim(),
          morph: form.morph.trim() || null,
          obtained: form.obtained ? 1 : 0,
        },
        bar,
        position,
        is_ultimate: isUlt,
      })
      slots = {
        ...slots,
        [bar]: slots[bar].map((s, i) => i === position ? result : s),
      }
      editing = null
      form = blankForm()
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function clearSlot(bar, position) {
    try {
      await api.clearSkillSlot(build.id, bar, position)
      slots = {
        ...slots,
        [bar]: slots[bar].map((s, i) => i === position ? null : s),
      }
    } catch (e) {
      error = e.message
    }
    if (editing?.bar === bar && editing?.position === position) editing = null
  }

  async function toggleObtained(assignment) {
    try {
      const res = await api.toggleSkillObtained(assignment.skill.id)
      const { bar, position } = assignment
      slots = {
        ...slots,
        [bar]: slots[bar].map((s, i) =>
          i === position ? { ...s, skill: { ...s.skill, obtained: res.obtained } } : s
        ),
      }
    } catch (e) {
      error = e.message
    }
  }

  load()
</script>

<div class="skill-section">
  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if loading}
    <p>Loading skills…</p>
  {:else}
    {#each ['bar1', 'bar2'] as bar, barIdx}
      <div class="bar-wrap">
        <div class="bar-label">Bar {barIdx + 1}</div>
        <div class="bar-slots">
          {#each Array(6) as _, pos}
            {@const a = slots[bar][pos]}
            {@const isUlt = pos === 5}
            <div class="slot-col">
              <button
                class="slot"
                class:filled={!!a}
                class:ult={isUlt}
                class:obtained={a?.skill?.obtained}
                onclick={() => openSlot(bar, pos)}
                title={a ? `${a.skill.name} (${a.skill.skill_line})` : isUlt ? 'Set Ultimate' : 'Add Skill'}
              >
                {#if a}
                  <span class="slot-name">{a.skill.morph || a.skill.name}</span>
                  <span class="slot-line">{a.skill.skill_line}</span>
                {:else}
                  <span class="slot-empty">{isUlt ? '★' : '+'}</span>
                {/if}
              </button>
              {#if a}
                <div class="slot-actions">
                  <button class="check-wrap" onclick={() => toggleObtained(a)}
                          title={a.skill.obtained ? 'Mark not obtained' : 'Mark obtained'}>
                    <span class="check-box" class:checked={a.skill.obtained}></span>
                  </button>
                  <button class="btn-icon" style="font-size:.65rem"
                          onclick={() => clearSlot(bar, pos)} title="Clear slot">✕</button>
                </div>
              {/if}
            </div>
          {/each}
        </div>
      </div>
    {/each}

    <!-- Inline edit form -->
    {#if editing}
      {@const isUlt = editing.position === 5}
      <div class="inline-form" style="margin-top:1rem">
        <h3 style="margin-bottom:.75rem">
          {isUlt ? 'Ultimate' : `Slot ${editing.position + 1}`} — Bar {editing.bar === 'bar1' ? 1 : 2}
        </h3>
        <div class="form-grid">
          <div class="form-row">
            <label>Skill Name *</label>
            <input bind:value={form.name} placeholder="e.g. Elemental Blockade" />
          </div>
          <div class="form-row">
            <label>Skill Line</label>
            <input bind:value={form.skill_line} placeholder="e.g. Destruction Staff" />
          </div>
          <div class="form-row">
            <label>Morph / Variant</label>
            <input bind:value={form.morph} placeholder="e.g. Unstable Wall of Elements" />
          </div>
          <div class="form-row" style="align-items:center">
            <label>Obtained</label>
            <input type="checkbox" bind:checked={form.obtained} style="width:auto;margin-top:.2rem" />
          </div>
        </div>
        <div class="flex" style="gap:.5rem;margin-top:.5rem">
          <button class="btn-primary" onclick={saveSlot}
                  disabled={saving || !form.name.trim()}>
            {saving ? 'Saving…' : 'Set Skill'}
          </button>
          <button class="btn-ghost" onclick={() => { editing = null; form = blankForm() }}>Cancel</button>
        </div>
      </div>
    {/if}

    <!-- Legend -->
    <div class="legend">
      <span class="check-box checked" style="display:inline-block;width:12px;height:12px;border-radius:3px"></span> obtained
      <span style="margin-left:.75rem">★ = ultimate slot</span>
    </div>
  {/if}
</div>

<style>
  .skill-section { display: flex; flex-direction: column; gap: 1.25rem; }

  .bar-wrap { }
  .bar-label {
    font-size: .75rem;
    font-weight: 700;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: .06em;
    margin-bottom: .4rem;
  }

  .bar-slots {
    display: flex;
    gap: .4rem;
    flex-wrap: wrap;
  }

  .slot-col { display: flex; flex-direction: column; align-items: center; gap: .2rem; }

  .slot {
    width: 80px;
    height: 72px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: .15rem;
    background: var(--surface-2);
    border: 2px dashed var(--border);
    border-radius: var(--radius);
    cursor: pointer;
    transition: border-color .15s, background .15s;
    padding: .25rem;
    overflow: hidden;
  }
  .slot:hover              { border-color: var(--gold-dim); background: var(--surface); }
  .slot.filled             { border-style: solid; border-color: var(--border); background: var(--surface); }
  .slot.filled:hover       { border-color: var(--gold-dim); }
  .slot.ult                { border-color: var(--gold-dim); }
  .slot.ult.filled         { border-color: var(--gold); }
  .slot.obtained.filled    { border-color: var(--green); }

  .slot-empty { font-size: 1.4rem; color: var(--text-dim); line-height: 1; }
  .slot-name  { font-size: .72rem; font-weight: 600; text-align: center; line-height: 1.2; color: var(--text); }
  .slot-line  { font-size: .62rem; text-align: center; color: var(--text-dim); line-height: 1.2; }

  .slot-actions { display: flex; align-items: center; gap: .2rem; }

  button.check-wrap {
    background: transparent;
    border: none;
    padding: 0;
  }

  .legend { font-size: .75rem; color: var(--text-dim); margin-top: .5rem; display: flex; align-items: center; gap: .25rem; }

  @media (max-width: 640px) {
    .slot { width: 64px; height: 60px; }
    .slot-name { font-size: .65rem; }
  }
</style>
