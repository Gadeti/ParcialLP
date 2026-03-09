"""
recursivo.py

Versión en Python del cálculo de Fibonacci
usando recursión.

Python es interpretado, por lo que normalmente
será más lento que C en este tipo de operaciones.
"""

import time


def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


inicio = time.time()

print("Resultado:", fib(35))

fin = time.time()

print("Tiempo:", fin - inicio)


"""
Ejecutar en terminal:

python3 recursivo.py
"""
