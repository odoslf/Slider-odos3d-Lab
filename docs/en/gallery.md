---
layout: public-page
title: "Slider technical gallery | Smart Timelapse AI"
description: "Premium Slider-odos3d technical gallery prepared for real photos covering overview, carriage, drive, electronics, and accessories."
permalink: /en/gallery/
lang: en
lang_page: en
alt_url: /gallery/
og_title: "Slider technical gallery | Smart Timelapse AI"
og_description: "Premium visual gallery ready for real photo ingestion in the Slider-odos3d ecosystem."
nav_key: gallery
page_heading: "Slider technical gallery"
page_intro: "A curated visual selection prepared to showcase assembly, carriage, transmission, electronics, and real hardware details from the Slider-odos3d ecosystem."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_en %}

<div class="public-band">
  <p>This public gallery is now wired to a central registry and ready to receive real photos without template or structural CSS rework.</p>
</div>

<h2>Overview</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_overview_a' lang='en' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_overview_b' lang='en' show_caption='true' %}</article>
</div>

<h2>Carriage and guidance</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_carriage_a' lang='en' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_carriage_b' lang='en' show_caption='true' %}</article>
</div>

<h2>Belt and drive</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_belt_a' lang='en' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_belt_b' lang='en' show_caption='true' %}</article>
</div>

<h2>Electronics and control</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_electronics' lang='en' show_caption='true' %}</article>
  <article class="public-media-card">{% include gallery-media-item.html slot_key='slot_endstop_x' lang='en' show_caption='true' %}</article>
</div>

<h2>Accessories</h2>
<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card wide">{% include gallery-media-item.html slot_key='slot_phone_mount' lang='en' show_caption='true' %}</article>
</div>

<div class="public-cta-band">
  <h3>Continue the technical flow</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Downloads</a>
    <a class="public-btn primary" href="{{ routes.support | relative_url }}">Support</a>
  </div>
</div>
