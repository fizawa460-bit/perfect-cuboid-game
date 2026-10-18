// Stage32 D8-LOW-GENUS: certified Fincke-Pohst enumeration with Cauchy-Schwarz pruning, using rigorous
// outward-rounded bounds (CONTRACT.md §2).
//
// Exact problem (all data rational; certified_driver.py supplies each rational q as doubles lo <= q <= hi):
//   enumerate integer z in Z^n with  sum_i d_i y_i^2 <= R,   y_i = z_i - c_i,  c_i = zs_i - sum_{j>i} U_ij (z_j - zs_j),
//   and for every k:  l_k := f0_k + sum_i g_ki y_i >= 0.
// Recursion fixes z_{n-1}, ..., z_0.  At level i (z_{>i} fixed, remaining radius rem_{i+1}):
//   exact candidate range  |z_i - c_i| <= sqrt(rem_{i+1} / d_i);  rem_i = rem_{i+1} - d_i y_i^2;
//   over the remaining ellipsoid {sum_{j<i} d_j y_j^2 <= rem_i}:  max l_k = f_k + sqrt(rem_i S_k(i)),
//   f_k = f0_k + sum_{j>=i} g_kj y_j,  S_k(i) = sum_{j<i} g_kj^2 / d_j  (Cauchy-Schwarz, attained).
//   The branch needs l_k >= 0 somewhere, i.e. max l_k >= 0.  Hence the exact branch is empty if rem_i < 0, or if
//   for some k the MAXIMUM f_k + sqrt(rem_i S_k(i)) < 0, i.e. f_k < 0 and f_k^2 > rem_i S_k(i).
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
// Range/conversion guards (abort with "ERROR ..." and exit 3 instead of continuing):
//   all input doubles finite; every computed bound (clo, chi, HU, y bounds, RH_i, FH_k) finite (this also excludes
//   NaN from 0*inf or inf-inf); every candidate range inside [-2^52, 2^52], so the casts double->long and
//   long->double are exact (|z| <= 2^52 < 2^53); node counter < 2^62; every malloc checked.
//   Under these guards every double operand above is an exact value or a rigorous bound, so the argument holds.
//   The final line reports max |z| visited and the max |centre bound|, as range diagnostics.
// So, if the run ends COMPLETE, the printed leaves form a SUPERSET of the exact solution set; the driver rechecks
// every leaf exactly.
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
static long maxabsz = 0; static double maxabsc = 0;
#define ZMAX 0x1p52

static void fail(const char *msg) { fflush(stdout); fprintf(stderr, "ERROR %s\n", msg); exit(3); }
static void *xmalloc(size_t sz) { void *p = malloc(sz ? sz : 1); if (!p) fail("malloc"); return p; }

