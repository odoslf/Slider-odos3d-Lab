---
title: "Firmware (GRBL 1.1)"
permalink: /grbl/
---

{% include topnav.html %}

# Firmware (GRBL 1.1)

El firmware recomendado para este slider es **GRBL 1.1** (en la rama oficial suele indicarse como **v1.1h**).

## Repo oficial (créditos)
- **Proyecto:** GRBL (gnea/grbl)
- **Autoría y mantenimiento:** Sungeun “Sonny” Jeon y la comunidad
- **Licencia:** GPLv3
- **Enlace oficial:** https://github.com/gnea/grbl

> Nota: este repositorio (**Slider-odos3d-Lab**) no sustituye al repo de GRBL.  
> Aquí guardamos **documentación, ajustes recomendados y troubleshooting** para el hardware del slider.

## Archivos útiles en este repo
- Puesta en marcha: [grbl/setup.md]({{ site.blob_base }}/grbl/setup.md)
- Ajustes recomendados: [grbl/recommended_settings.md]({{ site.blob_base }}/grbl/recommended_settings.md)
- Preset 60 cm: [grbl/presets/slider_60cm_o2.txt]({{ site.blob_base }}/grbl/presets/slider_60cm_o2.txt)
- Protocolo GRBL (comandos): [grbl/app_protocol.md]({{ site.blob_base }}/grbl/app_protocol.md)
- Notas del montaje y mods opcionales: [grbl/mods_slider_odos3d.md]({{ site.blob_base }}/grbl/mods_slider_odos3d.md)
- Homing solo X: [grbl/only_x_homing.md]({{ site.blob_base }}/grbl/only_x_homing.md)
- Ajuste de drivers A4988 (Vref): [grbl/a4988_vref.md]({{ site.blob_base }}/grbl/a4988_vref.md)

## Qué necesitas para dejarlo fino
1) Flashear GRBL 1.1 en la controladora compatible.
2) Guardar el “estado base” con `$$`.
3) Ajustar pasos/mm, velocidad, aceleración y recorrido máximo (especialmente `$100`, `$110`, `$120`, `$130`).
4) Si hay finales de carrera: activar y probar homing (`$22`, `$23`, `$27`).
