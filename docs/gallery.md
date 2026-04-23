---
layout: public-page
title: "Galería técnica del slider | Smart Timelapse AI"
description: "Galería técnica premium del Slider-odos3d preparada para fotos reales de montaje, carro, transmisión, electrónica y accesorios."
permalink: /gallery/
lang: es
lang_page: es
alt_url: /en/gallery/
og_title: "Galería técnica del slider | Smart Timelapse AI"
og_description: "Selección visual premium preparada para integrar fotos reales del ecosistema Slider-odos3d."
nav_key: gallery
page_heading: "Galería técnica del slider"
page_intro: "Una selección visual preparada para mostrar montaje, carro, transmisión, electrónica y detalles del hardware real del ecosistema Slider-odos3d."
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

[Hardware]({{ routes.hardware }}) [Descargas]({{ routes.downloads }}) [Soporte]({{ routes.support }})
