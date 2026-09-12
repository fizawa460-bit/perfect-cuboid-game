#include <bits/stdc++.h>
using namespace std;

struct G { long long r=0,i=0; };
static inline G add(G a,G b){return {a.r+b.r,a.i+b.i};}
static inline G mul(G a,G b){return {a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r};}
static inline G neg(G a){return {-a.r,-a.i};}
static inline bool zero(G a){return a.r==0&&a.i==0;}

struct NodeG { G z[7]; };
vector<NodeG> build_nodes(){
  vector<NodeG> v;
  auto push=[&](array<G,7> z){NodeG n{};for(int j=0;j<7;j++)n.z[j]=z[j];v.push_back(n);};
  // Type A: c=1; one a_j=+-1, corresponding b_j=0; other two b's=+-1.
  for(int j=0;j<3;j++) for(int sa:{1,-1}) for(int s1:{1,-1}) for(int s2:{1,-1}){
    array<G,7> z{}; z[j]={sa,0}; vector<int> o; for(int t=0;t<3;t++)if(t!=j)o.push_back(t);
    z[3+o[0]]={s1,0}; z[3+o[1]]={s2,0}; z[6]={1,0}; push(z);
  }
  // Type B: c=0; zero pair j; scale first remaining a=1 and second=+-i.
  for(int j=0;j<3;j++){
    vector<int> o; for(int t=0;t<3;t++)if(t!=j)o.push_back(t); int a=o[0],b=o[1];
    for(int sr:{1,-1}) for(int ep:{1,-1}) for(int eq:{1,-1}){
      array<G,7> z{}; z[a]={1,0}; z[b]={0,sr}; z[3+a]={0,ep}; z[3+b]={-eq*sr,0}; push(z);
    }
  }
  return v;
}

struct Key { array<int,7> a{}; bool operator==(Key const&o)const{return a==o.a;} };
struct KH { size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;for(int x:k.a){h^=(uint64_t)x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2);h*=1099511628211ULL;}return h;} };
long long modpow(long long a,long long e,int p){long long r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
int rootm1(int p){for(int x=2;x<p;x++)if(1LL*x*x%p==p-1)return x;return -1;}

bool normal6_mod(const array<array<int,7>,48>&N,const array<int,6>&idx,int p,Key&out){
  int M[6][7]; for(int r=0;r<6;r++)for(int c=0;c<7;c++)M[r][c]=N[idx[r]][c];
  int pc[6],rank=0;
  for(int c=0;c<7&&rank<6;c++){
    int piv=-1;for(int r=rank;r<6;r++)if(M[r][c]){piv=r;break;}if(piv<0)continue;
    if(piv!=rank)for(int j=0;j<7;j++)swap(M[piv][j],M[rank][j]);
    long long inv=modpow(M[rank][c],p-2,p);for(int j=0;j<7;j++)M[rank][j]=(int)(M[rank][j]*inv%p);
    for(int r=0;r<6;r++)if(r!=rank&&M[r][c]){int f=M[r][c];for(int j=0;j<7;j++){int x=(M[r][j]-(long long)f*M[rank][j])%p;if(x<0)x+=p;M[r][j]=x;}}
    pc[rank++]=c;
  }
  if(rank<6)return false;
  bool ispc[7]={};for(int r=0;r<6;r++)ispc[pc[r]]=1;int f=-1;for(int c=0;c<7;c++)if(!ispc[c]){f=c;break;}
  array<int,7>x{};x[f]=1;for(int r=0;r<6;r++){int z=M[r][f];x[pc[r]]=z?p-z:0;}
  int first=-1;for(int c=0;c<7;c++)if(x[c]){first=c;break;}long long inv=modpow(x[first],p-2,p);for(int c=0;c<7;c++)x[c]=(int)(x[c]*inv%p);
  out.a=x;return true;
}

G det6(const array<array<G,6>,6>&M){
  array<int,6> p={0,1,2,3,4,5}; G s{};
  do{
    int inv=0;for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)inv+=p[a]>p[b];
    G q{1,0};for(int r=0;r<6;r++)q=mul(q,M[r][p[r]]); if(inv&1)q=neg(q);s=add(s,q);
  }while(next_permutation(p.begin(),p.end()));
  return s;
}
array<G,7> exact_normal(const vector<NodeG>&Gv,const array<int,6>&idx){
  array<G,7> n{};
  for(int omit=0;omit<7;omit++){
    array<array<G,6>,6>M{};for(int r=0;r<6;r++){int cc=0;for(int c=0;c<7;c++)if(c!=omit)M[r][cc++]=Gv[idx[r]].z[c];}
    G d=det6(M);if(omit&1)d=neg(d);n[omit]=d;
  }
  return n;
}
uint64_t exact_mask(const vector<NodeG>&Gv,const array<G,7>&n){
  uint64_t m=0;for(int r=0;r<48;r++){G s{};for(int c=0;c<7;c++)s=add(s,mul(n[c],Gv[r].z[c]));if(zero(s))m|=1ULL<<r;}return m;
}

