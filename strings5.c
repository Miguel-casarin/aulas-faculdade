#include <stdio.h>

int main(){
    char tamanho[10];
    printf("digite uma frase o programa usara no maximo 9 caracteres\n");
    scanf("%9s", tamanho);
    printf("seu digito\n");
    printf("%s\n", tamanho);
    return 0; 
}