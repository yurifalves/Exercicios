#include <stdio.h>

double media(int vetor[], int tamanhoVetor) {
    int soma = 0;
    for (int i=0; i<tamanhoVetor; i++) {
        soma += vetor[i];
    }
    return (double)soma/tamanhoVetor;
}

int main() {
    int C;
    scanf("%d", &C);

    for (int i=0; i<C; i++) {
        int numeroAlunos, alunosDestaque = 0;
        scanf("%d", &numeroAlunos);
        int notas[numeroAlunos];

        for (int i=0; i<numeroAlunos; i++) {
            scanf("%d", &notas[i]);
        }

        int mediaTurma = media(notas, numeroAlunos);
        for (int i=0; i<numeroAlunos; i++) {
            if (notas[i] > mediaTurma) {
                alunosDestaque += 1;
            }
        }
        printf("%.3lf%%\n", 100*((double)alunosDestaque/numeroAlunos));
    }

    return 0;
}
