def read_log_file(file_path: str) -> list[str]: 

    lines = [] 

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    lines.append(clean_line)

    except FileNotFoundError:
        print(f"[ERROR] no sé encontro el archivo: {file_path}")

    except Exception as e:
        print(f"[ERROR] ocurrió un problema al leer el archivo: {e}")

    return lines

