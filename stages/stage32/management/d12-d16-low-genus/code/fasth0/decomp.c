/* 32R-70 decomposition search  c in {0..3}^140,  c.Cm = v  (replaces the HiGHS MILP).
   Variables: 76 free c_F; the 64 basis coefficients are  e = y - c_F.A  (y = v.Binv), each must lie in [0,3].
   Depth-first search with bounds propagation; a finished search is a proof (OK or INF), a search that hits
   the node limit answers UNK (caller falls back to the MILP).
   stdin, one query per line:  v[64] hint[140]   (hint: -1 = none)
   stdout:  OK c[140]  |  INF nodes  |  UNK nodes */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXF 128
#define MAXR 64
static int n, r, nf, P[MAXR], F[MAXF];
static long Binv[MAXR][MAXR];
static int A[MAXF][MAXR];
static int nzr[MAXR], nzidx[MAXR][MAXF];       /* per row: free vars with nonzero coefficient */
static long y[MAXR];
static int hint[MAXF];
static long nodes, limit;
static int sol[MAXF];
static long fdiv(long a, long b){ long q=a/b; if((a%b)&&((a<0)!=(b<0))) q--; return q; }
static long cdiv(long a, long b){ return -fdiv(-a,b); }
/* returns 0 on conflict */
static int propagate(int *lo, int *hi){
  int changed = 1;
  while(changed){
    changed = 0;
    for(int i=0;i<r;i++){
      long mn=y[i], mx=y[i];
      for(int t=0;t<nzr[i];t++){ int f=nzidx[i][t]; long a=A[f][i];
        if(a>0){ mn-=a*hi[f]; mx-=a*lo[f]; } else { mn-=a*lo[f]; mx-=a*hi[f]; } }
      if(mx<0||mn>3) return 0;
      if(mn>=0&&mx<=3) continue;
      for(int t=0;t<nzr[i];t++){ int f=nzidx[i][t]; if(lo[f]==hi[f]) continue; long a=A[f][i];
        long Rmin, Rmax;     /* range of y - sum_{g!=f} a_g c_g */
        if(a>0){ Rmin=mn+a*hi[f]; Rmax=mx+a*lo[f]; } else { Rmin=mn+a*lo[f]; Rmax=mx+a*hi[f]; }
        long L,U;
        if(a>0){ L=cdiv(Rmin-3,a); U=fdiv(Rmax,a); } else { L=cdiv(Rmax,a); U=fdiv(Rmin-3,a); }
        if(L>lo[f]){ lo[f]=(int)L; changed=1; }
        if(U<hi[f]){ hi[f]=(int)U; changed=1; }
        if(lo[f]>hi[f]) return 0;
      }
    }
  }
  return 1;
}
static int deg[MAXF];
/* 1 found, 0 exhausted, -1 limit */
static int dfs(int *lo, int *hi){
  if(++nodes>limit) return -1;
  if(!propagate(lo,hi)) return 0;
  int bf=-1, bs=99, bd=-1;
  for(int f=0;f<nf;f++){ int s=hi[f]-lo[f]; if(s==0) continue;
    if(s<bs||(s==bs&&deg[f]>bd)){ bs=s; bd=deg[f]; bf=f; } }
  if(bf<0){ memcpy(sol,lo,sizeof(int)*nf); return 1; }
  int vals[4], nv=0, h=hint[bf];
  if(h<lo[bf]||h>hi[bf]) h=lo[bf];
  vals[nv++]=h;
  for(int d=1;d<4;d++){ if(h-d>=lo[bf]) vals[nv++]=h-d; if(h+d<=hi[bf]) vals[nv++]=h+d; }
  int lo2[MAXF], hi2[MAXF];
  for(int k=0;k<nv;k++){
    memcpy(lo2,lo,sizeof(int)*nf); memcpy(hi2,hi,sizeof(int)*nf);
    lo2[bf]=hi2[bf]=vals[k];
    int s=dfs(lo2,hi2); if(s) return s;
  }
  return 0;
}
int main(int argc, char **argv){
  FILE *t=fopen(argv[1],"r"); limit = argc>2 ? atol(argv[2]) : 100000;
  if(fscanf(t,"%d %d",&n,&r)!=2) return 1; nf=n-r;
  for(int i=0;i<r;i++) if(fscanf(t,"%d",&P[i])!=1) return 1;
  for(int i=0;i<nf;i++) if(fscanf(t,"%d",&F[i])!=1) return 1;
  for(int i=0;i<r;i++) for(int j=0;j<r;j++) if(fscanf(t,"%ld",&Binv[i][j])!=1) return 1;
  for(int i=0;i<nf;i++) for(int j=0;j<r;j++) if(fscanf(t,"%d",&A[i][j])!=1) return 1;
  for(int i=0;i<r;i++){ nzr[i]=0; for(int f=0;f<nf;f++) if(A[f][i]){ nzidx[i][nzr[i]++]=f; deg[f]++; } }
  long v[MAXR]; int h[256];
  setvbuf(stdout,NULL,_IOLBF,0);
  while(1){
    for(int j=0;j<r;j++) if(scanf("%ld",&v[j])!=1) return 0;
    for(int j=0;j<n;j++) if(scanf("%d",&h[j])!=1) return 0;
    for(int k=0;k<r;k++){ long s=0; for(int j=0;j<r;j++) s+=v[j]*Binv[j][k]; y[k]=s; }
    for(int f=0;f<nf;f++){ hint[f]=h[F[f]]; if(hint[f]<0) hint[f]=0; }
    int lo[MAXF], hi[MAXF]; for(int f=0;f<nf;f++){ lo[f]=0; hi[f]=3; }
    nodes=0; int s=dfs(lo,hi);
    if(s==1){
      int c[256];
      for(int f=0;f<nf;f++) c[F[f]]=sol[f];
      for(int i=0;i<r;i++){ long e=y[i]; for(int f=0;f<nf;f++) e-=(long)A[f][i]*sol[f]; c[P[i]]=(int)e; }
      printf("OK"); for(int j=0;j<n;j++) printf(" %d",c[j]); printf("\n");
    } else printf("%s %ld\n", s==0?"INF":"UNK", nodes);
  }
}
