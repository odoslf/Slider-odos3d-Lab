# Binarios pendientes de normalización manual

Codex no debe tocar binarios en este repositorio. Las imágenes deben prepararse fuera de Codex y subirse manualmente.

## Archivos pendientes

### Favicon e iconos
Generar desde `docs/assets/media/app/logo-final.png`:

- `docs/assets/media/app/favicon-final.png` — PNG real 512x512
- `docs/assets/media/app/favicon-32.png` — PNG real 32x32
- `docs/assets/media/app/favicon-16.png` — PNG real 16x16
- `docs/assets/media/app/apple-touch-icon.png` — PNG real 180x180

Cuando esos archivos existan, se podrá activar su referencia en `docs/_includes/head-custom.html` y `docs/site.webmanifest`.

### Open Graph
Normalizar manualmente:

- `docs/assets/media/app/og-home-final.jpg` — JPEG real 1200x630

### JPG que ahora deben revisarse manualmente
Revisar/convertir fuera de Codex si hace falta:

- `docs/assets/media/app/slider-dslr-final.jpg`
- `docs/assets/media/app/video-thumb-final.jpg`
- `docs/assets/media/gallery/slider-gallery-01-overview-a.jpg`
- `docs/assets/media/gallery/slider-gallery-02-overview-b.jpg`
- `docs/assets/media/gallery/slider-gallery-03-in-use-mobile.jpg`

## Regla del repo

No pedir a Codex que convierta, regenere o sobrescriba binarios. Codex solo puede preparar referencias de texto después de que los archivos finales existan.
