import subprocess

# Archivos
archivo_lectura = "notas.txt"
archivo_writer = "detector.py"
archivo_writer_b = "escritor.py"
archivo_detector = "detector.py"

try:
    # Leer todas las líneas de notas.txt
    with open(archivo_lectura, "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]  # eliminar líneas vacías

    # Leer contenido original de writer.py
    with open(archivo_writer, "r", encoding="utf-8") as f:
        contenido = f.readlines()

    # Procesar cada línea
    for linea in lineas:
        # Modificar la línea del valor por defecto
        nuevo_contenido = []
        for c in contenido:
            if c.strip().startswith("write_text(text="):
                nuevo_contenido.append(f'write_text(text="{linea}", x=None, y=None)\n')
            else:
                nuevo_contenido.append(c)

        # Sobrescribir writer.py
        with open(archivo_writer, "w", encoding="utf-8") as f:
            f.writelines(nuevo_contenido)

        print(f"Se actualizó writer.py con la línea: {linea}")

        # Ejecutar detector.py después de modificar writer.py
        print(f"Ejecutando {archivo_detector}...")
        subprocess.run(["python", archivo_detector], check=True)

except FileNotFoundError:
    print(f"⚠️ No se encontró '{archivo_lectura}', '{archivo_writer}' o '{archivo_detector}'")
except Exception as e:
    print(f"⚠️ Ocurrió un error: {e}")
