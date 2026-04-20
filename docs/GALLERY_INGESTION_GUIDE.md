# GALLERY_INGESTION_GUIDE

Guía interna para ingestión de fotos reales en la galería pública premium.

## Inventario maestro y orden de petición

- Estado único de todos los assets: `docs/_data/asset-status.yml`
- Orden humano de solicitud (1→17): `docs/ASSET_REQUEST_ORDER.md`

## Ruta final obligatoria

Todas las fotos reales de galería van en:

- `docs/assets/media/gallery/`

## Tabla de slots congelados

| slot_key | archivo final | sección ES | ratio | uso esperado |
|---|---|---|---|---|
| slot_overview_a | slider-gallery-01-overview-a.jpg | Visión general | 16:9 | Vista principal del slider montado |
| slot_overview_b | slider-gallery-02-overview-b.jpg | Visión general | 16:9 | Vista general complementaria |
| slot_carriage_a | slider-gallery-03-carriage-a.jpg | Carro y guiado | 4:3 | Carro en primer plano técnico |
| slot_carriage_b | slider-gallery-04-carriage-b.jpg | Carro y guiado | 4:3 | Detalle alternativo del guiado |
| slot_belt_a | slider-gallery-05-belt-a.jpg | Correa y transmisión | 16:9 | Correa/poleas en vista funcional |
| slot_belt_b | slider-gallery-06-belt-b.jpg | Correa y transmisión | 16:9 | Vista secundaria de transmisión |
| slot_electronics | slider-gallery-07-electronics.jpg | Electrónica y control | 4:3 | Controladora, drivers y cableado |
| slot_endstop_x | slider-gallery-08-endstop-x.jpg | Electrónica y control | 1:1 | Detalle del endstop X |
| slot_phone_mount | slider-gallery-09-phone-mount.jpg | Accesorios | 4:3 | Soporte de móvil y anclaje |

## Flujo operativo real (galería + maestro)

1. Identificar asset en `docs/_data/asset-status.yml`.
2. Pedir al usuario el archivo según `docs/ASSET_REQUEST_ORDER.md`.
3. Subir la foto final al nombre congelado exacto en `docs/assets/media/gallery/`.
4. Marcar `uploaded_to_repo: true` en `asset-status.yml`.
5. En `docs/_data/gallery-media.yml`, cambiar `active_source` a `final` para ese slot.
6. Marcar `activated_in_yaml: true` en `asset-status.yml`.
7. Ejecutar `python scripts/public_site_audit.py`.
8. Revisar visualmente `/gallery/` y `/en/gallery/`.

## Qué revisar después

- Alt/caption correctos en ES/EN.
- Encuadre real respeta ratio declarado.
- El slot correcto muestra la foto correcta.

## Qué no hacer

- No subir fotos de galería en `docs/assets/media/app/`.
- No renombrar los 9 archivos congelados.
- No editar plantillas HTML/CSS para cada foto.
- No reintroducir rutas `images/gallery/` ni `raw.githubusercontent` para la galería nueva.
