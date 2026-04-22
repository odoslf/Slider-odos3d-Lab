---
layout: public-page
title: "Descargas de hardware | Smart Timelapse AI"
description: "Descarga STL, STEP y BOM del hardware Slider-odos3d con flujo versionado y enlaces técnicos del ecosistema Smart Timelapse AI."
permalink: /downloads/
lang: es
lang_page: es
alt_url: /en/downloads/
og_title: "Descargas STL/STEP/BOM | Smart Timelapse AI"
og_description: "Hub público de descargas técnicas, guías y referencias para el hardware Slider-odos3d."
nav_key: downloads
page_heading: "Hub de descargas y recursos públicos"
page_intro: "Centro de recursos para hardware, documentación y referencias del ecosistema Smart Timelapse AI Slider."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign external = links.external_links %}
{% assign routes = links.internal_routes_es %}


<div class="public-media-grid" style="margin-bottom:14px;">
  <article class="public-media-card">{% include public-media-item.html media_key='hero' lang='es' loading='lazy' show_caption='false' %}</article>
  <article class="public-media-card">{% include public-media-item.html media_key='app_screenshot' lang='es' loading='lazy' show_caption='true' %}</article>
</div>
<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Archivos reales disponibles en el repo</p>
    <h3>Estado actual de STL, STEP y BOM ({{ site.latest_pack }})</h3>
    <p>Listado real de lo que está subido ahora mismo en el repositorio público.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/prints/BOM/{{ site.latest_pack }}/slider-odos3d_bom_v1.csv">BOM CSV real (v1)</a>
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
      <a href="{{ site.tree_base }}/prints/STEP/{{ site.latest_pack }}/">STEP {{ site.latest_pack }} (sin archivos finales publicados)</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">Guías y documentación</p>
    <h3>Montaje, calibración y uso</h3>
    <p>Guías públicas para montaje y preparación del sistema físico.</p>
    <div class="public-links-list">
      <a href="{{ '/quick_assembly/' | relative_url }}">Guía rápida de montaje</a>
      <a href="{{ '/assembly_guide/' | relative_url }}">Guía de ensamblado</a>
      <a href="{{ '/calibration/' | relative_url }}">Calibración</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">Referencias GRBL</p>
    <h3>Control y comportamiento del slider</h3>
    <p>Base de referencia recomendada para control compatible.</p>
    <div class="public-links-list">
      <a href="{{ '/grbl/' | relative_url }}">Abrir referencia GRBL 1.1</a>
      <a href="{{ '/troubleshooting/' | relative_url }}">Resolución de problemas</a>
    </div>
  </article>
  <article class="public-card">
    <p class="public-kicker">Recursos relacionados con la app</p>
    <h3>Conecta descargas con flujo de producto</h3>
    <p>Contexto de soporte y hardware para quienes escalan desde la app móvil al ecosistema completo.</p>
    <div class="public-links-list">
      <a href="{{ routes.hardware | relative_url }}">Ver página hardware</a>
      <a href="{{ routes.gallery | relative_url }}">Abrir galería técnica</a>
      <a href="{{ routes.support | relative_url }}">Ir a soporte</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>Versiones y mantenimiento</h3>
  <p>Cuando publiquemos nuevas versiones (`v2`, `v3`, etc.), las anteriores se mantendrán disponibles para trazabilidad.</p>
  <ol>
    <li>Crear carpetas de versión en STL, STEP y BOM.</li>
    <li>Subir archivos definitivos.</li>
    <li>Mantener histórico.</li>
    <li>Actualizar solo `latest_pack` en `docs/_config.yml`.</li>
  </ol>
  <p class="public-note">Estado actual real: STL v1 y BOM v1 publicados. STEP {{ site.latest_pack }} sigue en preparación sin archivos finales.</p>
</div>

<div class="public-cta-band">
  <h3>Continúa con el flujo completo</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explorar hardware abierto</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Necesitas ayuda</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Volver a la home</a>
  </div>
</div>
