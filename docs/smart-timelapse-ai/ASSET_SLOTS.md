# ASSET SLOTS — Smart Timelapse AI

## Configuración central real

La capa pública se gobierna desde fuentes registradas:

- Media app/site: `docs/_data/public-media.yml`
- Media galería técnica: `docs/_data/gallery-media.yml`
- Estado maestro de assets: `docs/_data/asset-status.yml`
- Orden de solicitud: `docs/ASSET_REQUEST_ORDER.md`
- Links y datos públicos: `docs/_data/public-links.yml`

## Mapeo real de assets app por bloque visual

- `logo` → logo de header en `/`, `/en/` y páginas públicas secundarias.
- `hero` → hero principal y apoyo visual en bloques de prueba.
- `slider_mobile` → bloques de hardware/proof (slider + móvil).
- `slider_dslr` → bloques de hardware/proof (slider + DSLR).
- `app_screenshot` → bloques de app en home/downloads/support.
- `video_thumb` → bloque de vídeo demo en home ES/EN.
- `favicon` → head global y `site.webmanifest`.
- `og_image` → `og:image` y `twitter:image` de páginas públicas.

## Mapeo real de slots de galería técnica

- `slot_overview_a`, `slot_overview_b` → Visión general / Overview.
- `slot_carriage_a`, `slot_carriage_b` → Carro y guiado / Carriage and guidance.
- `slot_belt_a`, `slot_belt_b` → Correa y transmisión / Belt and drive.
- `slot_electronics`, `slot_endstop_x` → Electrónica y control / Electronics and control.
- `slot_phone_mount` → Accesorios / Accessories.

## Flujo operativo unificado

1. Identificar asset en `docs/_data/asset-status.yml`.
2. Pedirlo según `docs/ASSET_REQUEST_ORDER.md`.
3. Subir con nombre final congelado en carpeta final (`docs/assets/media/app/` o `docs/assets/media/gallery/`).
4. Marcar `uploaded_to_repo: true` en `asset-status.yml`.
5. Cambiar `active_source` a `final` en el registry correspondiente.
6. Marcar `activated_in_yaml: true` en `asset-status.yml`.
7. Ejecutar auditoría: `python scripts/public_site_audit.py`.
8. Revisión visual ES/EN.

## Documentación complementaria

- Guía operativa app: `docs/ASSET_INGESTION_GUIDE.md`
- Guía operativa galería: `docs/GALLERY_INGESTION_GUIDE.md`
- Ficha técnica app: `docs/assets/media/app/ASSET_TARGETS.md`

Estado actual de galería pública:
- 01–04 subidos y activados en registry.
- 05–09 pendientes y en placeholder.
