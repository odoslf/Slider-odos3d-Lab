---
title: "Piezas"
permalink: /parts/
---

{% include topnav.html %}

# Piezas

Este repo contiene las piezas y documentación del hardware **Slider-odos3d**.

## Descargas por versión

### Pack actual ({{ site.latest_pack }})
- STL: [`prints/STL/{{ site.latest_pack }}/`]({{ site.tree_base }}/prints/STL/{{ site.latest_pack }}/)
- STEP: [`prints/STEP/{{ site.latest_pack }}/`]({{ site.tree_base }}/prints/STEP/{{ site.latest_pack }}/)
- BOM: [`prints/BOM/{{ site.latest_pack }}/`]({{ site.tree_base }}/prints/BOM/{{ site.latest_pack }}/)

> Para publicar v2/v3, crea carpetas nuevas `v2`, `v3` y luego cambia `latest_pack` en `docs/_config.yml`.

---

## Documentación de piezas (plantillas)

Para documentar una pieza, copia la plantilla:

- [`docs/parts/_TEMPLATE_PART.md`](./parts/_TEMPLATE_PART.md)

Ejemplos (cuando los crees):
- `docs/parts/carro.md`
- `docs/parts/soporte_movil.md`
- `docs/parts/fin_de_carrera.md`
