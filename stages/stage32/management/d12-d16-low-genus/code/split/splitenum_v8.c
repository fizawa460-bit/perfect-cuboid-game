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
// 32R-65 in-C reduction (invmode): exact reconstruction of x, inventory filter, and orbit-representative test
// (keep x only if its intersection vector pe = P140.x is lexicographically maximal over the geometric group).
static int invmode = 0, dd, NP;
static long long xt0v[64], XTi[NMAX][64], Pmm[N48][64], Dden, SMD[N48][N48], Sm[N48][64], P140[140][64], degv[64], F1v[64], excv[64], Gnm[64][64];
static short *pinv;
static long long ninv = 0, nrep = 0;
static int ubmode = 0, ubneed = 0, ubscore = 0, ubones = 0, ubsuf[N48 + 1];
static void process_solution(void) {
    long long XT[64], x[64], r[N48], pe[140];
    for (int a = 0; a < 64; a++) { long long v = xt0v[a]; for (int j = 0; j < n; j++) v += w[j] * XTi[j][a]; XT[a] = v; }
    for (int i = 0; i < N48; i++) { long long v = m[i]; for (int a = 0; a < 64; a++) v -= Pmm[i][a] * XT[a]; r[i] = v; }
    long long ci[N48];
    for (int k = 0; k < N48; k++) { long long v = 0; for (int i = 0; i < N48; i++) v += r[i] * SMD[i][k];
        if (v % Dden != 0) { fprintf(stderr, "NONINTEGRAL\n"); exit(3); } ci[k] = v / Dden; }
    for (int a = 0; a < 64; a++) { long long v = XT[a]; for (int k = 0; k < N48; k++) v += ci[k] * Sm[k][a]; x[a] = v; }
    long long dg = 0, n1 = 0, e = 0, c2 = 0;
    for (int a = 0; a < 64; a++) { dg += x[a] * degv[a]; n1 += x[a] * F1v[a]; e += x[a] * excv[a]; }
    if (dg != dd) { fprintf(stderr, "DEGREE_MISMATCH\n"); exit(3); }
    for (int k = 0; k < 140; k++) { long long v = 0; for (int a = 0; a < 64; a++) v += P140[k][a] * x[a]; if (v < 0) return; pe[k] = v; }
    for (int a = 0; a < 64; a++) { if (!x[a]) continue; long long v = 0; for (int b = 0; b < 64; b++) v += Gnm[a][b] * x[b]; c2 += x[a] * v; }
    long long n2 = dd - n1, M = n1 > n2 ? n1 : n2, mn = n1 < n2 ? n1 : n2;
    if (n1 < 1 || n2 < 1) return;
    int g0 = (2 * M + 4 <= e) && (e <= 6 * mn) && (c2 >= -2 - dd);
    int g1 = (2 * M <= e) && (e <= (6 * mn < 2 * M + 3 ? 6 * mn : 2 * M + 3)) && (c2 >= -dd);
    if (!(g0 || g1)) return;
    if (ubmode) {
        long long nu = 0; for (int j = 0; j < N48; j++) if (m[j] > 0) nu++;
        // genuine per-genus conditions (the inventory's g1 cap e <= 2M+3 is only a slicing rule, not a property of g = 1)
        int u0 = (2 * M + 4 <= e) && (e <= 6 * mn) && (c2 >= -2 - dd) && (2 * nu >= e + 2 * M + 4);
        int u1 = (2 * M <= e) && (e <= 6 * mn) && (c2 >= -dd) && (2 * nu >= e + 2 * M);
        if (!(u0 || u1)) return;
    }
    ninv++;
    for (int g = 0; g < NP; g++) {
        const short *pi = pinv + (long)g * 140;
        for (int k = 0; k < 140; k++) { long long a = pe[pi[k]]; if (a > pe[k]) return; if (a < pe[k]) break; }
    }
    nrep++;
    for (int a = 0; a < 64; a++) printf("%lld ", x[a]);
    printf("\n");
}
static void out_solution(void) {
    if (invmode) { nsol++; process_solution(); return; }
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
// 32R-67 unibranch mode (env SPLIT_UB): score = sum_j (2[m_j>0] - m_j) must reach ubneed = d (2nu - e >= d + 4 - 4g >= d);
// each parity-1 position adds at most +1 (m = 1), parity-0 positions at most 0.

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
    if (ubmode && ubscore + ubsuf[t] < ubneed) return;
    int j = order[t];
    charge(j, -1);
    for (int v = par[j]; ; v += 2) {
        if (ubmode && ubscore + (v > 0 ? 2 - v : 0) + ubsuf[t + 1] < ubneed) break;
        if (s2 + v * v + needs2 > s2maxg) break;
        int ok = 1;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; if (slack[q] - MU[q][j] * v < needq[q]) { ok = 0; break; } }
        if (!ok) break;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] -= MU[q][j] * v; }
        m[j] = v; if (ubmode) ubscore += (v > 0 ? 2 - v : 0);
        vdfs(t + 1, s2 + v * v);
        if (ubmode) ubscore -= (v > 0 ? 2 - v : 0);
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] += MU[q][j] * v; }
        m[j] = 0;
    }
    charge(j, +1);
}
// 32R-67b: precomputed per-bit lists (positions toggled by bit i, positions determined at bit i) and running counts
static int tog[N48][N48], ntog[N48], newd[N48][N48], nnewd[N48], undet_at[N48 + 1], detones;
static void bitdfs(int i) {
    if (ubmode && detones + undet_at[i] < ubneed) return;
    if (i == NI) {
        if (ubmode) { ubsuf[N48] = 0; for (int t = N48 - 1; t >= 0; t--) ubsuf[t] = ubsuf[t + 1] + (par[order[t]] ? 1 : 0); ubscore = 0; }
        vdfs(0, 0); return;
    }
    for (int b = 0; b < 2; b++) {
        if (b) for (int c = 0; c < ntog[i]; c++) par[tog[i][c]] ^= 1;
        int ok = 1, c;
        for (c = 0; c < nnewd[i]; c++) { int k = newd[i][c]; charge(k, +1); detones += par[k]; if (!feasible(k)) ok = 0; }
        if (ok) bitdfs(i + 1);
        for (c = 0; c < nnewd[i]; c++) { int k = newd[i][c]; charge(k, -1); detones -= par[k]; }
        if (b) for (int c2 = 0; c2 < ntog[i]; c2++) par[tog[i][c2]] ^= 1;
    }
}
static void mrec(int t, int s2, int s2max) {
    (void)t; (void)s2;
    s2maxg = s2max;
    memset(needq, 0, sizeof needq); needs2 = 0;
    for (int j = 0; j < N48; j++) par[j] = mtv[j] & 1;
    detones = 0; for (int j = 0; j < N48; j++) if (lastdep[j] < 0) detones += par[j];
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
    if (scanf("%d", &invmode) != 1) invmode = 0;
    if (invmode) {
        RD("%d", &dd);
        for (int a = 0; a < 64; a++) RD("%lld", &xt0v[a]);
        for (int j = 0; j < n; j++) for (int a = 0; a < 64; a++) RD("%lld", &XTi[j][a]);
        for (int i = 0; i < N48; i++) for (int a = 0; a < 64; a++) RD("%lld", &Pmm[i][a]);
        RD("%lld", &Dden);
        for (int i = 0; i < N48; i++) for (int k = 0; k < N48; k++) RD("%lld", &SMD[i][k]);
        for (int k = 0; k < N48; k++) for (int a = 0; a < 64; a++) RD("%lld", &Sm[k][a]);
        for (int k = 0; k < 140; k++) for (int a = 0; a < 64; a++) RD("%lld", &P140[k][a]);
        for (int a = 0; a < 64; a++) RD("%lld", &degv[a]);
        for (int a = 0; a < 64; a++) RD("%lld", &F1v[a]);
        for (int a = 0; a < 64; a++) RD("%lld", &excv[a]);
        for (int a = 0; a < 64; a++) for (int b = 0; b < 64; b++) RD("%lld", &Gnm[a][b]);
        RD("%d", &NP);
        pinv = malloc(sizeof(short) * 140 * (size_t)NP);
        for (long g = 0; g < (long)NP * 140; g++) { int v; RD("%d", &v); pinv[g] = (short)v; }
    }
    if (getenv("SPLIT_UB")) { if (!invmode) { fprintf(stderr, "SPLIT_UB needs invmode\n"); return 2; } ubmode = 1; ubneed = dd; }
    { const char *e = getenv("SPLIT_DEPTH"); int dd = e ? atoi(e) : 4; slev = n - 1 - dd; if (slev < 0) slev = 0; }
    // 32R-67c: change of parity coordinates. Column j of Drow is a functional c_j on F2^NI; greedily pick new basis
    // functionals among the columns so that as many columns as possible lie in the span of the first k picks, then
    // rewrite every column in the new basis (par_j = mtv_j + sum_k a_jk y_k). Same parity set, earlier determination.
    if (!getenv("SPLIT_NOREBASIS")) {
        unsigned col[N48]; for (int j = 0; j < N48; j++) { col[j] = 0; for (int i = 0; i < NI; i++) if (Drow[i][j]) col[j] |= 1u << i; }
        static unsigned char inspan[1 << 12]; unsigned basis[N48]; int nbz = 0;
        memset(inspan, 0, sizeof inspan); inspan[0] = 1;
        static unsigned spanlist[1 << 12]; int nspan = 1; spanlist[0] = 0;
        while (nbz < NI) {
            int best = -1, bc = -1;
            for (int j = 0; j < N48; j++) { if (inspan[col[j]]) continue; int c = 0;
                for (int k = 0; k < N48; k++) { if (inspan[col[k]]) { c++; continue; } if (inspan[col[k] ^ col[j]]) c++; }
                if (c > bc) { bc = c; best = j; } }
            unsigned b = col[best]; basis[nbz++] = b;
            for (int t2 = 0, n0 = nspan; t2 < n0; t2++) { unsigned v = spanlist[t2] ^ b; if (!inspan[v]) { inspan[v] = 1; spanlist[nspan++] = v; } }
        }
        // express each column in the new basis: solve col = sum a_k basis[k] by Gaussian elimination over F2
        unsigned piv[16]; int pivbit[16]; unsigned comb[16]; int np2 = 0;
        for (int k = 0; k < NI; k++) { unsigned v = basis[k], cm = 1u << k;
            for (int t2 = 0; t2 < np2; t2++) if (v >> pivbit[t2] & 1) { v ^= piv[t2]; cm ^= comb[t2]; }
            int pb = 0; while (!(v >> pb & 1)) pb++; piv[np2] = v; pivbit[np2] = pb; comb[np2] = cm; np2++; }
        for (int j = 0; j < N48; j++) { unsigned v = col[j], cm = 0;
            for (int t2 = 0; t2 < np2; t2++) if (v >> pivbit[t2] & 1) { v ^= piv[t2]; cm ^= comb[t2]; }
            if (v) { fprintf(stderr, "REBASIS_FAIL\n"); return 4; }
            for (int i = 0; i < NI; i++) Drow[i][j] = (cm >> i) & 1; }
    }
    for (int j = 0; j < N48; j++) { lastdep[j] = -1; for (int i = 0; i < NI; i++) if (Drow[i][j]) lastdep[j] = i; }
    for (int i = 0; i < NI; i++) { ntog[i] = 0; nnewd[i] = 0; for (int j = 0; j < N48; j++) { if (Drow[i][j]) tog[i][ntog[i]++] = j; if (lastdep[j] == i) newd[i][nnewd[i]++] = j; } }
    for (int i = 0; i <= NI; i++) { undet_at[i] = 0; for (int j = 0; j < N48; j++) if (lastdep[j] >= i) undet_at[i]++; }
    int t = 0, used[N48] = {0};
    for (int i = 0; i < NI; i++) { order[t++] = Ipos[i]; isI[Ipos[i]] = 1; used[Ipos[i]] = 1; }
    for (int j = 0; j < N48; j++) { ncurves[j] = 0; for (int q = 0; q < NQ; q++) if (MU[q][j]) curves[j][ncurves[j]++] = q; }
    while (t < N48) { int best = -1; for (int j = 0; j < N48; j++) if (!used[j] && (best < 0 || ncurves[j] > ncurves[best])) best = j; used[best] = 1; order[t++] = best; }
    for (int a = 0; a < 16; a++) zc[n][a] = z0[a];
    for (int a = 0; a < N48; a++) mtc[n][a] = mt0[a];
    for (int b = 0; b < nb; b++) bqc[n][b] = bq0[b];
    rec(n - 1, R);
    fprintf(stderr, "nodes %lld yleaves %lld yok %lld solutions %lld inventory %lld reps %lld\n", nodes, nyleaf, nyok, nsol, ninv, nrep);
    return 0;
}
