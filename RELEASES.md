# Releases oficiales (descargas)

Este repositorio se distribuye mediante **GitHub Releases**.
El objetivo es que el público descargue **versiones oficiales** (v1, v1.1, v2…) con piezas y documentación coherentes.

## Qué debe incluir una Release
Adjunta como assets (archivos) en la Release:

1) `ODOS3D_Lab_vX.Y_prints_STL.zip`
   - Contenido: `prints/STL/vX.Y/` (solo STL listos para imprimir)

2) `ODOS3D_Lab_vX.Y_prints_STEP.zip`
   - Contenido: `prints/STEP/vX.Y/` (STEP para CAD)

3) `ODOS3D_Lab_vX.Y_docs.zip` (opcional)
   - Contenido: `docs/` + `hardware/` + `grbl/` (BOM, montaje, calibración, límites)

> Nota: El repo es público, pero las **descargas recomendadas** son las Releases.

## Estructura esperada dentro del ZIP (referencia)
- STL: `prints/STL/vX.Y/...`
- STEP: `prints/STEP/vX.Y/...`
- Docs: `docs/...` + `hardware/...` + `grbl/...`

## Checklist rápido antes de publicar
- [ ] Los STL/STEP están en la carpeta de versión correcta `vX.Y`
- [ ] BOM actualizada: `hardware/bom.md`
- [ ] Guía de montaje revisada: `docs/assembly_guide.md`
- [ ] Ajustes GRBL revisados: `grbl/recommended_settings.md`
- [ ] `CHANGELOG.md` actualizado
- [ ] La web (Pages) refleja enlaces correctos (privacidad / términos / checklist)

## Notas de soporte
Este repo es **solo lectura**:
- No se ofrece soporte público.
- Contacto: odos3d@gmail.com
