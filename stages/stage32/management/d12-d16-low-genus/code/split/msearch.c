// 32R-60: m-search for the split enumeration.
// Input (stdin): header "NQ NI", then MU (NQ x 48 ints), then the 10 information positions I and the RREF rows of D
// restricted (10 rows x 48 bits), then per case: "id s2max", mt[48], bq[NQ]. Terminated by EOF.
// For each case: all m in Z_{>=0}^48 with (m - mt) mod 2 in D, sum_j MU[q][j] m_j <= bq[q], sum m_j^2 <= s2max.
// Output: "id m_0 ... m_47" per solution.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 48
static int NQ, NI;
static int MU[256][N];
static int Ipos[N], Drow[N][N];     // Drow[i][j]: bit of the i-th RREF codeword at position j
static int order[N];                 // I positions first, then the others
static int isI[N];
static int curves[N][256], ncurves[N];
static long long nsol;
static int m[N], slack[256], vI[N], mt[N];
static int id;
static int target_parity[N];         // for J positions: required parity of m_j given current vI
static void out(void) {
    printf("%d", id);
    for (int j = 0; j < N; j++) printf(" %d", m[j]);
    printf("\n"); nsol++;
}
static void rec(int t, int s2, int s2max) {
    if (t == N) { out(); return; }
    int j = order[t];
    if (t == NI) {
        // all I bits chosen: determine parities of J positions: v = sum_i vI[i] * Drow[i]
        for (int jj = 0; jj < N; jj++) {
            int b = 0;
            for (int i = 0; i < NI; i++) if (vI[i]) b ^= Drow[i][jj];
            target_parity[jj] = (mt[jj] + b) & 1;
        }
    }
    int start = 0, step = 1;
    if (!isI[j]) { start = target_parity[j]; step = 2; }
    for (int v = start; ; v += step) {
        if (s2 + v * v > s2max) break;
        int ok = 1;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; if (slack[q] < MU[q][j] * v) { ok = 0; break; } }
        if (!ok) break;
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] -= MU[q][j] * v; }
        m[j] = v;
        if (isI[j]) {   // parity bit of (m_j - mt_j) for the information position
            int i = 0; while (Ipos[i] != j) i++;
            vI[i] = (v - mt[j]) & 1;
        }
        rec(t + 1, s2 + v * v, s2max);
        for (int c = 0; c < ncurves[j]; c++) { int q = curves[j][c]; slack[q] += MU[q][j] * v; }
        m[j] = 0;
    }
}
int main(void) {
    if (scanf("%d %d", &NQ, &NI) != 2) return 1;
    for (int q = 0; q < NQ; q++) for (int j = 0; j < N; j++) scanf("%d", &MU[q][j]);
    for (int i = 0; i < NI; i++) scanf("%d", &Ipos[i]);
    for (int i = 0; i < NI; i++) for (int j = 0; j < N; j++) scanf("%d", &Drow[i][j]);
    memset(isI, 0, sizeof isI);
    int t = 0;
    for (int i = 0; i < NI; i++) { order[t++] = Ipos[i]; isI[Ipos[i]] = 1; }
    // remaining positions: most constrained first
    int used[N] = {0};
    for (int i = 0; i < NI; i++) used[Ipos[i]] = 1;
    for (int j = 0; j < N; j++) { ncurves[j] = 0; for (int q = 0; q < NQ; q++) if (MU[q][j]) curves[j][ncurves[j]++] = q; }
    while (t < N) {
        int best = -1;
        for (int j = 0; j < N; j++) if (!used[j] && (best < 0 || ncurves[j] > ncurves[best])) best = j;
        used[best] = 1; order[t++] = best;
    }
    int s2max; long long ncase = 0;
    while (scanf("%d %d", &id, &s2max) == 2) {
        for (int j = 0; j < N; j++) scanf("%d", &mt[j]);
        for (int q = 0; q < NQ; q++) scanf("%d", &slack[q]);
        memset(m, 0, sizeof m);
        rec(0, 0, s2max);
        ncase++;
    }
    fprintf(stderr, "cases %lld solutions %lld\n", ncase, nsol);
    return 0;
}
