---
title: "Workflow de subida"
permalink: /upload-workflow/
---

# Guía rápida de subida (STL / STEP / BOM / Fotos)

## 1) Subir STL / STEP / BOM (v1 actual)

- STL: `prints/STL/v1/`
- STEP: `prints/STEP/v1/`
- BOM: `prints/BOM/v1/`

Pasos rápidos:
1. Arrastra archivos a la carpeta correcta.
2. Verifica nombres limpios (sin espacios raros ni acentos extraños).
3. Commit y push.

## 2) Crear una nueva versión (v2, v3…)

1. Crear carpetas nuevas:
   - `prints/STL/v2/`
   - `prints/STEP/v2/`
   - `prints/BOM/v2/`
2. Copiar/subir archivos de la nueva versión.
3. Mantener la versión anterior para histórico.
4. Actualizar `docs/downloads.md` para que la sección "Última versión" apunte a `v2`.

## 3) Añadir fotos a galería

- Carpeta: `images/gallery/`
- Sube solo fotos técnicas limpias del producto/proceso.

## 4) Nombres de archivo recomendados

Formato sugerido:
- STL/STEP: `slider-odos3d_<pieza>_v1.stl` / `slider-odos3d_<pieza>_v1.step`
- BOM: `slider-odos3d_bom_v1.csv` o `slider-odos3d_bom_v1.xlsx`
- Fotos: `slider-odos3d_<tema>_v1_01.jpg`

Evitar:
- Espacios dobles o nombres genéricos (`final-final-ok.stl`).
- Caracteres problemáticos para rutas (`#`, `?`, `&`).
