/**
 * unlock.js — client-side module gating by date.
 *
 * Drop a hidden <script type="application/json" id="unlock-config"> into a page:
 *   {"unlock": "2026-07-07T06:00:00-07:00", "label": "Track A · Week 4"}
 *
 * If the current date < unlock, the page's main content is hidden and
 * a friendly "comes back later" banner is shown. Add `?preview=1` to
 * the URL to bypass the gate (instructor preview).
 */
(function () {
  function $(sel, root = document) { return root.querySelector(sel); }
  function pad(n) { return String(n).padStart(2, "0"); }
  function fmt(d) {
    return d.toLocaleDateString(undefined, {
      weekday: "short", year: "numeric", month: "short", day: "numeric"
    }) + " " + pad(d.getHours()) + ":" + pad(d.getMinutes()) + " local";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var cfgEl = $("#unlock-config");
    if (!cfgEl) return;
    var cfg;
    try { cfg = JSON.parse(cfgEl.textContent); } catch (e) { return; }
    if (!cfg.unlock) return;

    var unlock = new Date(cfg.unlock);
    var now = new Date();
    var preview = new URLSearchParams(window.location.search).has("preview");
    if (now >= unlock || preview) return; // unlocked

    var content = $(".md-content__inner") || $("main");
    if (!content) return;

    var banner = document.createElement("div");
    banner.className = "module-locked";
    banner.innerHTML =
      "<strong>🔒 Module locked.</strong> " +
      (cfg.label ? cfg.label + " " : "") +
      "unlocks on <strong>" + fmt(unlock) + "</strong>." +
      "<br><em>Instructor preview:</em> append <code>?preview=1</code> to the URL.";
    var firstChild = content.firstElementChild;
    if (firstChild) content.insertBefore(banner, firstChild);

    // Hide all article content (h1 stays via banner above)
    Array.from(content.children).forEach(function (el) {
      if (el !== banner && el.tagName !== "H1") el.style.display = "none";
    });
  });
})();