// upper bound of g*y for g in [gl, gh], y in [yl, yh]
static inline double hiprod(I g, double yl, double yh) {
    double a = g.lo * yl, b = g.lo * yh, c = g.hi * yl, d = g.hi * yh;
    double mx = a > b ? a : b;
    if (c > mx) mx = c;
    if (d > mx) mx = d;
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
        if (c < pmn) pmn = c;
        if (d < pmn) pmn = d;
        if (c > pmx) pmx = c;
        if (d > pmx) pmx = d;
        clo = DN(clo - UP(pmx));
        chi = UP(chi - DN(pmn));
    }
    if (!isfinite(clo) || !isfinite(chi) || !isfinite(RH)) fail("nonfinite centre or radius");
    double rh = RH > 0 ? RH : 0.0;
    double HU = UP(sqrt(UP(rh / D[i].lo)));
    double lod = floor(DN(clo - HU)), hid = ceil(UP(chi + HU));
    if (!isfinite(HU) || !isfinite(lod) || !isfinite(hid)) fail("nonfinite range");
    if (lod < -ZMAX || hid > ZMAX) fail("range outside [-2^52, 2^52]");
    if (fabs(clo) > maxabsc) maxabsc = fabs(clo);
    if (fabs(chi) > maxabsc) maxabsc = fabs(chi);
    long lo = (long)lod, hi = (long)hid;                              // exact: |lod|, |hid| <= 2^52
    double *F2 = xmalloc(sizeof(double) * (size_t)m);
    for (long zi = lo; zi <= hi; zi++) {
        if (++nodes > 0x1p62) fail("node counter");
        if (limit && nodes > limit) { fprintf(stderr, "NODE_LIMIT nodes %lld\n", nodes); exit(2); }
        if ((zi < 0 ? -zi : zi) > maxabsz) maxabsz = zi < 0 ? -zi : zi;
        double ylo = DN((double)zi - chi), yhi = UP((double)zi - clo);   // (double)zi exact: |zi| <= 2^52
        double y2lo = 0.0;
        if (ylo > 0) y2lo = DN(ylo * ylo); else if (yhi < 0) y2lo = DN(yhi * yhi);
        double r2 = UP(RH - DN(D[i].lo * y2lo));
        if (!isfinite(ylo) || !isfinite(yhi) || !isfinite(r2)) fail("nonfinite y or radius");
        if (r2 < 0) continue;                                         // exact rem_i < 0
        int bad = 0;
        const I *Gi = GT + (size_t)i * m; const double *Si = ST + (size_t)i * m;   // level-i rows, contiguous in k
        for (int k = 0; k < m; k++) {
            double fh = UP(FH[k] + hiprod(Gi[k], ylo, yhi));
            F2[k] = fh;
            if (!isfinite(fh)) fail("nonfinite linear-form bound");
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
        if (!isfinite(a[i].lo) || !isfinite(a[i].hi) || !(a[i].lo <= a[i].hi)) return 0;
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc > 1) limit = atoll(argv[1]);
    if (scanf("%d %d", &n, &m) != 2) { fprintf(stderr, "INPUT_ERROR\n"); return 1; }
    if (n < 1 || m < 0 || n > 4096 || m > 4096) { fprintf(stderr, "INPUT_ERROR sizes\n"); return 1; }
    D = xmalloc(sizeof(I) * n); ZS = xmalloc(sizeof(I) * n); U = xmalloc(sizeof(I) * n * n);
    F0 = xmalloc(sizeof(I) * m); G = xmalloc(sizeof(I) * m * n); S = xmalloc(sizeof(I) * m * n);
    z = calloc(n, sizeof(long)); if (!z) fail("malloc");
    if (!rd(&R, 1) || !rd(D, n) || !rd(ZS, n) || !rd(U, n * n) || !rd(F0, m) || !rd(G, m * n) || !rd(S, m * n)) {
        fprintf(stderr, "INPUT_ERROR\n"); return 1;
    }
    for (int i = 0; i < n; i++) if (!(D[i].lo > 0)) { fprintf(stderr, "INPUT_ERROR d not positive\n"); return 1; }
    GT = xmalloc(sizeof(I) * m * n); ST = xmalloc(sizeof(double) * m * n);
    for (int k = 0; k < m; k++) for (int i = 0; i < n; i++) {
        GT[(size_t)i * m + k] = G[(size_t)k * n + i];
        ST[(size_t)i * m + k] = S[(size_t)k * n + i].hi > 0 ? S[(size_t)k * n + i].hi : 0.0;   // S >= 0 exactly
    }
    double *FH = xmalloc(sizeof(double) * m);
    for (int k = 0; k < m; k++) FH[k] = F0[k].hi;
    if (R.hi < 0) { fprintf(stderr, "COMPLETE nodes 0 leaves 0 maxabsz 0 maxabsc 0\n"); return 0; }
    rec(n - 1, R.hi, FH);
    if (fflush(stdout) != 0 || ferror(stdout)) fail("stdout write");
    fprintf(stderr, "COMPLETE nodes %lld leaves %lld maxabsz %ld maxabsc %.6g\n", nodes, leaves, maxabsz, maxabsc);
    return 0;
}
