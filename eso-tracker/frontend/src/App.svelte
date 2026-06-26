<script>
  import Nav           from './lib/Nav.svelte'
  import UserSelect    from './lib/UserSelect.svelte'
  import CharacterList from './lib/CharacterList.svelte'
  import BuildList     from './lib/BuildList.svelte'
  import GearChecklist from './lib/GearChecklist.svelte'
  import GearSetBrowser from './lib/GearSetBrowser.svelte'
  import SetComparison  from './lib/SetComparison.svelte'
  import Scraper        from './lib/Scraper.svelte'

  // ── Router state ─────────────────────────────────────────────────────────
  // page: 'home' | 'characters' | 'character' | 'build' | 'gear-sets' | 'compare' | 'scraper'
  let page      = $state('home')
  let curUser   = $state(null)
  let curChar   = $state(null)
  let curBuild  = $state(null)

  function navigate(to, ctx = {}) {
    page = to
    if ('user'      in ctx) curUser  = ctx.user
    if ('character' in ctx) curChar  = ctx.character
    if ('build'     in ctx) curBuild = ctx.build
  }
</script>

<Nav {page} {curUser} {curChar} {curBuild} {navigate} />

<main>
  {#if page === 'home'}
    <UserSelect
      onselect={(u) => navigate('characters', { user: u })}
    />

  {:else if page === 'characters'}
    <CharacterList
      user={curUser}
      onselect={(c) => navigate('character', { character: c })}
      onback={() => navigate('home')}
    />

  {:else if page === 'character'}
    <BuildList
      character={curChar}
      onselect={(b) => navigate('build', { build: b })}
      onback={() => navigate('characters')}
    />

  {:else if page === 'build'}
    <GearChecklist
      build={curBuild}
      character={curChar}
      onback={() => navigate('character')}
    />

  {:else if page === 'gear-sets'}
    <GearSetBrowser />

  {:else if page === 'compare'}
    <SetComparison />

  {:else if page === 'scraper'}
    <Scraper />
  {/if}
</main>

<style>
  main { flex: 1; }
</style>
