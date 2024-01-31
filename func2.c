#include <stdio.h>
#include <stdlib.h>

int ler_inteiro(){
    int i = 0;
    printf("encontre um inteiro : ");
    scanf("%i", &i);
    return i;
}

int main(){
    int n = ler_inteiro();
    printf("valor de entrada : %d", n);
    return 0; 
}