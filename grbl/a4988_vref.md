# A4988 — Ajuste de corriente (Vref) (recomendado)

En un montaje con **CNC Shield V4 + drivers A4988**, es **muy recomendable** ajustar el límite de corriente de cada driver (Vref).

## Por qué importa
- Si la corriente está **demasiado alta**: se calientan driver y motor, puede haber fallos y daños.
- Si está **demasiado baja**: el motor pierde fuerza y puede **perder pasos**.

## Tutorial recomendado (vídeo)
Para hacerlo bien sin liarte, sigue este tutorial de referencia (Pololu):
- “Setting the Current Limit on Pololu Stepper Motor Driver Carriers (video)”.
- Enlace: https://www.pololu.com/blog/484/video-setting-the-current-limit-on-pololu-stepper-motor-driver-carriers

## Fórmula (solo como referencia)
En A4988, la relación típica es:

- **Vref = 8 × Imax × Rcs**

⚠️ Importante: **Rcs (resistor de medida)** cambia según el módulo (hay valores típicos como 0.05Ω, 0.068Ω o 0.1Ω). Hay que mirar el que trae tu placa A4988.

> Consejo práctico: ajusta a un valor razonable (no al máximo) y verifica temperatura y que no pierda pasos.

## Nota de seguridad
No conectes/desconectes motores con el sistema alimentado. Ajusta con multímetro y calma.
(El texto del vídeo y la fórmula están respaldados por Pololu y referencias comunes de A4988.)
