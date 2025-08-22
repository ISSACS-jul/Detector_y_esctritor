# lector.py
import os
import detector  # importamos el módulo
from escritor import write_text

# Colores ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Carpeta base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
archivo_lectura = os.path.join(BASE_DIR, "notas.txt")

def mostrar_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"                {YELLOW}····································································{CYAN}")
    print(f"                {YELLOW}:                                                                  :{CYAN}")
    print(f"─▄█▀█▄──▄███▄  {YELLOW}:   ░█▀▀░█░█░█▀▄░▀█▀░█▀▄░█▀█░█▀▄░░░█▀▄░█▀▀░░░█▀█░█▀█░▀█▀░█▀█░█▀▀   :{CYAN}─▄█▀█▄──▄███▄")
    print(f"▐█░██████████▌ {YELLOW}:   ░▀▀█░█░█░█▀▄░░█░░█░█░█░█░█▀▄░░░█░█░█▀▀░░░█░█░█░█░░█░░█▀█░▀▀█   :{CYAN}▐█░██████████▌")
    print(f"─██▒█████████  {YELLOW}:   ░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░░▀▀▀░▀░▀░░░▀▀░░▀▀▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀   :{CYAN}─██▒█████████")
    print(f"──▀████████▀   {YELLOW}:   ░█▀█░█▀▄░█▀█░█▀▀░█▀▀░█▀▀░█▀█░█▀▄░░░▀▀█░█░█░█░░░▀█▀░█▀█░█▀█     :{CYAN}──▀████████▀")
    print(f"─────▀██▀      {YELLOW}:   ░█▀▀░█▀▄░█░█░█▀▀░█▀▀░▀▀█░█░█░█▀▄░░░░░█░█░█░█░░░░█░░█▀█░█░█     :{CYAN}─────▀██▀")
    print(f".──────▀.      {YELLOW}:   ░▀░░░▀░▀░▀▀▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀     :{CYAN}.──────▀.")
    print(f"                {YELLOW}:                                                                  :{CYAN}")
    print(f"                {YELLOW}····································································{CYAN}{RESET}")
    print(f"{GREEN}............................................................................................................")
    print(f":    1. Subir notas             :           2. Modificar notas               :            {RED}0. Salir{GREEN}         :")
    print(f"............................................................................................................{RESET}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                with open(archivo_lectura, "r", encoding="utf-8") as f:
                    lineas = [linea.strip() for linea in f if linea.strip()]

                for linea in lineas:
                    print(f"Procesando línea: {linea}")
                    detector.detect_click(text=linea)

            except FileNotFoundError:
                print(f" No se encontró '{archivo_lectura}'")
                input("Presiona Enter para continuar...")
            except Exception as e:
                print(f" Ocurrió un error: {e}")
                input("Presiona Enter para continuar...")

        elif opcion == "2":
            os.system(f"notepad {archivo_lectura}" if os.name == "nt" else f"nano {archivo_lectura}")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print(" Opción no válida")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
