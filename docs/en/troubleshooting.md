---
layout: public-page
title: "Troubleshooting | Smart Timelapse AI Slider"
description: "Public guide for solving mechanical, Bluetooth, GRBL, export, and basic slider issues."
permalink: /en/troubleshooting/
lang: en
lang_page: en
alt_url: /troubleshooting/
nav_key: support
page_heading: "Troubleshooting"
page_intro: "Quick checklist for common issues before contacting support."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign routes = links.internal_routes_en %}

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Mechanical</p>
    <h3>Friction, jams, or play</h3>
    <p>Check rod alignment, belt tension, parallelism, screws, and printed part orientation. The carriage should move smoothly across the full travel before motors are connected.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Motion</p>
    <h3>Lost steps or vibration</h3>
    <p>Lower speed and acceleration, adjust driver current, check pulley/shaft fit, and confirm the belt is not too tight. Test short travel first.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Bluetooth</p>
    <h3>Not connecting or not responding</h3>
    <p>Check Bluetooth module power, phone pairing, compatible serial speed, and whether it is already connected to another device. Restart the controller and connection if the app shows connected but receives no response.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">GRBL</p>
    <h3>ALARM or unsafe travel</h3>
    <p>If GRBL is in <code>ALARM</code>, use <code>$H</code> when homing is ready. Use <code>$X</code> only with the carriage in a safe position. Check physical limits before long routes.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Export</p>
    <h3>Black, slow, or failed video</h3>
    <p>Free storage, check photo/video permissions, confirm the project contains valid images, and try a lower resolution when the project has many photos.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Support</p>
    <h3>Minimum details to send</h3>
    <p>Send phone model, Android version, app version, mode used, whether you use a physical slider or phone-only flow, screenshot of the error, and exact steps.</p>
    <div class="public-links-list">
      <a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a>
      <a href="{{ routes.support | relative_url }}">Support center</a>
      <a href="{{ routes.downloads | relative_url }}">Downloads</a>
    </div>
  </article>
</div>
