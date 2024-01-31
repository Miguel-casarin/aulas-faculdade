#include <stdio.h>
#include <stdlib.h>

int main(){
    int *p = NULL;

    p = malloc(sizeof(int)*1);
		
		p[0]=99;

		printf("p - Endereco: %p Valor: %p Vetor: %i\n",&p,p,p[0]);
		
		int *aux = p;
			
		p = malloc(sizeof(int)*2);

		p[0]= aux[0];

		printf("p - Endereco: %p Valor: %p Vetor: %i %i\n",&p,p,p[0],p[1]);

		free(aux);
		
		free(p);
		
		
    return 0;
}