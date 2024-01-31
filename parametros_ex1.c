#include <stdio.h>

void linha(int n){

    if(n > 0){
        for(int i = 0; i <= n; i++){
            printf("#");
        }
    }
    else {
        printf("valor invalido\n");
    }
}

int main(){
    printf("digite um valor");
    int valor = 0;
    scanf("%d", &valor);
    linha(valor);
    }