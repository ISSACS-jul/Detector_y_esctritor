#!/usr/bin/env python3
import subprocess

archivo_objetivo = "input.py"   # archivo que se va a modificar
archivo_lineas = "notas.txt"    # archivo con los números
linea_insercion = 30            # número de línea donde insertar (0 = primera línea)
script_a_ejecutar = ["./click"] # comando a ejecutar

def procesar_lineas():
    # Leer todos los números desde el archivo
    with open(archivo_lineas, "r", encoding="utf-8") as f:
        numeros = f.readlines()

    for i, num in enumerate(numeros, 1):
        num = num.strip()
        linea_mod = f'texto="{num}"\n'

        print(f"Procesando número {i}: {num}")

        # Leer archivo objetivo
        with open(archivo_objetivo, "r", encoding="utf-8") as f:
            lineas_obj = f.readlines()

        # Insertar la línea en la posición deseada
        lineas_obj.insert(linea_insercion, linea_mod)

        # Guardar el archivo modificado
        with open(archivo_objetivo, "w", encoding="utf-8") as f:
            f.writelines(lineas_obj)

        print("Línea insertada:", linea_mod.strip())

        # Ejecutar el script
        try:
            subprocess.run(script_a_ejecutar, check=True)
            print("Script ejecutado")
        except subprocess.CalledProcessError:
            print("Error ejecutando el script")

        # Quitar la línea que se había insertado
        with open(archivo_objetivo, "w", encoding="utf-8") as f:
            for linea in lineas_obj:
                if linea != linea_mod:
                    f.write(linea)

        print("Línea eliminada:", linea_mod.strip())

if __name__ == "__main__":
    procesar_lineas()


