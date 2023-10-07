#include <stdio.h>
#include <stdlib.h> 

int main(){
    int produtos = 0;
    int caixas = 0;
    
    printf("digite o numero de produtos:");
    scanf("%i", &produtos); 
    printf("digite o numero de caixas");
    scanf("%i", &caixas); 

    int formula = produtos / caixas;
    int resto = produtos % caixas;

    printf("cabe um total de %i produtos\ne sobra %i", formula, resto); 
    system("pause"); 
    return 0;
}