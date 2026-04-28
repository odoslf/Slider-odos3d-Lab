---
layout: public-page
title: "Hardware downloads | Smart Timelapse AI"
description: "Download public STL, STEP, and BOM packages for Slider-odos3d hardware with direct links, public guides, and a prepared ZIP pack."
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
{% assign routes = links.internal_routes_en %}
{% assign external = links.external_links %}
{% assign zip_path = "/assets/downloads/slider-odos3d-lab-stl-pack-v1.zip" %}
{% assign zip_file = site.static_files | where: "path", zip_path | first %}

{% assign raw_stl_base = site.repo_url | append: "/raw/main/prints/STL/" | append: site.latest_pack %}
{% assign tree_stl_base = site.tree_base | append: "/prints/STL/" | append: site.latest_pack %}
{% assign blob_bom_base = site.blob_base | append: "/prints/BOM/" | append: site.latest_pack %}

<div class="public-cta-band">
  <p class="public-kicker">Android app</p>
  <h3>Get Smart Timelapse AI</h3>
  <p>Install the app from Google Play and use this page to download the open hardware files, STL, BOM and public guides.</p>
  <div class="public-cta-actions">
    <a class="public-btn primary" href="{{ external.play_store_url }}" target="_blank" rel="noopener noreferrer">Get it on Google Play</a>
  </div>
</div>

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Recommended download</p>
    <h3>Complete STL v1 pack</h3>
    <p>Download all slider STL parts in one ZIP file, ready to review and print.</p>
    <div class="public-cta-actions">
      {% if zip_file %}
        <a class="public-btn primary" href="{{ zip_path | relative_url }}" download>Download STL v1 pack (.zip)</a>
      {% else %}
        <span class="public-btn is-disabled" aria-disabled="true">ZIP pack pending publication</span>
      {% endif %}
    </div>
    <p class="public-note">Includes the published STL v1 parts for the slider. Before printing, check dimensions, orientation and recommended material in your slicer.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Individual files</p>
    <h3>STL parts and bill of materials</h3>
    <p>Open the BOM on GitHub for a readable view, and download individual STL parts only when you do not need the full pack.</p>
    <div class="public-links-list">
      <a href="{{ blob_bom_base }}/slider-odos3d_bom_v1.csv" target="_blank" rel="noopener noreferrer">View BOM v1 material list</a>
      <a href="{{ blob_bom_base }}/README.md" target="_blank" rel="noopener noreferrer">View BOM v1 notes</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-caja-electronica-v1.stl">Electronics box (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-carro-v1.stl">Slider carriage (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-escuadra-v1.stl">Side bracket (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-separador-v1.stl">Spacer (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-correa-v1.stl">Belt support (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-derecho-v1.stl">Right support (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-izquierdo-v1.stl">Left support (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-tapa-electronica-v1.stl">Electronics lid (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-tubo-camara-v1.stl">Camera tube (.stl)</a>
      <a href="{{ tree_stl_base }}" target="_blank" rel="noopener noreferrer">Open STL v1 folder on GitHub</a>
    </div>
    <p class="public-note">STEP v1 is in preparation and will be published when the reviewed files exist.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Guides and documentation</p>
    <h3>Assembly and calibration</h3>
    <p>Public guides for preparing the physical system without exposing internal repository workflow notes.</p>
    <div class="public-links-list">
      <a href="{{ '/en/quick-assembly/' | relative_url }}">Quick assembly guide</a>
      <a href="{{ '/en/assembly-guide/' | relative_url }}">Assembly guide</a>
      <a href="{{ '/en/calibration/' | relative_url }}">Calibration</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">GRBL references</p>
    <h3>Slider control behavior</h3>
    <p>Recommended base reference for compatible control.</p>
    <div class="public-links-list">
      <a href="{{ routes.grbl | relative_url }}">Open GRBL 1.1 reference</a>
      <a href="{{ routes.troubleshooting | relative_url }}">Troubleshooting</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>v1 pack status</h3>
  <p>The ZIP v1 pack, individual STL files and BOM v1 are now available. STEP v1 remains in preparation until the reviewed files exist.</p>
  <p class="public-note">Includes the published STL v1 parts for the slider. Before printing, check dimensions, orientation and recommended material in your slicer.</p>
</div>

<div class="public-cta-band">
  <h3>Continue with the full workflow</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explore open hardware</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Need help</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Back to home</a>
  </div>
</div>
