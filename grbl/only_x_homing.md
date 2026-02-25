# Homing SOLO en X (final de carrera solo en X-)

## Por qué hace falta
Si solo tienes final de carrera en **X**, quieres que `$H` haga homing únicamente en X
y no “dependa” de ejes que no tienen switch.

## Forma correcta (sin publicar parches aquí)
Se compila GRBL ajustando el ciclo de homing para incluir SOLO el eje X
(en GRBL esto se controla desde su configuración del homing).

## Alternativas si no quieres compilar
- Usar homing solo cuando toque (`$H`) y mantener Y como eje sin homing
- O desactivar homing (`$22=0`) y trabajar con límites/preset y cuidado (menos recomendable)

## Qué documentar siempre
- Que el final de carrera está en **X-**
- Que el límite seguro X es **600 mm** (`$130=600.000`)
