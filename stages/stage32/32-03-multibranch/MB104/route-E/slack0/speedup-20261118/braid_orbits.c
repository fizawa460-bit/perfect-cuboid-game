/* Braid-orbit census of slack-0 Nielsen classes.
   Tuples (g1..g6) of involutions in S_n, g_y has t(y) transpositions, g1*...*g6 = 1, transitive.
   Up to simultaneous conjugation.  Orbits of the full braid group B6 (Hurwitz moves) and, inside each
   profile, of the pure braid group P6 (generators A_ij).
   usage: braid_orbits n t1,t2,t3,t4,t5,t6 nseeds [seed]
   Seeds are random tuples of the given profile; every orbit met is explored completely. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXN 9
typedef struct { uint8_t g[6][MAXN]; } Tup;
static int n;
static uint64_t rs=88172645463325252ULL;
static uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static void compose(const uint8_t*a,const uint8_t*b,uint8_t*c){ for(int x=0;x<n;x++) c[x]=a[b[x]]; } /* c=a*b */
static void inverse(const uint8_t*a,uint8_t*c){ for(int x=0;x<n;x++) c[a[x]]=x; }
/* canonical form: min over start points of BFS relabelling; returns |Aut| */
static int canon(const Tup*t,Tup*out){
  int naut=0; Tup best; int have=0;
  for(int s=0;s<n;s++){
    int lab[MAXN],ord[MAXN],h=0,k=1; for(int x=0;x<n;x++) lab[x]=-1; lab[s]=0; ord[0]=s;
    while(h<k){ int x=ord[h++]; for(int y=0;y<6;y++){ int z=t->g[y][x]; if(lab[z]<0){ lab[z]=k; ord[k++]=z; } } }
    if(k<n) return -1; /* not transitive */
    Tup c; for(int y=0;y<6;y++) for(int x=0;x<n;x++) c.g[y][lab[x]]=lab[t->g[y][x]];
    for(int y=0;y<6;y++) for(int x=n;x<MAXN;x++) c.g[y][x]=0;
    int cmp= have? memcmp(&c,&best,sizeof(Tup)) : -1;
    if(cmp<0){ best=c; have=1; naut=1; } else if(cmp==0) naut++;
  }
  *out=best; return naut;
}
/* hash set of canonical tuples */
typedef struct { Tup t; int32_t orb, porb; int8_t used, aut; } Ent;
static Ent*H; static size_t HS;
static uint64_t hsh(const Tup*t){ uint64_t h=1469598103934665603ULL; const uint8_t*p=(const uint8_t*)t; for(size_t i=0;i<sizeof(Tup);i++){ h^=p[i]; h*=1099511628211ULL; } return h; }
static Ent* find(const Tup*t,int ins){ size_t i=hsh(t)&(HS-1); while(H[i].used){ if(!memcmp(&H[i].t,t,sizeof(Tup))) return &H[i]; i=(i+1)&(HS-1);} if(!ins) return NULL; H[i].used=1; H[i].t=*t; H[i].orb=-1; H[i].porb=-1; return &H[i]; }
static void hmove(Tup*t,int i,int inv){ /* sigma_i (0-based positions i,i+1) */
  uint8_t a[MAXN],b[MAXN],tmp[MAXN],c[MAXN];
  memcpy(a,t->g[i],n); memcpy(b,t->g[i+1],n);
  if(!inv){ compose(a,b,tmp); compose(tmp,a,c); /* a b a^-1, a involution */ memcpy(t->g[i],c,n); memcpy(t->g[i+1],a,n); }
  else { compose(b,a,tmp); compose(tmp,b,c); memcpy(t->g[i],b,n); memcpy(t->g[i+1],c,n); }
}
static void Aij(Tup*t,int i,int j){ /* A_ij = s_{j-1}..s_{i+1} s_i^2 s_{i+1}^-1 .. s_{j-1}^-1, applied right to left */
  for(int k=i+1;k<j;k++) hmove(t,k,1);
  hmove(t,i,0); hmove(t,i,0);
  for(int k=j-1;k>i;k--) hmove(t,k,0);
}
static int ntr(const uint8_t*g){ int c=0; for(int x=0;x<n;x++) if(g[x]!=x) c++; return c/2; }
static void rand_inv(uint8_t*g,int t){ int p[MAXN]; for(int x=0;x<n;x++){p[x]=x;g[x]=x;} for(int x=n-1;x>0;x--){int r=rnd()%(x+1);int s=p[x];p[x]=p[r];p[r]=s;} for(int k=0;k<t;k++){ g[p[2*k]]=p[2*k+1]; g[p[2*k+1]]=p[2*k]; } }
static long grouporder(const Tup*t){ /* closure, n<=8 */
  size_t cap=1<<17; uint8_t (*el)[MAXN]=malloc(cap*MAXN); size_t m=0;
  /* simple: BFS over elements, membership by encoding to int */
  int fact=1; for(int k=2;k<=n;k++) fact*=k;
  char*seen=calloc(40320*9+1,1);
  /* rank permutation (Lehmer) */
  #define RANK(p,r) { r=0; for(int u=0;u<n;u++){ int cq=0; for(int v=u+1;v<n;v++) if(p[v]<p[u]) cq++; r=r*(n-u)+cq; } }
  uint8_t id[MAXN]; for(int x=0;x<n;x++) id[x]=x; memcpy(el[m++],id,n); long r; RANK(id,r); seen[r]=1;
  for(size_t h=0;h<m;h++) for(int y=0;y<6;y++){ uint8_t c[MAXN]; compose(t->g[y],el[h],c); RANK(c,r); if(!seen[r]){ seen[r]=1; if(m==cap){cap*=2; el=realloc(el,cap*MAXN);} memcpy(el[m++],c,n);} }
  free(el); free(seen); (void)fact; return (long)m;
}
int main(int argc,char**argv){
  n=atoi(argv[1]); int prof[6]; sscanf(argv[2],"%d,%d,%d,%d,%d,%d",prof,prof+1,prof+2,prof+3,prof+4,prof+5);
  long nseeds=atol(argv[3]); if(argc>4) rs^=strtoull(argv[4],0,10)*0x9E3779B97F4A7C15ULL;
  HS=1<<24; H=calloc(HS,sizeof(Ent));
  Ent**queue=malloc(sizeof(Ent*)*(HS/2)); 
  int norb=0; double orbw[256]; long orbsz[256]; long orbgrp[256]; double profw[256]; int npor[256]; long hits[256];
  long tries=0,acc=0;
  for(long s=0;s<nseeds;s++){
    Tup t; memset(&t,0,sizeof t); uint8_t P[MAXN],tmp[MAXN];
    for(int x=0;x<n;x++) P[x]=x;
    for(int y=0;y<5;y++){ rand_inv(t.g[y],prof[y]); compose(P,t.g[y],tmp); memcpy(P,tmp,n); }
    inverse(P,t.g[5]); tries++;
    /* g6 must be involution of type prof[5] */
    compose(t.g[5],t.g[5],tmp); int ok=1; for(int x=0;x<n;x++) if(tmp[x]!=x) ok=0;
    if(!ok||ntr(t.g[5])!=prof[5]){ s--; if(tries>nseeds*100000L) break; continue; }
    Tup c; int au=canon(&t,&c); if(au<0){ s--; continue; }
    acc++;
    Ent*e=find(&c,1);
    if(e->orb>=0){ hits[e->orb]++; continue; }
    /* explore full B6 orbit */
    int o=norb++; orbw[o]=0; orbsz[o]=0; profw[o]=0; npor[o]=0; hits[o]=1; orbgrp[o]=grouporder(&c);
    size_t qh=0,qt=0; e->orb=o; e->aut=au; queue[qt++]=e;
    while(qh<qt){ Ent*f=queue[qh++]; orbsz[o]++; orbw[o]+=1.0/f->aut;
      for(int i=0;i<5;i++) for(int inv=0;inv<2;inv++){ Tup u=f->t; hmove(&u,i,inv); Tup cu; int a2=canon(&u,&cu); Ent*g=find(&cu,1); if(g->orb<0){ g->orb=o; g->aut=a2; queue[qt++]=g; } } }
    /* pure-braid components among tuples of the seed profile */
    int prof_ok;
    for(size_t k=0;k<qt;k++){ Ent*f=queue[k]; prof_ok=1; for(int y=0;y<6;y++) if(ntr(f->t.g[y])!=prof[y]) prof_ok=0;
      if(!prof_ok||f->porb>=0) continue;
      int po=npor[o]++; double w=0; long sz=0;
      size_t ph=0,pt=0; Ent**pq=malloc(sizeof(Ent*)*qt); f->porb=po; pq[pt++]=f;
      while(ph<pt){ Ent*g=pq[ph++]; sz++; w+=1.0/g->aut;
        for(int i=0;i<6;i++) for(int j=i+1;j<6;j++){ Tup u=g->t; Aij(&u,i,j); Tup cu; canon(&u,&cu); Ent*h=find(&cu,0); if(h->porb<0){ h->porb=po; pq[pt++]=h; } } }
      printf("  orbit %d pure-braid component %d: tuples %ld weighted %.4f group %ld\n",o,po,sz,w,grouporder(&f->t));
      profw[o]+=w; free(pq);
    }
    printf("orbit %d: full-B6 tuples %ld weighted %.4f (all orderings), this profile weighted %.4f in %d pure components, monodromy group order %ld\n",o,orbsz[o],orbw[o],profw[o],npor[o],orbgrp[o]);
    fflush(stdout);
  }
  double tot=0; for(int o=0;o<norb;o++) tot+=profw[o];
  printf("seeds accepted %ld (tries %ld). orbits %d. profile weighted total %.4f\n",acc,tries,norb,tot);
  for(int o=0;o<norb;o++) printf("  orbit %d seed hits %ld\n",o,hits[o]);
  return 0;
}
