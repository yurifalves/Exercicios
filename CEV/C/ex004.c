#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(0, "Portuguese");
    char nome1[20], nome2[20], nome3[20];
    char sexo1, sexo2, sexo3;
    float nota1, nota2, nota3;

    printf("<<< EX004 - LISTAGEM >>>\n\n");

    printf("Cadastrando a primeira pessoa:\n");
    printf("------------------------------\n");
    printf("NOME: ");
    fflush(stdin);
    gets(nome1);
    printf("SEXO [M/F]: ");
    fflush(stdin);
    sexo1 = getchar();
    printf("NOTA: ");
    fflush(stdin);
    scanf("%f", &nota1);

    printf("\nCadastrando a segunda pessoa:\n");
    printf("------------------------------\n");
    printf("NOME: ");
    fflush(stdin);
    gets(nome2);
    printf("SEXO [M/F]: ");
    fflush(stdin);
    sexo2 = getchar();
    printf("NOTA: ");
    fflush(stdin);
    scanf("%f", &nota2);

    printf("\nCadastrando a terceira pessoa:\n");
    printf("------------------------------\n");
    printf("NOME: ");
    fflush(stdin);
    gets(nome3);
    printf("SEXO [M/F]: ");
    fflush(stdin);
    sexo3 = getchar();
    printf("NOTA: ");
    fflush(stdin);
    scanf("%f", &nota3);

    printf("\n\nLISTAGEM COMPLETA");
    printf("\n-----------------------------------\n");
    printf("NOME               SEXO  NOTA\n");
    printf("%-20s%c%8.1f", nome1, sexo1, nota1);
    printf("\n%-20s%c%8.1f", nome2, sexo2, nota2);
    printf("\n%-20s%c%8.1f", nome3, sexo3, nota3);
    printf("\n-----------------------------------\n");

    return 0;
}
