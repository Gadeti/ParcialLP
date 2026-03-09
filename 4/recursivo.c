/*
recursivo.c
*/

#include <stdio.h>
#include <time.h>

long fib(int n){

    if(n<=1)
        return n;

    return fib(n-1) + fib(n-2);
}

int main(){

    clock_t inicio = clock();

    printf("Resultado: %ld\n", fib(35));

    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("Tiempo de ejecucion: %f segundos\n", tiempo);

    return 0;
}


/*
Compilar:

gcc recursivo.c

Ejecutar:

./a.out
*/
