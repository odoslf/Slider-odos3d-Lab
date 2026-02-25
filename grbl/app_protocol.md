# Protocolo de control (GRBL) — comandos estándar

> Nota: esto NO incluye código de ninguna app.
> Solo describe comandos GRBL estándar que se usan en sliders.

## Básicos
- Estado: `?`
- Unlock: `$X`
- Homing: `$H`
- Ver modo: `$G`
- Ver configuración: `$$`
- Ver startup blocks: `$N`

## Movimiento típico
- Absoluto en mm: `G90 G21` y luego `G1 X... F...`
- Jog en mm: `$J=G91 G21 F... X...`

## Diagnóstico rápido
Si “conecta pero no mueve”:
1) `?` debe responder
2) si hay ALARM → `$X`
3) comprobar que existe `MPos:` o `WPos:` en la línea de estado
