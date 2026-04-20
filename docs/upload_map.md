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
