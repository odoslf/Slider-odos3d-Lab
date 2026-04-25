---
layout: public-page
title: "Resolución de problemas | Smart Timelapse AI Slider"
description: "Guía pública para resolver problemas mecánicos, Bluetooth, GRBL, exportación y uso básico del slider."
permalink: /troubleshooting/
lang: es
lang_page: es
alt_url: /en/troubleshooting/
nav_key: support
page_heading: "Resolución de problemas"
page_intro: "Checklist rápido para detectar fallos comunes antes de contactar con soporte."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign routes = links.internal_routes_es %}

<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Mecánica</p>
    <h3>Roces, atascos u holgura</h3>
    <p>Revisa alineación de varillas, tensión de correa, paralelismo, tornillería y orientación de piezas impresas. El carro debe moverse suave en todo el recorrido antes de conectar motores.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Movimiento</p>
    <h3>Pérdida de pasos o vibración</h3>
    <p>Baja velocidad y aceleración, ajusta corriente del driver, revisa polea/eje y confirma que la correa no está demasiado tensa. Prueba primero recorridos cortos.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Bluetooth</p>
    <h3>No conecta o no responde</h3>
    <p>Comprueba alimentación del módulo Bluetooth, emparejamiento con el móvil, velocidad serie compatible y que no esté conectado a otro dispositivo. Reinicia controlador y conexión si la app muestra conectado pero no recibe respuesta.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">GRBL</p>
    <h3>ALARM o recorrido inseguro</h3>
    <p>Si GRBL está en <code>ALARM</code>, usa <code>$H</code> con homing preparado. Usa <code>$X</code> solo con el carro en posición segura. Revisa límites físicos antes de rutas largas.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Exportación</p>
    <h3>Vídeo negro, lento o fallido</h3>
    <p>Libera espacio, revisa permisos de fotos/vídeos, confirma que el proyecto contiene imágenes válidas y prueba resolución menor si hay muchas fotos.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Soporte</p>
    <h3>Datos mínimos para ayudar</h3>
    <p>Envía modelo de móvil, versión de Android, versión de la app, modo usado, si usas slider físico o solo móvil, captura del error y pasos exactos.</p>
    <div class="public-links-list">
      <a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a>
      <a href="{{ routes.support | relative_url }}">Centro de soporte</a>
      <a href="{{ routes.downloads | relative_url }}">Descargas</a>
    </div>
  </article>
</div>
