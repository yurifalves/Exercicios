#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    char nome[30];
    float nota1, nota2, media;

    printf("<<< EX009 - MÉDIA DO ALUNO >>>\n\n");
    printf("Nome do aluno: ");
    gets(nome);
    printf("Nota 1: ");
    fflush(stdin);
    scanf("%f", &nota1);
    printf("Nota2: ");
    fflush(stdin);
    scanf("%f", &nota2);
    media = (nota1+nota2)/2;
    printf("O aluno %s tirou notas %.1f e %.1f e ficou com média %.1f\n", nome, nota1, nota2, media);

    return 0;
}
