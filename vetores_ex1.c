#include <stdio.h>
#include <stdlib.h>

int main(){
int v[5] = {4,1,5,8,6};
int n = 5;
int menor = v[0];
int maior = v[0];

for (int i = 0; i < n; i++) {
int t = v[i];
if (t > maior) {
maior = t;
}
if (t < menor) {
menor = t;
}
}

printf("menor valor: %i\n", menor);
printf("maior valor: %i\n", maior);

return 0;
}