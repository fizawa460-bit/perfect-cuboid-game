#include <bits/stdc++.h>
using namespace std;using ll=long long;
bool square(ll n){ll r=sqrtl((long double)n);while(r*r<n)++r;while(r*r>n)--r;return r*r==n;}
int main(int argc,char**argv){int B=argc>1?atoi(argv[1]):1000000;vector<vector<int>>adj(B+1);ll links=0,trials=0;for(int m=2;(ll)m*m+1<=B;m++)for(int n=1;n<m;n++){ll h=(ll)m*m+(ll)n*n;if(h>B)break;if(((m-n)&1)==0||gcd(m,n)!=1)continue;int x=m*m-n*n,y=2*m*n;for(int k=1;k*h<=B;k++){adj[k*x].push_back(k*y);adj[k*y].push_back(k*x);links+=2;}}
set<array<int,3>>out;for(int a=1;a<=B;a++){auto &v=adj[a];sort(v.begin(),v.end());if(unique(v.begin(),v.end())!=v.end())return 2;for(size_t j=0;j<v.size();j++)for(size_t k=j;k<v.size();k++){int b=v[j],c=v[k];ll t=(ll)a*a+(ll)b*b+(ll)c*c;if(t>(ll)B*B)break;trials++;if(gcd(a,gcd(b,c))!=1||!square(t))continue;array<int,3>q{a,b,c};sort(q.begin(),q.end());out.insert(q);}}
ofstream f("M3-T11-207-euclid-keys.tsv");for(auto q:out)f<<q[0]<<'\t'<<q[1]<<'\t'<<q[2]<<'\n';cerr<<"B="<<B<<" distinct_raw="<<out.size()<<" directed_circle_pairs="<<links<<" sphere_trials="<<trials<<"\n";
}
