// Generic Fincke-Pohst enumerator with Cauchy-Schwarz half-space pruning (floating point, safety margin).
// Input (text, stdin): n m R
//   Rc (n x n upper triangular, row-major), zs (n), Rk (m x n), Sfree (m x (n+1)), f0 (m)
// Enumerates integer z with ||Rc (z - zs)||^2 <= R and, for every row k, f0_k + Rk_k . u >= -eps
// (u = Rc (z - zs)), printing every leaf z (space separated) for exact verification by the caller.
// Build: gcc -O2 -o fp_enum fp_enum.c -lm
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
static int n, m; static double R;
static double *Rc, *zs, *Rk, *Sf, *f0;
static long long nodes = 0, leaves = 0, limit = 4000000000LL;
static double *z;
#define RC(i,j) Rc[(i)*n+(j)]
#define RK(k,i) Rk[(k)*n+(i)]
#define SF(k,i) Sf[(k)*(n+1)+(i)]
static double eps = 1e-6;
static void rec(int i, double rem, double *lin) {
    double off = 0;
    for (int j = i + 1; j < n; j++) off += RC(i,j) * (z[j] - zs[j]);
    double rii = RC(i,i), half = sqrt(rem > 0 ? rem : 0) / rii, cen = zs[i] - off / rii;
    long lo = (long)ceil(cen - half - eps), hi = (long)floor(cen + half + eps);
    double *l2 = malloc(sizeof(double) * m);
    for (long zi = lo; zi <= hi; zi++) {
        if (++nodes > limit) { fprintf(stderr, "NODE_LIMIT\n"); exit(2); }
        double ui = rii * (zi - zs[i]) + off, r2 = rem - ui * ui;
        if (r2 < -eps) continue;
        int bad = 0; double rr = r2 > 0 ? r2 : 0;
        for (int k = 0; k < m; k++) {
            l2[k] = lin[k] + RK(k,i) * ui;
            if (l2[k] + sqrt(rr * SF(k,i)) < -eps) { bad = 1; break; }
        }
        if (bad) continue;
        z[i] = zi;
        if (i == 0) {
            leaves++;
            for (int j = 0; j < n; j++) printf("%ld ", (long)z[j]);
            printf("\n");
        } else rec(i - 1, r2, l2);
        z[i] = 0;
    }
    free(l2);
}
int main(int argc, char **argv) {
    if (argc > 1) limit = atoll(argv[1]);
    if (scanf("%d %d %lf", &n, &m, &R) != 3) return 1;
    Rc = malloc(sizeof(double)*n*n); zs = malloc(sizeof(double)*n); Rk = malloc(sizeof(double)*m*n);
    Sf = malloc(sizeof(double)*m*(n+1)); f0 = malloc(sizeof(double)*m); z = calloc(n, sizeof(double));
    for (int i = 0; i < n*n; i++) scanf("%lf", &Rc[i]);
    for (int i = 0; i < n; i++) scanf("%lf", &zs[i]);
    for (int i = 0; i < m*n; i++) scanf("%lf", &Rk[i]);
    for (int i = 0; i < m*(n+1); i++) scanf("%lf", &Sf[i]);
    for (int i = 0; i < m; i++) scanf("%lf", &f0[i]);
    if (R < 0) { fprintf(stderr, "EMPTY nodes 0 leaves 0\n"); return 0; }
    rec(n - 1, R, f0);
    fprintf(stderr, "COMPLETE nodes %lld leaves %lld\n", nodes, leaves);
    return 0;
}
