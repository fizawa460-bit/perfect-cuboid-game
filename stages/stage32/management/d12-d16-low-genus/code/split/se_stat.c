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
// 32R-70 fast path: x*Dden is affine in (w, m): x*Dden = A0 + sum_j w_j Aw[j] + sum_i m_i Bm[i]; the same holds for
// n1 = F1.x, e = exc.x, deg = degv.x and pe = P140.x. The w part is cached per y-leaf; the cheap linear filters
// (n1, e, nu) run before x, C^2 and pe are formed. Integer arithmetic; divisibility by Dden is asserted.
static long long A0[64], Aw[NMAX][64], Bm[N48][64];
static long long PE0[140], PEw[NMAX][140], PEm[N48][140];
static long long N10, N1w[NMAX], N1m[N48], E0, Ew[NMAX], Em[N48], DG0, DGw[NMAX], DGm[N48];
static long long leafid = 0, cacheid = -1, xwc[64], pewc[140], n1wc, ewc, dgwc;
static void lin(const long long *vec, long long *o0, long long *ow, long long *om) {
    long long v = 0; for (int a = 0; a < 64; a++) v += vec[a] * A0[a]; *o0 = v;
    for (int j = 0; j < n; j++) { v = 0; for (int a = 0; a < 64; a++) v += vec[a] * Aw[j][a]; ow[j] = v; }
    for (int i = 0; i < N48; i++) { v = 0; for (int a = 0; a < 64; a++) v += vec[a] * Bm[i][a]; om[i] = v; }
}
static void fast_setup(void) {
    for (int i = 0; i < N48; i++) for (int a = 0; a < 64; a++) { long long v = 0; for (int k = 0; k < N48; k++) v += SMD[i][k] * Sm[k][a]; Bm[i][a] = v; }
    long long pm[N48];
    for (int i = 0; i < N48; i++) { long long v = 0; for (int b = 0; b < 64; b++) v += Pmm[i][b] * xt0v[b]; pm[i] = v; }
    for (int a = 0; a < 64; a++) { long long v = Dden * xt0v[a]; for (int i = 0; i < N48; i++) v -= pm[i] * Bm[i][a]; A0[a] = v; }
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < N48; i++) { long long v = 0; for (int b = 0; b < 64; b++) v += Pmm[i][b] * XTi[j][b]; pm[i] = v; }
        for (int a = 0; a < 64; a++) { long long v = Dden * XTi[j][a]; for (int i = 0; i < N48; i++) v -= pm[i] * Bm[i][a]; Aw[j][a] = v; }
    }
    lin(F1v, &N10, N1w, N1m); lin(excv, &E0, Ew, Em); lin(degv, &DG0, DGw, DGm);
    for (int k = 0; k < 140; k++) {
        long long v = 0; for (int a = 0; a < 64; a++) v += P140[k][a] * A0[a]; PE0[k] = v;
        for (int j = 0; j < n; j++) { v = 0; for (int a = 0; a < 64; a++) v += P140[k][a] * Aw[j][a]; PEw[j][k] = v; }
        for (int i = 0; i < N48; i++) { v = 0; for (int a = 0; a < 64; a++) v += P140[k][a] * Bm[i][a]; PEm[i][k] = v; }
    }
}
static void process_solution(void) {
    if (cacheid != leafid) {
        cacheid = leafid;
        for (int a = 0; a < 64; a++) { long long v = A0[a]; for (int j = 0; j < n; j++) v += w[j] * Aw[j][a]; xwc[a] = v; }
        for (int k = 0; k < 140; k++) { long long v = PE0[k]; for (int j = 0; j < n; j++) v += w[j] * PEw[j][k]; pewc[k] = v; }
        n1wc = N10; ewc = E0; dgwc = DG0;
        for (int j = 0; j < n; j++) { n1wc += w[j] * N1w[j]; ewc += w[j] * Ew[j]; dgwc += w[j] * DGw[j]; }
    }
    int nz[N48], nnz = 0;
    long long n1 = n1wc, e = ewc, dg = dgwc;
    for (int i = 0; i < N48; i++) if (m[i]) { nz[nnz++] = i; n1 += m[i] * N1m[i]; e += m[i] * Em[i]; dg += m[i] * DGm[i]; }
    if (n1 % Dden || e % Dden || dg % Dden) { fprintf(stderr, "NONINTEGRAL\n"); exit(3); }
    n1 /= Dden; e /= Dden; dg /= Dden;
    if (dg != dd) { fprintf(stderr, "DEGREE_MISMATCH\n"); exit(3); }
    long long n2 = dd - n1, M = n1 > n2 ? n1 : n2, mn = n1 < n2 ? n1 : n2;
    if (n1 < 1 || n2 < 1) return;
    int g0e = (2 * M + 4 <= e) && (e <= 6 * mn);
    int g1e = (2 * M <= e) && (e <= (6 * mn < 2 * M + 3 ? 6 * mn : 2 * M + 3));
    if (!(g0e || g1e)) return;
    long long nu = nnz;
    if (ubmode) {
        int u0e = (2 * M + 4 <= e) && (e <= 6 * mn) && (2 * nu >= e + 2 * M + 4);
        int u1e = (2 * M <= e) && (e <= 6 * mn) && (2 * nu >= e + 2 * M);
        if (!(u0e || u1e)) return;
    }
    long long x[64], pe[140], c2 = 0;
    for (int a = 0; a < 64; a++) { long long v = xwc[a]; for (int t = 0; t < nnz; t++) v += m[nz[t]] * Bm[nz[t]][a];
        if (v % Dden) { fprintf(stderr, "NONINTEGRAL\n"); exit(3); } x[a] = v / Dden; }
    for (int a = 0; a < 64; a++) { if (!x[a]) continue; long long v = 0; for (int b = 0; b < 64; b++) v += Gnm[a][b] * x[b]; c2 += x[a] * v; }
    int g0 = g0e && (c2 >= -2 - dd);
    int g1 = g1e && (c2 >= -dd);
    if (!(g0 || g1)) return;
    if (ubmode) {
        int u0 = (2 * M + 4 <= e) && (e <= 6 * mn) && (c2 >= -2 - dd) && (2 * nu >= e + 2 * M + 4);
        int u1 = (2 * M <= e) && (e <= 6 * mn) && (c2 >= -dd) && (2 * nu >= e + 2 * M);
        if (!(u0 || u1)) return;
    }
    for (int k = 0; k < 140; k++) { long long v = pewc[k]; for (int t = 0; t < nnz; t++) v += m[nz[t]] * PEm[nz[t]][k];
        if (v < 0) return; pe[k] = v / Dden; }
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

// 32R-70: dense, vectorizable versions of charge/feasible (MUT[j][q] = MU[q][j], padded to NBP lanes).
#define NBP 128
static int MUT[N48][NBP] __attribute__((aligned(32)));
static int needqd[NBP] __attribute__((aligned(32))), slackd[NBP] __attribute__((aligned(32)));
static inline int charge(int j, int sgn) {
    if (!par[j]) return 1;
    needs2 += sgn;
    const int *mu = MUT[j];
    if (sgn > 0) { for (int q = 0; q < NBP; q++) needqd[q] += mu[q]; } else { for (int q = 0; q < NBP; q++) needqd[q] -= mu[q]; }
    return 1;
}
static inline int feasible(int j) {
    (void)j;
    if (needs2 > s2maxg) return 0;
    int bad = 0;
    for (int q = 0; q < NBP; q++) bad |= (slackd[q] < needqd[q]);
    return !bad;
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
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; if (slackd[q] - MU[q][j] * v < needqd[q]) { ok = 0; break; } }
        if (!ok) break;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slackd[q] -= MU[q][j] * v; }
        m[j] = v; if (ubmode) ubscore += (v > 0 ? 2 - v : 0);
        vdfs(t + 1, s2 + v * v);
        if (ubmode) ubscore -= (v > 0 ? 2 - v : 0);
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slackd[q] += MU[q][j] * v; }
        m[j] = 0;
    }
    charge(j, +1);
}
// 32R-67b: precomputed per-bit lists (positions toggled by bit i, positions determined at bit i) and running counts
static int tog[N48][N48], ntog[N48], newd[N48][N48], nnewd[N48], undet_at[N48 + 1], detones;
static long long nbit=0,nbitleaf=0,npat=0,nzero=0;
static void bitdfs(int i) { nbit++;
    if (ubmode && detones + undet_at[i] < ubneed) return;
    if (i == NI) {
        if (ubmode) { ubsuf[N48] = 0; for (int t = N48 - 1; t >= 0; t--) ubsuf[t] = ubsuf[t + 1] + (par[order[t]] ? 1 : 0); ubscore = 0; }
        nbitleaf++; vdfs(0, 0); return;
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
    { unsigned long long base = 0, col[16]; for (int j = 0; j < N48; j++) if (mtv[j] & 1) base |= 1ull << j;
      for (int i = 0; i < NI; i++) { col[i] = 0; for (int j = 0; j < N48; j++) if (Drow[i][j]) col[i] |= 1ull << j; }
      int cnt = 0;
      for (unsigned b = 0; b < (1u << NI); b++) { unsigned long long v = base; for (int i = 0; i < NI; i++) if (b >> i & 1) v ^= col[i];
        int pc = __builtin_popcountll(v); if (pc >= ubneed && pc <= s2max) cnt++; }
      npat += cnt; if (cnt == 0) nzero++; }
    s2maxg = s2max;
    memset(needqd, 0, sizeof needqd); needs2 = 0;
    for (int j = 0; j < N48; j++) par[j] = mtv[j] & 1;
    detones = 0; for (int j = 0; j < N48; j++) if (lastdep[j] < 0) detones += par[j];
    for (int j = 0; j < N48; j++) if (lastdep[j] < 0) { charge(j, +1); if (!feasible(j)) { for (int k = 0; k <= j; k++) if (lastdep[k] < 0) charge(k, -1); return; } }
    bitdfs(0);
    for (int j = 0; j < N48; j++) if (lastdep[j] < 0) charge(j, -1);
}
static void leaf(void) {
    nyleaf++; leafid++;
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
    for (int q = 0; q < NBP; q++) slackd[q] = q < nb ? (int)bqc[0][q] : 1 << 28;
    memset(m, 0, sizeof m);
    if (!getenv("SPLIT_NOM")) mrec(0, 0, s2max);
}
// 32R-68 CS pruning in the y-stage: with w_i..w_{n-1} fixed and budget nr, the remaining coordinates range over an
// ellipsoid with centre w* (back-substitution with t_k = 0) and form R_i^T D_i R_i; max of a linear form l over it is
// l.w* + sqrt(nr) * sigma[i][q], sigma[i][q]^2 = l^T (R_i^T D_i R_i)^{-1} l. Prune if some b_q cannot reach 0.
static double sigma[NMAX + 1][BMAX];
static int cs_on = 1;
static long long cs_pruned = 0;
static void cs_setup(void) {
    for (int i = 1; i <= n; i++) for (int q = 0; q < nb; q++) {
        double u[NMAX];
        for (int k = 0; k < i; k++) { double v = (double)BQ[k][q]; for (int j = 0; j < k; j++) v -= U[j][k] * u[j]; u[k] = v; }
        double ss = 0; for (int k = 0; k < i; k++) ss += u[k] * u[k] / D[k];
        sigma[i][q] = sqrt(ss);
    }
}
static int cs_ok(int i, double nr) {
    double ws[NMAX];
    for (int k = i - 1; k >= 0; k--) { double c = cen[k];
        for (int j = k + 1; j < n; j++) c -= U[k][j] * ((j < i ? ws[j] : (double)w[j]) - cen[j]);
        ws[k] = c; }
    double sq = sqrt(nr > 0 ? nr : 0);
    for (int q = 0; q < nb; q++) {
        double v = (double)bqc[i][q];
        for (int k = 0; k < i; k++) v += ws[k] * (double)BQ[k][q];
        v += sq * sigma[i][q];
        if (v < -1e-6 * (1.0 + fabs(v))) { cs_pruned++; return 0; }
    }
    return 1;
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
        } else if (!cs_on || i > slev || cs_ok(i, nr)) rec(i - 1, nr);
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
    if (invmode) fast_setup();
    if (getenv("SPLIT_NOCS")) cs_on = 0;
    cs_setup();
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
    if (NQ > NBP) { fprintf(stderr, "NBP too small"); return 5; }
    for (int j = 0; j < N48; j++) for (int q = 0; q < NBP; q++) MUT[j][q] = q < NQ ? MU[q][j] : 0;
    while (t < N48) { int best = -1; for (int j = 0; j < N48; j++) if (!used[j] && (best < 0 || ncurves[j] > ncurves[best])) best = j; used[best] = 1; order[t++] = best; }
    for (int a = 0; a < 16; a++) zc[n][a] = z0[a];
    for (int a = 0; a < N48; a++) mtc[n][a] = mt0[a];
    for (int b = 0; b < nb; b++) bqc[n][b] = bq0[b];
    rec(n - 1, R);
    fprintf(stderr, "cs_pruned %lld bitnodes %lld bitleaves %lld patterns %lld zeroleaves %lld\n", cs_pruned, nbit, nbitleaf, npat, nzero);
    fprintf(stderr, "nodes %lld yleaves %lld yok %lld solutions %lld inventory %lld reps %lld\n", nodes, nyleaf, nyok, nsol, ninv, nrep);
    return 0;
}
