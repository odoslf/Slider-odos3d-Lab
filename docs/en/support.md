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
    <p>Enable Bluetooth, grant the permissions requested by Android, and start scanning from the app. On Android 12 or newer, Nearby devices permission may appear. Some phones may also require location permission to discover classic Bluetooth devices.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Bluetooth / GRBL</p>
    <h3>Slider not visible or not connecting</h3>
    <p>Check that the Bluetooth module is powered, paired with the phone, and not already connected to another device. The expected flow is phone → serial Bluetooth → GRBL controller. If it shows as connected but does not respond, restart the controller and reconnect from the app.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">ALARM / homing</p>
    <h3>GRBL ALARM, unlock, and homing</h3>
    <p>After power-up, GRBL may start in ALARM until homing or unlock is performed. Use <code>$H</code> when your build has homing ready. Use <code>$X</code> only when you know the carriage is in a safe position. Check endstops, travel range, and movement direction before running a route.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Export</p>
    <h3>Slow, black, or failed export</h3>
    <p>Free storage, avoid battery saver, keep the app open during long processes, and try a lower resolution if the project has many photos. If the video is black or photos do not appear, check photo/video permissions and confirm the project contains valid images.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">DSLR / relay</p>
    <h3>DSLR trigger with relay</h3>
    <p>DSLR triggering depends on wiring, relay behavior, and the remote connector of each camera. Test short pulses first without moving the slider. Do not connect unknown voltages to the camera. If the camera does not trigger, check polarity, common ground, and remote mode.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Local remote / Wi-Fi</p>
    <h3>Local remote panel</h3>
    <p>For local remote control, the phone and control device must be on the same network. Disable VPN, AP isolation, or guest networks if the panel does not open. Local remote control does not replace a physical travel and safety test.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">What to send</p>
    <h3>What to send to support</h3>
    <p>Send phone model, Android version, app version, mode used, whether you use a physical slider or phone-only flow, screenshot of the error, and exact reproduction steps.</p>
    <div class="public-links-list"><a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a></div>
  </article>
</div>

<div class="public-cta-band">
  <h3>Quick support links</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Downloads</a>
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.gallery | relative_url }}">Technical gallery</a>
    <a class="public-btn" href="{{ routes.privacy | relative_url }}">Privacy</a>
    <a class="public-btn" href="{{ routes.terms | relative_url }}">Terms</a>
  </div>
</div>
