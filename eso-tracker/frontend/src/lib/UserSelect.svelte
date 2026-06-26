<script>
  import { api } from '../api.js'

  let { onselect } = $props()

  let users    = $state([])
  let loading  = $state(true)
  let error    = $state('')
  let showForm = $state(false)
  let saving   = $state(false)

  let form = $state({ name: '', display_name: '' })

  async function load() {
    try {
      users = await api.getUsers()
    } catch (e) {
      error = e.message
    } finally {
      loading = false
    }
  }

  async function createUser() {
    if (!form.name.trim()) return
    saving = true
    try {
      const u = await api.createUser({
        id: crypto.randomUUID(),
        name: form.name.trim(),
        display_name: form.display_name.trim() || null,
        created_at: new Date().toISOString(),
      })
      users = [...users, u]
      form = { name: '', display_name: '' }
      showForm = false
    } catch (e) {
      error = e.message
    } finally {
      saving = false
    }
  }

  async function deleteUser(id) {
    if (!confirm('Remove this profile? Characters will be unlinked but not deleted.')) return
    try {
      await api.deleteUser(id)
      users = users.filter(u => u.id !== id)
    } catch (e) {
      error = e.message
    }
  }

  load()
</script>

<div class="page">
  <div class="flex-between" style="margin-bottom:1.5rem">
    <h1>Select Your Profile</h1>
    <button class="btn-secondary" onclick={() => { showForm = !showForm; error = '' }}>
      {showForm ? 'Cancel' : '+ New Profile'}
    </button>
  </div>

  {#if error}
    <div class="notice notice-error">{error}</div>
  {/if}

  {#if showForm}
    <div class="inline-form" style="margin-bottom:1.5rem">
      <h3 style="margin-bottom:.75rem">New Profile</h3>
      <div class="form-grid">
        <div class="form-row">
          <label>Username *</label>
          <input bind:value={form.name} placeholder="e.g. Covert" onkeydown={(e) => e.key === 'Enter' && createUser()} />
        </div>
        <div class="form-row">
          <label>Display Name</label>
          <input bind:value={form.display_name} placeholder="e.g. Covert the Mighty" />
        </div>
      </div>
      <button class="btn-primary" onclick={createUser} disabled={saving || !form.name.trim()}>
        {saving ? 'Creating…' : 'Create Profile'}
      </button>
    </div>
  {/if}

  {#if loading}
    <p>Loading profiles…</p>
  {:else if users.length === 0}
    <div class="empty">
      <div class="empty-icon">⚔</div>
      <h2>No profiles yet</h2>
      <p>Create your first profile to start tracking builds.</p>
    </div>
  {:else}
    <div class="grid-2">
      {#each users as u (u.id)}
        <div class="card card-clickable user-card" onclick={() => onselect(u)}>
          <div class="avatar">{(u.display_name || u.name).charAt(0).toUpperCase()}</div>
          <div class="user-info">
            <div class="uname">{u.display_name || u.name}</div>
            {#if u.display_name}
              <div class="uhandle">@{u.name}</div>
            {/if}
          </div>
          <button class="btn-icon delete-btn"
                  onclick={(e) => { e.stopPropagation(); deleteUser(u.id) }}
                  title="Remove profile">✕</button>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .user-card {
    display: flex;
    align-items: center;
    gap: 1rem;
    position: relative;
  }

  .avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: var(--gold-dim);
    color: var(--gold);
    font-size: 1.5rem;
    font-weight: 700;
    display: grid;
    place-items: center;
    flex-shrink: 0;
    border: 2px solid var(--gold-dim);
  }

  .uname   { font-weight: 600; font-size: 1.05rem; }
  .uhandle { font-size: .8rem; color: var(--text-dim); }

  .delete-btn {
    margin-left: auto;
    opacity: 0;
    transition: opacity .15s;
  }
  .user-card:hover .delete-btn { opacity: 1; }
</style>
