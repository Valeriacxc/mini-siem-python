from db import create_connection

def show_all_events():
    conn= create_connection()
    cursor= conn.cursor()

    cursor.execute("""
        SELECT id, date, source_ip, event_type, severity
        FROM events
        ORDER BY date ASC
    """)

    rows= cursor.fetchall()
    conn.close()

    print("\n=== TODOS LOS EVENTOS ===")

    if not rows:
        print("No hay eventos registrados.")
        return

    for row in rows:
        print(f"ID: {row[0]} | Fecha: {row[1]} | IP: {row[2]} | Tipo: {row[3]} | Severidad: {row[4]}")

def show_event_summary():
    conn= create_connection()
    cursor= conn.cursor()

    cursor.execute("""
        SELECT event_type, COUNT(*)
        FROM events
        GROUP BY event_type
        ORDER BY COUNT(*) DESC
    """)
    rows = cursor.fetchall()
    conn.close()

    print("\n=== RESUMEN POR TIPO DE EVENTO ===")

    if not rows:
        print("No hay datos para mostrar.")
        return

    for row in rows:
        print(f"{row[0]}: {row[1]}")

