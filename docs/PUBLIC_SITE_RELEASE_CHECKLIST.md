# PUBLIC SITE RELEASE CHECKLIST

Checklist interno para publicar la capa pública cuando lleguen assets reales y URLs finales.

## Inventario maestro y orden de petición

- Estado operativo único: `docs/_data/asset-status.yml`
- Orden oficial de solicitud: `docs/ASSET_REQUEST_ORDER.md`

## Flujo operativo obligatorio

1. Identificar asset en `asset-status.yml`.
2. Pedir archivo según `ASSET_REQUEST_ORDER.md`.
3. Subir con nombre final congelado a carpeta final.
4. Marcar `uploaded_to_repo: true`.
5. Cambiar `active_source` a `final` en registry (`public-media.yml` o `gallery-media.yml`).
6. Marcar `activated_in_yaml: true`.
7. Ejecutar auditoría.
8. Revisión visual ES/EN.

## Sustitución de assets reales APP

Sustituir en `docs/assets/media/app/`:
- logo real → `logo-final.svg`
- hero real → `hero-final.jpg`
- slider mobile real → `slider-mobile-final.jpg`
- slider dslr real → `slider-dslr-final.jpg`
- screenshot app real → `app-screenshot-final.png`
- video thumb real → `video-thumb-final.jpg`
- favicon real → `favicon-final.svg`
- og image real → `og-home-final.jpg`

## Sustitución de assets reales GALERÍA

Sustituir en `docs/assets/media/gallery/`:
- overview a real → `slider-gallery-01-overview-a.jpg`
- overview b real → `slider-gallery-02-overview-b.jpg`
- carriage a real → `slider-gallery-03-carriage-a.jpg`
- carriage b real → `slider-gallery-04-carriage-b.jpg`
- belt a real → `slider-gallery-05-belt-a.jpg`
- belt b real → `slider-gallery-06-belt-b.jpg`
- electronics real → `slider-gallery-07-electronics.jpg`
- endstop x real → `slider-gallery-08-endstop-x.jpg`
- phone mount real → `slider-gallery-09-phone-mount.jpg`

## Validación final

- [ ] Ejecutar `python scripts/public_site_audit.py` y confirmar PASS.
- [ ] Revisar `/` y `/en/`.
- [ ] Revisar `/hardware/`, `/downloads/`, `/support/` y equivalentes EN.
- [ ] Revisar `/gallery/` y `/en/gallery/`.
- [ ] Revisar favicon y OG image.
- [ ] Confirmar que no quedan placeholders activados si el release ya es final.

## Qué NO tocar si solo cambian assets

- No tocar templates HTML, includes ni layouts.
- No tocar CSS ni estructura visual.
- No tocar rutas públicas ni slugs.
- No tocar textos legales salvo necesidad legal real.


- [ ] Activar **YouTube real** solo con URL final en `public-links.yml`.
- [ ] Activar **Play Store real** solo con URL final en `public-links.yml`.

## Revisión final antes de publicar

Confirmar checklist completo, auditoría en PASS y revisión visual ES/EN cerrada.
