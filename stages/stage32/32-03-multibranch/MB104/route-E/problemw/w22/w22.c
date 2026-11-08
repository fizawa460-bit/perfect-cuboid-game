/* Problem W, bidegree (2,2): all curves W in P1xP1 of bidegree (2,2) through >= 8 points of BxB, B = {0,inf,1,-1,i,-i},
   computed mod p = 10009 (i = 792^2).  DFS over increasing point indices, each new point must raise the rank.
   rank 8 at depth 8: unique curve W -> accepted once (greedy basis of its point set), |Omega| computed.
   rank 7 at depth 7 with >= 1 dependent point: a pencil through >= 8 points -> printed as FAMILY (analysed separately).
   Omega (E10 s2): |O1| + |O2| - 2j - h, O1 = 2 * #{beta : disc_x(beta) != 0}, j/h = points (beta,beta') on W simple in
   both directions with equal / different type.  Fibres with disc = 0 are flagged SPECIAL if the double point is singular. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define P 10009
typedef long long ll;
static ll md(ll a){a%=P; return a<0?a+P:a;}
static ll pw(ll a,ll e){ll r=1;a=md(a);while(e){if(e&1)r=r*a%P;a=a*a%P;e>>=1;}return r;}
static ll inv(ll a){return pw(a,P-2);}
static ll BX0[6],BX1[6]; static int TY[6];
static ll ROW[36][9];
static ll cnt_curve=0,cnt_fam=0,cnt_keep=0;
/* monomial index m = 3*a + b : X0^a X1^(2-a) Y0^b Y1^(2-b) */
static void rowof(int pt, ll *r){int bx=pt/6,by=pt%6; for(int a=0;a<3;a++)for(int b=0;b<3;b++){
  r[3*a+b]= pw(BX0[bx],a)*pw(BX1[bx],2-a)%P * (pw(BX0[by],b)*pw(BX1[by],2-b)%P) %P;}}
static ll evalW(const ll *w,int pt){ll s=0; for(int m=0;m<9;m++) s+=w[m]*ROW[pt][m]%P; return s%P;}
/* restriction of W to x = beta: quadratic in (Y0,Y1): coefficient of Y0^b Y1^(2-b) */
static void fibx(const ll *w,int bx,ll *q){for(int b=0;b<3;b++){ll s=0;for(int a=0;a<3;a++) s+=w[3*a+b]*(pw(BX0[bx],a)*pw(BX1[bx],2-a)%P)%P; q[b]=s%P;}}
static void fiby(const ll *w,int by,ll *q){for(int a=0;a<3;a++){ll s=0;for(int b=0;b<3;b++) s+=w[3*a+b]*(pw(BX0[by],b)*pw(BX1[by],2-b)%P)%P; q[a]=s%P;}}
static ll disc(const ll *q){return md(q[1]*q[1]-4*q[0]%P*q[2]);}
static int iszero(const ll *q){return q[0]==0&&q[1]==0&&q[2]==0;}
/* rank-reduced basis kept per depth */
static ll RB[10][9][9]; static int PIV[10][9]; static int RK[10];
static int chosen[9];
static int reduce_into(int d,const ll *r,ll *out){ /* reduce r by basis at depth d; return pivot col or -1 */
  memcpy(out,r,9*sizeof(ll));
  for(int k=0;k<RK[d];k++){int c=PIV[d][k]; if(out[c]){ll f=out[c]; for(int m=0;m<9;m++) out[m]=md(out[m]-f*RB[d][k][m]);}}
  for(int m=0;m<9;m++) if(out[m]) return m; return -1;}
static void push(int d,const ll *red,int piv){ /* basis at d+1 = basis d + red (normalized, fully reduced) */
  RK[d+1]=RK[d]; memcpy(RB[d+1],RB[d],sizeof(RB[d])); memcpy(PIV[d+1],PIV[d],sizeof(PIV[d]));
  ll v[9]; ll f=inv(red[piv]); for(int m=0;m<9;m++) v[m]=red[m]*f%P;
  for(int k=0;k<RK[d+1];k++){ll g=RB[d+1][k][piv]; if(g) for(int m=0;m<9;m++) RB[d+1][k][m]=md(RB[d+1][k][m]-g*v[m]);}
  memcpy(RB[d+1][RK[d+1]],v,sizeof(v)); PIV[d+1][RK[d+1]]=piv; RK[d+1]++;}
static void kernel(int d,ll *w){ /* rank 8: kernel vector */
  int isp[9]={0}; for(int k=0;k<8;k++) isp[PIV[d][k]]=1; int fr=-1; for(int m=0;m<9;m++) if(!isp[m]) fr=m;
  for(int m=0;m<9;m++) w[m]=0; w[fr]=1; for(int k=0;k<8;k++) w[PIV[d][k]]=md(-RB[d][k][fr]);
  for(int m=0;m<9;m++) if(w[m]){ll f=inv(w[m]); for(int t=0;t<9;t++) w[t]=w[t]*f%P; break;}}
