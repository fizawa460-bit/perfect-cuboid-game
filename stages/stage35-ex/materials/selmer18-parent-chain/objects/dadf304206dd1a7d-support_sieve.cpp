#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
const vector<long long> H={1,44,1270,28812,477465,5618656,47373712,287482208,1209582452,2824772240,-3771459480,-74385103984,-414222799612,-1518034787424,-4101637562640,-8488886675168,-13953062018450,-19740131328056,-27586913989820,-40411519970680,-54532738391954,-57355978166240,-41845692697360,-18563645381472,-2246866224380,3943381946384,3740390482536,1412091528720,226745215348,20739562080,13322701712,1409546976,60743449,-7165076,-51210,-1716,1};
int mod(long long a,int p){int z=a%p;return z<0?z+p:z;}
int pw(int a,int n,int p){int z=1;for(;n;n>>=1,a=a*a%p)if(n&1)z=z*a%p;return z;}
int normrem(const vector<int>& c,int p){
 int d=c.size();vector<int> r(d);
 for(auto it=H.rbegin();it!=H.rend();++it){int top=r.back();for(int i=d-1;i>0;i--)r[i]=mod(r[i-1]-top*c[i],p);r[0]=mod(*it-top*c[0],p);}
 vector<vector<int>> M(d,vector<int>(d));
 for(int j=0;j<d;j++){for(int i=0;i<d;i++)M[i][j]=r[i];int top=r.back();for(int i=d-1;i>0;i--)r[i]=mod(r[i-1]-top*c[i],p);r[0]=mod(-top*c[0],p);}
 int det=1;
 for(int j=0;j<d;j++){int k=j;while(k<d&&!M[k][j])k++;if(k==d)return 0;if(k!=j){swap(M[k],M[j]);det=p-det;}int v=M[j][j];det=det*v%p;int iv=pw(v,p-2,p);for(int i=j+1;i<d;i++){int a=M[i][j]*iv%p;for(int t=j+1;t<d;t++)M[i][t]=mod(M[i][t]-a*M[j][t],p);}}
 return det;
}
struct Table{int p;vector<unsigned char> pass;vector<int> inverse;};
int main(int argc,char**argv){
 if(argc!=6)return 2;int d=atoi(argv[1]),amax=atoi(argv[2]),bound=atoi(argv[3]),pmax=atoi(argv[4]);ofstream out(argv[5]);if(d<2||d>3)return 2;
 vector<Table> tables;
 for(int p:{3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}){
  if(p>pmax)break;size_t size=1;for(int i=0;i<d;i++)size*=p;Table t{p,vector<unsigned char>(size),vector<int>(p)};for(int a=1;a<p;a++)t.inverse[a]=pw(a,p-2,p);
  vector<int> c(d);for(size_t i=0;i<size;i++){size_t q=i;for(int j=0;j<d;j++){c[j]=q%p;q/=p;}int n=normrem(c,p);t.pass[i]=n==0||pw(n,(p-1)/2,p)==1;}tables.push_back(move(t));
 }
 cerr<<"tables_ready degree="<<d<<" primes="<<tables.size()<<endl;
 uint64_t tested=0,survived=0;vector<int> cs(d);vector<uint64_t> rejected(tables.size());
 for(int a=1;a<=amax;a++){
  vector<int> ai;for(auto&t:tables)ai.push_back(t.inverse[a%t.p]);
  for(int b=-bound;b<=bound;b++)for(int c=-bound;c<=bound;c++)for(int e=(d==3?-bound:0);e<=(d==3?bound:0);e++){
   cs[0]=c;cs[1]=b;if(d==3)cs[2]=e;if(c==0)continue;int g=a;for(int v:cs)g=gcd(g,abs(v));if(g!=1)continue;
   long long vm=0,v3=0;long long p3=1;for(int j=0;j<d;j++){vm+=cs[j]*(j%2?-1:1);v3+=cs[j]*(j%2?-1:1)*(long long)pow(3,d-j);}vm+=(d%2?-a:a);v3+=a*(d%2?-1:1);if(vm==0||v3==0)continue;
   if(d==2){long long disc=1LL*b*b-4LL*a*c;if(disc>=0){long long s=sqrt(disc);if(s*s==disc||(s+1)*(s+1)==disc)continue;}}
   tested++;bool ok=true;
   for(size_t k=0;k<tables.size();k++){auto&t=tables[k];if(!ai[k])continue;size_t index=0;for(int j=d-1;j>=0;j--)index=index*t.p+mod(1LL*cs[j]*ai[k],t.p);if(!t.pass[index]){ok=false;rejected[k]++;break;}}
   if(ok){out<<a;for(int v:cs)out<<' '<<v;out<<'\n';survived++;}
  }
  cerr<<"a="<<a<<" tested="<<tested<<" survivors="<<survived<<endl;
 }
 cerr<<"rejected_by_prime=";for(auto n:rejected)cerr<<n<<',';cerr<<endl;
}
