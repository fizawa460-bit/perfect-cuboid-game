// 32R-60: Fincke-Pohst over the rank-15 lattice (kernel of K on Λ) for the split enumeration.
// Input: n=15, nb=92; R (radius^2 bound for ||w - c||_Q), D[n] (pivots), U[n*n] (upper unit), cen[n],
//        bq0[nb] (float or int), BQ[n][nb] (ints): bq(w) = bq0 + sum_i w_i BQ[i]  (exact integers).
// Output: every w with ||w-c||^2 <= R (float, with margin) and bq(w) >= 0 componentwise, as one line of ints.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define NMAX 16
#define BMAX 128
static int n, nb;
static double R, D[NMAX], U[NMAX][NMAX], cen[NMAX];
static long long bq0[BMAX], BQ[NMAX][BMAX];
static long long w[NMAX], cur[NMAX + 1][BMAX];
static long long nodes = 0, outc = 0;
static void rec(int i, double rem) {
    double c = cen[i];
    for (int j = i + 1; j < n; j++) c -= U[i][j] * ((double)w[j] - cen[j]);
    double r = sqrt(rem > 0 ? rem / D[i] : 0) + 1e-7;
    long lo = (long)ceil(c - r), hi = (long)floor(c + r);
    for (long v = lo; v <= hi; v++) {
        nodes++;
        double nr = rem - D[i] * (v - c) * (v - c);
        if (nr < -1e-7) continue;
        w[i] = v;
        long long *src = cur[i + 1], *dst = cur[i];
        for (int b = 0; b < nb; b++) dst[b] = src[b] + v * BQ[i][b];
        if (i == 0) {
            int ok = 1;
            for (int b = 0; b < nb; b++) if (dst[b] < 0) { ok = 0; break; }
            if (ok) {
                for (int j = 0; j < n; j++) printf("%lld ", w[j]);
                printf("\n"); outc++;
            }
        } else rec(i - 1, nr);
    }
    w[i] = 0;
}
int main(void) {
    if (scanf("%d %d %lf", &n, &nb, &R) != 3) return 1;
    for (int i = 0; i < n; i++) if (scanf("%lf", &D[i]) != 1) return 1;
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (scanf("%lf", &U[i][j]) != 1) return 1;
    for (int i = 0; i < n; i++) if (scanf("%lf", &cen[i]) != 1) return 1;
    for (int b = 0; b < nb; b++) if (scanf("%lld", &bq0[b]) != 1) return 1;
    for (int i = 0; i < n; i++) for (int b = 0; b < nb; b++) if (scanf("%lld", &BQ[i][b]) != 1) return 1;
    for (int b = 0; b < nb; b++) cur[n][b] = bq0[b];
    rec(n - 1, R);
    fprintf(stderr, "nodes %lld output %lld\n", nodes, outc);
    return 0;
}
