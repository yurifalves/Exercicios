#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    char produto[30];
    float preco, desconto, novopreco;

    printf("<<< EX010 - PREÇO DO PRODUTO >>>\n\n");
    printf("Produto: ");
    gets(produto);
    printf("Preço de %s: R$", produto);
    fflush(stdin);
    scanf("%f", &preco);
    printf("Desconto: %%");
    fflush(stdin);
    scanf("%f", &desconto);
    novopreco = preco - (desconto/100)*(preco);
    printf("O produto %s custava R$%.2f mas com %.2f%% de desconto, passa a custar R$%.2f.\n", produto, preco, desconto, novopreco);

    return 0;
}
