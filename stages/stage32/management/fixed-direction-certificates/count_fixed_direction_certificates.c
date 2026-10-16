// Stage32 FIXED-DIRECTION-CERTIFICATES (research cycle 32R-12): exact count of compressed terminals surviving
//   unibranch census predicate (N220 family, support S10 + min(38, e - M10) >= req)
//   AND exact Hodge bound (h0 >= L)  AND  no fixed-direction certificate kills.
// Integer (__int128) arithmetic only.  Input: forms.txt (built by verify_fixed_direction_certificates.py) and strata.txt.
// Build: gcc -O2 -fopenmp -o count count_fixed_direction_certificates.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
typedef __int128 i128;
typedef long long ll;

static ll Q[13][13], QDEN;
static int ND;
static ll LIN[32][13], LDEN[32], CN[32], CD[32];
// precomputed per direction: RHS factor = CN * LDEN^2, LHS factor = QDEN * CD
static i128 RF[32], LF[32];

static int ord[10] = {0,1,2,3,5,6,7,8,9,10};   // exceptional positions in t (x4 = index 4)

typedef struct { int g, d, e, req; ll expect_prefixes; ll prefixes, survivors; ll hodge_only_survivors; } Stratum;

static void die(const char *m){ fprintf(stderr, "FAIL: %s\n", m); exit(1); }

// overflow guard for products used below
static i128 mul_chk(i128 a, i128 b) {
    i128 r;
    if (__builtin_mul_overflow(a, b, &r)) die("int128 overflow");
    return r;
}

static void count_prefix(const int *x, int g, int d, int e, ll *surv, ll *hsurv) {
    // t = (x0..x10, d, e); x4 varies 0..X
    ll t[13];
    for (int i = 0; i < 11; i++) t[i] = x[i];
    t[11] = d; t[12] = e;
    t[4] = 0;
    ll X = 19LL*d - 5LL*e;
    ll L = 2LL*g - 2 - d;
    // H(x4) = a x4^2 + b x4 + c
    i128 a = Q[4][4], b = 0, c = 0;
    for (int j = 0; j < 13; j++) if (j != 4) b += (i128)2*Q[4][j]*t[j];
    for (int i = 0; i < 13; i++) if (i != 4) for (int j = 0; j < 13; j++) if (j != 4) c += (i128)Q[i][j]*t[i]*t[j];
    i128 l0[32], l1[32];
    for (int k = 0; k < ND; k++) {
        i128 s = 0;
        for (int j = 0; j < 13; j++) if (j != 4) s += (i128)LIN[k][j]*t[j];
        l0[k] = s; l1[k] = LIN[k][4];
    }
    i128 LQ = (i128)L*QDEN;
    ll s1 = 0, s2 = 0;
    for (ll x4 = 0; x4 <= X; x4++) {
        i128 H = a*x4*x4 + b*x4 + c;
        if (H < LQ) continue;                 // Hodge-empty
        s2++;
        int killed = 0;
        i128 slack = H - LQ;                  // >= 0
        for (int k = 0; k < ND && !killed; k++) {
            i128 l = l0[k] + l1[k]*x4;
            if (l >= 0) continue;
            i128 lhs = mul_chk(mul_chk(l, l), LF[k]);
            i128 rhs = mul_chk(slack, RF[k]);
            if (lhs > rhs) killed = 1;
        }
        if (!killed) s1++;
    }
    *surv += s1; *hsurv += s2;
}

