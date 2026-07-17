<script>
  import { api } from '../api.js'

  let { page, curUser, curChar, curBuild, navigate } = $props()

  let version = $state('')
  $effect(() => {
    api.getVersion().then(d => version = d.version).catch(() => {})
  })

  let crumbs = $derived.by(() => {
    if (page === 'home')       return []
    if (page === 'characters') return [{ label: curUser?.display_name || curUser?.name }]
    if (page === 'character')  return [
      { label: curUser?.display_name || curUser?.name, page: 'characters' },
      { label: curChar?.name },
    ]
    if (page === 'build')      return [
      { label: curUser?.display_name || curUser?.name, page: 'characters' },
      { label: curChar?.name, page: 'character' },
      { label: curBuild?.name },
    ]
    return []
  })
</script>

<header>
  <div class="brand" role="button" tabindex="0"
       onclick={() => navigate('home')}
       onkeydown={(e) => e.key === 'Enter' && navigate('home')}>
    ⚔ ESO Build Companion
    {#if version}<span class="version">v{version}</span>{/if}
  </div>

  {#if curUser}
    <nav>
      <button class:active={page === 'characters' || page === 'character' || page === 'build'}
              onclick={() => navigate('characters')}>
        Characters
      </button>
      <button class:active={page === 'gear-sets'}
              onclick={() => navigate('gear-sets')}>
        Gear Sets
      </button>
      <button class:active={page === 'compare'}
              onclick={() => navigate('compare')}>
        Compare
      </button>
      <button class:active={page === 'scraper'}
              onclick={() => navigate('scraper')}>
        Import
      </button>
      <button class:active={page === 'reference'}
              onclick={() => navigate('reference')}>
        Reference
      </button>
    </nav>

    <div class="user-chip">
      <span class="user-name">{curUser.display_name || curUser.name}</span>
      <button class="btn-ghost switch" onclick={() => navigate('home')}>Switch</button>
    </div>
  {/if}
</header>

{#if crumbs.length > 0}
  <div class="breadcrumb">
    <span role="button" tabindex="0" class="crumb-home"
          onclick={() => navigate('home')}
          onkeydown={(e) => e.key === 'Enter' && navigate('home')}>Home</span>
    {#each crumbs as c, i}
      <span class="sep">›</span>
      {#if c.page && i < crumbs.length - 1}
        <span role="button" tabindex="0" class="crumb-link"
              onclick={() => navigate(c.page)}
              onkeydown={(e) => e.key === 'Enter' && navigate(c.page)}>
          {c.label}
        </span>
      {:else}
        <span class="crumb-current">{c.label}</span>
      {/if}
    {/each}
  </div>
{/if}

<style>
  header {
    display: flex;
    align-items: center;
    gap: 1.5rem;
    padding: .75rem 2rem;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 10;
  }

  .brand {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--gold);
    cursor: pointer;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .brand:hover { opacity: .8; }
  .version { font-size: .65rem; font-weight: 400; color: var(--text-dim); margin-left: .35rem; vertical-align: middle; }

  nav { display: flex; gap: .25rem; flex: 1; }

  nav button {
    background: transparent;
    color: var(--text-dim);
    padding: .35rem .85rem;
    border-radius: var(--radius);
  }
  nav button:hover { color: var(--text); background: var(--surface-2); }
  nav button.active { color: var(--gold); background: var(--surface-2); }

  .user-chip { display: flex; align-items: center; gap: .5rem; flex-shrink: 0; }
  .user-name { font-size: .875rem; color: var(--text); }
  .switch { font-size: .8rem; color: var(--text-dim); }

  .breadcrumb {
    display: flex;
    align-items: center;
    gap: .4rem;
    padding: .4rem 2rem;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    font-size: .8rem;
  }
  .crumb-home, .crumb-link {
    color: var(--text-dim);
    cursor: pointer;
  }
  .crumb-home:hover, .crumb-link:hover { color: var(--gold); }
  .crumb-current { color: var(--text); }
  .sep { color: var(--border); }

  @media (max-width: 640px) {
    header { padding: .6rem 1rem; gap: .75rem; }
    .brand { font-size: .9rem; }
    nav button { padding: .3rem .55rem; font-size: .8rem; }
    .breadcrumb { padding: .4rem 1rem; }
  }
</style>
