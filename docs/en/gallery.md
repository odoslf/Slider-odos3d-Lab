---
layout: public-page
title: "Slider technical gallery | Smart Timelapse AI"
description: "Public gallery with real slider views and real workflow usage inside Smart Timelapse AI."
permalink: /en/gallery/
lang: en
lang_page: en
alt_url: /gallery/
og_title: "Slider technical gallery | Smart Timelapse AI"
og_description: "Real hardware and in-use workflow views inside the Smart Timelapse AI ecosystem."
nav_key: gallery
page_heading: "Real slider gallery"
page_intro: "Four real slider views: two overviews, one with phone and one with DSLR."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_en %}

<p>The public gallery shows four real hardware photos and real workflow usage inside Smart Timelapse AI. Additional detail photos will be added as reviewed hardware assets are published.</p>

<div class="gallery-grid-public">
  {% include gallery-media-item.html slot_key='slot_overview_a' lang='en' class_name='gallery-photo' show_caption='false' %}
  {% include gallery-media-item.html slot_key='slot_overview_b' lang='en' class_name='gallery-photo' show_caption='false' %}
  {% include gallery-media-item.html slot_key='slot_carriage_a' lang='en' class_name='gallery-photo' show_caption='false' %}
  {% include gallery-media-item.html slot_key='slot_carriage_b' lang='en' class_name='gallery-photo' show_caption='false' %}
</div>

<div class="public-cta-band">
  <h3>Next technical step</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Downloads</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Support</a>
  </div>
</div>
