from parser import read_log_file
from detector import detect_event
from db import create_tables, insert_event
from reports import show_all_events, show_event_summary

def main():
    log_path= "logs/ejemplo.log"

    print("=== MINI SIEM EN PYTHON ===")
    print("Inicializando base de datos...")
    create_tables()

    print(f"Leyendo archivo de log: {log_path}")
    log_lines = read_log_file(log_path)

    if not log_lines:
        print("No se encontraron líneas para procesar.")
        return

    detected_count = 0

    for line in log_lines:
        event = detect_event(line)

        if event:
            insert_event(
                event["date"],
                event["source_ip"],
                event["event_type"],
                event["description"],
                event["severity"]
            )
            detected_count += 1

    print(f"\nProcesamiento terminado. Eventos sospechosos detectados: {detected_count}")

    show_all_events()
    show_event_summary()

if __name__ == "__main__":
    main()