# ASSET TARGETS (producción)

Ruta productiva final de assets:
- `docs/assets/media/app/`

Nombres finales congelados:
- `logo-final.png` (png, transparencia: sí) — uso: logo de header público.
- `hero-final.jpg` (jpg, transparencia: no) — uso: hero principal home ES/EN.
- `slider-mobile-final.jpg` (jpg, transparencia: no) — uso: media de hardware/proof.
- `slider-dslr-final.jpg` (jpg, transparencia: no) — uso: media de hardware/proof.
- `app-screenshot-final.png` (png, transparencia: no) — uso: captura app en home/support/downloads.
- `video-thumb-final.jpg` (jpg, transparencia: no) — uso: thumbnail bloque vídeo demo en home.
- `favicon-final.svg` (svg, transparencia: sí) — uso: favicon head + webmanifest.
- `og-home-final.jpg` (jpg, transparencia: no) — uso: og/twitter image.

Nota técnica:
- Mientras no existan assets reales, el sistema usa placeholders definidos en `docs/_data/public-media.yml`.

Flujo de activación:
1. Subir archivo final con nombre congelado.
2. Cambiar `active_source` del `media_key` correspondiente a `final` en `docs/_data/public-media.yml`.
3. Actualizar `is_placeholder: false` para ese asset.
4. Ejecutar `python scripts/public_site_audit.py`.
