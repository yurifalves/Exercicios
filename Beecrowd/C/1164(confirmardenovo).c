#include <stdio.h>

int ehPerfeito(int num);

int main() {
    int N;
    scanf("%d", &N);

    for (int i=0; i<N; i++) {
        int num;

        scanf("%d", &num);

        if (ehPerfeito(num)) {
            printf("%d eh perfeito\n", num);
        }
        else {
            printf("%d nao eh perfeito\n", num);
        }
    }

    return 0;
}

int ehPerfeito(int num) {
    int somaDivisores = 0;
    
    for (int i=1; i<=num; i++) {
        if (num%i == 0) {
            somaDivisores += i;
        }
    }
    if (somaDivisores-num == num) {
        return 1;
    }
    return 0;
}
