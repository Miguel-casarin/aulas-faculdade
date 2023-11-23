#include <stdio.h>
#include <stdlib.h>

int main(){
char lista[21];
printf("digite uma string ai BLZ : ");
scanf("%20s", lista);



for (int l =0 ; lista[l] != '\0'; l++){
	if (lista[l] == 'a' ){
	printf("%d\n", l );}
}

return 0; 
}
