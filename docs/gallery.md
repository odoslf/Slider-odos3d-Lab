---
layout: public-page
title: "Galería técnica del slider | Smart Timelapse AI"
description: "Galería pública con vistas reales del slider y su uso dentro del flujo Smart Timelapse AI."
permalink: /gallery/
lang: es
lang_page: es
alt_url: /en/gallery/
og_title: "Galería técnica del slider | Smart Timelapse AI"
og_description: "Vistas reales del hardware y del flujo en uso dentro del ecosistema Smart Timelapse AI."
nav_key: gallery
page_heading: "Galería real del slider"
page_intro: "Vistas reales ya publicadas del hardware y del flujo en uso."
---

{% assign links = site.data.public-links %}
{% assign routes = links.internal_routes_es %}
{% assign gallery = site.data.gallery-media.gallery_media %}

La galería pública muestra las vistas reales ya disponibles del hardware y su uso dentro del flujo Smart Timelapse AI.

## Visión general

{% include gallery-media-item.html slot_key='slot_overview_a' lang='es' show_caption='false' %}
{% include gallery-media-item.html slot_key='slot_overview_b' lang='es' show_caption='false' %}

## En uso

{% include gallery-media-item.html slot_key='slot_carriage_a' lang='es' show_caption='false' %}
{% include gallery-media-item.html slot_key='slot_carriage_b' lang='es' show_caption='false' %}

### Siguiente paso del flujo técnico

[Hardware]({{ routes.hardware }}) · [Descargas]({{ routes.downloads }}) · [Soporte]({{ routes.support }})
