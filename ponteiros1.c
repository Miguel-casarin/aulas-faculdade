#include <stdio.h>

int main() {
    int valor = 15;
    int *p_valor;
    
    // Armazenando o endereço da variável valor no ponteiro p_valor
    p_valor = &valor;

    printf("conteudo da variavel = %d\n", valor);
    printf("endereco da variavel valor = %p\n", &valor);
    printf("conteudo apontado pelo ponteiro = %d\n", *p_valor);
    printf("endereco apontado pelo ponteiro = %p\n", p_valor);
    printf("endereco do ponteiro = %p\n", &p_valor);
    
    return 0;
}

