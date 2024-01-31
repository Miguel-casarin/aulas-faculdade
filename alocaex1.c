#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Definindo as strings iniciais
    const char *string1 = "copa";
    const char *string2 = "cabana";

    // Alocando memória para a string resultante, considerando o tamanho necessário
    // que é a soma dos tamanhos das duas strings mais 1 para o terminador '\0'
    char *p_resultatado = (char *)malloc(strlen(string1) + strlen(string2) + 1);

    // Copiando a primeira string para a string resultante
    strcpy(p_resultatado, string1);

    // Concatenando a segunda string à string resultante
    strcat(p_resultatado, string2);

    // Imprimindo o resultado
    printf("String resultante: %s\n", p_resultatado);

    // Liberando a memória alocada
    free(p_resultatado);

    return 0;
}