#include <bits/stdc++.h>
using namespace std;using ll=long long;
ll p;ll md(ll x){x%=p;return x<0?x+p:x;}ll pw(ll x,ll n){ll r=1;for(;n;n>>=1,x=x*x%p)if(n&1)r=r*x%p;return r;}
using Pt=array<ll,2>;using Mat=array<ll,4>;using Pol=vector<ll>;
ll det(Pt a,Pt b){return md(a[0]*b[1]-a[1]*b[0]);}Pt mv(Mat a,Pt b){return {md(a[0]*b[0]+a[1]*b[1]),md(a[2]*b[0]+a[3]*b[1])};}
Mat frame(Pt a,Pt b,Pt c){ll u=det(c,b),v=det(a,c);return {a[0]*u%p,b[0]*v%p,a[1]*u%p,b[1]*v%p};}
Mat adj(Mat a){return{a[3],md(-a[1]),md(-a[2]),a[0]};}Mat mm(Mat a,Mat b){return {md(a[0]*b[0]+a[1]*b[2]),md(a[0]*b[1]+a[1]*b[3]),md(a[2]*b[0]+a[3]*b[2]),md(a[2]*b[1]+a[3]*b[3])};}
Pol mul(Pol a,Pol b){Pol c(a.size()+b.size()-1);for(int i=0;i<a.size();i++)for(int j=0;j<b.size();j++)c[i+j]=md(c[i+j]+a[i]*b[j]);return c;}
Pol comp(Pol a,Mat m){int n=a.size()-1;Pol r(n+1);for(int k=0;k<=n;k++){Pol v={1};for(int j=0;j<k;j++)v=mul(v,{m[1],m[0]});for(int j=k;j<n;j++)v=mul(v,{m[3],m[2]});for(int j=0;j<=n;j++)r[j]=md(r[j]+a[k]*v[j]);}return r;}
struct Cover{int n;Pol P,Q;vector<Pt>S;vector<int>L;};
int main(){int count;cin>>p>>count;vector<Pt>B(6);for(auto &x:B)cin>>x[0]>>x[1];vector<Cover>C(count);for(auto &c:C){cin>>c.n;c.P.resize(c.n+1);c.Q.resize(c.n+1);for(auto &x:c.P)cin>>x;for(auto &x:c.Q)cin>>x;int s=2*c.n+4;c.S.resize(s);c.L.resize(s);for(auto &v:c.S){ll x;cin>>x;v=x==p?Pt{1,0}:Pt{x,1};}for(auto &l:c.L)cin>>l;}
vector<Mat>auts;Mat base=adj(frame(B[0],B[1],B[2]));for(int i=0;i<6;i++)for(int j=0;j<6;j++)for(int k=0;k<6;k++){if(i==j||i==k||j==k)continue;Mat U=mm(frame(B[i],B[j],B[k]),base);bool good=true;for(Pt x:B){bool ok=false;for(Pt y:B)if(det(mv(U,x),y)==0)ok=true;good&=ok;}if(good)auts.push_back(U);}assert(auts.size()==24);
for(auto [a,b]:vector<pair<int,int>>{{2,3},{3,3}}){map<int,ll>hist,hits;ll total=0,uncertified=0;int nA=2*a+4,nB=2*b+4,jmin=max(nA,nB)-4,first=nA-jmin+3;
for(int ia=0;ia<count;ia++){if(C[ia].n!=a)continue;auto &A=C[ia];for(int ib=0;ib<count;ib++){if(C[ib].n!=b)continue;auto &D=C[ib];for(int i=0;i<first;i++)for(int j=i+1;j<first;j++)for(int k=j+1;k<first;k++){Mat Fs=adj(frame(A.S[i],A.S[j],A.S[k]));for(int u=0;u<nB;u++){if(A.L[i]!=D.L[u])continue;for(int v=0;v<nB;v++){if(v==u||A.L[j]!=D.L[v])continue;for(int w=0;w<nB;w++){if(w==u||w==v||A.L[k]!=D.L[w])continue;Mat M=mm(frame(D.S[u],D.S[v],D.S[w]),Fs);assert(md(M[0]*M[3]-M[1]*M[2]));int same=0,diff=0;for(int x=0;x<nA;x++){Pt z=mv(M,A.S[x]);for(int y=0;y<nB;y++)if(det(z,D.S[y])==0){if(A.L[x]==D.L[y])same++;else diff++;}}
int om=nA+nB-2*same-diff;hist[om]++;total++;if(om<=4){hits[om]++;bool certified=false;if(a==b){Pol P=comp(D.P,M),Q=comp(D.Q,M);for(Mat U:auts){Pol R(a+1),S(a+1);for(int l=0;l<=a;l++){R[l]=md(U[0]*A.P[l]+U[1]*A.Q[l]);S[l]=md(U[2]*A.P[l]+U[3]*A.Q[l]);}if(mul(P,S)==mul(Q,R)){certified=true;break;}}}if(!certified)uncertified++;}
}}}}}cerr<<"completed a="<<a<<" b="<<b<<" first="<<ia<<" total="<<total<<"\n";}
cout<<"PAIR "<<a<<" "<<b<<" TOTAL "<<total<<" UNCLASSIFIED "<<uncertified<<"\n";for(auto [o,n]:hist)cout<<"HIST "<<o<<" "<<n<<"\n";for(auto [o,n]:hits)cout<<"HIT "<<o<<" "<<n<<"\n";cout.flush();assert(uncertified==0);
}}