struct Run { map<int,long long> dist; vector<uint64_t> exact_masks; size_t distinct=0; int root=0; };
Run enumerate_prime(const vector<NodeG>&Gv,int p){
  int ir=rootm1(p); if(ir<0)throw runtime_error("no sqrt(-1)");
  array<array<int,7>,48>N{};for(int r=0;r<48;r++)for(int c=0;c<7;c++){long long x=(Gv[r].z[c].r+Gv[r].z[c].i*(long long)ir)%p;if(x<0)x+=p;N[r][c]=(int)x;}
  unordered_map<Key,array<int,6>,KH> mp;mp.reserve(800000);
  array<int,6> id{};
  for(id[0]=0;id[0]<43;id[0]++)for(id[1]=id[0]+1;id[1]<44;id[1]++)for(id[2]=id[1]+1;id[2]<45;id[2]++)for(id[3]=id[2]+1;id[3]<46;id[3]++)for(id[4]=id[3]+1;id[4]<47;id[4]++)for(id[5]=id[4]+1;id[5]<48;id[5]++){
    Key k;if(normal6_mod(N,id,p,k))mp.emplace(k,id);
  }
  Run out;out.distinct=mp.size();out.root=ir;
  for(auto const&kv:mp){
    int cnt=0;uint64_t mm=0;for(int r=0;r<48;r++){long long s=0;for(int c=0;c<7;c++)s+=(long long)kv.first.a[c]*N[r][c];if(s%p==0){cnt++;mm|=1ULL<<r;}}
    out.dist[cnt]++;
    if(cnt>=14){
      auto en=exact_normal(Gv,kv.second);bool nz=false;for(auto z:en)nz|=!zero(z);if(!nz)throw runtime_error("exact rank failure");
      uint64_t em=exact_mask(Gv,en);if(em!=mm)throw runtime_error("modular high-incidence support not exact");out.exact_masks.push_back(em);
    }
  }
  sort(out.exact_masks.begin(),out.exact_masks.end());
  if(adjacent_find(out.exact_masks.begin(),out.exact_masks.end())!=out.exact_masks.end())throw runtime_error("duplicate exact support");
  return out;
}

uint64_t fnv_masks(const vector<uint64_t>&v){uint64_t h=1469598103934665603ULL;for(uint64_t x:v)for(int j=0;j<8;j++){h^=(x>>(8*j))&255;h*=1099511628211ULL;}return h;}

int main(){
  try{
    auto Gv=build_nodes();if(Gv.size()!=48)throw runtime_error("node count");
    const int p1=1097,p2=1153; if(1LL*p1*p2<=46656)throw runtime_error("Hadamard product bound not separated");
    Run a=enumerate_prime(Gv,p1),b=enumerate_prime(Gv,p2);
    map<int,long long> expected={{6,372608},{7,114624},{8,61440},{9,32256},{10,8736},{12,1648},{13,768},{14,1248},{15,256},{16,27},{19,48},{20,48},{24,28}};
    if(a.dist!=expected||b.dist!=expected)throw runtime_error("distribution mismatch");
    if(a.distinct!=593735||b.distinct!=593735)throw runtime_error("distinct count mismatch");
    if(a.exact_masks.size()!=1655||b.exact_masks.size()!=1655)throw runtime_error("high count mismatch");
    if(a.exact_masks!=b.exact_masks)throw runtime_error("two-prime exact support sets differ");
    map<int,int> hd;for(auto m:a.exact_masks)hd[__builtin_popcountll(m)]++;
    map<int,int> hexp={{14,1248},{15,256},{16,27},{19,48},{20,48},{24,28}};if(hd!=hexp)throw runtime_error("exact high distribution mismatch");
    uint64_t h=fnv_masks(a.exact_masks);if(h!=0xba8379b50029db53ULL)throw runtime_error("support digest mismatch");
    cout<<"PASS STAGE32_MB104_GENUS1_SPAN5_HYPERPLANE_FINITE_REDUCTION_V1\n";
    cout<<"nodes=48 p1="<<p1<<" i1="<<a.root<<" p2="<<p2<<" i2="<<b.root<<"\n";
    cout<<"distinct_mod_hyperplanes_per_prime=593735 exact_high_incidence_hyperplanes=1655\n";
    cout<<"high_distribution=14:1248,15:256,16:27,19:48,20:48,24:28\n";
    cout<<"exact_support_fnv64=ba8379b50029db53 hadamard_norm_bound=46656 prime_product="<<1LL*p1*p2<<"\n";
    cout<<"scope=genus1_span5_N_ge_14_supports_finitely_reduced_not_closed\n";
    return 0;
  }catch(exception const&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
