# lector.py
import detector  # importamos el módulo
from escritor import write_text

# Archivo de lectura
archivo_lectura = "notas.txt"

try:
    with open(archivo_lectura, "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]

    for linea in lineas:
        print(f"Procesando línea: {linea}")
        # Llama a detector directamente con el texto
        detector.detect_click(text=linea)

except FileNotFoundError:
    print(f" No se encontró '{archivo_lectura}'")
except Exception as e:
    print(f" Ocurrió un error: {e}")
