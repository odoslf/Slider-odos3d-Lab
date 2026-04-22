---
title: "Mapa de subida interno"
permalink: /upload-map/
---

# Mapa de subida alineado con la web pública nueva

## Dónde vive cada tipo de asset

- **Assets de app/site pública general** (logo, hero, screenshot, etc.):
  - `docs/assets/media/app/`
  - Registro fuente: `docs/_data/public-media.yml`
- **Assets de galería pública premium** (slots de hardware):
  - `docs/assets/media/gallery/`
  - Registro fuente: `docs/_data/gallery-media.yml`

## Flujo cuando llega una foto real de galería

1. Subir la imagen final al nombre exacto congelado en `docs/assets/media/gallery/`.
2. Abrir `docs/_data/gallery-media.yml` y cambiar `active_source` del slot correspondiente a `final`.
3. Ejecutar auditoría: `python scripts/public_site_audit.py`.
4. Revisar visualmente las dos rutas públicas:
   - `/gallery/`
   - `/en/gallery/`

## Paquetes de hardware versionados (se mantiene)

- STL: `prints/STL/v1/`
- STEP: `prints/STEP/v1/`
- BOM: `prints/BOM/v1/`

Al crear `v2`, `v3`, etc., mantener histórico y actualizar solo `latest_pack` en `docs/_config.yml`.

Estado actual de galería pública:
- 01–04 subidos y activados en registry.
- 05–09 pendientes y en placeholder.

Estado actual de descargas hardware:
- STL v1 disponible con estos archivos reales:
  - `Slider ODOS3D Lab caja electroniica.stl`
  - `Slider ODOS3D Lab carro.stl`
  - `Slider ODOS3D Lab escuadra.stl`
  - `Slider ODOS3D Lab separador.stl`
  - `Slider ODOS3D Lab soporte correa.stl`
  - `Slider ODOS3D Lab soporte derecho.stl`
  - `Slider ODOS3D Lab soporte izquierdo.stl`
  - `Slider ODOS3D Lab tubo camara.stl`
  - `Slider ODOS3D Labtapa electroniica.stl`
- BOM v1 disponible (`slider-odos3d_bom_v1.csv` y `README.md`).
- STEP v1 sigue pendiente de archivos finales.
