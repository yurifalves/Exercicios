#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int X[N], menor, posicao;

    for (int i=0; i<N; i++) {
        scanf("%d", &X[i]);
        if (i == 0) {
            menor = X[i];
            posicao = i;
        }
        else if (X[i] < menor) {
            menor = X[i];
            posicao = i;
        }
    }


    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

    return 0;
}
