#include <stdio.h>

int main(){

    int v[10] = {7, 1, 5, 4, 0, 8, 12, -3, 10, 2};
    int len_v = 10; // gurda o tamanho do meu vetor vou ussa comparando com o acumulador para percorrer o vetor
    
    for(int i = 0; i < len_v; i++){
        printf("%i", v[i]);// seria mais simples se eu usasse a string.h aqui
    }
    printf("\n");
    return 0;
}