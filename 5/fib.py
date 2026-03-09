FIBO(8)

"""

def fibonacci(n):

    a = 0
    b = 1

    secuencia = []

    for i in range(n):
        secuencia.append(a)
        a, b = b, a + b

    return secuencia


entrada = input("Ingrese numero: ")

n = int(entrada)

print(fibonacci(n))


"""
Generar parser ANTLR:

antlr4 -Dlanguage=Python3 fib.g4

Ejecutar programa:

python3 fib.py
"""
