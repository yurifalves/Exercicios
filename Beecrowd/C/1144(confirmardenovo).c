#include <stdio.h>
#include <math.h>

int main() {
    int N;
    scanf("%d", &N);

    for (int i=1; i<=N; i++) {
        printf("%d %.0lf %.0lf\n", i, pow(i, 2), pow(i, 3));
	printf("%d %.0lf %.0lf\n", i, pow(i, 2)+1, pow(i, 3)+1);
    }

    return 0;
}
