---
title: "Workflow de subida interno"
permalink: /upload-workflow/
---

# Workflow de subida (hardware + media pública)

## 1) Subida de archivos STL / STEP / BOM

- STL: `prints/STL/v1/`
- STEP: `prints/STEP/v1/`
- BOM: `prints/BOM/v1/`

Pasos:
1. Subir archivos en la carpeta correcta.
2. Validar nombres limpios y consistentes.
3. Commit + push.
4. Mantener histórico al abrir nuevas versiones (`v2`, `v3`, …).

## 2) Assets de app/site pública

- Carpeta final: `docs/assets/media/app/`
- Registro: `docs/_data/public-media.yml`

Este flujo sigue vigente para home, branding y media general del sitio público.

## 3) Assets de galería pública nueva

- Carpeta final: `docs/assets/media/gallery/`
- Registro: `docs/_data/gallery-media.yml`

La galería pública premium `/gallery/` y `/en/gallery/` se alimenta **solo** desde ese registro.

## 4) Sustitución de placeholder por foto real de galería

1. Subir la foto real con el **nombre final exacto** en `docs/assets/media/gallery/`.
2. Cambiar `active_source` del slot correspondiente a `final` en `docs/_data/gallery-media.yml`.
3. Ejecutar auditoría: `python scripts/public_site_audit.py`.
4. Revisar visualmente ES/EN:
   - `/gallery/`
   - `/en/gallery/`

> Si el archivo final ya tiene nombre congelado correcto, no hay que tocar HTML ni CSS estructural.
