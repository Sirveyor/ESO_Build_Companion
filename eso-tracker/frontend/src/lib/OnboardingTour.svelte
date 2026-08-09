<script>
  let { steps, onfinish } = $props()

  let index = $state(0)
  let rect  = $state(null)

  const step   = $derived(steps[index])
  const isLast = $derived(index === steps.length - 1)

  function measure() {
    if (step?.selector) {
      const el = document.querySelector(step.selector)
      rect = el ? el.getBoundingClientRect() : null
    } else {
      rect = null
    }
  }

  $effect(() => {
    step // re-measure whenever the current step changes
    measure()
    const onChange = () => measure()
    window.addEventListener('resize', onChange)
    window.addEventListener('scroll', onChange, true)
    return () => {
      window.removeEventListener('resize', onChange)
      window.removeEventListener('scroll', onChange, true)
    }
  })

  function next() {
    if (isLast) onfinish()
    else index += 1
  }
  function back() {
    if (index > 0) index -= 1
  }

  function onKeydown(e) {
    if (e.key === 'Escape') onfinish()
    else if (e.key === 'Enter' || e.key === 'ArrowRight') next()
    else if (e.key === 'ArrowLeft') back()
  }

  const PAD = 8

  const bubbleStyle = $derived.by(() => {
    if (!rect) return 'top:50%; left:50%; transform:translate(-50%,-50%);'
    const spaceBelow  = window.innerHeight - rect.bottom
    const placeBelow  = spaceBelow > 200
    const top  = placeBelow ? rect.bottom + 16 : Math.max(16, rect.top - 16)
    const left = Math.min(Math.max(16, rect.left), window.innerWidth - 336)
    return `top:${top}px; left:${left}px; ${placeBelow ? '' : 'transform: translateY(-100%);'}`
  })
</script>

<svelte:window onkeydown={onKeydown} />

<div class="tour-overlay"></div>

{#if rect}
  <div class="tour-highlight"
       style="top:{rect.top - PAD}px; left:{rect.left - PAD}px; width:{rect.width + PAD * 2}px; height:{rect.height + PAD * 2}px;">
  </div>
{/if}

<div class="tour-bubble" style={bubbleStyle}>
  <div class="tour-title">{step.title}</div>
  <p class="tour-text">{step.text}</p>
  <div class="tour-footer">
    <div class="tour-dots">
      {#each steps as _, i}
        <span class="dot" class:active={i === index}></span>
      {/each}
    </div>
    <div class="tour-actions">
      <button class="btn-ghost" onclick={onfinish}>Skip</button>
      {#if index > 0}
        <button class="btn-secondary" onclick={back}>Back</button>
      {/if}
      <button class="btn-primary" onclick={next}>{isLast ? 'Done' : 'Next'}</button>
    </div>
  </div>
</div>

<style>
  .tour-overlay {
    position: fixed;
    inset: 0;
    background: rgba(4, 4, 10, .72);
    z-index: 1000;
  }

  .tour-highlight {
    position: fixed;
    border: 2px solid var(--gold);
    border-radius: 8px;
    box-shadow: 0 0 0 4px rgba(201, 168, 76, .25), 0 0 24px rgba(201, 168, 76, .35);
    z-index: 1001;
    pointer-events: none;
    transition: top .2s, left .2s, width .2s, height .2s;
  }

  .tour-bubble {
    position: fixed;
    z-index: 1002;
    width: 320px;
    background: var(--surface);
    border: 1px solid var(--gold-dim);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    padding: 1rem;
  }

  .tour-title { color: var(--gold); font-weight: 700; margin-bottom: .4rem; }
  .tour-text  { color: var(--text); font-size: .875rem; margin-bottom: .9rem; }

  .tour-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: .5rem;
  }

  .tour-dots { display: flex; gap: .3rem; }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--border); }
  .dot.active { background: var(--gold); }

  .tour-actions { display: flex; gap: .4rem; }
</style>
