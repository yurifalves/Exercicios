#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    printf("<<< EX001 - LISTAGEM >>>\n\n");
    printf("Listagem de Alunos\n");
    printf("Nome\t\tNota\n");
    printf("----------------------\n");
    printf("Ana Beatriz\t8.5\n");
    printf("Bianca Martins\t9.0\n");
    printf("Cláudio Sá\t5.5\n");
    printf("Giovana Silva\t7.5\n");
    printf("----------------------\n");
    return 0;
}

