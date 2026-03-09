Programa que calcula raíz cuadrada usando el método de Newton-Raphson.

Herramientas usadas:
Flex -> analizador léxico
Bison -> parser

Compilar:

bison -d calc.y
flex calc.l
gcc calc.tab.c lex.yy.c -lm

Ejecutar:

./a.out < entrada.txt
