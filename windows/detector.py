# detector.py
import mouse
from escritor import write_text

def detect_click(text="35"):
    print("Haz clic donde quieras escribir...")

    # Espera a que el usuario haga clic izquierdo
    mouse.wait(button='left')

    # Obtiene la posición exacta del clic
    x, y = mouse.get_position()

    # Llama a la función que escribe el texto
    write_text(text=text, x=x, y=y)

if __name__ == "__main__":
    detect_click()
