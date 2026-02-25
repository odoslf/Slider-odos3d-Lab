---
title: "Descargas"
permalink: /downloads/
---

{% include topnav.html %}

# Descargas

Repositorio público de archivos del slider **Slider-odos3d** (hardware/3D/GRBL).

## Última versión ({{ site.latest_pack }})

- **STL {{ site.latest_pack }}:** [abrir carpeta]({{ site.tree_base }}/prints/STL/{{ site.latest_pack }}/)
- **STEP {{ site.latest_pack }}:** [abrir carpeta]({{ site.tree_base }}/prints/STEP/{{ site.latest_pack }}/)
- **BOM {{ site.latest_pack }}:** [abrir carpeta]({{ site.tree_base }}/prints/BOM/{{ site.latest_pack }}/)

## Versiones anteriores

Cuando publiquemos nuevas versiones (`v2`, `v3`, etc.), las anteriores se mantendrán disponibles en sus carpetas de versión para trazabilidad.

## STL / STEP

- Usa **STL** para impresión 3D directa.
- Usa **STEP** para edición CAD, adaptación y fabricación.
- Usa **BOM** para materiales, tornillería y referencias de montaje.

## Cómo publicar una nueva versión (v2, v3…)

1. Crear carpetas de versión en cada tipo de archivo:
   - `prints/STL/v2/`
   - `prints/STEP/v2/`
   - `prints/BOM/v2/`
2. Subir los archivos definitivos de esa versión.
3. Mantener versiones anteriores sin borrar para histórico.
4. Cambiar **solo** `latest_pack` en `docs/_config.yml` para que la web apunte a la nueva versión.


> Estado de algunos contenidos: **en preparación** hasta completar subidas definitivas.