static void analyse(const ll *w){
  /* point set and greedy-basis dedupe */
  int on[36],n=0; for(int pt=0;pt<36;pt++){on[pt]=(evalW(w,pt)==0); n+=on[pt];}
  { ll B2[9][9]; int pv[9]; int rk=0; int g[9]; int ng=0;
    for(int pt=0;pt<36 && rk<8;pt++) if(on[pt]){ ll r[9]; memcpy(r,ROW[pt],sizeof(r));
      for(int k=0;k<rk;k++){if(r[pv[k]]){ll f=r[pv[k]]; for(int m=0;m<9;m++) r[m]=md(r[m]-f*B2[k][m]);}}
      int c=-1; for(int m=0;m<9;m++) if(r[m]){c=m;break;}
      if(c>=0){ll f=inv(r[c]); for(int m=0;m<9;m++) r[m]=r[m]*f%P; for(int k=0;k<rk;k++){ll gg=B2[k][c]; if(gg) for(int m=0;m<9;m++) B2[k][m]=md(B2[k][m]-gg*r[m]);}
        memcpy(B2[rk],r,sizeof(r)); pv[rk]=c; rk++; g[ng++]=pt;}}
    for(int k=0;k<8;k++) if(g[k]!=chosen[k]) return; }
  cnt_curve++;
  int O1=0,O2=0,j=0,h=0,special=0,vline=0; ll q[3]; int dx[6],dy[6];
  for(int b=0;b<6;b++){fibx(w,b,q); if(iszero(q)){vline=1;dx[b]=0;} else {dx[b]=(disc(q)!=0); if(dx[b]) O1+=2;}}
  for(int b=0;b<6;b++){fiby(w,b,q); if(iszero(q)){vline=1;dy[b]=0;} else {dy[b]=(disc(q)!=0); if(dy[b]) O2+=2;}}
  for(int pt=0;pt<36;pt++) if(on[pt]){int bx=pt/6,by=pt%6;
    if(dx[bx]&&dy[by]){ if(TY[bx]==TY[by]) j++; else h++; }
    else if(!dx[bx]&&!dy[by]) special=1; /* double in both directions: possibly a singular point */ }
  int om=O1+O2-2*j-h;
  if(om<=4||special||vline){ cnt_keep++;
    printf("CURVE om %d O1 %d O2 %d j %d h %d npts %d special %d vline %d w",om,O1,O2,j,h,n,special,vline);
    for(int m=0;m<9;m++) printf(" %lld",w[m]); printf("\n"); }
}
static void dfs(int d,int start){
  if(RK[d]==8){ ll w[9]; kernel(d,w); analyse(w); return; }
  if(d==7){ /* rank 7: is there a dependent point (pencil through >= 8 points)? only report once: first dependent > last chosen not required */
    int dep=0; ll red[9]; for(int pt=0;pt<36;pt++){int used=0; for(int k=0;k<7;k++) if(chosen[k]==pt) used=1; if(used) continue;
      if(reduce_into(d,ROW[pt],red)<0) dep++;}
    if(dep>0){ /* report only if chosen is the greedy basis of the common point set */
      int common[36]; int nc=0; for(int pt=0;pt<36;pt++){ if(reduce_into(d,ROW[pt],red)<0) {common[nc++]=pt;} }
      /* greedy basis of common set */
      ll B2[9][9]; int pv[9]; int rk=0; int g[9],ng=0;
      for(int t=0;t<nc && rk<7;t++){ll r[9]; memcpy(r,ROW[common[t]],sizeof(r));
        for(int k=0;k<rk;k++){if(r[pv[k]]){ll f=r[pv[k]]; for(int m=0;m<9;m++) r[m]=md(r[m]-f*B2[k][m]);}}
        int c=-1; for(int m=0;m<9;m++) if(r[m]){c=m;break;}
        if(c>=0){ll f=inv(r[c]); for(int m=0;m<9;m++) r[m]=r[m]*f%P; for(int k=0;k<rk;k++){ll gg=B2[k][c]; if(gg) for(int m=0;m<9;m++) B2[k][m]=md(B2[k][m]-gg*r[m]);}
          memcpy(B2[rk],r,sizeof(r)); pv[rk]=c; rk++; g[ng++]=common[t];}}
      int same=1; for(int k=0;k<7;k++) if(g[k]!=chosen[k]) same=0;
      if(same){ cnt_fam++; printf("FAMILY npts %d pts",nc); for(int t=0;t<nc;t++) printf(" %d",common[t]); printf("\n"); }
    }
  }
  for(int pt=start;pt<36;pt++){ ll red[9]; int c=reduce_into(d,ROW[pt],red); if(c<0) continue;
    chosen[d]=pt; push(d,red,c); dfs(d+1,pt+1); }
}
int main(void){
  ll I=pw(792,2); /* i */
  ll xs[6]={0,0,1,P-1,I,md(-I)}; int inf[6]={0,1,0,0,0,0}; int ty[6]={0,0,1,1,2,2}; /* e,e,b,b,a,a */
  for(int b=0;b<6;b++){ if(inf[b]){BX0[b]=0;BX1[b]=1;} else {BX0[b]=1;BX1[b]=xs[b];} TY[b]=ty[b]; }
  if(md(I*I+1)!=0){printf("bad i\n");return 1;}
  for(int pt=0;pt<36;pt++) rowof(pt,ROW[pt]);
  RK[0]=0; dfs(0,0);
  fprintf(stderr,"curves(rank8) %lld families(rank7,>=8pts) %lld kept %lld\n",cnt_curve,cnt_fam,cnt_keep);
  printf("SUMMARY curves %lld families %lld kept %lld\n",cnt_curve,cnt_fam,cnt_keep);
  return 0;}
