---
title: "Montaje rápido (10 pasos)"
permalink: /quick-assembly/
---

{% include topnav.html %}

# Montaje rápido (10 pasos)

> Esto es un resumen “humano”. El diseño exacto lo definen los STL/STEP del pack.

1) Imprime las piezas del pack v1 (`prints/STL/v1/`)
2) Prepara varillas Ø8mm a la medida del modelo
3) Monta el carro y comprueba que desliza suave
4) Monta poleas/correa GT2 y deja tensión correcta
5) Monta motores NEMA17 y verifica alineación
6) Monta Arduino Nano + CNC Shield V4 + A4988
7) Ajusta la corriente (Vref) de los A4988  
   → ver guía: `/grbl/` → “A4988 Vref”
8) Conecta final de carrera X- (inicio)
9) Flashea GRBL 1.1 oficial y aplica preset 60 cm
10) Haz homing y prueba recorrido corto antes de hacer recorrido largo

Listo: ya puedes usar el slider con seguridad.
