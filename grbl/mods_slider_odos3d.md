# Enfoque del montaje (O2) — Slider 60 cm

## Lo que define tu montaje
- Final de carrera SOLO en **X-** (inicio)
- Límite seguro X: **600 mm**
- Eje Y sin final de carrera (eje auxiliar)

## Comportamiento deseado
- X siempre “vuelve al inicio” (X-) cuando se hace homing
- X nunca se pasa de 60 cm de recorrido seguro

## Auto-homing al encender (opcional)
GRBL oficial normalmente hace homing cuando se ejecuta `$H`.
Si tú quieres que “al encender se vaya directo a X-”:
- eso implica un firmware modificado (opcional)

### Nota legal (simple y clara)
GRBL es GPLv3: si algún día distribuyes un firmware GRBL modificado (por ejemplo un `.hex`),
lo correcto es publicar el **código fuente de GRBL modificado** (solo esa parte).
Tu app puede seguir siendo propietaria.
