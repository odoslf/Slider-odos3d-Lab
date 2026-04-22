# Guía de ingestión de assets reales (capa pública)

Guía interna para sustituir placeholders por assets finales **sin tocar plantillas HTML**.

## Inventario maestro y orden de petición

- Estado único de todos los assets: `docs/_data/asset-status.yml`
- Orden humano de solicitud (1→17): `docs/ASSET_REQUEST_ORDER.md`

## Tabla técnica de assets finales

| media_key | archivo final | formato esperado | tamaño mínimo recomendado | ratio | transparencia | dónde se usa | observaciones de recorte / zona segura |
|---|---|---|---|---|---|---|---|
| logo | `logo-final.png` | png | 512x512 | 1:1 | Sí | Header público ES/EN y páginas secundarias | Mantener marca centrada con margen interno (10%). |
| hero | `hero-final.png` | png | 1920x1200 | 16:10 | No | Home `/` y `/en/`, bloque visual y apoyo en downloads | Foco central; evitar texto en bordes. |
| slider_mobile | `slider-mobile-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home y páginas hardware ES/EN | Carril + móvil centrados, sin elementos críticos en bordes. |
| slider_dslr | `slider-dslr-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home y páginas hardware ES/EN | Cámara/slider legibles en zona central. |
| app_screenshot | `app-screenshot-final.jpg` | jpg | 1600x900 | 16:9 | No | Home, downloads y support ES/EN | Captura limpia; evitar barras ajenas sin valor. |
| video_thumb | `video-thumb-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home ES/EN (bloque vídeo) | Reservar esquina inferior izquierda para overlay CTA/play. |
| favicon | `favicon-final.png` | png | 512x512 | 1:1 | Sí | Head global + `site.webmanifest` + 404 | Debe leerse a tamaño pequeño (zona central 70%). |
| og_image | `og-home-final.jpg` | jpg | 1200x630 | 1200:630 | No | Open Graph/Twitter en capa pública | Composición social estable, sin texto pegado a bordes. |

## Flujo operativo real (app + maestro)

1. Identificar el asset en `docs/_data/asset-status.yml`.
2. Pedir al usuario el archivo correspondiente según `docs/ASSET_REQUEST_ORDER.md`.
3. Subir el archivo final a `docs/assets/media/app/` usando el nombre congelado exacto.
4. Marcar `uploaded_to_repo: true` en `asset-status.yml` para ese asset.
5. En `docs/_data/public-media.yml`, cambiar `active_source` a `final`.
6. Marcar `activated_in_yaml: true` en `asset-status.yml`.
7. Ejecutar auditoría: `python scripts/public_site_audit.py`.
8. Validar visualmente `/` y `/en/` + hardware/downloads/support ES/EN.

## Qué no hacer

- No cambiar nombres de archivo finales.
- No subir assets a otra carpeta distinta de `docs/assets/media/app/`.
- No tocar HTML, CSS ni includes si solo cambian assets.
- No forzar proporciones que rompan composición del layout actual.
- No activar YouTube/Play sin URL real y flags coherentes en `public-links.yml`.
