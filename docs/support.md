---
layout: public-page
title: "Soporte técnico | Smart Timelapse AI"
description: "Centro oficial de soporte Smart Timelapse AI con ayuda para Bluetooth, GRBL, exportación, remoto local y contacto técnico."
permalink: /support/
lang: es
lang_page: es
alt_url: /en/support/
og_title: "Soporte Smart Timelapse AI"
og_description: "Guía rápida de soporte y contacto técnico para flujo móvil, slider GRBL y DSLR."
nav_key: support
page_heading: "Centro de ayuda"
page_intro: "Guía de soporte para arrancar rápido, resolver incidencias y mantener el flujo estable."
---

{% assign links = site.data.public-links %}
{% assign identity = links.site_identity %}
{% assign external = links.external_links %}
{% assign routes = links.internal_routes_es %}


<div class="public-grid cols-2">
  <article class="public-card">
    <p class="public-kicker">Primeros pasos</p>
    <h3>Conexión inicial y permisos</h3>
    <p>Activa Bluetooth y ubicación, revisa permisos de Bluetooth cercano en Android 12/13 y confirma que el slider aparece al escanear.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Flujo con slider GRBL</p>
    <h3>Estado ALARM y estabilidad</h3>
    <p>Si GRBL entra en ALARM, usa <code>$X</code> y verifica topes/homing. Para remoto Wi‑Fi, valida red común y ausencia de AP isolation o VPN.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Exportación y formatos</p>
    <h3>Rendimiento de salida</h3>
    <p>Si exportar es lento o falla, libera espacio, evita ahorro energético y reduce resolución cuando el proyecto sea largo.</p>
  </article>
  <article class="public-card">
    <p class="public-kicker">Soporte y contacto</p>
    <h3>Qué enviar al contactar</h3>
    <p>Comparte captura + diagnóstico copiado para acelerar soporte técnico.</p>
    <div class="public-links-list"><a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a></div>
  </article>
</div>

<div class="public-cta-band">
  <h3>Accesos rápidos de soporte</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Ver descargas</a>
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Ver hardware</a>
    <a class="public-btn" href="{{ routes.gallery | relative_url }}">Galería técnica</a>
    <a class="public-btn" href="{{ routes.privacy | relative_url }}">Privacidad</a>
    <a class="public-btn" href="{{ routes.terms | relative_url }}">Términos</a>
  </div>
</div>
