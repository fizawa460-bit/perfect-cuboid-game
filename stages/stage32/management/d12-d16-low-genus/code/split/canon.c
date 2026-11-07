/* 32R-70: orbit canonical form (lex-max of pe[g]) and 128-bit hash, one line per input x */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  FILE*t=fopen(argv[1],"r"); int NP,NX,NG; if(fscanf(t,"%d %d %d",&NP,&NX,&NG)!=3)return 1;
  long*P=malloc(sizeof(long)*NP*NX); int*G=malloc(sizeof(int)*NG*NP);
  for(int i=0;i<NP*NX;i++) if(fscanf(t,"%ld",&P[i])!=1)return 1;
  for(int i=0;i<NG*NP;i++) if(fscanf(t,"%d",&G[i])!=1)return 1;
  long x[256],pe[256];
  while(1){
    for(int j=0;j<NX;j++) if(scanf("%ld",&x[j])!=1) return 0;
    for(int k=0;k<NP;k++){long s=0;for(int j=0;j<NX;j++)s+=P[k*NX+j]*x[j];pe[k]=s;}
    int best=0;
    for(int g=1;g<NG;g++){const int*a=G+g*NP,*b=G+best*NP;
      for(int k=0;k<NP;k++){long u=pe[a[k]],v=pe[b[k]]; if(u!=v){ if(u>v)best=g; break;}}}
    uint64_t h1=1469598103934665603ULL,h2=0x9E3779B97F4A7C15ULL; const int*b=G+best*NP;
    for(int k=0;k<NP;k++){uint64_t v=(uint64_t)pe[b[k]]; h1=(h1^v)*1099511628211ULL; h2=(h2+v*0xBF58476D1CE4E5B9ULL); h2^=h2>>31; h2*=0x94D049BB133111EBULL;}
    printf("%016llx%016llx\n",(unsigned long long)h1,(unsigned long long)h2);
  }
}
