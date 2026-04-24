---
layout: public-page
title: "Hardware abierto | Smart Timelapse AI"
description: "Hardware abierto para Smart Timelapse AI: piezas, descargas STL/STEP/BOM y referencias GRBL para escalar del móvil al control físico."
permalink: /hardware/
lang: es
lang_page: es
alt_url: /en/hardware/
og_title: "Hardware abierto para timelapse | Smart Timelapse AI"
og_description: "Piezas, descargas y referencia GRBL para escalar tu flujo de Smart Timelapse AI con hardware open source."
nav_key: hardware
page_heading: "Hardware abierto para escalar el ecosistema"
page_intro: "Puedes empezar solo con móvil. El hardware abierto no es obligatorio, pero te permite escalar cuando necesitas más control físico y movimiento."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_es %}

<div class="media-stack media-stack--hardware">
  {% include public-media-item.html media_key='slider_mobile' lang='es' loading='lazy' show_caption='false' %}
  {% include public-media-item.html media_key='slider_dslr' lang='es' loading='lazy' show_caption='false' %}
</div>

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Qué es</p>
    <h3>Hardware abierto conectado a la app</h3>
    <p>El sistema open source amplía Smart Timelapse AI con control físico y movimiento sobre GRBL en proyectos más exigentes.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Qué puedes consultar</p>
    <h3>Descargas y referencia técnica</h3>
    <p>Desde aquí accedes a STL, STEP, BOM y referencias GRBL para montaje y ajustes.</p>
    <div class="public-links-list">
      <a href="{{ routes.downloads | relative_url }}">Ver descargas</a>
      <a href="{{ routes.gallery | relative_url }}">Ver galería técnica</a>
      <a href="{{ '/grbl/' | relative_url }}">Ver GRBL 1.1</a>
    </div>
  </article>
</div>
