#include <stdio.h>
#include <stdlib.h>

void func(char s1[], char *s2) {
    printf("%s %s\n", s1, s2);
}

int main() {
    char b[] = "bola";
    char *c = "dado";
    func(b, c);

    return 0;
}
