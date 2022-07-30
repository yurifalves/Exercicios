#include <stdio.h>

int quadrante(int x, int y) {
    if (x>0 && y>0) {
        return 1;
    }
    else if (x<0 && y>0) {
        return 2;
    }
    else if (x<0 && y<0) {
        return 3;
    }
    else if (x>0 && y<0) {
        return 4;
    }
    else {
        return 0;
    }
}

int main() {
    int x, y;

    while (1) {
        scanf("%d %d", &x, &y);
        if (quadrante(x, y) == 0) {
            break;
        }
        else if (quadrante(x, y) == 1) {
            printf("primeiro\n");
        }
        else if (quadrante(x, y) == 2) {
            printf("segundo\n");
        }
        else if (quadrante(x, y) == 3) {
            printf("terceiro\n");
        }
        else if (quadrante(x, y) == 4) {
            printf("quarto\n");
        }
    }

    return 0;
}
