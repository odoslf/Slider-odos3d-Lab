# ORDEN MAESTRO DE PETICIÓN DE ASSETS (1→17)

Este documento define el orden único en que se pedirán los archivos reales.

- Primero se piden los **assets de app/landing** (1→8).
- Después se piden los **assets de galería técnica** (9→17).
- Al recibir cada archivo **no se toca HTML ni CSS**: solo subida + actualización de YAML + auditoría.

## Lista ordenada exacta

1. **Logo de marca** (`asset_key: logo`)
   - Archivo final: `logo-final.png`
   - Dónde se usa: header global ES/EN y páginas públicas secundarias.
   - Imagen esperada: logo vectorial limpio de marca.
   - Transparencia: **sí**.
   - Encuadre: **cuadrado (1:1)**.

2. **Hero principal app** (`asset_key: hero`)
   - Archivo final: `hero-final.jpg`
   - Dónde se usa: home ES/EN y apoyo en descargas.
   - Imagen esperada: foto horizontal premium del ecosistema.
   - Transparencia: no.
   - Encuadre: **horizontal (16:10)**.

3. **Captura principal de app** (`asset_key: app_screenshot`)
   - Archivo final: `app-screenshot-final.jpg`
   - Dónde se usa: home, downloads y support ES/EN.
   - Imagen esperada: screenshot real y limpio de UI.
   - Transparencia: no.
   - Encuadre: **horizontal (16:9)**.

4. **Slider con móvil** (`asset_key: slider_mobile`)
   - Archivo final: `slider-mobile-final.jpg`
   - Dónde se usa: bloques hardware/proof ES/EN.
   - Imagen esperada: slider real con móvil montado.
   - Transparencia: no.
   - Encuadre: **horizontal (16:9)**.

5. **Slider con DSLR** (`asset_key: slider_dslr`)
   - Archivo final: `slider-dslr-final.jpg`
   - Dónde se usa: bloques hardware/proof ES/EN.
   - Imagen esperada: slider real en flujo DSLR.
   - Transparencia: no.
   - Encuadre: **horizontal (16:9)**.

6. **Miniatura de vídeo demo** (`asset_key: video_thumb`)
   - Archivo final: `video-thumb-final.jpg`
   - Dónde se usa: bloque vídeo en home ES/EN.
   - Imagen esperada: miniatura real con espacio para overlay.
   - Transparencia: no.
   - Encuadre: **horizontal (16:9)**.

7. **Favicon** (`asset_key: favicon`)
   - Archivo final: `favicon-final.png`
   - Dónde se usa: head global + manifest + 404.
   - Imagen esperada: icono simplificado de marca.
   - Transparencia: **sí**.
   - Encuadre: **cuadrado (1:1)**.

8. **Imagen social OG** (`asset_key: og_image`)
   - Archivo final: `og-home-final.jpg`
   - Dónde se usa: Open Graph/Twitter ES/EN.
   - Imagen esperada: composición social final.
   - Transparencia: no.
   - Encuadre: **horizontal social (1200:630)**.

9. **Galería overview A** (`asset_key: overview_a`)
   - Archivo final: `slider-gallery-01-overview-a.jpg`
   - Dónde se usa: sección Visión general / Overview.
   - Imagen esperada: vista general principal del slider.
   - Transparencia: no.
   - Encuadre: **horizontal (16:9)**.

10. **Galería overview B** (`asset_key: overview_b`)
    - Archivo final: `slider-gallery-02-overview-b.jpg`
    - Dónde se usa: sección Visión general / Overview.
    - Imagen esperada: segunda vista general del slider.
    - Transparencia: no.
    - Encuadre: **horizontal (16:9)**.

11. **Galería carriage A** (`asset_key: carriage_a`)
    - Archivo final: `slider-gallery-03-in-use-mobile.jpg`
    - Dónde se usa: sección Carro y guiado / Carriage and guidance.
    - Imagen esperada: detalle técnico de carro.
    - Transparencia: no.
    - Encuadre: **horizontal (4:3)**.

12. **Galería carriage B** (`asset_key: carriage_b`)
    - Archivo final: `slider-gallery-04-in-use-dslr.jpg`
    - Dónde se usa: sección Carro y guiado / Carriage and guidance.
    - Imagen esperada: detalle alternativo de guiado.
    - Transparencia: no.
    - Encuadre: **horizontal (4:3)**.

13. **Galería belt A** (`asset_key: belt_a`)
    - Archivo final: `slider-gallery-05-belt-a.jpg`
    - Dónde se usa: sección Correa y transmisión / Belt and drive.
    - Imagen esperada: transmisión principal con correa/poleas.
    - Transparencia: no.
    - Encuadre: **horizontal (16:9)**.

14. **Galería belt B** (`asset_key: belt_b`)
    - Archivo final: `slider-gallery-06-belt-b.jpg`
    - Dónde se usa: sección Correa y transmisión / Belt and drive.
    - Imagen esperada: vista secundaria de transmisión.
    - Transparencia: no.
    - Encuadre: **horizontal (16:9)**.

15. **Galería electronics** (`asset_key: electronics`)
    - Archivo final: `slider-gallery-07-electronics.jpg`
    - Dónde se usa: sección Electrónica y control / Electronics and control.
    - Imagen esperada: electrónica y control en plano claro.
    - Transparencia: no.
    - Encuadre: **horizontal (4:3)**.

16. **Galería endstop X** (`asset_key: endstop_x`)
    - Archivo final: `slider-gallery-08-endstop-x.jpg`
    - Dónde se usa: sección Electrónica y control / Electronics and control.
    - Imagen esperada: detalle del final de carrera X.
    - Transparencia: no.
    - Encuadre: **cuadrado (1:1)**.

17. **Galería phone mount** (`asset_key: phone_mount`)
    - Archivo final: `slider-gallery-09-phone-mount.jpg`
    - Dónde se usa: sección Accesorios / Accessories.
    - Imagen esperada: accesorio soporte móvil montado.
    - Transparencia: no.
    - Encuadre: **horizontal (4:3)**.

## Flujo operativo al recibir cada asset

1. Identificar asset en `docs/_data/asset-status.yml`.
2. Pedir archivo según este orden.
3. Subir al nombre final congelado en carpeta final.
4. Marcar `uploaded_to_repo: true` en `asset-status.yml`.
5. Cambiar `active_source` a `final` en su registry (`public-media.yml` o `gallery-media.yml`).
6. Marcar `activated_in_yaml: true` en `asset-status.yml`.
7. Ejecutar `python scripts/public_site_audit.py`.
8. Revisión visual ES/EN.
