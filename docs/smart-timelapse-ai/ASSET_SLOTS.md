# ASSET SLOTS — Smart Timelapse AI

## Configuración central real

La capa pública se gobierna desde dos fuentes:

- Media: `docs/_data/public-media.yml`
- Links y datos públicos: `docs/_data/public-links.yml`

## Mapeo real de assets por bloque visual

- `logo` → logo de header en `/`, `/en/` y páginas públicas secundarias.
- `hero` → hero principal y apoyo visual en bloques de prueba.
- `slider_mobile` → bloques de hardware/proof (slider + móvil).
- `slider_dslr` → bloques de hardware/proof (slider + DSLR).
- `app_screenshot` → bloques de app en home/downloads/support.
- `video_thumb` → bloque de vídeo demo en home ES/EN.
- `favicon` → head global y `site.webmanifest`.
- `og_image` → `og:image` y `twitter:image` de páginas públicas.

## Home real y redirecciones

- Landings reales: `/` y `/en/`.
- Redirecciones (no canónicas): `/smart-timelapse-ai/` y `/en/smart-timelapse-ai/`.

## Nombres finales congelados y carpeta definitiva

Carpeta final obligatoria:
- `docs/assets/media/app/`

Nombres finales exactos:
- `logo-final.svg`
- `hero-final.jpg`
- `slider-mobile-final.jpg`
- `slider-dslr-final.jpg`
- `app-screenshot-final.png`
- `video-thumb-final.jpg`
- `favicon-final.svg`
- `og-home-final.jpg`

## Flujo operativo

1. Sustituir archivo final en `docs/assets/media/app/`.
2. Cambiar `active_source` de `placeholder` a `final` en el `media_key` correspondiente de `docs/_data/public-media.yml`.
3. Ajustar `is_placeholder: false` para ese asset y, si aplica, activar YouTube/Play en `docs/_data/public-links.yml`.
4. Ejecutar auditoría: `python scripts/public_site_audit.py`.

## Documentación complementaria

- Guía operativa completa: `docs/ASSET_INGESTION_GUIDE.md`
- Ficha técnica de carpeta final: `docs/assets/media/app/ASSET_TARGETS.md`
