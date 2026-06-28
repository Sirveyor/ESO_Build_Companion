<script>
  import { api } from '../api.js'

  let { build } = $props()

  let cp      = $state({ build_id: '', warfare: '', fitness: '', craft: '' })
  let loading = $state(true)
  let saving  = $state(false)
  let saved   = $state(false)
  let error   = $state('')

  // Example placeholders so users know the format
  const PLACEHOLDERS = {
    warfare: 'Fighting Finesse: 20\nBiting Aura: 20\nMaster-at-Arms: 20\nDeadly Aim: 20\nWrathful Strikes: 50\n…',
    fitness: 'Boundless Vitality: 50\nUndaunted Endurance: 30\nConstitution: 20\n…',
    craft:   'Plentiful Harvest: 50\nGifted Rider: 75\nSpeedy Courier: 20\n…',
  }

  const TREE_COLORS = {
    warfare: 'var(--red)',
    fitness: 'var(--green)',
    craft:   'var(--blue)',
  }

  async function load() {
    try {
      const data = await api.getBuildCP(build.id)
      cp = {
        build_id: build.id,
        warfare: data.warfare || '',
        fitness: data.fitness || '',
        craft:   data.craft   || '',
      }
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function save() {
    saving = true; error = ''; saved = false
    try {
      await api.saveBuildCP(build.id, {
        build_id: build.id,
        warfare: cp.warfare || null,
        fitness: cp.fitness || null,
        craft:   cp.craft   || null,
      })
      saved = true
      setTimeout(() => saved = false, 2500)
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  load()
</script>

<div class="cp-section">
  <p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1rem">
    Record your Champion Point allocations per tree. One ability per line in the format
    <code style="background:var(--surface-2);padding:.1rem .3rem;border-radius:3px">Name: points</code>.
  </p>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if loading}
    <p>Loading…</p>
  {:else}
    <div class="trees">
      {#each [['warfare', 'Warfare ⚔'], ['fitness', 'Fitness 🛡'], ['craft', 'Craft 🔨']] as [key, label]}
        <div class="tree-card card">
          <div class="tree-header" style="color:{TREE_COLORS[key]}">{label}</div>
          <textarea
            bind:value={cp[key]}
            placeholder={PLACEHOLDERS[key]}
            rows="8"
          ></textarea>
        </div>
      {/each}
    </div>

    <div class="flex" style="gap:.5rem;margin-top:1rem;align-items:center">
      <button class="btn-primary" onclick={save} disabled={saving}>
        {saving ? 'Saving…' : 'Save Champion Points'}
      </button>
      {#if saved}
        <span style="color:var(--green);font-size:.875rem">✓ Saved</span>
      {/if}
    </div>
  {/if}
</div>

<style>
  .cp-section { }

  .trees {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: .75rem;
  }

  .tree-card { padding: .75rem; }

  .tree-header {
    font-weight: 700;
    font-size: .9rem;
    margin-bottom: .5rem;
  }

  textarea {
    width: 100%;
    min-height: 160px;
    resize: vertical;
    font-family: 'Courier New', monospace;
    font-size: .8rem;
    line-height: 1.5;
    background: var(--bg);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: .5rem .6rem;
    box-sizing: border-box;
  }
  textarea:focus { outline: none; border-color: var(--gold-dim); }

  @media (max-width: 720px) {
    .trees { grid-template-columns: 1fr; }
  }
</style>
