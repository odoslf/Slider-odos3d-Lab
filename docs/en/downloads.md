---
layout: public-page
title: "Hardware downloads | Smart Timelapse AI"
description: "Download public STL, STEP, and BOM packages for Slider-odos3d hardware with versioned release workflow and technical resources."
permalink: /en/downloads/
lang: en
lang_page: en
alt_url: /downloads/
og_title: "STL/STEP/BOM downloads | Smart Timelapse AI"
og_description: "Public downloads hub with files, guides, and references for Slider-odos3d hardware."
nav_key: downloads
page_heading: "Downloads and resources hub"
page_intro: "Resource center for hardware files, documentation, and references in the Smart Timelapse AI Slider ecosystem."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign external = links.external_links %}
{% assign routes = links.internal_routes_en %}


<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include public-media-item.html media_key='hero' lang='en' loading='lazy' show_caption='false' %}</article>
  <article class="public-media-card">{% include public-media-item.html media_key='app_screenshot' lang='en' loading='lazy' show_caption='true' %}</article>
</div>
<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Hardware parts and files</p>
    <h3>Versioned STL, STEP, and BOM</h3>
    <p>Public hardware packages for printing, adaptation, and assembly.</p>
    <div class="public-links-list">
      <a href="{{ external.github_tree_main }}/prints/STL/{{ site.latest_pack }}/">STL {{ site.latest_pack }}</a>
      <a href="{{ external.github_tree_main }}/prints/STEP/{{ site.latest_pack }}/">STEP {{ site.latest_pack }}</a>
      <a href="{{ external.github_tree_main }}/prints/BOM/{{ site.latest_pack }}/">BOM {{ site.latest_pack }}</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">Guides and documentation</p>
    <h3>Assembly, calibration, and usage</h3>
    <p>Public guides for setup and physical system preparation.</p>
    <div class="public-links-list">
      <a href="{{ '/quick_assembly/' | relative_url }}">Quick assembly guide</a>
      <a href="{{ '/assembly_guide/' | relative_url }}">Assembly guide</a>
      <a href="{{ '/calibration/' | relative_url }}">Calibration</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">GRBL references</p>
    <h3>Slider control behavior</h3>
    <p>Recommended base reference for compatible control.</p>
    <div class="public-links-list">
      <a href="{{ '/grbl/' | relative_url }}">Open GRBL 1.1 reference</a>
      <a href="{{ '/troubleshooting/' | relative_url }}">Troubleshooting</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">App-related resources</p>
    <h3>Connect downloads to product workflow</h3>
    <p>Support and hardware context for users scaling from mobile app to full ecosystem.</p>
    <div class="public-links-list">
      <a href="{{ routes.hardware | relative_url }}">Open hardware page</a>
      <a href="{{ routes.gallery | relative_url }}">Open technical gallery</a>
      <a href="{{ routes.support | relative_url }}">Go to support</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>Versioning and maintenance</h3>
  <p>When new versions (`v2`, `v3`, etc.) are published, previous versions remain available for traceability.</p>
  <ol>
    <li>Create version folders in STL, STEP, and BOM.</li>
    <li>Upload final files.</li>
    <li>Keep history.</li>
    <li>Update only `latest_pack` in `docs/_config.yml`.</li>
  </ol>
  <p class="public-note">Some content status: in preparation until final uploads are completed.</p>
</div>

<div class="public-cta-band">
  <h3>Continue with the full workflow</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explore open hardware</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Need help</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Back to home</a>
  </div>
</div>
