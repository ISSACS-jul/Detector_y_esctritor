# escritor.py
import pyautogui
import time

def write_text(text="543", x=None, y=None):
    """
    Escribe el texto en la posición indicada.
    Si no se indican coordenadas, escribe donde esté el cursor.
    """
    if x is not None and y is not None:
        pyautogui.click(x, y)  # enfoca la ventana en las coordenadas
        time.sleep(0.1)

    pyautogui.typewrite(text)
    print(f"Texto '{text}' escrito en ({x}, {y})")
