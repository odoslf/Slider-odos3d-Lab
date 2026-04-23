---
layout: public-page
title: "Technical support | Smart Timelapse AI"
description: "Official Smart Timelapse AI support center for Bluetooth, GRBL, export, local remote panel, DSLR workflow, and technical contact."
permalink: /en/support/
lang: en
lang_page: en
alt_url: /support/
og_title: "Smart Timelapse AI support"
og_description: "Quick support guidance and technical contact for mobile, GRBL slider, and DSLR workflows."
nav_key: support
page_heading: "Help center"
page_intro: "Support guidance to start quickly, solve issues, and keep workflow stable."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign external = links.external_links %}
{% assign routes = links.internal_routes_en %}


<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">First steps</p>
    <h3>Initial connection and permissions</h3>
    <p>Enable Bluetooth and location, check Nearby Bluetooth permissions on Android 12/13, and confirm slider visibility during scan.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">GRBL slider workflow</p>
    <h3>ALARM state and stability</h3>
    <p>If GRBL enters ALARM, send <code>$X</code> and verify limits/homing. For Wi‑Fi remote, validate shared network and no AP isolation or VPN.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Export and formats</p>
    <h3>Output performance</h3>
    <p>If export is slow or fails, free storage, disable battery saver for the app, and lower resolution for long projects.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Support and contact</p>
    <h3>What to send</h3>
    <p>Send screenshot + copied diagnostics for faster support handling.</p>
    <div class="public-links-list"><a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a></div>
  </article>
</div>

<div class="public-cta-band">
  <h3>Quick support links</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">View downloads</a>
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">View hardware</a>
    <a class="public-btn" href="{{ routes.gallery | relative_url }}">Technical gallery</a>
    <a class="public-btn" href="{{ routes.privacy | relative_url }}">Privacy</a>
    <a class="public-btn" href="{{ routes.terms | relative_url }}">Terms</a>
  </div>
</div>
