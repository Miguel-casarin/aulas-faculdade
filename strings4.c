#include <stdio.h>

int main(){
    char s[6];
    s[0] = 'h';
    s[1] = 'i';
    s[2] = ' ';
    s[3] = 'p';
    s[4] = 'c';
    s[5] = '\0';

    printf("%s", s);
    return 0;
}