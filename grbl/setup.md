# GRBL — Puesta en marcha (Slider-odos3d)

## 1) Montaje objetivo (tu caso)
- Arduino Nano + CNC Shield V4
- Drivers A4988
- 2 motores (X e Y)
- Final de carrera SOLO en **X-** (inicio del carril)
- Recorrido real ~61 cm, recorrido seguro configurado: **60 cm (600 mm)**

## 2) Créditos del firmware
GRBL 1.1 (gnea/grbl) — GPLv3  
Repo oficial: https://github.com/gnea/grbl

## 3) Prueba rápida en consola (lo mínimo)
1) Ver configuración:
- `$$`  (guárdala como backup)

2) Si aparece ALARM:
- `$X`  (unlock)

3) Estado:
- `?`   (debe devolver una línea tipo `<Idle|...|MPos:...>` o `<Idle|...|WPos:...>`)

4) Ver modo actual:
- `$G`  (busca `G21` si quieres confirmar mm)

## 4) Homing
- Homing manual: `$H`

Tu montaje tiene final de carrera SOLO en X:
- Ver: `grbl/only_x_homing.md` (cómo dejar `$H` coherente solo con X)

## 5) Aplicar preset Slider 60 cm
- Ver: `grbl/presets/slider_60cm_o2.txt`

## 6) “Pulgadas vs mm” (sin líos)
- El control usa milímetros.
- Para evitar confusiones al reportar posición:
  - usa `$13=0` (recomendado)
- Si alguien tiene un arranque que pone pulgadas (G20), se corrige en `startup blocks` (ver preset).

## 7) Drivers A4988 (muy recomendado)
Antes de hacer pruebas largas, ajusta el límite de corriente (Vref) de los A4988.
- Guía y vídeo recomendado: `grbl/a4988_vref.md`
