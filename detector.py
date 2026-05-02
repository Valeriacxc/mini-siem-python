import re
from datetime import datetime

def extract_ip(log_line: str)->str:
    match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log_line)
    return match.group() if match else "IP desconocida"

def extract_date(log_line: str)->str:
    match = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", log_line)
    return match.group(1) if match else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def detect_event(log_line: str)->dict | None:
    lower_line = log_line.lower()
    event_date = extract_date(log_line)
    source_ip = extract_ip(log_line)

    rules = [
        {
            "keywords": ["failed login", "login failed", "failed"],
            "event_type": "Intento de login fallido",
            "severity": "Media",
            "description": "Se detectó un intento de autenticación fallido."
        },
        {
            "keywords": ["denied", "access denied"],
            "event_type": "Acceso denegado",
            "severity": "Alta",
            "description": "Se detectó un acceso denegado."
        },
        {
            "keywords": ["ssh"],
            "event_type": "Conexión SSH",
            "severity": "Media",
            "description": "Se detectó una conexión SSH."
        },
        {
            "keywords": ["rdp"],
            "event_type": "Conexión RDP",
            "severity": "Alta",
            "description": "Se detectó una conexión RDP."
        },
        {
            "keywords": ["admin configuration changed", "configuration changed"],
            "event_type": "Cambio administrativo",
            "severity": "Crítica",
            "description": "Se detectó un cambio administrativo sospechoso."
        }
    ]
    for rule in rules:
        for keyword in rule["keywords"]:
            if keyword in lower_line:
                return {
                    "date": event_date,
                    "source_ip": source_ip,
                    "event_type": rule["event_type"],
                    "description": f'{rule["description"]} Línea original: {log_line}',
                    "severity": rule["severity"]
                }
    return None 

  
