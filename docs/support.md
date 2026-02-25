---
layout: default
title: "Soporte"
permalink: /support/
---

{% include topnav.html %}

# Soporte

## FAQ

### No aparece el slider por Bluetooth
Activa Bluetooth y ubicación en Android, acerca el móvil al slider y vuelve a escanear desde la app. Si sigue sin aparecer, reinicia el módulo Bluetooth del slider y repite el emparejamiento.

### Android 12/13: permisos Bluetooth
En Android 12/13 debes aceptar permisos de **Bluetooth cercano** para escanear y conectar. Revisa Ajustes > Apps > Smart Timelapse AI > Permisos y habilita Bluetooth.

### GRBL en ALARM: cómo desbloquear ($X)
Si GRBL está en **ALARM**, abre consola y envía `$X` para desbloquear. Después ejecuta un homing o mueve ejes con cuidado para confirmar que no hay topes mecánicos.

### Exportación lenta o falla
Comprueba espacio libre en el dispositivo y desactiva ahorro de energía para la app durante la exportación. Si el proyecto es largo, prueba una resolución menor y cierra otras apps.

### Remoto Wi-Fi no conecta
Verifica que móvil y slider estén en la misma red. En hotspot o routers con **AP isolation** activo, los dispositivos pueden no verse entre sí. También revisa que no haya VPN activa.

### Simulación (sin slider): qué es
La simulación permite preparar tomas y tiempos sin hardware conectado. Sirve para planificar secuencias antes de ejecutar el movimiento real.

### DSLR: requiere relé/opto (no es USB directo)
El disparo DSLR requiere interfaz de relé/opto compatible con tu cámara. La app no dispara DSLR por USB directo; necesitas el cableado y electrónica adecuados.

### Eje Z no aparece
El eje Z solo aparece si tu hardware/firmware lo soporta. Actívalo en ajustes avanzados y confirma en GRBL que el eje está habilitado.

## Contacto
- Email: **[odos3d@gmail.com](mailto:odos3d@gmail.com)**
- Qué enviar: **captura + diagnóstico copiado**
