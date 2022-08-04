#include <stdio.h>

int main() {
    char cpf[14];
    for (int i=0; i<14; i++) {
        scanf("%c", &cpf[i]);
    }

    // 1
    for (int i=0; i<3; i++) {
        printf("%c", cpf[i]);
    }
    printf("\n");

    // 2
    for (int i=4; i<7; i++) {
        printf("%c", cpf[i]);
    }
    printf("\n");

    // 3
    for (int i=8; i<11; i++) {
        printf("%c", cpf[i]);
    }
    printf("\n");

    // 4
    for (int i=12; i<14; i++) {
        printf("%c", cpf[i]);
    }
    printf("\n");

    return 0;
}
