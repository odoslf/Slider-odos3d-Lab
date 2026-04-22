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
    <p class="public-kicker">Real files currently available in the repo</p>
    <h3>Current STL, STEP, and BOM status ({{ site.latest_pack }})</h3>
    <p>Real-time list of what is already uploaded in the public repository.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/prints/BOM/{{ site.latest_pack }}/slider-odos3d_bom_v1.csv">Real BOM CSV (v1)</a>
      <a href="{{ site.blob_base }}/prints/BOM/{{ site.latest_pack }}/README.md">BOM README (v1)</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20caja%20electroniica.stl">Slider ODOS3D Lab caja electroniica.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20carro.stl">Slider ODOS3D Lab carro.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20escuadra.stl">Slider ODOS3D Lab escuadra.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20separador.stl">Slider ODOS3D Lab separador.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20correa.stl">Slider ODOS3D Lab soporte correa.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20derecho.stl">Slider ODOS3D Lab soporte derecho.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20izquierdo.stl">Slider ODOS3D Lab soporte izquierdo.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20tubo%20camara.stl">Slider ODOS3D Lab tubo camara.stl</a>
      <a href="{{ site.blob_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Labtapa%20electroniica.stl">Slider ODOS3D Labtapa electroniica.stl</a>
      <a href="{{ site.tree_base }}/prints/STEP/{{ site.latest_pack }}/">STEP {{ site.latest_pack }} (no final files published yet)</a>
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
  <p class="public-note">Current real status: STL v1 and BOM v1 are published. STEP {{ site.latest_pack }} is still in preparation with no final files yet.</p>
</div>

<div class="public-cta-band">
  <h3>Continue with the full workflow</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explore open hardware</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Need help</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Back to home</a>
  </div>
</div>