// enumerate canonical exceptional prefixes for a stratum, restricted to x0 == fix_x0
static void run_task(Stratum *S, int fix_x0, ll *pref, ll *surv, ll *hsurv) {
    int g = S->g, d = S->d, e = S->e, req = S->req;
    int x[11]; memset(x, 0, sizeof x);
    // iterative DFS over ord[1..9] with x0 fixed
    int v[10]; int mass[11]; int supp[11];
    v[0] = fix_x0; mass[0] = fix_x0; supp[0] = fix_x0 > 0;
    if (fix_x0 > e) return;
    int lvl = 1; v[1] = -1;
    while (lvl >= 1) {
        v[lvl]++;
        int m = mass[lvl-1] + v[lvl];
        if (m > e) { lvl--; continue; }
        // constraint x0 <= x1 at lvl==1
        if (lvl == 1 && v[1] < v[0]) { v[1] = v[0] - 1; continue; }
        mass[lvl] = m; supp[lvl] = supp[lvl-1] + (v[lvl] > 0);
        // prune: final S10 + (e - M10) >= req is necessary; each further positive coordinate adds 1 to S10 but at
        // least 1 to M10, so (e - m) - (req - supp) can only decrease -> if negative now, no completion survives,
        // and larger v at this level is no better (v=0 -> v=1 keeps it equal, larger v lowers it).
        if ((e - m) < (req - supp[lvl])) { lvl--; continue; }
        // second necessary part: S10 + 38 >= req, S10 <= supp + remaining variables
        if (supp[lvl] + (9 - lvl) + 38 < req) { if (v[lvl] == 0) continue; lvl--; continue; }
        if (lvl < 9) { lvl++; v[lvl] = -1; continue; }
        // full prefix: map to x
        for (int i = 0; i < 10; i++) x[ord[i]] = v[i];
        x[4] = 0;
        int M10 = mass[9], S10 = supp[9];
        int cap = e - M10 < 38 ? e - M10 : 38;
        if (S10 + cap < req) continue;
        if ((x[1] + x[8] + x[9] + x[10]) & 1) continue;
        if (x[0] == x[1]) {
            if (x[5] > x[8] || (x[5] == x[8] && x[6] > x[9])) continue;
        }
        (*pref)++;
        count_prefix(x, g, d, e, surv, hsurv);
    }
}

int main(int argc, char **argv) {
    if (argc < 3) die("usage: count forms.txt strata.txt");
    FILE *f = fopen(argv[1], "r"); if (!f) die("forms");
    if (fscanf(f, "%lld", &QDEN) != 1) die("qden");
    for (int i = 0; i < 13; i++) for (int j = 0; j < 13; j++) if (fscanf(f, "%lld", &Q[i][j]) != 1) die("Q");
    if (fscanf(f, "%d", &ND) != 1) die("nd");
    for (int k = 0; k < ND; k++) {
        if (fscanf(f, "%lld %lld %lld", &LDEN[k], &CN[k], &CD[k]) != 3) die("dir hdr");
        for (int j = 0; j < 13; j++) if (fscanf(f, "%lld", &LIN[k][j]) != 1) die("lin");
        RF[k] = mul_chk(mul_chk(CN[k], LDEN[k]), LDEN[k]);
        LF[k] = mul_chk(QDEN, CD[k]);
    }
    fclose(f);
    FILE *s = fopen(argv[2], "r"); if (!s) die("strata");
    int n; if (fscanf(s, "%d", &n) != 1) die("n");
    Stratum *St = calloc(n, sizeof(Stratum));
    for (int i = 0; i < n; i++) if (fscanf(s, "%d %d %d %d %lld", &St[i].g, &St[i].d, &St[i].e, &St[i].req, &St[i].expect_prefixes) != 5) die("stratum");
    fclose(s);
    // tasks = (stratum, x0)
    int nt = 0; int *ts = malloc(sizeof(int) * n * 80), *tx = malloc(sizeof(int) * n * 80);
    for (int i = 0; i < n; i++) for (int x0 = 0; x0 <= St[i].e / 2; x0++) { ts[nt] = i; tx[nt] = x0; nt++; }
    #pragma omp parallel for schedule(dynamic, 1)
    for (int k = 0; k < nt; k++) {
        ll p = 0, sv = 0, hs = 0;
        run_task(&St[ts[k]], tx[k], &p, &sv, &hs);
        #pragma omp atomic
        St[ts[k]].prefixes += p;
        #pragma omp atomic
        St[ts[k]].survivors += sv;
        #pragma omp atomic
        St[ts[k]].hodge_only_survivors += hs;
    }
    ll P = 0, SV = 0, HS = 0; int bad = 0;
    for (int i = 0; i < n; i++) {
        printf("%d %d %d %lld %lld %lld\n", St[i].g, St[i].d, St[i].e, St[i].prefixes, St[i].hodge_only_survivors, St[i].survivors);
        if (St[i].prefixes != St[i].expect_prefixes) { fprintf(stderr, "prefix mismatch g%d d%d e%d: %lld vs %lld\n", St[i].g, St[i].d, St[i].e, St[i].prefixes, St[i].expect_prefixes); bad = 1; }
        P += St[i].prefixes; SV += St[i].survivors; HS += St[i].hodge_only_survivors;
    }
    fprintf(stderr, "TOTAL prefixes %lld  hodge_survivors %lld  final_survivors %lld\n", P, HS, SV);
    if (bad) die("prefix count mismatch");
    return 0;
}
