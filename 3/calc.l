/* calc.l
Analizador léxico usando Flex
Reconoce el comando sqrt y números */

%{
#include "calc.tab.h"
#include <stdlib.h>
%}

%%

sqrt        { return SQRT; }
[0-9]+      { yylval.num = atof(yytext); return NUMBER; }
\n          { return EOL; }
[ \t]       ;

%%

int yywrap(){
    return 1;
}
