# PUBLIC SITE RELEASE CHECKLIST

Checklist interno para publicar la capa pública cuando lleguen assets reales y URLs finales.

## 1) Assets reales a sustituir

Sustituir en `docs/assets/media/app/`:
- logo real → `logo-final.svg`
- hero real → `hero-final.jpg`
- slider mobile real → `slider-mobile-final.jpg`
- slider dslr real → `slider-dslr-final.jpg`
- screenshot app real → `app-screenshot-final.png`
- video thumb real → `video-thumb-final.jpg`
- favicon real → `favicon-final.svg`
- og image real → `og-home-final.jpg`

## 2) Dónde tocar configuración

- Revisar/actualizar rutas de media en `docs/_data/public-media.yml`.
- Revisar/actualizar identidad y enlaces públicos en `docs/_data/public-links.yml`.

## 3) Claves YAML a revisar

En `public-links.yml`:
- `site_identity.product_name`
- `site_identity.product_name_short`
- `site_identity.support_email`
- `external_links.youtube_url`
- `external_links.play_store_url`
- `flags.has_youtube`
- `flags.has_play_store`

En `public-media.yml`:
- `site_media.*.placeholder_path`
- `site_media.*.final_path`
- `site_media.*.active_source`
- `site_media.*.target_filename`
- `site_media.*.target_directory`
- `site_media.*.preferred_format`
- `site_media.*.recommended_min_width`
- `site_media.*.recommended_min_height`
- `site_media.*.crop_strategy`
- `site_media.*.safe_area_notes`
- `site_media.*.transparency_required`
- `site_media.*.used_on_pages`
- `site_media.*.used_in_sections`
- `site_media.*.current_slot_source`
- `site_media.video_thumb.youtube_url_source`
- `site_media.*.is_placeholder`

## Sustitución de assets reales

- [ ] Sustituir **logo** real (`logo-final.svg`) y cambiar `site_media.logo.active_source` a `final`.
- [ ] Sustituir **hero** real (`hero-final.jpg`) y cambiar `site_media.hero.active_source` a `final`.
- [ ] Sustituir **slider mobile** real (`slider-mobile-final.jpg`) y cambiar `site_media.slider_mobile.active_source` a `final`.
- [ ] Sustituir **slider dslr** real (`slider-dslr-final.jpg`) y cambiar `site_media.slider_dslr.active_source` a `final`.
- [ ] Sustituir **screenshot app** real (`app-screenshot-final.png`) y cambiar `site_media.app_screenshot.active_source` a `final`.
- [ ] Sustituir **video thumb** real (`video-thumb-final.jpg`) y cambiar `site_media.video_thumb.active_source` a `final`.
- [ ] Sustituir **favicon** real (`favicon-final.svg`) y cambiar `site_media.favicon.active_source` a `final`.
- [ ] Sustituir **og image** real (`og-home-final.jpg`) y cambiar `site_media.og_image.active_source` a `final`.
- [ ] Activar **YouTube real** solo si hay URL final (`external_links.youtube_url` + `flags.has_youtube: true`).
- [ ] Activar **Play Store real** solo si hay URL final (`external_links.play_store_url` + `flags.has_play_store: true`).

## Validación después de sustituir assets

- [ ] Revisar home ES (`/`).
- [ ] Revisar home EN (`/en/`).
- [ ] Revisar hardware/downloads/support ES y EN.
- [ ] Revisar header/footer en desktop y móvil.
- [ ] Revisar OG image y favicons en previews.
- [ ] Ejecutar auditoría: `python scripts/public_site_audit.py`.

## 5) Revisión final antes de publicar

- Ejecutar `python scripts/public_site_audit.py` y confirmar `PASS`.
- Verificar visualmente `/` y `/en/` con los nuevos assets.
- Verificar favicon y OG image en preview social.
- Verificar que soporte/legal siguen con rutas correctas ES/EN.
- Confirmar que no aparecen placeholders en zonas públicas finales.

## 6) Revisión después del merge

- Confirmar workflow `Public Site Audit` en verde en `push` y `pull_request`.
- Confirmar publicación de Pages sin errores de rutas canónicas.
- Revisar una vez más sitemap/robots en entorno publicado.

## 7) Qué NO tocar si solo cambian assets

- No tocar templates HTML, includes ni layouts.
- No tocar rutas públicas ni slugs.
- No tocar textos legales salvo necesidad legal real.
- Limitarse a reemplazar archivos finales y ajustar YAML central.
