/* 32R-93, k = 4 (Problem W4), bidegree (2,3) [deg p1 = 2: W quadratic in Y; deg p2 = 3: W cubic in X].
   B = mu_8 mod p = 10009 (labels: odd powers of zeta = u, even = v).  j >= 4 max(a,b) = 12 label-matched points.
   W has 12 coefficients: DFS over the 32 matched points with rank increase (each set = greedy basis of the point set
   of the result, so every curve / family is reported once).  rank 11: unique curve, |Omega| computed;
   rank 10 / rank 9 with >= 12 common matched points: FAMILY / NET lines (analysed separately).
   |Omega| = O1 + O2 - 2j - h: x-fibre (quadratic in Y) gives 2 if disc != 0; y-fibre (cubic in X) gives 3 if
   disc != 0, else 1 (one simple root, or a triple root); a point counts in j / h if it is odd in both directions. */
#include <stdio.h>
#include <string.h>
#define P 10009
#define NM 12
typedef long long ll;
static ll md(ll a){a%=P; return a<0?a+P:a;}
static ll pw(ll a,ll e){ll r=1;a=md(a);while(e){if(e&1)r=r*a%P;a=a*a%P;e>>=1;}return r;}
static ll inv(ll a){return pw(a,P-2);}
static ll XV[8]; static int TY[8];
static ll ROW[64][NM]; static int MT[32]; static int NMT=0;
static long long cnt_curve=0,cnt_fam=0,cnt_net=0,cnt_keep=0;
/* monomial m = 3*j + i : X^i Y^j (affine x = X, y = Y), i = 0..3, j = 0..2 */
static void rowof(int pt, ll *r){int bx=pt/8,by=pt%8; for(int j=0;j<3;j++)for(int i=0;i<4;i++) r[3*0+4*j+i]=pw(XV[bx],i)*pw(XV[by],j)%P;}
static ll evalW(const ll *w,int pt){ll s=0; for(int m=0;m<NM;m++) s+=w[m]*ROW[pt][m]%P; return s%P;}
static void fibx(const ll *w,int bx,ll *q){for(int j=0;j<3;j++){ll s=0;for(int i=0;i<4;i++) s+=w[4*j+i]*pw(XV[bx],i)%P; q[j]=s%P;}} /* quadratic in y */
static void fiby(const ll *w,int by,ll *q){for(int i=0;i<4;i++){ll s=0;for(int j=0;j<3;j++) s+=w[4*j+i]*pw(XV[by],j)%P; q[i]=s%P;}} /* cubic in x */
static ll disc2(const ll *q){return md(q[1]*q[1]-4*q[0]%P*q[2]);}
static ll disc3(const ll *q){ll a=q[3],b=q[2],c=q[1],d=q[0]; /* a x^3 + b x^2 + c x + d */
  return md(b*b%P*c%P*c - 4*a%P*c%P*c%P*c - 4*b%P*b%P*b%P*d - 27*a%P*a%P*d%P*d + 18*a%P*b%P*c%P*d);}
static int deg3(const ll *q){for(int i=3;i>=0;i--) if(q[i]) return i; return -1;}
static int rootmult(const ll *q,ll x){ /* multiplicity of root x of the affine cubic q (degree <= 3) */
  ll c[4]; memcpy(c,q,sizeof(c)); int n=deg3(c); int m=0;
  while(n>=1){ ll v=0; for(int i=n;i>=0;i--) v=md(v*x+c[i]); if(v) break; /* divide by (X - x) */
    ll b[4]={0,0,0,0}; b[n-1]=c[n]; for(int i=n-1;i>=1;i--) b[i-1]=md(c[i]+x*b[i]); memcpy(c,b,sizeof(c)); n--; m++; }
  return m; }
static ll RB[13][NM][NM]; static int PIV[13][NM]; static int RK[13]; static int chosen[NM];
static int reduce_into(int d,const ll *r,ll *out){ memcpy(out,r,NM*sizeof(ll));
  for(int k=0;k<RK[d];k++){int c=PIV[d][k]; if(out[c]){ll f=out[c]; for(int m=0;m<NM;m++) out[m]=md(out[m]-f*RB[d][k][m]);}}
  for(int m=0;m<NM;m++) if(out[m]) return m; return -1;}
static void push(int d,const ll *red,int piv){ RK[d+1]=RK[d]; memcpy(RB[d+1],RB[d],sizeof(RB[d])); memcpy(PIV[d+1],PIV[d],sizeof(PIV[d]));
  ll v[NM]; ll f=inv(red[piv]); for(int m=0;m<NM;m++) v[m]=red[m]*f%P;
  for(int k=0;k<RK[d+1];k++){ll g=RB[d+1][k][piv]; if(g) for(int m=0;m<NM;m++) RB[d+1][k][m]=md(RB[d+1][k][m]-g*v[m]);}
  memcpy(RB[d+1][RK[d+1]],v,sizeof(v)); PIV[d+1][RK[d+1]]=piv; RK[d+1]++;}
