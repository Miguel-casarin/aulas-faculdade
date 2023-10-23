#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int a =0;
	int b =0;

	printf("digite ai:");
	scanf("%i", &a);
	printf("mais um na hulmilda:");
	scanf("%i", &b);
	
	if (a <= b ){
		while ( a < b){
		a +=1;
		printf("%i", a);
		}
	}
	
	if (b < a){
		while (a >b){
		a -=1;
		printf("%i", a);
		}
	}
 

return 0;
}
