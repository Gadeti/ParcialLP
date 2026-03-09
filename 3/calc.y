/* calc.y
Parser usando Bison
Calcula raíz cuadrada usando Newton-Raphson */

%{
#include <stdio.h>
#include <math.h>

double newton(double n){
    double x = n;

    for(int i=0;i<10;i++){
        x = 0.5*(x + n/x);
    }

    return x;
}

void yyerror(char *s);
int yylex();

%}

%union{
double num;
}

%token <num> NUMBER
%token SQRT
%token EOL

%%

input:
    | input line
;

line:
    SQRT NUMBER EOL
    {
        printf("Resultado: %f\n", newton($2));
    }
;

%%

void yyerror(char *s){
    printf("Error de sintaxis\n");
}

int main(){
    yyparse();
    return 0;
}
