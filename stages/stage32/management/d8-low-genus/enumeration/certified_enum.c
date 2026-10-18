// Stage32 D8-LOW-GENUS: certified Fincke-Pohst enumeration with Cauchy-Schwarz pruning, using rigorous
// outward-rounded bounds (CONTRACT.md §2).
//
// Exact problem (all data rational; certified_driver.py supplies each rational q as doubles lo <= q <= hi):
//   enumerate integer z in Z^n with  sum_i d_i y_i^2 <= R,   y_i = z_i - c_i,  c_i = zs_i - sum_{j>i} U_ij (z_j - zs_j),
//   and for every k:  l_k := f0_k + sum_i g_ki y_i >= 0.
// Recursion fixes z_{n-1}, ..., z_0.  At level i (z_{>i} fixed, remaining radius rem_{i+1}):
//   exact candidate range  |z_i - c_i| <= sqrt(rem_{i+1} / d_i);  rem_i = rem_{i+1} - d_i y_i^2;
//   over the remaining ellipsoid {sum_{j<i} d_j y_j^2 <= rem_i}:  min l_k = f_k - sqrt(rem_i S_k(i)),
//   f_k = f0_k + sum_{j>=i} g_kj y_j,  S_k(i) = sum_{j<i} g_kj^2 / d_j  (Cauchy-Schwarz, attained).
//   Hence the exact branch is empty if rem_i < 0, or if for some k: f_k < 0 and f_k^2 > rem_i S_k(i).
// Certification.  We carry, for every exact quantity, rigorous bounds:
//   c_i in [clo, chi] (both bounds),  y_i in [ylo, yhi],  rem_i <= RH,  f_k <= FH_k.
// Every floating operation is done in round-to-nearest and then pushed outward by UP()/DN():
//   UP(x) = x + (|x| 2^-51 + 2^-1022),  DN(x) = x - (|x| 2^-51 + 2^-1022).
//   For a round-to-nearest result r of an exact value v, |v - r| <= ulp(r)/2 <= |r| 2^-52 (normal range) or
//   <= 2^-1075 (subnormal), and r + (|r| 2^-51 + 2^-1022) rounds to a double >= r + ulp(r) >= v; symmetrically for DN.
// A branch is discarded only if the exact condition is implied by the bounds:
//   range:  visit all integers in [floor(DN(clo - HU)), ceil(UP(chi + HU))], HU >= sqrt(RH_{i+1} / lo(d_i));
//   radius: discard iff RH_i < 0, with RH_i = UP(RH_{i+1} - DN(lo(d_i) * lo(y_i^2)));
//   CS:     discard iff FH_k < 0 and DN(FH_k^2) > UP(max(RH_i,0) * hi(S_k(i))).
// So the printed leaves form a SUPERSET of the exact solution set; the driver rechecks every leaf exactly.
// Build (x86-64 SSE2 doubles; no FMA contraction, no fast-math):
//   gcc -O2 -std=c11 -ffp-contract=off -fno-fast-math -o certified_enum certified_enum.c -lm
// Input (stdin): "n m", then pairs (lo hi) for: R; d[n]; zs[n]; U[n*n] (row-major); f0[m]; g[m*n]; S[m*n].
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define EPSR 0x1p-51
#define TINY 0x1p-1022
static inline double UP(double x) { return x + ((x < 0 ? -x : x) * EPSR + TINY); }
static inline double DN(double x) { return x - ((x < 0 ? -x : x) * EPSR + TINY); }

typedef struct { double lo, hi; } I;
static int n, m;
static I R, *D, *ZS, *U, *F0, *G, *S;
static I *GT; static double *ST;            // transposed copies: GT[i*m+k] = G[k*n+i], ST[i*m+k] = hi(S[k*n+i])
static long long nodes = 0, leaves = 0, limit = 0;
static long *z;

// upper bound of g*y for g in [gl, gh], y in [yl, yh]
static inline double hiprod(I g, double yl, double yh) {
    double a = g.lo * yl, b = g.lo * yh, c = g.hi * yl, d = g.hi * yh;
    double mx = a > b ? a : b; if (c > mx) mx = c; if (d > mx) mx = d;
    return UP(mx);
}

