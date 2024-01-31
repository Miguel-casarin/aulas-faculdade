#include <stdio.h>

// primeira função
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

//chegunda função
void quadrado(int n){

    if(n > 0){
        for(int i = 0; i <= n; i++){
            //aqui eu usso os valores e retorno a primaeira função
            linha(n);
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
    quadrado(valor);
    }