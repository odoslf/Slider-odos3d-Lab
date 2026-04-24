---
layout: public-page
title: "Galería técnica del slider | Smart Timelapse AI"
description: "Galería pública con vistas reales del slider y su uso dentro del flujo Smart Timelapse AI."
permalink: /gallery/
lang: es
lang_page: es
alt_url: /en/gallery/
og_title: "Galería técnica del slider | Smart Timelapse AI"
og_description: "Vistas reales del hardware y del flujo en uso dentro del ecosistema Smart Timelapse AI."
nav_key: gallery
page_heading: "Galería real del slider"
page_intro: "Tres vistas reales: una general, una con móvil y una con DSLR."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_es %}

<p>La galería pública muestra una selección limpia de fotos reales del hardware y su uso dentro del flujo Smart Timelapse AI.</p>

<div class="gallery-grid-public">
  {% include gallery-media-item.html slot_key='slot_overview_a' lang='es' class_name='gallery-photo' show_caption='false' %}
  {% include gallery-media-item.html slot_key='slot_carriage_a' lang='es' class_name='gallery-photo' show_caption='false' %}
  {% include gallery-media-item.html slot_key='slot_carriage_b' lang='es' class_name='gallery-photo' show_caption='false' %}
</div>

<div class="public-cta-band">
  <h3>Siguiente paso del flujo técnico</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Descargas</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Soporte</a>
  </div>
</div>
