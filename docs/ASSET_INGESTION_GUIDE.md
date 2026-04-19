# Guía de ingestión de assets reales (capa pública)

Guía interna para sustituir placeholders por assets finales **sin tocar plantillas HTML**.

## Tabla técnica de assets finales

| media_key | archivo final | formato esperado | tamaño mínimo recomendado | ratio | transparencia | dónde se usa | observaciones de recorte / zona segura |
|---|---|---|---|---|---|---|---|
| logo | `logo-final.svg` | svg | 512x512 | 1:1 | Sí | Header público ES/EN y páginas secundarias | Mantener marca centrada con margen interno (10%). |
| hero | `hero-final.jpg` | jpg | 1920x1200 | 16:10 | No | Home `/` y `/en/`, bloque visual y apoyo en downloads | Foco central; evitar texto en bordes. |
| slider_mobile | `slider-mobile-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home y páginas hardware ES/EN | Carril + móvil centrados, sin elementos críticos en bordes. |
| slider_dslr | `slider-dslr-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home y páginas hardware ES/EN | Cámara/slider legibles en zona central. |
| app_screenshot | `app-screenshot-final.png` | png | 1600x900 | 16:9 | No | Home, downloads y support ES/EN | Captura limpia; evitar barras ajenas sin valor. |
| video_thumb | `video-thumb-final.jpg` | jpg | 1920x1080 | 16:9 | No | Home ES/EN (bloque vídeo) | Reservar esquina inferior izquierda para overlay CTA/play. |
| favicon | `favicon-final.svg` | svg | 512x512 | 1:1 | Sí | Head global + `site.webmanifest` + 404 | Debe leerse a tamaño pequeño (zona central 70%). |
| og_image | `og-home-final.jpg` | jpg | 1200x630 | 1200:630 | No | Open Graph/Twitter en capa pública | Composición social estable, sin texto pegado a bordes. |

## Flujo exacto de sustitución

1. Subir el archivo final a `docs/assets/media/app/`.
2. Usar **exactamente** el nombre final congelado (no variantes).
3. En `docs/_data/public-media.yml`, localizar el `media_key` del asset.
4. Cambiar `active_source: placeholder` a `active_source: final`.
5. Ajustar `is_placeholder: false` para reflejar el estado activo real.
6. No tocar includes, layouts, HTML ni CSS.
7. Ejecutar auditoría: `python scripts/public_site_audit.py`.
8. Validar visualmente `/` y `/en/` + soporte/downloads/hardware ES/EN.

## Reglas específicas por asset

- **logo**: vector limpio, fondo transparente, lectura clara sobre fondo claro.
- **hero**: imagen horizontal premium, sin texto crítico pegado a bordes.
- **slider_mobile**: composición con móvil y slider claramente visibles.
- **slider_dslr**: composición con cámara y slider bien definidos.
- **app_screenshot**: captura real de la app, sin elementos del SO que distraigan.
- **video_thumb**: apta para superposición de CTA/play.
- **favicon**: icono simplificado y legible en 16–32 px.
- **og_image**: composición preparada para preview social (1200x630).

## Qué no hacer

- No cambiar nombres de archivo finales.
- No subir assets a otra carpeta distinta de `docs/assets/media/app/`.
- No tocar HTML, CSS ni includes si solo cambian assets.
- No forzar proporciones que rompan composición del layout actual.
- No activar YouTube/Play sin URL real y flags coherentes en `public-links.yml`.
