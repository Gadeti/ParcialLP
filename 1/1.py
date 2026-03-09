# 1.py
# Lenguajes de programación - Parcial
# Se usa una expresión regular para validar el patrón.

import re

# Patron basado en ejemplos del enunciado
patron = r"([a-z]+->?[a-z][0-9])|([a-z]+\sX\s[a-z]+)"

def verificar(cadena):
    """
    Verifica si la cadena cumple con el patrón
    """
    if re.fullmatch(patron, cadena):
        return "ACEPTA"
    else:
        return "NO ACEPTA"


pruebas = [
    "p->k4",
    "kbp X qn",
    "p->a5",
    "hola"
]

for p in pruebas:
    print(p, ":", verificar(p))


# Ejecutar en terminal:
# python3 1.py
