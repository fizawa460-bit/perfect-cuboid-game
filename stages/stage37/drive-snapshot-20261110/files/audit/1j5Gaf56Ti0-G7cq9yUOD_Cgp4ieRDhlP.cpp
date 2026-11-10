#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <tuple>
#include <vector>
using namespace std; using ll=long long; using i128=__int128_t;
using State=tuple<ll,ll,ll,ll>;
ll rt(ll n){ll r=sqrtl(n);while((r+1)*(r+1)<=n)++r;while(r*r>n)--r;return r;}
vector<State> finish(vector<vector<ll>>& f,ll B){
 vector<State> out;
 for(ll y=1;y<=B;++y){auto &v=f[y];sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());
  for(size_t i=0;i<v.size();++i)for(size_t j=i;j<v.size();++j){ll c=v[i],x=v[j],n=y*y+c*c+x*x;if(n>B*B||gcd(y,gcd(c,x))!=1)continue;ll r=rt(n);if(r*r==n)out.emplace_back(y,c,x,r);}
 }sort(out.begin(),out.end());return out;
}
int main(int argc,char**argv){
 ll B=argc>1?stoll(argv[1]):100000;assert(B<=1000000);
 vector<int> spf(B+1),primes;for(int n=2;n<=B;++n){if(!spf[n]){spf[n]=n;primes.push_back(n);}for(int p:primes){if(p>spf[n]||1LL*n*p>B)break;spf[n*p]=p;}}
 vector<vector<ll>> f(B+1);
 for(ll m=2;m*m+1<=B;++m)for(ll n=1;n<m&&m*m+n*n<=B;++n){if((m-n)%2==0||gcd(m,n)!=1)continue;ll a=m*m-n*n,b=2*m*n,h=m*m+n*n;for(ll k=1;k*h<=B;++k){f[k*a].push_back(k*b);f[k*b].push_back(k*a);}}
 auto e=finish(f,B); f.clear();f.resize(B+1);
 for(ll s=2;s<=B;++s){vector<ll> ds{1};ll rem=s;while(rem>1){ll p=spf[rem];int a=0;while(rem%p==0){rem/=p;++a;}auto old=ds;ll pw=1;for(int j=1;j<=2*a;++j){if(pw>(s-1)/p)break;pw*=p;for(ll d:old)if(d<=(s-1)/pw)ds.push_back(d*pw);}}
  for(ll d:ds)if(d<s){ll q=s*s/d;if((q-d)%2)continue;ll h=(q+d)/2,c=(q-d)/2;if(c>0&&h<=B)f[s].push_back(c);}
 }
 auto d=finish(f,B);assert(d==e);
 ofstream out("M3-T11-160-physical-host.tsv");out<<"Y\tC\tX\tR\tprimitive_C\tprimitive_X\tsquarefree_missing_norm\ta\tb\tp\tq\tepsilon\tZ\n";
 map<ll,ll> classes;ll squares=0;
 for(auto[y,c,x,r]:e){ll g=gcd(r,c),D=r/g,C=c/g,L=rt(x*x+y*y);assert(L*L==x*x+y*y&&L%g==0);L/=g;
  ll abg=gcd(D+L,C),a=(D+L)/abg,b=C/abg,A=a*a+b*b,ep=2*D/A;assert(ep*A==2*D&&(ep==1||ep==2)&&ep*a*b==C);
  ll Q=rt(c*c+y*y);assert(Q*Q==c*c+y*y);ll pqg=gcd(r+x,Q),p=(r+x)/pqg,q=Q/pqg,S=p*p+q*q;
  assert(p>q&&q>0&&S<=2*r&&y*S%(g*ep)==0);ll Z=y*S/(g*ep);
  i128 F=(i128)(b*p-a*q)*(a*q+b*p)*(b*q-a*p)*(b*q+a*p);assert(F==(i128)Z*Z&&Z>0);
  ll D0=p*p-q*q;i128 H=(i128)A*A*D0*D0+(i128)4*a*a*b*b*S*S;
  assert(H+(i128)4*F==(i128)A*A*S*S);
  assert(H*g*g*ep*ep==(i128)4*S*S*(c*c+x*x));
  ll cg=gcd(c,x),c0=c/cg,x0=x/cg,nn=c0*c0+x0*x0,rem=nn,k=1;
  for(ll pp:primes){if(pp*pp>rem)break;int v=0;while(rem%pp==0){rem/=pp;++v;}if(v%2)k*=pp;}if(rem>1)k*=rem;
  classes[k]++;if(k==1)squares++;
  out<<y<<'\t'<<c<<'\t'<<x<<'\t'<<r<<'\t'<<c0<<'\t'<<x0<<'\t'<<k<<'\t'<<a<<'\t'<<b<<'\t'<<p<<'\t'<<q<<'\t'<<ep<<'\t'<<Z<<'\n';
 }
 ll energy=0,mx=0;for(auto[k,n]:classes){energy+=n*n;mx=max(mx,n);}
 cerr<<"PASS B="<<B<<" physical_preselector_states="<<e.size()<<" classes="<<classes.size()<<" energy="<<energy<<" max_class="<<mx<<" class1="<<squares<<" dual_enumeration_and_chart=PASS\n";
}
