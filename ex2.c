#include <stdio.h>
#include <stdlib.h>

int main(){
    float largura = 0;
    float altura = 0;

    printf("qual a largura:");
    scanf("%f", &largura);
    printf("qual a altura");
    scanf("%f", &altura);

    float formula = largura * altura;
    if(largura > altura){
        printf("retrangulo area = %.2f", formula);
    }else{
        printf("quadrado area = %.2f", formula);
    } 
    system("pause"); 

    return 0;
}