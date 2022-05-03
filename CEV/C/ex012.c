#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    float nota1, nota2, media;

    printf("<<< EX012 - SITUAÇÃO DO ALUNO >>>\n\n");
    printf("Primeira nota: ");
    scanf("%f", &nota1);
    printf("Segunda nota: ");
    fflush(stdin);
    scanf("%f", &nota2);
    media = (nota1+nota2)/2;

    printf("A média do aluno foi %.2f\n", media);
    printf("Situação --> %s\n", (media >= 6)?"APROVADO":"REPROVADO");

    return 0;
}
