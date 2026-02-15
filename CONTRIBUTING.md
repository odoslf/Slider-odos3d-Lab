# Contribuir

## Reglas
- Este repo es hardware/piezas/docs/GRBL. No se sube código de la app aquí.
- Todo debe ser reproducible: archivos + docs + BOM + ajustes.

## Convención de nombres (recomendada)
`odos3d_<categoria>_<pieza>_vX_Y.ext`

Ejemplos:
- `odos3d_carriage_main_v1_0.stl`
- `odos3d_endstop_mount_v1_0.stl`

## Qué debe traer un aporte (mínimo)
- STL (y STEP si existe)
- Nota rápida de impresión (en `docs/print_settings.md`)
- Si cambia tornillería/material: actualizar `hardware/bom.md`
- Si cambia montaje: actualizar `docs/assembly_guide.md`
