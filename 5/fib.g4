// fib.g4
// Gramática para reconocer el comando FIBO(numero)

grammar fib;

prog: 'FIBO' '(' NUM ')' ;

NUM: [0-9]+;

WS: [ \t\r\n]+ -> skip;
