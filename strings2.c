#include <stdio.h>

int main(){
    char s[] = "abcd";
    for (int i = 0; s[i] != '\0'; i++) {
    printf("%c", s[i]);
    }
    printf("\n");
    
return 0;
}