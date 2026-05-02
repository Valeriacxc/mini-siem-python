# Mini SIEM en Python
## Descripción
Este proyecto corresponde a un prototipo básico de SIEM desarrollado en Python, orientado al análisis de archivos de logs y detección de eventos sospechosos mediante expresiones regulares.

El sistema procesa registros desde archivos `.log`, identifica patrones asociados a eventos de seguridad y almacena los resultados en una base de datos SQLite.

## Tecnologías utilizadas
- Python
- SQLite
- Expresiones regulares (Regex)

## Funcionalidades
- Lectura de archivos de logs
- Detección de eventos sospechosos
- Identificación de direcciones IP
- Clasificación de eventos por tipo
- Almacenamiento en base de datos
- Visualización de resultados en consola

## Eventos detectados
- Intentos de login fallido
- Accesos denegados
- Conexiones SSH
- Conexiones RDP
- Cambios de configuración

## Estructura del proyecto
mini-siem-python/
├── main.py
├── db.py
├── logs/
│ └── ejemplo.log

## Autor
Valeria Cofré
