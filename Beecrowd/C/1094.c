#include <stdio.h>

void saida(int coelhos, int ratos, int sapos);

int main() {
    int coelhos, ratos, sapos;
    char stringLida[100];
    int N;
    scanf("%d", &N);
    
    for (int i=0; i<N; i++) {
        stringLida = fgets(stringLida, sizeof(stringLida), stdin);
    }
    
    saida(coelhos, ratos, sapos);

    return 0;
}

void saida(int coelhos, int ratos, int sapos) {
    printf("Total: %d cobaias\n", coelhos+ratos+sapos);

    printf("Total de coelhos: %d\n", coelhos);
    printf("Total de ratos: %d\n", ratos);
    printf("Total de sapos: %d\n", sapos);

    printf("Percentual de coelhos: %.2f %%\n", 100*(float)coelhos/(coelhos+ratos+sapos));
    printf("Percentual de ratos: %.2f %%\n", 100*(float)ratos/(coelhos+ratos+sapos));
    printf("Percentual de sapos: %.2f %%\n", 100*(float)sapos/(coelhos+ratos+sapos));
}
