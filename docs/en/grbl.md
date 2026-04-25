---
layout: public-page
title: "GRBL 1.1 for slider control | Smart Timelapse AI"
description: "Public GRBL 1.1 reference for using Slider-odos3d hardware with Smart Timelapse AI."
permalink: /en/grbl/
lang: en
lang_page: en
alt_url: /grbl/
nav_key: downloads
page_heading: "GRBL 1.1 reference"
page_intro: "Configuration, safety, and technical links for controlling the slider with compatible GRBL firmware."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_en %}

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Firmware</p>
    <h3>Original GRBL project</h3>
    <p>The slider is designed for controllers compatible with GRBL 1.1. This repository does not replace the original project: it only documents settings and references for Slider-odos3d hardware.</p>
    <div class="public-links-list">
      <a href="https://github.com/gnea/grbl">Official GRBL repository</a>
      <a href="{{ site.blob_base }}/grbl/setup.md">GRBL setup</a>
      <a href="{{ site.blob_base }}/grbl/recommended_settings.md">Recommended settings</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">Safety</p>
    <h3>ALARM, unlock, and homing</h3>
    <p>After power-up, GRBL may start in <code>ALARM</code>. Use <code>$H</code> when your build has homing ready. Use <code>$X</code> only when you know the carriage is in a safe position and the travel path is clear.</p>
    <p>Before a long route, test short movements and confirm direction, endstops, and real travel range.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Base settings</p>
    <h3>Common parameters</h3>
    <p>The key values are usually steps/mm, speed, acceleration, and maximum travel. On a 60 cm slider, review especially <code>$100</code>, <code>$110</code>, <code>$120</code>, and <code>$130</code>.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/grbl/presets/slider_60cm_o2.txt">60 cm preset</a>
      <a href="{{ site.blob_base }}/grbl/only_x_homing.md">X-only homing</a>
      <a href="{{ site.blob_base }}/grbl/a4988_vref.md">A4988 Vref adjustment</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">App</p>
    <h3>Communication from Smart Timelapse AI</h3>
    <p>The app communicates with the controller through compatible serial Bluetooth. The expected flow is phone → serial Bluetooth module → GRBL.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/grbl/app_protocol.md">Command protocol</a>
      <a href="{{ routes.support | relative_url }}">Technical support</a>
      <a href="{{ routes.downloads | relative_url }}">Downloads</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>Before using the full travel range</h3>
  <p>Save the base state with <code>$$</code>, check physical limits, confirm the carriage moves in the expected direction, and lower speed/acceleration if steps are lost.</p>
</div>
