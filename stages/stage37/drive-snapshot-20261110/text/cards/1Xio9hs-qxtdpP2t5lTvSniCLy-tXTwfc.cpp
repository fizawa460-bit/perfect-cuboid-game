#include <bits/stdc++.h>
using namespace std;using ll=long long;
struct Obj{int a,b,c,R,faces;ll cmax,craw;int hmin,hmid,hmax;};
ll isq(ll x){ll r=sqrtl((long double)x);while((r+1)*(r+1)<=x)++r;while(r*r>x)--r;return r*r==x?r:0;}
int main(int argc,char**argv){int B=argc>1?atoi(argv[1]):1000000;
 vector<int>spf(B+1);for(int p=2;p<=B;p++)if(!spf[p]){spf[p]=p;if((ll)p*p<=B)for(ll j=(ll)p*p;j<=B;j+=p)if(!spf[j])spf[j]=p;}
 map<array<int,3>,Obj>objects;ll trials=0,circles=0;
 for(int a=1;a<=B;a++){
  int n=a;vector<pair<int,int>> fac;while(n>1){int p=spf[n],e=0;while(n%p==0)n/=p,++e;fac.push_back({p,2*e});}
  vector<ll>ds{1};for(auto [p,e]:fac){int sz=ds.size();ll z=1;for(int j=1;j<=e;j++){z*=p;for(int k=0;k<sz;k++)ds.push_back(ds[k]*z);}}
  vector<int>legs;ll aa=(ll)a*a;
  for(ll d:ds)if(d<a){ll q=aa/d;if((d+q)&1)continue;ll b=(q-d)/2,h=(q+d)/2;if(b>0&&h<=B)legs.push_back(b);}
  sort(legs.begin(),legs.end());circles+=legs.size();
  for(int j=0;j<(int)legs.size();j++)for(int k=j;k<(int)legs.size();k++){
   int b=legs[j],c=legs[k];ll T=aa+(ll)b*b+(ll)c*c;if(T>(ll)B*B)break;++trials;
   if(gcd(a,gcd(b,c))!=1)continue;ll R=isq(T);if(!R)continue;
   array<int,3>key{a,b,c};sort(key.begin(),key.end());if(objects.count(key))continue;
   int nf=0;vector<int>hs;ll craw=0;
   for(int i=0;i<3;i++){hs.push_back(gcd((int)R,key[i]));if(isq(T-(ll)key[i]*key[i]))nf++;}
   for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(isq(T-(ll)key[i]*key[i])&&isq(T-(ll)key[j]*key[j]))craw=max(craw,(ll)hs[i]*hs[j]);
   sort(hs.begin(),hs.end());objects[key]={key[0],key[1],key[2],(int)R,nf,(ll)hs[1]*hs[2],craw,hs[0],hs[1],hs[2]};
  }
 }
 ofstream f("M3-T11-221-raw-census.tsv");f<<"a\tb\tc\tR\tintegral_faces\tc_max\tc_raw_max\th_min\th_mid\th_max\n";
 for(auto [k,o]:objects)f<<o.a<<'\t'<<o.b<<'\t'<<o.c<<'\t'<<o.R<<'\t'<<o.faces<<'\t'<<o.cmax<<'\t'<<o.craw<<'\t'<<o.hmin<<'\t'<<o.hmid<<'\t'<<o.hmax<<'\n';
 cerr<<"B="<<B<<" distinct_raw="<<objects.size()<<" circle_pairs="<<circles<<" sphere_trials="<<trials<<"\n";
}
