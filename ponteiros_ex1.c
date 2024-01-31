#include <stdio.h>
#include <stdlib.h>

void somar(int *p_numero) {
    (*p_numero)++;
}

int main() {
    int variavel = 0;
    
    printf("Digite um numero: ");
    scanf("%d", &variavel);

    //realizo a adiçao diretamente no endereço de mémoria
    somar(&variavel);

    printf("Número + 1 = %d\n", variavel);

    return 0;
}
