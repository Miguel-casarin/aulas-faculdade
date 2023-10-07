#include <stdio.h>
#include <stdlib.h>

int main(){
    int temperatura = 40;
    int formula = ((9* temperatura) + 160)/5;

    // Para printar preciso antes declarar o tipo de variavel se não for uma mensagem 
    printf("%i", formula); 
    return 0;
}