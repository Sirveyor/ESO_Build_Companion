<script>
  import { api } from '../api.js'

  let query       = $state('')
  let results     = $state([])
  let searching   = $state(false)
  let preview     = $state(null)   // parsed set data to review
  let importing   = $state(false)
  let importedSet = $state(null)   // successfully imported GearSetSchema
  let error       = $state('')
  let searchError = $state('')

  async function search() {
    if (!query.trim() || query.trim().length < 2) return
    searching = true; searchError = ''; results = []; preview = null; importedSet = null
    try {
      results = await api.scraperSearch(query.trim())
      if (results.length === 0) searchError = 'No ESO set pages found for that query.'
    } catch (e) {
      searchError = e.message
    } finally {
      searching = false
    }
  }

  async function loadPreview(url) {
    error = ''; preview = null; importedSet = null
    try {
      preview = await api.scraperPreview(url)
      preview._url = url
    } catch (e) {
      error = e.message
    }
  }

  async function doImport(overwrite = false) {
    if (!preview) return
    importing = true; error = ''
    try {
      importedSet = await api.scraperImport(preview._url, overwrite)
      preview = null
    } catch (e) {
      if (e.message?.includes('409') || e.message?.includes('already exists')) {
        error = `"${preview.name}" is already in the database. Import again to overwrite it.`
        preview._overwrite = true
      } else {
        error = e.message
      }
    } finally {
      importing = false
    }
  }

  function clearAll() {
    query = ''; results = []; preview = null; importedSet = null; error = ''; searchError = ''
  }
</script>

<div class="page">
  <h1 style="margin-bottom:.25rem">Import from UESP</h1>
  <p style="margin-bottom:1.25rem;color:var(--text-dim)">
    Search the Unofficial Elder Scrolls Pages wiki to import gear set data into your database.
  </p>

  <!-- Search bar -->
  <div class="search-row">
    <input
      class="search-input"
      bind:value={query}
      placeholder="Search for a set… e.g. Mother's Sorrow, Oakensoul"
      onkeydown={(e) => e.key === 'Enter' && search()}
    />
    <button class="btn-primary" onclick={search} disabled={searching || query.trim().length < 2}>
      {searching ? 'Searching…' : 'Search'}
    </button>
    {#if results.length || preview || importedSet}
      <button class="btn-ghost" onclick={clearAll}>Clear</button>
    {/if}
  </div>

  {#if searchError}
    <div class="notice notice-info" style="margin-top:.75rem">{searchError}</div>
  {/if}

  <!-- Search results -->
  {#if results.length > 0 && !preview && !importedSet}
    <div class="results-list">
      {#each results as r}
        <button class="card result-row" onclick={() => loadPreview(r.url)}>
          <div class="result-name">{r.name}</div>
          {#if r.snippet}
            <div class="result-snippet">{r.snippet}</div>
          {/if}
          <div class="result-url">{r.url}</div>
        </button>
      {/each}
    </div>
  {/if}

  {#if error}
    <div class="notice notice-error" style="margin-top:.75rem">
      {error}
      {#if preview?._overwrite}
        <button class="btn-danger" style="margin-top:.5rem;width:100%" onclick={() => doImport(true)}>
          Overwrite existing set
        </button>
      {/if}
    </div>
  {/if}

  <!-- Preview panel -->
  {#if preview}
    <div class="card preview-card">
      <h2 style="margin-bottom:.5rem">{preview.name || '(unknown name)'}</h2>

      <div class="preview-meta flex" style="flex-wrap:wrap;gap:.4rem;margin-bottom:1rem">
        {#if preview.set_type}
          <span class="badge badge-blue">{preview.set_type}</span>
        {/if}
        {#if preview.location}
          <span class="badge">{preview.location}</span>
        {/if}
        {#if preview.num_pieces}
          <span class="badge">{preview.num_pieces}-piece set</span>
        {/if}
      </div>

      {#if preview.bonuses?.length}
        <h3 style="margin-bottom:.5rem">Set Bonuses</h3>
        <div class="bonus-preview">
          {#each preview.bonuses as b}
            <div class="bonus-row">
              <span class="piece-badge badge badge-gold">{b.pieces_required} pc</span>
              <span class="bonus-text">{b.bonus_description}</span>
            </div>
          {/each}
        </div>
      {:else}
        <div class="notice notice-info">No bonuses found on this page.</div>
      {/if}

      <div class="preview-source" style="margin-top:.75rem">
        Source: <a href={preview._url} target="_blank" rel="noreferrer">{preview._url}</a>
      </div>

      <div class="flex" style="gap:.5rem;margin-top:1rem">
        <button class="btn-primary" onclick={() => doImport(false)} disabled={importing}>
          {importing ? 'Importing…' : 'Import into Database'}
        </button>
        <button class="btn-ghost" onclick={() => { preview = null }}>Cancel</button>
      </div>
    </div>
  {/if}

  <!-- Success state -->
  {#if importedSet}
    <div class="card success-card">
      <div class="success-icon">✓</div>
      <h2>Imported: {importedSet.name}</h2>
      <div class="flex" style="flex-wrap:wrap;gap:.4rem;margin:.5rem 0 1rem">
        {#if importedSet.set_type}
          <span class="badge badge-blue">{importedSet.set_type}</span>
        {/if}
        {#if importedSet.location}
          <span class="badge">{importedSet.location}</span>
        {/if}
        <span class="badge badge-green">{importedSet.bonuses?.length || 0} bonuses saved</span>
      </div>
      <p style="color:var(--text-dim);font-size:.9rem">
        The set is now in your Gear Sets database and available for comparison.
      </p>
      <div class="flex" style="gap:.5rem;margin-top:.75rem">
        <button class="btn-primary" onclick={() => { importedSet = null; query = '' }}>
          Import Another
        </button>
      </div>
    </div>
  {/if}
</div>

<style>
  .search-row {
    display: flex;
    gap: .5rem;
    align-items: center;
    flex-wrap: wrap;
  }

  .search-input {
    flex: 1;
    min-width: 220px;
  }

  .results-list {
    display: flex;
    flex-direction: column;
    gap: .4rem;
    margin-top: .75rem;
  }

  .result-row {
    text-align: left;
    cursor: pointer;
    padding: .65rem .875rem;
    transition: border-color .15s;
  }
  .result-row:hover { border-color: var(--gold-dim); }

  .result-name   { font-weight: 600; margin-bottom: .2rem; }
  .result-snippet { font-size: .82rem; color: var(--text-dim); margin-bottom: .2rem; }
  .result-url    { font-size: .75rem; color: var(--blue); word-break: break-all; }

  .preview-card { margin-top: .75rem; }
  .preview-source { font-size: .78rem; color: var(--text-dim); }
  .preview-source a { color: var(--blue); }

  .bonus-preview { display: flex; flex-direction: column; gap: .35rem; }
  .bonus-row     { display: flex; align-items: center; gap: .5rem; flex-wrap: wrap;
                   padding: .3rem .5rem; background: var(--bg); border-radius: var(--radius); }
  .piece-badge   { font-weight: 700; flex-shrink: 0; }
  .bonus-text    { font-size: .9rem; }

  .success-card { margin-top: .75rem; text-align: center; padding: 2rem 1.5rem; }
  .success-icon { font-size: 2.5rem; color: var(--green); margin-bottom: .5rem; }
</style>
