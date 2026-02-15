# Límites y rangos (hardware + GRBL)

Este documento define límites para que el hardware y el control (GRBL/software) no se salgan de rango.

## 1) Límites físicos del slider
- Recorrido útil (mm): _____
- Finales de carrera: SI/NO
- Zona segura (margen antes del final): _____ mm
- Carga recomendada (cámara/móvil): _____

## 2) GRBL (parámetros relacionados con límites)
Pegar valores reales cuando tengamos el `$$`.

- Velocidad máxima X ($110): _____
- Aceleración X ($120): _____
- Recorrido máximo X ($130): _____
- Homing ($22): _____
- Dirección homing ($23): _____
- Pull-off ($27): _____

## 3) Reglas de seguridad
- Nunca poner $130 por encima del recorrido real.
- Si hay finales de carrera: homing activo y probado.
- Si cambian pasos/mm o mecánica: recalibrar.
