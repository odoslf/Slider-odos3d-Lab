---
layout: public-page
title: "Descargas de hardware | Smart Timelapse AI"
description: "Descarga STL, STEP y BOM del hardware Slider-odos3d con enlaces directos, guías públicas y pack ZIP preparado."
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
{% assign routes = links.internal_routes_es %}
{% assign zip_path = "/assets/downloads/slider-odos3d-lab-stl-pack-v1.zip" %}
{% assign zip_file = site.static_files | where: "path", zip_path | first %}

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Descarga recomendada</p>
    <h3>Pack STL v1 completo</h3>
    <p>Descarga todas las piezas STL del slider en un único archivo cuando el ZIP esté publicado.</p>
    <div class="public-cta-actions">
      {% if zip_file %}
        <a class="public-btn primary" href="{{ zip_path | relative_url }}" download>Descargar pack STL v1 (.zip)</a>
      {% else %}
        <span class="public-btn is-disabled" aria-disabled="true">ZIP pendiente: slider-odos3d-lab-stl-pack-v1.zip</span>
      {% endif %}
    </div>
    <p class="public-note">Nombre exacto esperado: <code>slider-odos3d-lab-stl-pack-v1.zip</code></p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Archivos individuales</p>
    <h3>STL y BOM disponibles ahora mismo</h3>
    <p>Enlaces directos a los archivos publicados. Los nombres visibles están normalizados aunque el archivo original conserve su nombre real.</p>
    <div class="public-links-list">
      <a href="{{ site.raw_base }}/prints/BOM/{{ site.latest_pack }}/slider-odos3d_bom_v1.csv">BOM CSV v1</a>
      <a href="{{ site.raw_base }}/prints/BOM/{{ site.latest_pack }}/README.md">BOM README v1</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20caja%20electroniica.stl">Caja electrónica STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20carro.stl">Carro STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20escuadra.stl">Escuadra STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20separador.stl">Separador STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20correa.stl">Soporte de correa STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20derecho.stl">Soporte derecho STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20soporte%20izquierdo.stl">Soporte izquierdo STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Lab%20tubo%20camara.stl">Tubo cámara STL</a>
      <a href="{{ site.raw_base }}/prints/STL/{{ site.latest_pack }}/Slider%20ODOS3D%20Labtapa%20electroniica.stl">Tapa electrónica STL</a>
      <a href="{{ site.tree_base }}/prints/STEP/{{ site.latest_pack }}/">STEP {{ site.latest_pack }} en preparación</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">Guías y documentación</p>
    <h3>Montaje, ensamblado y calibración</h3>
    <p>Guías públicas para preparar el sistema físico sin depender de documentación interna del repositorio.</p>
    <div class="public-links-list">
      <a href="{{ '/quick-assembly/' | relative_url }}">Guía rápida de montaje</a>
      <a href="{{ '/assembly-guide/' | relative_url }}">Guía de ensamblado</a>
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
</div>

<div class="public-band">
  <h3>Estado del pack v1</h3>
  <p>STL v1 y BOM v1 están publicados. STEP {{ site.latest_pack }} sigue en preparación hasta que existan archivos finales revisados.</p>
  <p class="public-note">El ZIP único se activará automáticamente cuando se suba <code>docs/assets/downloads/slider-odos3d-lab-stl-pack-v1.zip</code>.</p>
</div>

<div class="public-cta-band">
  <h3>Continúa con el flujo completo</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explorar hardware abierto</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Necesitas ayuda</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Volver a la home</a>
  </div>
</div>
