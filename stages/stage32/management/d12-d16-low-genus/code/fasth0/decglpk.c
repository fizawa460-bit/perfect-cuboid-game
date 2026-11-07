/* 32R-70 decomposition of m K - x  (c in {0..3}^140, c.Cm = m K - x, smallest m in 1..3) with GLPK's
   branch-and-cut, called in-process (replaces the per-call scipy/HiGHS-1.2 MILP).
   usage: decglpk decomp_cm.txt [tm_lim_ms] < xlist   (one x[64] per line)
   output per line:  m c[140]   |  NONE  (no bounded decomposition for m = 1..3)  |  UNK m  (time limit) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
static double now(void){ struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + 1e-9 * t.tv_nsec; }
static double T[8]; static long NC[8];
typedef struct glp_prob glp_prob; typedef struct glp_tree glp_tree;
typedef struct {
  int msg_lev, br_tech, bt_tech; double tol_int, tol_obj; int tm_lim, out_frq, out_dly;
  void (*cb_func)(glp_tree *T, void *info); void *cb_info; int cb_size, pp_tech; double mip_gap;
  int mir_cuts, gmi_cuts, cov_cuts, clq_cuts, presolve, binarize, fp_heur, ps_heur, ps_tm_lim, sr_heur;
  int use_sol; const char *save_sol; int alien; int flip; double foo_bar[23];
} glp_iocp;
typedef union { glp_iocp p; char pad[4096]; } iocp_u;
glp_prob *glp_create_prob(void); int glp_add_rows(glp_prob*, int); int glp_add_cols(glp_prob*, int);
void glp_set_row_bnds(glp_prob*, int, int, double, double); void glp_set_col_bnds(glp_prob*, int, int, double, double);
void glp_set_obj_coef(glp_prob*, int, double); void glp_set_col_kind(glp_prob*, int, int);
void glp_set_mat_col(glp_prob*, int, int, const int[], const double[]); void glp_init_iocp(glp_iocp*);
int glp_intopt(glp_prob*, const glp_iocp*); int glp_mip_status(glp_prob*); double glp_mip_col_val(glp_prob*, int);
int glp_term_out(int); int glp_simplex(glp_prob*, const void*); int glp_get_status(glp_prob*); void glp_set_obj_dir(glp_prob*, int);
#define GLP_MIN 1
#define GLP_DB 4
#define GLP_FX 5
#define GLP_IV 2
#define GLP_ON 1
#define GLP_OFF 0
#define GLP_OPT 5
#define GLP_FEAS 2
#define GLP_NOFEAS 4
/* ---- 32R-70 LP-based depth-first dive (own branch-and-bound without GLPK's tree overhead) ---- */
double glp_get_col_prim(glp_prob*, int); void glp_init_smcp(void*);
typedef union { struct { int msg_lev, meth; } p; char pad[4096]; } smcp_u;
static smcp_u SM; static glp_prob *GP; static int GN; static long dnodes, dlimit; static int dsol[256];
static int dive(void){
  if(++dnodes > dlimit) return -1;
  if(glp_simplex(GP, &SM) != 0) return 0;
  if(glp_get_status(GP) != GLP_OPT) return 0;
  int bf = -1; double bfr = 1.0, bx = 0;
  for(int i = 1; i <= GN; i++){ double v = glp_get_col_prim(GP, i); double fr = fabs(v - floor(v + 0.5));
    if(fr > 1e-6 && fr < bfr){ bfr = fr; bf = i; bx = v; } }
  if(bf < 0){ for(int i = 1; i <= GN; i++) dsol[i - 1] = (int)lround(glp_get_col_prim(GP, i)); return 1; }
  double lo = 0, hi = 3;   /* current bounds of bf: recover via glp_get_col_lb/ub */
  extern double glp_get_col_lb(glp_prob*, int); extern double glp_get_col_ub(glp_prob*, int);
  lo = glp_get_col_lb(GP, bf); hi = glp_get_col_ub(GP, bf);
  double fl = floor(bx), ce = fl + 1; int s;
  int up_first = (bx - fl) > 0.5;
  for(int k = 0; k < 2; k++){
    int up = (k == 0) ? up_first : !up_first;
    if(up){ glp_set_col_bnds(GP, bf, ce == hi ? GLP_FX : GLP_DB, ce, hi); }
    else  { glp_set_col_bnds(GP, bf, fl == lo ? GLP_FX : GLP_DB, lo, fl); }
    s = dive();
    glp_set_col_bnds(GP, bf, lo == hi ? GLP_FX : GLP_DB, lo, hi);
    if(s) return s;
  }
  return 0;
}
int main(int argc, char **argv){
  FILE *t = fopen(argv[1], "r"); int n, r; if(fscanf(t, "%d %d", &n, &r) != 2) return 1;
  int tm = argc > 2 ? atoi(argv[2]) : 20000; int objone = argc > 3 ? atoi(argv[3]) : 1;
  long *Cm = malloc(sizeof(long) * n * r), K[64];
  for(int i = 0; i < n * r; i++) if(fscanf(t, "%ld", &Cm[i]) != 1) return 1;
  for(int j = 0; j < r; j++) if(fscanf(t, "%ld", &K[j]) != 1) return 1;
  glp_term_out(GLP_OFF);
  glp_prob *P = glp_create_prob(); glp_set_obj_dir(P, GLP_MIN);
  glp_add_rows(P, r); glp_add_cols(P, n);
  int ind[65]; double val[65];
  for(int i = 0; i < n; i++){
    int k = 0; for(int j = 0; j < r; j++) if(Cm[i * r + j]){ k++; ind[k] = j + 1; val[k] = (double)Cm[i * r + j]; }
    glp_set_mat_col(P, i + 1, k, ind, val);
    glp_set_col_kind(P, i + 1, GLP_IV); glp_set_col_bnds(P, i + 1, GLP_DB, 0.0, 3.0);
    glp_set_obj_coef(P, i + 1, objone ? 1.0 : 0.0);
  }
  iocp_u U; memset(&U, 0, sizeof U); glp_init_iocp(&U.p);
  U.p.presolve = GLP_ON; U.p.tm_lim = tm; U.p.mip_gap = 1e9; U.p.msg_lev = 0;
  int fl = argc > 4 ? atoi(argv[4]) : 0;   /* bit0 fp_heur, bit1 gmi, bit2 mir, bit3 no sr_heur, bit4 br=most-frac(2), bit5 bt=depth(1), bit6 bt=best(3) */
  if(fl & 1) U.p.fp_heur = GLP_ON;
  if(fl & 2) U.p.gmi_cuts = GLP_ON;
  if(fl & 4) U.p.mir_cuts = GLP_ON;
  if(fl & 8) U.p.sr_heur = GLP_OFF;
  if(fl & 16) U.p.br_tech = 2;
  if(fl & 32) U.p.bt_tech = 1;
  if(fl & 64) U.p.bt_tech = 3;
  if(fl & 128) U.p.br_tech = 5;
  if(fl & 256) U.p.pp_tech = 0;
  if(fl & 1024) U.p.br_tech = 1;
  if(fl & 2048) U.p.br_tech = 3;
  int warm = (fl & 512) != 0; if(warm) U.p.presolve = GLP_OFF;
  int usedive = (fl & 4096) != 0; dlimit = argc > 5 ? atol(argv[5]) : 200;
  glp_init_smcp(&SM); SM.p.msg_lev = 0; SM.p.meth = 2; GP = P; GN = n;
  long x[64]; setvbuf(stdout, NULL, _IOLBF, 0);
  while(1){
    for(int j = 0; j < r; j++) if(scanf("%ld", &x[j]) != 1){ fprintf(stderr, "lp %.2fs n%ld lpinf %ld | mip feas %.2fs n%ld | mip inf %.2fs n%ld | dive %.2fs n%ld found %ld proved-inf %ld\n", T[0], NC[0], NC[1], T[2], NC[2], T[3], NC[3], T[4], NC[4], NC[5], NC[6]); return 0; }
    int done = 0;
    for(int m = 1; m <= 3 && !done; m++){
      for(int j = 0; j < r; j++){ double b = (double)(m * K[j] - x[j]); glp_set_row_bnds(P, j + 1, GLP_FX, b, b); }
      double t0 = now();
      if(warm){ int rs = glp_simplex(P, NULL); int ls = glp_get_status(P); T[0] += now() - t0; NC[0]++;
        if(rs == 0 && (ls == GLP_NOFEAS || ls == 6)){ NC[1]++; continue; }   /* LP relaxation infeasible (GLP_NOFEAS / GLP_UNBND n/a) */
        if(rs != 0 || ls != GLP_OPT){ printf("UNK %d lp %d %d\n", m, rs, ls); done = 1; break; } }
      if(usedive){ double t2 = now(); dnodes = 0; int ds = dive(); T[4] += now() - t2; NC[4]++;
        if(ds == 1){ NC[5]++;
          int ok = 1; for(int j = 0; j < r && ok; j++){ long s = 0; for(int i = 0; i < n; i++) s += dsol[i] * Cm[i * r + j]; if(s != m * K[j] - x[j]) ok = 0; }
          for(int i = 0; i < n; i++) if(dsol[i] < 0 || dsol[i] > 3) ok = 0;
          if(!ok){ printf("UNK %d divebad\n", m); done = 1; break; }
          printf("%d", m); for(int i = 0; i < n; i++) printf(" %d", dsol[i]); printf("\n"); done = 1; break; }
        if(ds == 0){ NC[6]++; continue; }   /* exhaustive: proof of infeasibility */
        glp_simplex(P, NULL); }
      double t1 = now(); int ret = glp_intopt(P, &U.p); int st = glp_mip_status(P); int cls = (st == GLP_OPT || st == GLP_FEAS) ? 2 : 3; T[cls] += now() - t1; NC[cls]++; if(getenv("DEC_TRACE")) fprintf(stderr, "T %d %.5f\n", cls, now() - t1);
      if(st == GLP_OPT || st == GLP_FEAS){
        int c[256]; for(int i = 0; i < n; i++) c[i] = (int)lround(glp_mip_col_val(P, i + 1));
        int ok = 1; for(int j = 0; j < r && ok; j++){ long s = 0; for(int i = 0; i < n; i++) s += c[i] * Cm[i * r + j]; if(s != m * K[j] - x[j]) ok = 0; }
        for(int i = 0; i < n; i++) if(c[i] < 0 || c[i] > 3) ok = 0;
        if(!ok){ printf("UNK %d bad\n", m); done = 1; break; }
        printf("%d", m); for(int i = 0; i < n; i++) printf(" %d", c[i]); printf("\n"); done = 1;
      } else if(st == GLP_NOFEAS || ret == 0x0A){ continue; }
      else { printf("UNK %d %d %d\n", m, ret, st); done = 1; }
    }
    if(!done) printf("NONE\n");
  }
}
