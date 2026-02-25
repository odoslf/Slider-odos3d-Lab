# Ajustes recomendados (Slider-odos3d · 60 cm)

## Idea del sistema
- **X** = eje del carril (tiene final de carrera en X- y límite seguro)
- **Y** = eje auxiliar (sin final de carrera; se deja libre)

## 1) Recorrido seguro (tu caso)
- Límite seguro X: **600 mm**
  - `$130=600.000`

## 2) Reporte en milímetros (recomendado)
- `$13=0`
Esto evita que la posición reportada salga en pulgadas.

> Nota: aunque un controlador mande `G21`, si `$13=1` el reporte puede confundir a quien lee posiciones.

## 3) Homing (mínimo)
- `$22=1`  (homing ON)
- `$23=0`  (dirección de homing; si va al revés, se ajusta)
- `$27=1.000` (pull-off)

Si SOLO tienes final de carrera en X:
- ver `grbl/only_x_homing.md`

## 4) Límites (elige una opción)

### Opción A — Simple (compatible, sin sustos)
- No activar soft limits.
- Dejar el límite como “seguridad” en preset/app.

### Opción B — Más segura (recomendable si homing está bien)
- `$20=1` (soft limits ON)
- mantener `$130=600.000`
- hacer homing `$H` antes de mover largo

## 5) No ponemos números “robot” para pasos y velocidades
Dependen de:
- poleas/correa, microstepping, motor, carga mecánica
Se calibran al final:
- `$100/$110/$120` para X
- `$101/$111/$121` para Y (si lo usas)

## Drivers (A4988)
Aunque no es un ajuste de GRBL, el rendimiento depende de la corriente del driver.
- Ver: `grbl/a4988_vref.md`
