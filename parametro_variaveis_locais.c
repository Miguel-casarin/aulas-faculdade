#include <stdio.h>
#include <stdlib.h>

void contagem (int n){
    for (int c = 1; c <= n ;c++){
        printf("%i\n", c);
    }
}

int main(){
    contagem(5);
    return 0;
}