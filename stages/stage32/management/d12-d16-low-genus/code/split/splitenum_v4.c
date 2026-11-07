// 32R-62: streaming split enumeration (y-stage + exact y^2 + m-stage in one pass).
// Input (stdin):
//   n nb R ; D[n] ; U[n][n] ; cen[n]                    (Fincke-Pohst data for w, float)
//   z0[16] ; NR[n][16]                                  (z = z0 + w.NR, integer)
//   G4[16][16]                                          (4 * Gram of Λ, integer)
//   y4lo y4hi c2min                                     (bounds on 4y^2; c2min for Σ m^2 <= 2(y^2 - c2min))
//   mt0[48] ; MT[n][48]                                 (m~ = mt0 + w.MT)
//   bq0[nb] ; BQ[n][nb]                                 (b_q = bq0 + w.BQ)
//   NQ NI ; MU[NQ][48] ; Ipos[NI] ; Drow[NI][48]        (m-search data, NQ = nb)
//   shard nshard                                         (process top-level values v with (v mod nshard) == shard)
//   env SPLIT_DEPTH (default 4): shard round-robin over the subtrees at level n-1-SPLIT_DEPTH (32R-64)
// Output: lines "w_0..w_{n-1} | m_0..m_47" for every solution.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define NMAX 16
#define BMAX 128
#define N48 48
static int n, nb, NQ, NI, shard = 0, nshard = 1, slev = -1;
static long long subctr = 0;
static double R, D[NMAX], U[NMAX][NMAX], cen[NMAX];
static long long z0[16], NR[NMAX][16], G4[16][16], y4lo, y4hi, c2min;
static long long mt0[N48], MT[NMAX][N48], bq0[BMAX], BQ[NMAX][BMAX];
static int MU[BMAX][N48], Ipos[N48], Drow[N48][N48], isI[N48], order[N48], curves[N48][BMAX], ncurves[N48];
static long long w[NMAX], zc[NMAX + 1][16], mtc[NMAX + 1][N48], bqc[NMAX + 1][BMAX];
static long long nodes = 0, nyleaf = 0, nyok = 0, nsol = 0;
// m-search state
static int m[N48], slack[BMAX], vI[N48], mtv[N48], tpar[N48];
static void out_solution(void) {
    for (int j = 0; j < n; j++) printf("%lld ", w[j]);
    printf("|");
    for (int j = 0; j < N48; j++) printf(" %d", m[j]);
    printf("\n"); nsol++;
}
// 32R-64 parity-first search. The parity of every m_j is mtv[j] + sum_i bit_i Drow[i][j] (mod 2) for the 10 free
// bits. bitdfs fixes the bits one by one; a position is "determined" once its last dependent bit is fixed, and its
// minimal demand (m_j >= parity) is charged to needq / needs2 at once, so infeasible parity patterns die early.
// Then vdfs enumerates the values m_j = par, par+2, ... with the full look-ahead.
static int needq[BMAX], needs2, par[N48], lastdep[N48], bitv[N48];
static int s2maxg;
static int charge(int j, int sgn) {
    if (!par[j]) return 1;
    needs2 += sgn;
    for (int c = 0; c < ncurves[j]; c++) needq[curves[j][c]] += sgn * MU[curves[j][c]][j];
    return 1;
}
static int feasible(int j) {
    if (needs2 > s2maxg) return 0;
    for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; if (slack[q] < needq[q]) return 0; }
    return 1;
}
static void vdfs(int t, int s2) {
    if (t == N48) { out_solution(); return; }
    int j = order[t];
    charge(j, -1);
    for (int v = par[j]; ; v += 2) {
        if (s2 + v * v + needs2 > s2maxg) break;
        int ok = 1;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; if (slack[q] - MU[q][j] * v < needq[q]) { ok = 0; break; } }
        if (!ok) break;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] -= MU[q][j] * v; }
        m[j] = v;
        vdfs(t + 1, s2 + v * v);
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] += MU[q][j] * v; }
        m[j] = 0;
    }
    charge(j, +1);
}
static void bitdfs(int i) {
    if (i == NI) { vdfs(0, 0); return; }
    for (int b = 0; b < 2; b++) {
        if (b) for (int j = 0; j < N48; j++) if (Drow[i][j]) par[j] ^= 1;
        int ok = 1, k;
        for (k = 0; k < N48; k++) if (lastdep[k] == i) { charge(k, +1); if (!feasible(k)) ok = 0; }
        if (ok) bitdfs(i + 1);
        for (k = 0; k < N48; k++) if (lastdep[k] == i) charge(k, -1);
        if (b) for (int j = 0; j < N48; j++) if (Drow[i][j]) par[j] ^= 1;
    }
}
static void mrec(int t, int s2, int s2max) {
    (void)t; (void)s2;
    s2maxg = s2max;
    memset(needq, 0, sizeof needq); needs2 = 0;
    for (int j = 0; j < N48; j++) par[j] = mtv[j] & 1;
    for (int j = 0; j < N48; j++) if (lastdep[j] < 0) { charge(j, +1); if (!feasible(j)) { for (int k = 0; k <= j; k++) if (lastdep[k] < 0) charge(k, -1); return; } }
    bitdfs(0);
    for (int j = 0; j < N48; j++) if (lastdep[j] < 0) charge(j, -1);
}
static void leaf(void) {
    nyleaf++;
    long long *z = zc[0];
    long long y4 = 0;
    for (int a = 0; a < 16; a++) { if (!z[a]) continue; long long s = 0; for (int b = 0; b < 16; b++) s += G4[a][b] * z[b]; y4 += z[a] * s; }
    if (y4 < y4lo || y4 > y4hi) return;
    nyok++;
    // s2max = floor(2 (y^2 - c2min)) = floor((y4 - 4 c2min) / 2)
    long long num = y4 - 4 * c2min;
    if (num < 0) return;
    int s2max = (int)(num / 2);
    for (int j = 0; j < N48; j++) mtv[j] = (int)mtc[0][j];
    for (int q = 0; q < nb; q++) slack[q] = (int)bqc[0][q];
    memset(m, 0, sizeof m);
    if (!getenv("SPLIT_NOM")) mrec(0, 0, s2max);
}
static void rec(int i, double rem) {
    double c = cen[i];
    for (int j = i + 1; j < n; j++) c -= U[i][j] * ((double)w[j] - cen[j]);
    double r = sqrt(rem > 0 ? rem / D[i] : 0) + 1e-7;
    long lo = (long)ceil(c - r), hi = (long)floor(c + r);
    for (long v = lo; v <= hi; v++) {
        if (nshard > 1 && i == slev) { long long k = subctr++; if (k % nshard != shard) continue; }
        nodes++;
        double nr = rem - D[i] * (v - c) * (v - c);
        if (nr < -1e-7) continue;
        w[i] = v;
        for (int b = 0; b < nb; b++) bqc[i][b] = bqc[i + 1][b] + v * BQ[i][b];
        for (int a = 0; a < 16; a++) zc[i][a] = zc[i + 1][a] + v * NR[i][a];
        for (int a = 0; a < N48; a++) mtc[i][a] = mtc[i + 1][a] + v * MT[i][a];
        if (i == 0) {
            int ok = 1;
            for (int b = 0; b < nb; b++) if (bqc[0][b] < 0) { ok = 0; break; }
            if (ok) leaf();
        } else rec(i - 1, nr);
    }
    w[i] = 0;
}
#define RD(fmt, p) if (scanf(fmt, p) != 1) { fprintf(stderr, "INPUT_ERROR\n"); return 1; }
int main(void) {
    if (scanf("%d %d %lf", &n, &nb, &R) != 3) return 1;
    for (int i = 0; i < n; i++) RD("%lf", &D[i]);
    for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) RD("%lf", &U[i][j]);
    for (int i = 0; i < n; i++) RD("%lf", &cen[i]);
    for (int a = 0; a < 16; a++) RD("%lld", &z0[a]);
    for (int i = 0; i < n; i++) for (int a = 0; a < 16; a++) RD("%lld", &NR[i][a]);
    for (int a = 0; a < 16; a++) for (int b = 0; b < 16; b++) RD("%lld", &G4[a][b]);
    if (scanf("%lld %lld %lld", &y4lo, &y4hi, &c2min) != 3) return 1;
    for (int a = 0; a < N48; a++) RD("%lld", &mt0[a]);
    for (int i = 0; i < n; i++) for (int a = 0; a < N48; a++) RD("%lld", &MT[i][a]);
    for (int b = 0; b < nb; b++) RD("%lld", &bq0[b]);
    for (int i = 0; i < n; i++) for (int b = 0; b < nb; b++) RD("%lld", &BQ[i][b]);
    if (scanf("%d %d", &NQ, &NI) != 2) return 1;
    for (int q = 0; q < NQ; q++) for (int j = 0; j < N48; j++) RD("%d", &MU[q][j]);
    for (int i = 0; i < NI; i++) RD("%d", &Ipos[i]);
    for (int i = 0; i < NI; i++) for (int j = 0; j < N48; j++) RD("%d", &Drow[i][j]);
    if (scanf("%d %d", &shard, &nshard) != 2) { shard = 0; nshard = 1; }
    { const char *e = getenv("SPLIT_DEPTH"); int dd = e ? atoi(e) : 4; slev = n - 1 - dd; if (slev < 0) slev = 0; }
    for (int j = 0; j < N48; j++) { lastdep[j] = -1; for (int i = 0; i < NI; i++) if (Drow[i][j]) lastdep[j] = i; }
    int t = 0, used[N48] = {0};
    for (int i = 0; i < NI; i++) { order[t++] = Ipos[i]; isI[Ipos[i]] = 1; used[Ipos[i]] = 1; }
    for (int j = 0; j < N48; j++) { ncurves[j] = 0; for (int q = 0; q < NQ; q++) if (MU[q][j]) curves[j][ncurves[j]++] = q; }
    while (t < N48) { int best = -1; for (int j = 0; j < N48; j++) if (!used[j] && (best < 0 || ncurves[j] > ncurves[best])) best = j; used[best] = 1; order[t++] = best; }
    for (int a = 0; a < 16; a++) zc[n][a] = z0[a];
    for (int a = 0; a < N48; a++) mtc[n][a] = mt0[a];
    for (int b = 0; b < nb; b++) bqc[n][b] = bq0[b];
    rec(n - 1, R);
    fprintf(stderr, "nodes %lld yleaves %lld yok %lld solutions %lld\n", nodes, nyleaf, nyok, nsol);
    return 0;
}
