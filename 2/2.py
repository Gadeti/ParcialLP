# 2.py
# Programa AFD para validar identificadores

import re

# Expresion regular del enunciado
patron = r"[A-Za-z][A-Za-z0-9]*"

def validar(cadena):
    """
    Verifica si la cadena es un identificador valido
    """
    if re.fullmatch(patron, cadena):
        return "ACEPTA"
    else:
        return "NO ACEPTA"


# Pruebas 
pruebas = [
    "variable",   # acepta
    "A123",       # acepta
    "x9",         # acepta
    "9variable",  # no acepta
    "_temp"       # no acepta
]

for p in pruebas:
    print(p, ":", validar(p))


# Ejecutar en terminal:
# python3 2.py
