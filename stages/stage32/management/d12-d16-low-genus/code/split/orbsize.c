// 32R-65: orbit sizes of representatives under the geometric group. stdin: NP, perms[NP][140], P140[140][64],
// Gn[64][64], then lines of 64 ints (reps). stdout per rep: "orbit C2" ; orbit = NP / |stabilizer|.
#include <stdio.h>
#include <stdlib.h>
int main(void) {
    int NP; if (scanf("%d", &NP) != 1) return 1;
    short *P = malloc(sizeof(short) * 140 * (size_t)NP);
    for (long i = 0; i < 140L * NP; i++) { int v; if (scanf("%d", &v) != 1) return 1; P[i] = (short)v; }
    static long long A[140][64], G[64][64];
    for (int k = 0; k < 140; k++) for (int a = 0; a < 64; a++) if (scanf("%lld", &A[k][a]) != 1) return 1;
    for (int a = 0; a < 64; a++) for (int b = 0; b < 64; b++) if (scanf("%lld", &G[a][b]) != 1) return 1;
    long long x[64], pe[140];
    while (1) {
        for (int a = 0; a < 64; a++) if (scanf("%lld", &x[a]) != 1) return 0;
        for (int k = 0; k < 140; k++) { long long v = 0; for (int a = 0; a < 64; a++) v += A[k][a] * x[a]; pe[k] = v; }
        long long c2 = 0; for (int a = 0; a < 64; a++) { long long v = 0; for (int b = 0; b < 64; b++) v += G[a][b] * x[b]; c2 += x[a] * v; }
        int stab = 0;
        for (int g = 0; g < NP; g++) { const short *p = P + (long)g * 140; int k; for (k = 0; k < 140; k++) if (pe[p[k]] != pe[k]) break; if (k == 140) stab++; }
        printf("%d %lld\n", NP / stab, c2);
    }
}
