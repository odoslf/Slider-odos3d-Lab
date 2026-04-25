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
    <p>Activa Bluetooth, concede los permisos que pida Android y abre el escaneo desde la app. En Android 12 o superior puede aparecer el permiso de dispositivos cercanos. En algunos móviles también se necesita ubicación para detectar dispositivos Bluetooth clásicos.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Bluetooth / GRBL</p>
    <h3>Slider no aparece o no conecta</h3>
    <p>Comprueba que el módulo Bluetooth esté alimentado, emparejado con el móvil y que no esté conectado a otro dispositivo. El flujo esperado es móvil → Bluetooth serie → controlador GRBL. Si aparece conectado pero no responde, reinicia el controlador y vuelve a abrir la conexión desde la app.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Estado ALARM / homing</p>
    <h3>GRBL en ALARM, desbloqueo y homing</h3>
    <p>Después de encender, GRBL puede arrancar en ALARM hasta hacer homing o desbloqueo. Usa <code>$H</code> cuando el montaje tenga homing preparado. Usa <code>$X</code> solo si sabes que el carro está en una posición segura. Verifica topes, recorrido y sentido de movimiento antes de lanzar una ruta.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Exportación</p>
    <h3>Exportación lenta, negra o fallida</h3>
    <p>Libera espacio, evita el ahorro de batería, mantén la app abierta durante procesos largos y prueba una resolución menor si el proyecto tiene muchas fotos. Si el vídeo sale negro o no aparecen fotos, revisa permisos de fotos/vídeos y confirma que el proyecto tiene imágenes válidas.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">DSLR / relé</p>
    <h3>Disparo DSLR con relé</h3>
    <p>El disparo DSLR depende del cableado, del relé y del conector remoto de cada cámara. Prueba primero con pulsos cortos y sin mover el slider. No conectes tensiones desconocidas a la cámara. Si una cámara no dispara, revisa polaridad, masa común y modo remoto.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Remoto local / Wi-Fi</p>
    <h3>Panel remoto local</h3>
    <p>Para control remoto local, móvil y dispositivo de control deben estar en la misma red. Desactiva VPN, aislamiento AP o redes de invitados si el panel no abre. El remoto local no sustituye una prueba física de recorrido y seguridad.</p>
  </article>

  <article class="public-card">
    <p class="public-kicker">Qué enviar al contactar</p>
    <h3>Qué enviar al soporte</h3>
    <p>Envía modelo de móvil, versión de Android, versión de la app, modo usado, si usas slider físico o solo móvil, captura del error y pasos exactos para reproducirlo.</p>
    <div class="public-links-list"><a href="mailto:{{ identity.support_email }}">{{ identity.support_email }}</a></div>
  </article>
</div>

<div class="public-cta-band">
  <h3>Accesos rápidos de soporte</h3>
  <div class="public-cta-actions">
    <a class="public-btn" href="{{ routes.downloads | relative_url }}">Descargas</a>
    <a class="public-btn" href="{{ routes.hardware | relative_url }}">Hardware</a>
    <a class="public-btn" href="{{ routes.gallery | relative_url }}">Galería técnica</a>
    <a class="public-btn" href="{{ routes.privacy | relative_url }}">Privacidad</a>
    <a class="public-btn" href="{{ routes.terms | relative_url }}">Términos</a>
  </div>
</div>
