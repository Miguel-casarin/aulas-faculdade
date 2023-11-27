#include <stdio.h>
#include <stdlib.h>

int main(){
int a = 5;
int *p_a = &a;
int b = (*p_a);
printf ("%i\n", (*p_a));

return 0;
}
