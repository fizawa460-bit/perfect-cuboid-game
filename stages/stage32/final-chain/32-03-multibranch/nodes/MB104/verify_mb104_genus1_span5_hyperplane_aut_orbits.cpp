#include <bits/stdc++.h>
using namespace std;
struct G{int r=0,i=0;};
G gm(G a,G b){return {a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r};}
bool gz(G a){return a.r==0&&a.i==0;}
struct Node{array<G,7> z;};
vector<Node> nodes(){
 vector<Node> v; auto push=[&](array<G,7> z){v.push_back({z});};
 for(int j=0;j<3;j++)for(int sa:{1,-1})for(int s1:{1,-1})for(int s2:{1,-1}){
  array<G,7> z{}; z[j]={sa,0}; vector<int>o;for(int t=0;t<3;t++)if(t!=j)o.push_back(t); z[3+o[0]]={s1,0};z[3+o[1]]={s2,0};z[6]={1,0};push(z);
 }
 for(int j=0;j<3;j++){vector<int>o;for(int t=0;t<3;t++)if(t!=j)o.push_back(t);int a=o[0],b=o[1];
  for(int sr:{1,-1})for(int ep:{1,-1})for(int eq:{1,-1}){array<G,7>z{};z[a]={1,0};z[b]={0,sr};z[3+a]={0,ep};z[3+b]={-eq*sr,0};push(z);} }
 return v;
}
bool peq(Node const&a,Node const&b){int k=-1;for(int j=0;j<7;j++)if(!gz(a.z[j])){k=j;break;} if(k<0)return false; for(int j=0;j<7;j++){G l=gm(a.z[j],b.z[k]), r=gm(b.z[j],a.z[k]); if(l.r!=r.r||l.i!=r.i)return false;}return true;}
Node apply(Node const&x, array<int,7> const&src,array<G,7>const&cf){Node y{};for(int j=0;j<7;j++)y.z[j]=gm(cf[j],x.z[src[j]]);return y;}
using Perm=array<unsigned char,48>;
vector<Perm> gens(vector<Node> const&V){
 vector<array<int,7>> S;vector<array<G,7>> C;
 auto ones=[](){array<G,7>c{};for(auto &x:c)x={1,0};return c;};
 S.push_back({1,0,2,4,3,5,6});C.push_back(ones());
 S.push_back({2,1,0,5,4,3,6});C.push_back(ones());
 S.push_back({6,1,2,3,5,4,0});{auto c=ones();c[0]={0,1};c[4]={0,1};c[5]={0,-1};c[6]={0,-1};C.push_back(c);}
 for(int q=0;q<6;q++){array<int,7>s={0,1,2,3,4,5,6};auto c=ones();c[q]={-1,0};S.push_back(s);C.push_back(c);}
 vector<Perm> gs;
 for(int g=0;g<9;g++){Perm p{};for(int r=0;r<48;r++){Node y=apply(V[r],S[g],C[g]);int at=-1;for(int s=0;s<48;s++)if(peq(y,V[s])){at=s;break;}if(at<0){cerr<<"no match gen "<<g<<" node "<<r<<"\n";exit(2);}p[r]=at;}gs.push_back(p);}return gs;
}
Perm compose(Perm const&a,Perm const&b){Perm c{};for(int i=0;i<48;i++)c[i]=a[b[i]];return c;}
struct PH{size_t operator()(Perm const&p)const noexcept{uint64_t h=1469598103934665603ULL;for(auto x:p){h^=x;h*=1099511628211ULL;}return h;}};
vector<Perm> group(vector<Perm> const&gs){Perm id{};for(int i=0;i<48;i++)id[i]=i;unordered_set<Perm,PH> seen;seen.insert(id);vector<Perm> v{id};for(size_t q=0;q<v.size();q++)for(auto const&g:gs){Perm h=compose(g,v[q]);if(seen.insert(h).second)v.push_back(h);}return v;}
long long mpow(long long a,long long e,int p){long long r=1;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
struct Key{array<int,7>a{};bool operator==(Key const&o)const{return a==o.a;}};struct KH{size_t operator()(Key const&k)const noexcept{uint64_t h=1469598103934665603ULL;for(int x:k.a){h^=(unsigned)x+0x9e3779b9u;h*=1099511628211ULL;}return h;}};
bool normal6(array<array<int,7>,48> const&N,array<int,6>const&id,int p,Key&out){int M[6][7];for(int r=0;r<6;r++)for(int c=0;c<7;c++)M[r][c]=N[id[r]][c];int pc[6],rk=0;for(int c=0;c<7&&rk<6;c++){int pv=-1;for(int r=rk;r<6;r++)if(M[r][c]){pv=r;break;}if(pv<0)continue;if(pv!=rk)for(int j=0;j<7;j++)swap(M[pv][j],M[rk][j]);long long inv=mpow(M[rk][c],p-2,p);for(int j=0;j<7;j++)M[rk][j]=M[rk][j]*inv%p;for(int r=0;r<6;r++)if(r!=rk&&M[r][c]){int f=M[r][c];for(int j=0;j<7;j++){long long z=M[r][j]-(long long)f*M[rk][j];z%=p;if(z<0)z+=p;M[r][j]=z;}}pc[rk++]=c;}if(rk<6)return false;bool isp[7]={};for(int r=0;r<6;r++)isp[pc[r]]=1;int f=0;while(isp[f])f++;array<int,7>x{};x[f]=1;for(int r=0;r<6;r++){int z=M[r][f];x[pc[r]]=z?p-z:0;}int fst=0;while(!x[fst])fst++;long long inv=mpow(x[fst],p-2,p);for(int c=0;c<7;c++)x[c]=x[c]*inv%p;out.a=x;return true;}
uint64_t actmask(uint64_t m,Perm const&p){uint64_t z=0;for(int i=0;i<48;i++)if((m>>i)&1)z|=1ULL<<p[i];return z;}
uint64_t fnv_masks(vector<uint64_t> const&v){uint64_t h=1469598103934665603ULL;for(uint64_t x:v)for(int j=0;j<8;j++){h^=(x>>(8*j))&255;h*=1099511628211ULL;}return h;}
int main(){auto V=nodes();auto gs=gens(V);auto Gp=group(gs);cout<<"group="<<Gp.size()<<"\n";if(Gp.size()!=1536)return 3;
 const int p=1097,ii=341;array<array<int,7>,48>N{};for(int r=0;r<48;r++)for(int c=0;c<7;c++){long long z=V[r].z[c].r+(long long)V[r].z[c].i*ii;z%=p;if(z<0)z+=p;N[r][c]=z;}
 unordered_map<Key,array<int,6>,KH> mp;mp.reserve(800000);array<int,6>id{};for(id[0]=0;id[0]<43;id[0]++)for(id[1]=id[0]+1;id[1]<44;id[1]++)for(id[2]=id[1]+1;id[2]<45;id[2]++)for(id[3]=id[2]+1;id[3]<46;id[3]++)for(id[4]=id[3]+1;id[4]<47;id[4]++)for(id[5]=id[4]+1;id[5]<48;id[5]++){Key k;if(normal6(N,id,p,k))mp.emplace(k,id);}cout<<"hyp="<<mp.size()<<"\n";
 vector<uint64_t> hi;map<int,int>dist;for(auto const&kv:mp){uint64_t m=0;int n=0;for(int r=0;r<48;r++){long long s=0;for(int c=0;c<7;c++)s+=(long long)kv.first.a[c]*N[r][c];if(s%p==0){m|=1ULL<<r;n++;}}if(n>=14){hi.push_back(m);dist[n]++;}}
 sort(hi.begin(),hi.end());hi.erase(unique(hi.begin(),hi.end()),hi.end());if(fnv_masks(hi)!=0xba8379b50029db53ULL){cerr<<"digest mismatch\n";return 5;}cout<<"hi="<<hi.size()<<" dist";for(auto [n,c]:dist)cout<<" "<<n<<":"<<c;cout<<"\n";
 unordered_set<uint64_t> H(hi.begin(),hi.end()),done;map<int,vector<int>> orbitSizes;vector<pair<int,uint64_t>> reps;uint64_t c0=0;for(int i=24;i<48;i++)c0|=1ULL<<i;
 int c0orb=-1;for(uint64_t m:hi)if(!done.count(m)){unordered_set<uint64_t> O;for(auto const&p:Gp){uint64_t z=actmask(m,p);if(!H.count(z)){cerr<<"orbit leaves high set n="<<__builtin_popcountll(m)<<"\n";return 4;}O.insert(z);}for(auto z:O)done.insert(z);int n=__builtin_popcountll(m);orbitSizes[n].push_back((int)O.size());uint64_t rep=*min_element(O.begin(),O.end());reps.push_back({n,rep});if(O.count(c0))c0orb=O.size();}
 cout<<"orbit_summary\n";for(auto &[n,v]:orbitSizes){sort(v.begin(),v.end());cout<<n<<" count="<<v.size()<<" sizes=";for(int x:v)cout<<x<<",";cout<<"\n";}cout<<"c0_orbit_size="<<c0orb<<"\n";
 cout<<"inc24_orbits\n";for(auto [n,r]:reps)if(n==24){unordered_set<uint64_t>O;for(auto const&p:Gp)O.insert(actmask(r,p));cout<<"rep="<<hex<<setw(12)<<setfill('0')<<r<<dec<<" size="<<O.size()<<" contains_c0="<<O.count(c0)<<"\n";}
 map<int,vector<int>> exp={{14,{96,192,192,384,384}},{15,{256}},{16,{3,24}},{19,{48}},{20,{48}},{24,{4,24}}};
 if(orbitSizes!=exp){cerr<<"orbit summary mismatch\n";return 6;}
 uint64_t h2=0;for(int r=0;r<48;r++){G s{};s.r=V[r].z[0].r+V[r].z[1].r-V[r].z[5].r;s.i=V[r].z[0].i+V[r].z[1].i-V[r].z[5].i;if(gz(s))h2|=1ULL<<r;}
 if(h2!=0x005a5affa5a5ULL){cerr<<"H2 support mismatch\n";return 7;}
 vector<vector<int>> comps;
 for(int br=0;br<2;br++)for(int ep:{1,-1})for(int de:{1,-1}){vector<int>w;for(int r=0;r<48;r++)if((h2>>r)&1){auto z=V[r].z;auto eq=[&](G x){return gz(x);};auto sub=[&](G x,G y){return G{x.r-y.r,x.i-y.i};};auto scale=[&](G x,int q){return G{x.r*q,x.i*q};};bool ok=false;if(br==0)ok=eq(z[0])&&eq(sub(z[5],z[1]))&&eq(sub(z[4],scale(z[2],ep)))&&eq(sub(z[6],scale(z[3],de)));else ok=eq(z[1])&&eq(sub(z[5],z[0]))&&eq(sub(z[3],scale(z[2],ep)))&&eq(sub(z[6],scale(z[4],de)));if(ok)w.push_back(r);}if(w.size()!=6){cerr<<"conic node count mismatch\n";return 8;}comps.push_back(w);}
 array<int,48> mult{};for(auto const&w:comps)for(int r:w)mult[r]++;for(int r=0;r<48;r++)if((h2>>r)&1){if(mult[r]!=2){cerr<<"node-conic incidence mismatch\n";return 9;}}else if(mult[r]!=0){cerr<<"off-H2 conic incidence\n";return 10;}
 cout<<"PASS STAGE32_MB104_GENUS1_SPAN5_HYPERPLANE_AUT_ORBITS_V1\n";
 cout<<"aut_group_order=1536 high_hyperplanes=1655 aut_orbits=12\n";
 cout<<"orbit_sizes=14:[96,192,192,384,384];15:[256];16:[3,24];19:[48];20:[48];24:[4,24]\n";
 cout<<"incidence24=two_orbits_4_plus_24 second_rep=a1+a2-b3 eight_conics_each_6_nodes_each_node_on_2\n";
}
