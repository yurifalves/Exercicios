#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int num;

    printf("<<< EX011 - PAR OU ÍMPAR >>>\n\n");
    printf("Digite um número qualquer: ");
    scanf("%d", &num);
    printf("O número que você digitou é %s\n", (num%2==0)?"PAR":"ÍMPAR");

    return 0;
}
