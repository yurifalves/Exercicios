#include <stdio.h>
#include <locale.h>
int main() {
    setlocale(LC_ALL, "Portuguese");
    char nome[50];
    int idade;
    float peso;
    printf("<<< EX003 - DADOS >>>\n\n");
    printf("Qual é o seu nome? ");
    gets(nome);
    printf("Quantos anos você têm? ");
    fflush(stdin);
    scanf("%d", &idade);
    printf("Qual é o seu peso(Kg)? ");
    fflush(stdin);
    scanf("%f", &peso);

    printf("\n-------------------------------------------------\n");
    printf("Muito prazer, %s. Você tem %d anos e pesa %.2fKg correto?", nome, idade, peso);
    printf("\nFIM.\n");
    return 0;
}
