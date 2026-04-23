---
layout: public-page
title: "Open hardware | Smart Timelapse AI"
description: "Open hardware for Smart Timelapse AI with STL/STEP/BOM downloads and GRBL references to scale from phone-only to motion control."
permalink: /en/hardware/
lang: en
lang_page: en
alt_url: /hardware/
og_title: "Open hardware for timelapse | Smart Timelapse AI"
og_description: "Downloads and GRBL references to scale Smart Timelapse AI with open-source hardware."
nav_key: hardware
page_heading: "Open hardware to scale the ecosystem"
page_intro: "You can start phone-only. Open hardware is optional, but it lets you scale when you need more physical control and motion."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign external = links.external_links %}
{% assign routes = links.internal_routes_en %}


<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include public-media-item.html media_key='slider_mobile' lang='en' loading='lazy' show_caption='false' %}</article>
  <article class="public-media-card">{% include public-media-item.html media_key='slider_dslr' lang='en' loading='lazy' show_caption='false' %}</article>
</div>
<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">What it is</p>
    <h3>Open hardware connected to the app</h3>
    <p>The open-source system extends Smart Timelapse AI with physical control and GRBL motion for more demanding projects.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">What you can access</p>
    <h3>Downloads and technical reference</h3>
    <p>From here you access STL/STEP/BOM and GRBL references for assembly and adjustment.</p>
    <div class="public-links-list">
      <a href="{{ routes.downloads | relative_url }}">Open downloads</a>
      <a href="{{ routes.gallery | relative_url }}">Open technical gallery</a>
      <a href="{{ '/grbl/' | relative_url }}">Open GRBL 1.1</a>
    </div>
  </article></div>

<div class="public-cta-band">
  <h3>Next step in the ecosystem</h3>
  <p>Open downloads, gallery, or support depending on where you are in the workflow.</p>
  <div class="public-cta-actions">
    <a class="public-btn primary" href="{{ routes.downloads | relative_url }}">Go to downloads</a>
    <a class="public-btn" href="{{ routes.gallery | relative_url }}">Open gallery</a>
    <a class="public-btn" href="{{ routes.home | relative_url }}">Back to home</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Need help</a>
  </div>
</div>
