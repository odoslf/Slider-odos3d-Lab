---
layout: public-page
title: "GRBL 1.1 para slider | Smart Timelapse AI"
description: "Referencia pública de GRBL 1.1 para usar el hardware Slider-odos3d con Smart Timelapse AI."
permalink: /grbl/
lang: es
lang_page: es
alt_url: /en/grbl/
nav_key: downloads
page_heading: "Referencia GRBL 1.1"
page_intro: "Base de configuración, seguridad y enlaces técnicos para controlar el slider con firmware GRBL compatible."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_es %}

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Firmware</p>
    <h3>Proyecto GRBL original</h3>
    <p>El slider está pensado para controladores compatibles con GRBL 1.1. Este repositorio no sustituye al proyecto original: aquí solo se documentan ajustes y referencias para el hardware Slider-odos3d.</p>
    <div class="public-links-list">
      <a href="https://github.com/gnea/grbl">Repositorio oficial GRBL</a>
      <a href="{{ site.blob_base }}/grbl/setup.md">Puesta en marcha GRBL</a>
      <a href="{{ site.blob_base }}/grbl/recommended_settings.md">Ajustes recomendados</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">Seguridad</p>
    <h3>ALARM, desbloqueo y homing</h3>
    <p>Después de encender, GRBL puede arrancar en estado <code>ALARM</code>. Usa <code>$H</code> si tu montaje tiene homing preparado. Usa <code>$X</code> solo cuando sepas que el carro está en una posición segura y el recorrido está despejado.</p>
    <p>Antes de una ruta larga, prueba movimientos cortos y confirma dirección, topes y recorrido real.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Ajustes base</p>
    <h3>Parámetros habituales</h3>
    <p>Los valores importantes suelen ser pasos/mm, velocidad, aceleración y recorrido máximo. En un slider de 60 cm, revisa especialmente <code>$100</code>, <code>$110</code>, <code>$120</code> y <code>$130</code>.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/grbl/presets/slider_60cm_o2.txt">Preset 60 cm</a>
      <a href="{{ site.blob_base }}/grbl/only_x_homing.md">Homing solo X</a>
      <a href="{{ site.blob_base }}/grbl/a4988_vref.md">Ajuste Vref A4988</a>
    </div>
  </article>

  <article class="public-card">
    <p class="public-kicker">App</p>
    <h3>Comunicación desde Smart Timelapse AI</h3>
    <p>La app se comunica con el controlador a través de Bluetooth serie compatible. El flujo esperado es móvil → módulo Bluetooth serie → GRBL.</p>
    <div class="public-links-list">
      <a href="{{ site.blob_base }}/grbl/app_protocol.md">Protocolo de comandos</a>
      <a href="{{ routes.support | relative_url }}">Soporte técnico</a>
      <a href="{{ routes.downloads | relative_url }}">Descargas</a>
    </div>
  </article>
</div>

<div class="public-band">
  <h3>Antes de usar el recorrido completo</h3>
  <p>Guarda el estado base con <code>$$</code>, revisa límites físicos, confirma que el carro se mueve en el sentido esperado y baja velocidad/aceleración si hay pérdida de pasos.</p>
</div>
