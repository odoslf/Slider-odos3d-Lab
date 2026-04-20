---
layout: public-page
title: "Galería técnica del slider | Smart Timelapse AI"
description: "Galería técnica premium del Slider-odos3d preparada para fotos reales de montaje, carro, transmisión, electrónica y accesorios."
permalink: /gallery/
lang: es
lang_page: es
alt_url: /en/gallery/
og_title: "Galería técnica del slider | Smart Timelapse AI"
og_description: "Selección visual premium preparada para integrar fotos reales del ecosistema Slider-odos3d."
nav_key: gallery
page_heading: "Galería técnica del slider"
page_intro: "Una selección visual preparada para mostrar montaje, carro, transmisión, electrónica y detalles del hardware real del ecosistema Slider-odos3d."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_es %}
{% assign gallery = site.data.gallery-media.gallery_media %}

<div class="public-band">
  <p>La galería pública ya está conectada a un registro central y lista para recibir fotos reales sin tocar plantillas ni estructura visual.</p>
</div>

<h2>Visión general</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_overview_a' lang='es' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_overview_b' lang='es' show_caption='true' %}</article>
</div>

<h2>Carro y guiado</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_carriage_a' lang='es' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_carriage_b' lang='es' show_caption='true' %}</article>
</div>

<h2>Correa y transmisión</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_belt_a' lang='es' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_belt_b' lang='es' show_caption='true' %}</article>
</div>

<h2>Electrónica y control</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_electronics' lang='es' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_endstop_x' lang='es' show_caption='true' %}</article>
</div>

<h2>Accesorios</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card wide">{% include gallery-media-item.html slot_key='slot_phone_mount' lang='es' show_caption='true' %}</article>
</div>

<div class="public-cta-band">
  <h3>Siguiente paso del flujo técnico</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Descargas</a>
    <a class="public-btn primary" href="{{ routes.support | relative_url }}">Soporte</a>
  </div>
</div>
