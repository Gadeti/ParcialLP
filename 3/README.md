# Calculadora de Raíz Cuadrada — Newton-Raphson

Programa que calcula la raíz cuadrada usando el método de Newton-Raphson.

## Herramientas
- **Flex** — analizador léxico
- **Bison** — parser

## Compilar
```bash
bison -d calc.y
flex calc.l
gcc calc.tab.c lex.yy.c -lm
```

## Ejecutar
```bash
./a.out < entrada.txt
```
