#include <stdio.h>

int main() {
    int coelhos = 0, ratos = 0, sapos = 0;
    char tipo;
    int N;
    scanf("%d", &N);

    for (int i=0; i<N; i++) {
        int qtd;
        scanf("%d %c", &qtd, &tipo);

        switch (tipo) {
            case 'C':
                coelhos += qtd;
                break;
            case 'R':
                ratos += qtd;
                break;
            case 'S':
                sapos += qtd;
                break;
        }
    }

    printf("Total: %d cobaias\n", coelhos+ratos+sapos);
    printf("Total de coelhos: %d\n", coelhos);
    printf("Total de ratos: %d\n", ratos);
    printf("Total de sapos: %d\n", sapos);
    printf("Percentual de coelhos: %.2f %%\n", 100*(float)coelhos/(coelhos+ratos+sapos));
    printf("Percentual de ratos: %.2f %%\n", 100*(float)ratos/(coelhos+ratos+sapos));
    printf("Percentual de sapos: %.2f %%\n", 100*(float)sapos/(coelhos+ratos+sapos));

    return 0;
}
