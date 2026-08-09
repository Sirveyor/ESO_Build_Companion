<script>
  import Nav           from './lib/Nav.svelte'
  import UserSelect    from './lib/UserSelect.svelte'
  import OnboardingTour from './lib/OnboardingTour.svelte'
  import CharacterList from './lib/CharacterList.svelte'
  import BuildList     from './lib/BuildList.svelte'
  import GearChecklist from './lib/GearChecklist.svelte'
  import GearSetBrowser from './lib/GearSetBrowser.svelte'
  import SetComparison  from './lib/SetComparison.svelte'
  import ReferenceLibrary from './lib/ReferenceLibrary.svelte'
  import RecipeTracker    from './lib/RecipeTracker.svelte'
  import MotifTracker     from './lib/MotifTracker.svelte'
  import FragmentTracker  from './lib/FragmentTracker.svelte'

  // ── Router state ─────────────────────────────────────────────────────────
  // page: 'home' | 'characters' | 'character' | 'build' | 'gear-sets' | 'compare' | 'reference' | 'recipes' | 'motifs' | 'fragments'
  let page      = $state('home')
  let curUser   = $state(null)
  let curChar   = $state(null)
  let curBuild  = $state(null)
  let showTour  = $state(false)

  function navigate(to, ctx = {}) {
    page = to
    if ('user'      in ctx) curUser  = ctx.user
    if ('character' in ctx) curChar  = ctx.character
    if ('build'     in ctx) curBuild = ctx.build
  }

  function selectUser(u) {
    navigate('characters', { user: u })
    if (!localStorage.getItem(`eso_tour_seen:${u.id}`)) showTour = true
  }

  function finishTour() {
    if (curUser) localStorage.setItem(`eso_tour_seen:${curUser.id}`, '1')
    showTour = false
  }

  const tourSteps = $derived([
    {
      title: `Welcome, ${curUser?.display_name || curUser?.name || 'adventurer'}!`,
      text: 'A quick look around — takes about 30 seconds.',
    },
    {
      selector: '[data-tour="nav-characters"]',
      title: 'Characters',
      text: 'Your characters live here. Pick one to manage its builds and gear.',
    },
    {
      selector: '[data-tour="nav-gear-sets"]',
      title: 'Gear Sets',
      text: 'Browse every ESO gear set and its bonuses.',
    },
    {
      selector: '[data-tour="nav-compare"]',
      title: 'Compare',
      text: 'Put two sets side by side to decide which fits your build.',
    },
    {
      selector: '[data-tour="nav-reference"]',
      title: 'Reference',
      text: 'A quick-lookup library for traits, motifs, and more.',
    },
    {
      selector: '[data-tour="user-chip"]',
      title: 'Switching profiles',
      text: 'Come back here anytime to switch to the other profile.',
    },
    {
      title: "That's it!",
      text: 'Have fun gearing up.',
    },
  ])
</script>

