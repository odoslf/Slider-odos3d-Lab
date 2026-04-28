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
{% assign external = links.external_links %}
{% assign zip_path = "/assets/downloads/slider-odos3d-lab-stl-pack-v1.zip" %}
{% assign zip_file = site.static_files | where: "path", zip_path | first %}

{% assign raw_stl_base = site.repo_url | append: "/raw/main/prints/STL/" | append: site.latest_pack %}
{% assign tree_stl_base = site.tree_base | append: "/prints/STL/" | append: site.latest_pack %}
{% assign blob_bom_base = site.blob_base | append: "/prints/BOM/" | append: site.latest_pack %}

<div class="public-cta-band">
  <p class="public-kicker">App Android</p>
  <h3>Descarga Smart Timelapse AI</h3>
  <p>Instala la app desde Google Play y usa esta página para descargar el hardware abierto, STL, BOM y guías públicas.</p>
  <div class="public-cta-actions">
    <a class="public-btn primary" href="{{ external.play_store_url }}" target="_blank" rel="noopener noreferrer">Descargar en Google Play</a>
  </div>
</div>

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Descarga recomendada</p>
    <h3>Pack STL v1 completo</h3>
    <p>Descarga todas las piezas STL del slider en un único archivo ZIP listo para imprimir y revisar.</p>
    <div class="public-cta-actions">
      {% if zip_file %}
        <a class="public-btn primary" href="{{ zip_path | relative_url }}" download>Descargar pack STL v1 (.zip)</a>
      {% else %}
        <span class="public-btn is-disabled" aria-disabled="true">Pack ZIP pendiente de publicar</span>
      {% endif %}
    </div>
    <p class="public-note">Incluye las piezas STL v1 publicadas para el slider. Antes de imprimir, revisa medidas, orientación y material recomendado en tu slicer.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Archivos individuales</p>
    <h3>Piezas STL y lista de materiales</h3>
    <p>Abre el BOM en GitHub para verlo correctamente y descarga piezas STL individuales solo si no necesitas el pack completo.</p>
    <div class="public-links-list">
      <a href="{{ blob_bom_base }}/slider-odos3d_bom_v1.csv" target="_blank" rel="noopener noreferrer">Ver lista de materiales BOM v1</a>
      <a href="{{ blob_bom_base }}/README.md" target="_blank" rel="noopener noreferrer">Ver notas del BOM v1</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-caja-electronica-v1.stl">Caja electrónica (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-carro-v1.stl">Carro del slider (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-escuadra-v1.stl">Escuadra lateral (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-separador-v1.stl">Separador (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-correa-v1.stl">Soporte de correa (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-derecho-v1.stl">Soporte derecho (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-soporte-izquierdo-v1.stl">Soporte izquierdo (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-tapa-electronica-v1.stl">Tapa electrónica (.stl)</a>
      <a href="{{ raw_stl_base }}/slider-odos3d-lab-tubo-camara-v1.stl">Tubo de cámara (.stl)</a>
      <a href="{{ tree_stl_base }}" target="_blank" rel="noopener noreferrer">Abrir carpeta STL v1 en GitHub</a>
    </div>
    <p class="public-note">STEP v1 está en preparación y se publicará cuando existan los archivos revisados.</p>
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
      <a href="{{ routes.grbl | relative_url }}">Abrir referencia GRBL 1.1</a>
      <a href="{{ routes.troubleshooting | relative_url }}">Resolución de problemas</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>Estado del pack v1</h3>
  <p>El pack ZIP v1, los STL individuales y el BOM v1 ya están disponibles. Los STEP v1 siguen en preparación hasta que existan los archivos revisados.</p>
</div>

<div class="public-cta-band">
  <h3>Continúa con el flujo completo</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Explorar hardware abierto</a>
    <a class="public-btn" href="{{ routes.support | relative_url }}">Necesitas ayuda</a>
    <a class="public-btn primary" href="{{ routes.home | relative_url }}">Volver a la home</a>
  </div>
</div>
