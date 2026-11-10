#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std;
using ll=long long;
using Brick=tuple<ll,ll,ll,ll>;
ll root(ll n){ll r=sqrtl(n);while((r+1)*(r+1)<=n)++r;while(r*r>n)--r;return r;}
vector<Brick> finish(const vector<vector<ll>>& faces,ll B){
 vector<Brick> out;
 for(ll x=1;x<=B;x+=2){auto ys=faces[x];sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());
  for(size_t i=0;i<ys.size();++i)for(size_t j=i+1;j<ys.size();++j){ll y=ys[i],z=ys[j],t=x*x+y*y+z*z;
   if(t>B*B||gcd(x,gcd(y,z))!=1)continue;
   ll d=root(y*y+z*z);if(d*d==y*y+z*z)out.emplace_back(x,y,z,t);
  }
 }sort(out.begin(),out.end());return out;
}
int main(int argc,char**argv){
 ll B=argc>1?stoll(argv[1]):1000000;assert(B<=2000000);
 vector<int> spf(B+1);vector<int> primes;
 for(int n=2;n<=B;++n){if(!spf[n]){spf[n]=n;primes.push_back(n);}for(int p:primes){if(p>spf[n]||1LL*n*p>B)break;spf[n*p]=p;}}
 vector<vector<ll>> faces(B+1);
 for(ll x=1;x<=B;x+=2){vector<ll> divs{1};ll n=x;
  while(n>1){int p=spf[n],e=0;while(n%p==0){n/=p;++e;}auto old=divs;ll pow=1;for(int j=1;j<=2*e;++j){if(pow>(x-1)/p)break;pow*=p;for(ll a:old)if(a< x && a<=(x-1)/pow)divs.push_back(a*pow);}}
  for(ll a:divs)if(a<x){ll y=(x*x/a-a)/2;if(y>0&&y<=B&&x*x+y*y<=B*B)faces[x].push_back(y);}
 }
 auto bydiv=finish(faces,B);faces.clear();faces.resize(B+1);
 for(ll m=2;m*m+1<=B;++m)for(ll n=1;n<m&&m*m+n*n<=B;++n){if((m-n)%2==0||gcd(m,n)!=1)continue;ll x=m*m-n*n,y=2*m*n,h=m*m+n*n;for(ll k=1;k*h<=B;k+=2)faces[k*x].push_back(k*y);}
 auto byeuclid=finish(faces,B);assert(bydiv==byeuclid);
 ofstream f("M3-T11-158-census.tsv");f<<"X\tY\tZ\tT\tDxy\tDxz\tDyz\tsquarefree_T\n";
 for(auto[x,y,z,t]:bydiv){assert(x%2&&y%4==0&&z%4==0&&t%8==1);ll sf=1,n=t;
  for(ll p:primes){if(p*p>n)break;int e=0;while(n%p==0){n/=p;++e;}if(e%2)sf*=p;}if(n>1)sf*=n;
  f<<x<<'\t'<<y<<'\t'<<z<<'\t'<<t<<'\t'<<root(x*x+y*y)<<'\t'<<root(x*x+z*z)<<'\t'<<root(y*y+z*z)<<'\t'<<sf<<'\n';
 }
 cerr<<"B="<<B<<" M3="<<bydiv.size()<<" independent_divisor_Euclid_match=PASS\n";
}
