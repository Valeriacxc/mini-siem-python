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

## Cómo funciona

El sistema lee un archivo de logs (`ejemplo.log`) y analiza cada línea utilizando expresiones regulares.

Cuando detecta un patrón sospechoso, extrae información relevante como:

- Fecha del evento
- Dirección IP
- Tipo de evento
- Severidad

Luego almacena los eventos detectados en una base de datos SQLite y muestra un resumen en consola.

## Cómo ejecutar

Desde la raíz del proyecto, ejecutar:

bash
python main.py

=== MINI SIEM EN PYTHON ===
Inicializando base de datos...
Leyendo archivo de log: logs/ejemplo.log

Procesamiento terminado. Eventos sospechosos detectados: 8

=== TODOS LOS EVENTOS ===
ID: 1 | IP: 192.168.1.15 | Tipo: Intento de login fallido | Severidad: Media
ID: 2 | IP: 10.0.0.5 | Tipo: Acceso denegado | Severidad: Alta
ID: 3 | IP: 172.16.0.8 | Tipo: Conexión SSH | Severidad: Media

Objetivo del proyecto
Este prototipo busca demostrar el uso de Python para procesar datos de logs, detectar patrones relevantes y almacenar eventos para su posterior análisis.

## Autor
Valeria Cofré