static void rec(int i, double RH, const double *FH) {
    // c_i = zs_i - sum_{j>i} U_ij (z_j - zs_j): rigorous [clo, chi]
    double clo = ZS[i].lo, chi = ZS[i].hi;
    for (int j = i + 1; j < n; j++) {
        double wl = DN((double)z[j] - ZS[j].hi), wh = UP((double)z[j] - ZS[j].lo);   // w_j = z_j - zs_j
        I u = U[i * n + j];
        double a = u.lo * wl, b = u.lo * wh, c = u.hi * wl, d = u.hi * wh;
        double pmn = a < b ? a : b, pmx = a > b ? a : b;
        if (c < pmn) pmn = c; if (d < pmn) pmn = d; if (c > pmx) pmx = c; if (d > pmx) pmx = d;
        clo = DN(clo - UP(pmx));
        chi = UP(chi - DN(pmn));
    }
    double rh = RH > 0 ? RH : 0.0;
    double HU = UP(sqrt(UP(rh / D[i].lo)));
    long lo = (long)floor(DN(clo - HU)), hi = (long)ceil(UP(chi + HU));
    double *F2 = malloc(sizeof(double) * (size_t)m);
    for (long zi = lo; zi <= hi; zi++) {
        ++nodes;
        if (limit && nodes > limit) { fprintf(stderr, "NODE_LIMIT nodes %lld\n", nodes); exit(2); }
        double ylo = DN((double)zi - chi), yhi = UP((double)zi - clo);
        double y2lo = 0.0;
        if (ylo > 0) y2lo = DN(ylo * ylo); else if (yhi < 0) y2lo = DN(yhi * yhi);
        double r2 = UP(RH - DN(D[i].lo * y2lo));
        if (r2 < 0) continue;                                         // exact rem_i < 0
        int bad = 0;
        const I *Gi = GT + (size_t)i * m; const double *Si = ST + (size_t)i * m;   // level-i rows, contiguous in k
        for (int k = 0; k < m; k++) {
            double fh = UP(FH[k] + hiprod(Gi[k], ylo, yhi));
            F2[k] = fh;
            if (fh < 0 && DN(fh * fh) > UP(r2 * Si[k])) { bad = 1; break; }   // exact f<0 and f^2 > rem*S
        }
        if (bad) continue;
        z[i] = zi;
        if (i == 0) {
            leaves++;
            for (int j = 0; j < n; j++) printf("%ld ", z[j]);
            printf("\n");
        } else rec(i - 1, r2, F2);
        z[i] = 0;
    }
    free(F2);
}

static int rd(I *a, int cnt) {
    for (int i = 0; i < cnt; i++) {
        if (scanf("%lf %lf", &a[i].lo, &a[i].hi) != 2) return 0;
        if (!(a[i].lo <= a[i].hi)) return 0;
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc > 1) limit = atoll(argv[1]);
    if (scanf("%d %d", &n, &m) != 2) { fprintf(stderr, "INPUT_ERROR\n"); return 1; }
    D = malloc(sizeof(I) * n); ZS = malloc(sizeof(I) * n); U = malloc(sizeof(I) * n * n);
    F0 = malloc(sizeof(I) * m); G = malloc(sizeof(I) * m * n); S = malloc(sizeof(I) * m * n);
    z = calloc(n, sizeof(long));
    if (!rd(&R, 1) || !rd(D, n) || !rd(ZS, n) || !rd(U, n * n) || !rd(F0, m) || !rd(G, m * n) || !rd(S, m * n)) {
        fprintf(stderr, "INPUT_ERROR\n"); return 1;
    }
    for (int i = 0; i < n; i++) if (!(D[i].lo > 0)) { fprintf(stderr, "INPUT_ERROR d not positive\n"); return 1; }
    GT = malloc(sizeof(I) * m * n); ST = malloc(sizeof(double) * m * n);
    for (int k = 0; k < m; k++) for (int i = 0; i < n; i++) {
        GT[(size_t)i * m + k] = G[(size_t)k * n + i];
        ST[(size_t)i * m + k] = S[(size_t)k * n + i].hi > 0 ? S[(size_t)k * n + i].hi : 0.0;   // S >= 0 exactly
    }
    double *FH = malloc(sizeof(double) * m);
    for (int k = 0; k < m; k++) FH[k] = F0[k].hi;
    if (R.hi < 0) { fprintf(stderr, "COMPLETE nodes 0 leaves 0\n"); return 0; }
    rec(n - 1, R.hi, FH);
    fprintf(stderr, "COMPLETE nodes %lld leaves %lld\n", nodes, leaves);
    return 0;
}
