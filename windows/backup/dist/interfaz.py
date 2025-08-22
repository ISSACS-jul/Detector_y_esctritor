import os
import subprocess

# Ruta base = carpeta donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Colores ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

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
            lector_path = os.path.join(BASE_DIR, "lector.exe")
            if os.path.exists(lector_path):
                subprocess.run([lector_path], shell=True)
            else:
                print(f"{RED}No se encontró {lector_path}{RESET}")
            input("Presiona Enter para continuar...")

        elif opcion == "2":
            notas_path = os.path.join(BASE_DIR, "notas.txt")
            os.system(f"notepad {notas_path}")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
