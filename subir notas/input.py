#!/usr/bin/env python3
import uinput
import time

# --- Mapeo básico de caracteres a teclas ---
char_to_key = {
    "a": uinput.KEY_A, "b": uinput.KEY_B, "c": uinput.KEY_C,
    "d": uinput.KEY_D, "e": uinput.KEY_E, "f": uinput.KEY_F,
    "g": uinput.KEY_G, "h": uinput.KEY_H, "i": uinput.KEY_I,
    "j": uinput.KEY_J, "k": uinput.KEY_K, "l": uinput.KEY_L,
    "m": uinput.KEY_M, "n": uinput.KEY_N, "o": uinput.KEY_O,
    "p": uinput.KEY_P, "q": uinput.KEY_Q, "r": uinput.KEY_R,
    "s": uinput.KEY_S, "t": uinput.KEY_T, "u": uinput.KEY_U,
    "v": uinput.KEY_V, "w": uinput.KEY_W, "x": uinput.KEY_X,
    "y": uinput.KEY_Y, "z": uinput.KEY_Z,

    "0": uinput.KEY_0, "1": uinput.KEY_1, "2": uinput.KEY_2,
    "3": uinput.KEY_3, "4": uinput.KEY_4, "5": uinput.KEY_5,
    "6": uinput.KEY_6, "7": uinput.KEY_7, "8": uinput.KEY_8,
    "9": uinput.KEY_9,

    " ": uinput.KEY_SPACE,
}

# --- Crear teclado virtual ---
device = uinput.Device(list(set(char_to_key.values())))

time.sleep(0.3)  # Espera para que el dispositivo esté listo

# --- Texto fijo a escribir ---


# --- Escribir cada caracter ---
for ch in texto.lower():
    if ch in char_to_key:
        device.emit_click(char_to_key[ch])
    else:
        print(f"⚠️ Caracter no soportado: {ch}")

