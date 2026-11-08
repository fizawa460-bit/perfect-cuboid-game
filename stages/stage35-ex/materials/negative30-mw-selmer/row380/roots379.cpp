#include <bits/stdc++.h>
#include <gmpxx.h>
using namespace std;
using ll=long long;
int mod(ll x,int p){int z=(int)(x%p);return z<0?z+p:z;}
int modpow(int b,int e,int p){ll r=1,x=b;while(e){if(e&1)r=r*x%p;x=x*x%p;e>>=1;}return (int)r;}
using Poly=vector<int>;
void trim(Poly& a){while(!a.empty() && a.back()==0) a.pop_back();}
Poly mulmod(const Poly& a,const Poly& b,const Poly& f,int p){
 if(a.empty()||b.empty())return {};
 const int n=105;
 ll v[209]={};
 for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)b.size();j++)v[i+j] += (ll)a[i]*b[j];
 for(int k=min(208,(int)a.size()+(int)b.size()-2);k>=n;k--){
   int t=mod(v[k],p); if(!t)continue;
   for(int j=0;j<n;j++)v[k-n+j]-=(ll)t*f[j];
 }
 Poly z(n);
 for(int i=0;i<n;i++) z[i]=mod(v[i],p);
 trim(z);return z;
}
int gcd_degree(Poly a,Poly b,int p){
 trim(a);trim(b);
 while(!b.empty()){
   int inv=modpow(b.back(),p-2,p);
   while(a.size()>=b.size()){
     int t=(int)((ll)a.back()*inv%p),delta=(int)(a.size()-b.size());
     for(int i=0;i<(int)b.size();i++)a[i+delta]=mod((ll)a[i+delta]-(ll)t*b[i],p);
     trim(a);
   }
   a.swap(b);
 }
 return (int)a.size()-1;
}
int degree_one(const vector<mpz_class>& big,int p){
 Poly f(106);for(int i=0;i<106;i++)f[i]=mpz_fdiv_ui(big[i].get_mpz_t(),p);
 if(f[105]!=1)throw runtime_error("nonmonic");
 Poly r={1},b={0,1};
 int e=p;
 while(e){if(e&1)r=mulmod(r,b,f,p);e>>=1;if(e)b=mulmod(b,b,f,p);}
 if(r.size()<2)r.resize(2,0);r[1]=mod((ll)r[1]-1,p);
 trim(r);return gcd_degree(f,r,p);
}
int main(int argc,char** argv){
 int maxn=1982760,lo=5003;
 int maxcount=argc>1?atoi(argv[1]):maxn;
 if(maxcount>maxn)maxcount=maxn;
 ifstream ff("/mnt/data/row379_audit/coeff_asc.txt");
 vector<mpz_class> big(106);string s;for(auto& v:big){ff>>s;v=mpz_class(s);}
 vector<bool> prime(maxcount+1,true);prime[0]=prime[1]=false;
 for(int p=2;(ll)p*p<=maxcount;p++) if(prime[p])for(int j=p*p;j<=maxcount;j+=p)prime[j]=false;
 vector<int> ps;for(int p=lo+1;p<=maxcount;p++)if(prime[p])ps.push_back(p);
 vector<int> r(ps.size());
 int threads=5;
 atomic<int> done=0;
 vector<thread> workers;
 for(int j=0;j<threads;j++)workers.emplace_back([&,j](){for(int i=j;i<(int)ps.size();i+=threads){r[i]=degree_one(big,ps[i]);int n=++done;if(n%20000==0)fprintf(stderr,"%d/%lu done\n",n,ps.size());}});
 for(auto &t:workers)t.join();
 ofstream of("/mnt/data/row379_audit/tail_roots_independent.csv");
 long long c=0;for(int i=0;i<(int)ps.size();i++){of<<ps[i]<<","<<r[i]<<"\n";c+=r[i];}
 cerr<<"ALL PRIMES "<<ps.size()<<" ROOT COUNT "<<c<<"\n";
}
