> Nota interna: este archivo conserva información operativa del repositorio. No forma parte de la web pública principal.

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
  - `slider-odos3d-lab-caja-electronica-v1.stl`
  - `slider-odos3d-lab-carro-v1.stl`
  - `slider-odos3d-lab-escuadra-v1.stl`
  - `slider-odos3d-lab-separador-v1.stl`
  - `slider-odos3d-lab-soporte-correa-v1.stl`
  - `slider-odos3d-lab-soporte-derecho-v1.stl`
  - `slider-odos3d-lab-soporte-izquierdo-v1.stl`
  - `slider-odos3d-lab-tubo-camara-v1.stl`
  - `slider-odos3d-lab-tapa-electronica-v1.stl`
- BOM v1 disponible (`slider-odos3d_bom_v1.csv` y `README.md`).
- STEP v1 sigue pendiente de archivos finales.