<div class="app-watermark" aria-hidden="true">
  <svg viewBox="0 0 400 400">
    <g fill="none" stroke="#c9a84c" stroke-linecap="round">
      <circle cx="200" cy="200" r="178" stroke="#7a6530" stroke-width="1.5"/>
      <circle cx="200" cy="200" r="132" stroke-width="2"/>
      <g stroke-width="2">
        <line x1="364.0" y1="200.0" x2="378.0" y2="200.0" />
        <line x1="358.4" y1="242.4" x2="371.9" y2="246.1" />
        <line x1="342.0" y1="282.0" x2="354.2" y2="289.0" />
        <line x1="316.0" y1="316.0" x2="325.9" y2="325.9" />
        <line x1="282.0" y1="342.0" x2="289.0" y2="354.2" />
        <line x1="242.4" y1="358.4" x2="246.1" y2="371.9" />
        <line x1="200.0" y1="364.0" x2="200.0" y2="378.0" />
        <line x1="157.6" y1="358.4" x2="153.9" y2="371.9" />
        <line x1="118.0" y1="342.0" x2="111.0" y2="354.2" />
        <line x1="84.0" y1="316.0" x2="74.1" y2="325.9" />
        <line x1="58.0" y1="282.0" x2="45.8" y2="289.0" />
        <line x1="41.6" y1="242.4" x2="28.1" y2="246.1" />
        <line x1="36.0" y1="200.0" x2="22.0" y2="200.0" />
        <line x1="41.6" y1="157.6" x2="28.1" y2="153.9" />
        <line x1="58.0" y1="118.0" x2="45.8" y2="111.0" />
        <line x1="84.0" y1="84.0" x2="74.1" y2="74.1" />
        <line x1="118.0" y1="58.0" x2="111.0" y2="45.8" />
        <line x1="157.6" y1="41.6" x2="153.9" y2="28.1" />
        <line x1="200.0" y1="36.0" x2="200.0" y2="22.0" />
        <line x1="242.4" y1="41.6" x2="246.1" y2="28.1" />
        <line x1="282.0" y1="58.0" x2="289.0" y2="45.8" />
        <line x1="316.0" y1="84.0" x2="325.9" y2="74.1" />
        <line x1="342.0" y1="118.0" x2="354.2" y2="111.0" />
        <line x1="358.4" y1="157.6" x2="371.9" y2="153.9" />
      </g>
      <g stroke="#7a6530" stroke-width="1.5">
        <line x1="288.7" y1="236.7" x2="346.0" y2="260.5" />
        <line x1="236.7" y1="288.7" x2="260.5" y2="346.0" />
        <line x1="163.3" y1="288.7" x2="139.5" y2="346.0" />
        <line x1="111.3" y1="236.7" x2="54.0" y2="260.5" />
        <line x1="111.3" y1="163.3" x2="54.0" y2="139.5" />
        <line x1="163.3" y1="111.3" x2="139.5" y2="54.0" />
        <line x1="236.7" y1="111.3" x2="260.5" y2="54.0" />
        <line x1="288.7" y1="163.3" x2="346.0" y2="139.5" />
      </g>
    </g>
    <g fill="#c9a84c">
      <polygon points="332.0,194.0 338.0,200.0 332.0,206.0 326.0,200.0" />
      <polygon points="293.3,287.3 299.3,293.3 293.3,299.3 287.3,293.3" />
      <polygon points="200.0,326.0 206.0,332.0 200.0,338.0 194.0,332.0" />
      <polygon points="106.7,287.3 112.7,293.3 106.7,299.3 100.7,293.3" />
      <polygon points="68.0,194.0 74.0,200.0 68.0,206.0 62.0,200.0" />
      <polygon points="106.7,100.7 112.7,106.7 106.7,112.7 100.7,106.7" />
      <polygon points="200.0,62.0 206.0,68.0 200.0,74.0 194.0,68.0" />
      <polygon points="293.3,100.7 299.3,106.7 293.3,112.7 287.3,106.7" />
    </g>
    <g transform="translate(200,200) scale(3) translate(-24,-24)">
      <polygon points="9,25 20,22.5 20,29.5" fill="#c9a84c"/>
      <rect x="18" y="21" width="19" height="8" rx="1.5" fill="#c9a84c"/>
      <rect x="23.5" y="29" width="8" height="5" fill="#c9a84c"/>
      <rect x="17" y="34" width="20" height="5" rx="1.5" fill="#c9a84c"/>
      <rect x="14" y="39" width="26" height="3" rx="1" fill="#7a6530"/>
      <g transform="translate(48,0) scale(-1,1) translate(30 20) rotate(35)">
        <rect x="-1.6" y="-24" width="3.2" height="17" rx="1" fill="#8a6a3f"/>
        <rect x="-6.5" y="-7" width="13" height="7" rx="1.5" fill="#c9a84c" stroke="#7a6530" stroke-width="0.6"/>
      </g>
    </g>
  </svg>
</div>

<Nav {page} {curUser} {curChar} {curBuild} {navigate} />

<main>
  {#if page === 'home'}
    <UserSelect
      onselect={selectUser}
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

  {:else if page === 'reference'}
    <ReferenceLibrary />

  {:else if page === 'recipes'}
    <RecipeTracker character={curChar} />

  {:else if page === 'motifs'}
    <MotifTracker character={curChar} />

  {:else if page === 'fragments'}
    <FragmentTracker character={curChar} />
  {/if}
</main>

{#if showTour}
  <OnboardingTour steps={tourSteps} onfinish={finishTour} />
{/if}

<style>
  main { flex: 1; position: relative; z-index: 1; }

  .app-watermark {
    position: fixed;
    inset: 0;
    z-index: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: .08;
    pointer-events: none;
  }
  .app-watermark svg { width: 480px; height: 480px; max-width: 70vw; max-height: 70vw; }
</style>
