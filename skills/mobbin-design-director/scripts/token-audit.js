// Token audit: counts the unique rendered style values on the current page.
// Pass the whole function to the browser devtools MCP `evaluate_script`
// (e.g. chrome-devtools `evaluate_script` with `function` = this file's text).
// Never copy it into the project. It only counts; comparing the values with
// the project's tokens is the agent's job.
() => {
  const props = {
    color: 'color',
    background: 'backgroundColor',
    border: 'borderTopColor',
    radius: 'borderTopLeftRadius',
    fontSize: 'fontSize',
    fontFamily: 'fontFamily',
    fontWeight: 'fontWeight',
    letterSpacing: 'letterSpacing',
    shadow: 'boxShadow',
    backgroundImage: 'backgroundImage',
  };
  const skip = new Set(['', 'none', 'normal', '0px', 'rgba(0, 0, 0, 0)', 'transparent']);
  const counts = Object.fromEntries(Object.keys(props).map((k) => [k, {}]));
  let visible = 0;
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width * r.height < 4) continue; // invisible or zero-size
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    visible++;
    const hasText = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    for (const [key, prop] of Object.entries(props)) {
      // Text properties only matter where there is text; borders only where drawn.
      if (['color', 'fontSize', 'fontFamily', 'fontWeight', 'letterSpacing'].includes(key) && !hasText) continue;
      if (key === 'border' && cs.borderTopStyle === 'none') continue;
      if (key === 'backgroundImage' && !/gradient/.test(cs.backgroundImage)) continue;
      const v = cs[prop];
      if (skip.has(v)) continue;
      counts[key][v] = (counts[key][v] || 0) + 1;
    }
  }
  const sorted = Object.fromEntries(
    Object.entries(counts).map(([k, m]) => [k, Object.entries(m).sort((a, b) => b[1] - a[1])]),
  );
  const distinct = Object.fromEntries(Object.entries(sorted).map(([k, l]) => [k, l.length]));
  return { url: location.href, viewport: `${innerWidth}x${innerHeight}`, visibleElements: visible, distinct, values: sorted };
}