static void kernel(int d,ll *w){ int isp[NM]={0}; for(int k=0;k<RK[d];k++) isp[PIV[d][k]]=1; int fr=-1; for(int m=0;m<NM;m++) if(!isp[m]) fr=m;
  for(int m=0;m<NM;m++) w[m]=0; w[fr]=1; for(int k=0;k<RK[d];k++) w[PIV[d][k]]=md(-RB[d][k][fr]);
  for(int m=0;m<NM;m++) if(w[m]){ll f=inv(w[m]); for(int t=0;t<NM;t++) w[t]=w[t]*f%P; break;}}
static int greedy_is(const int *common,int nc,int rk){ /* chosen[0..rk-1] == greedy basis of the common set? */
  ll B2[NM][NM]; int pv[NM]; int r=0; int g[NM],ng=0;
  for(int t=0;t<nc && r<rk;t++){ ll x[NM]; memcpy(x,ROW[common[t]],sizeof(x));
    for(int k=0;k<r;k++){if(x[pv[k]]){ll f=x[pv[k]]; for(int m=0;m<NM;m++) x[m]=md(x[m]-f*B2[k][m]);}}
    int c=-1; for(int m=0;m<NM;m++) if(x[m]){c=m;break;}
    if(c>=0){ll f=inv(x[c]); for(int m=0;m<NM;m++) x[m]=x[m]*f%P; for(int k=0;k<r;k++){ll gg=B2[k][c]; if(gg) for(int m=0;m<NM;m++) B2[k][m]=md(B2[k][m]-gg*x[m]);}
      memcpy(B2[r],x,sizeof(x)); pv[r]=c; r++; g[ng++]=common[t];}}
  for(int k=0;k<rk;k++) if(g[k]!=chosen[k]) return 0; return 1;}
static void analyse(const ll *w){
  int common[32],nc=0; for(int t=0;t<NMT;t++) if(evalW(w,MT[t])==0) common[nc++]=MT[t];
  if(nc<12) return;
  if(!greedy_is(common,nc,11)) return;
  cnt_curve++;
  int O1=0,O2=0,j=0,h=0,vl=0; ll q[4]; int dx[8],ny[8]; ll cy[8][4];
  for(int b=0;b<8;b++){fibx(w,b,q); if(!q[0]&&!q[1]&&!q[2]){vl=1;dx[b]=0;} else {dx[b]=(disc2(q)!=0); if(dx[b]) O1+=2;}}
  for(int b=0;b<8;b++){fiby(w,b,cy[b]); if(deg3(cy[b])<0){vl=1;ny[b]=0;} else { if(deg3(cy[b])<3) ny[b]=-1; /* root at infinity: not in B */ O2+= (disc3(cy[b])!=0)?3:1; }}
  for(int pt=0;pt<64;pt++) if(evalW(w,pt)==0){int bx=pt/8,by=pt%8; if(!dx[bx]) continue; if(deg3(cy[by])<0) continue;
    if(rootmult(cy[by],XV[bx])%2==1){ if(TY[bx]==TY[by]) j++; else h++; } }
  int om=O1+O2-2*j-h;
  if(om<=4 && !vl){ cnt_keep++; printf("CURVE om %d O1 %d O2 %d j %d h %d npts %d w",om,O1,O2,j,h,nc); for(int m=0;m<NM;m++) printf(" %lld",w[m]); printf("\n"); }
}
static void family(int d){ /* rank d (10 or 9): common matched points */
  int common[32],nc=0; ll red[NM]; for(int t=0;t<NMT;t++) if(reduce_into(d,ROW[MT[t]],red)<0) common[nc++]=MT[t];
  if(nc<12) return; if(!greedy_is(common,nc,RK[d])) return;
  if(RK[d]==10){cnt_fam++; printf("FAMILY npts %d pts",nc);} else {cnt_net++; printf("NET rank %d npts %d pts",RK[d],nc);}
  for(int t=0;t<nc;t++) printf(" %d",common[t]); printf("\n");}
static void dfs(int d,int start){
  if(RK[d]==11){ ll w[NM]; kernel(d,w); analyse(w); return; }
  if(RK[d]==10||RK[d]==9) family(d);
  for(int tt=start;tt<NMT;tt++){ int pt=MT[tt]; ll red[NM]; int c=reduce_into(d,ROW[pt],red); if(c<0) continue;
    chosen[d]=pt; push(d,red,c); dfs(d+1,tt+1); }
}
int main(void){
  ll z=0; for(ll g=2;g<P;g++){ if(pw(g,4)==P-1){z=g;break;} }
  for(int b=0;b<8;b++){ XV[b]=pw(z,b); TY[b]=(b%2==1)?0:1; }
  for(int pt=0;pt<64;pt++){ rowof(pt,ROW[pt]); if(TY[pt/8]==TY[pt%8]) MT[NMT++]=pt; }
  printf("zeta %lld matched %d\n",z,NMT);
  RK[0]=0; dfs(0,0);
  fprintf(stderr,"curves %lld families %lld nets %lld kept %lld\n",cnt_curve,cnt_fam,cnt_net,cnt_keep);
  printf("SUMMARY curves %lld families %lld nets %lld kept %lld\n",cnt_curve,cnt_fam,cnt_net,cnt_keep);
  return 0;}
