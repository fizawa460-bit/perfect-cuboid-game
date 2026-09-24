#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>
#include <vector>

using i64 = long long;

static void req(bool ok, const char* msg){ if(!ok){ std::cerr<<"FAIL: "<<msg<<"\n"; std::exit(1);} }

struct Feat { int support; int bits; bool operator<(Feat const&o)const{return std::tie(support,bits)<std::tie(o.support,o.bits);} };
struct Base { int b,c,support,t,r; bool operator<(Base const&o)const{return std::tie(b,c,support,t,r)<std::tie(o.b,o.c,o.support,o.t,o.r);} };
using QMap = std::map<int,i64>;
struct FeatureLevels { std::map<Feat,QMap> q; std::map<Feat,i64> total; };
struct Retained { std::map<int,std::map<int,i64>> levels; std::map<int,i64> total; };

static QMap first8(QMap const& in){ QMap out; int n=0; for(auto const&kv:in){ if(n++==8) break; out.insert(kv);} return out; }

static std::vector<std::vector<FeatureLevels>> build_strict(int H){
 std::vector<std::vector<FeatureLevels>> out(H+1,std::vector<FeatureLevels>(H+1));
 for(int u=0;u<=H;++u) for(int v=0;v<=H;++v){
   std::map<Feat,QMap> tmp;
   for(int x0=0;x0<=v;++x0){ int x6=v-x0; for(int x1=x0+1;x1<=u;++x1){ int x9=u-x1;
     int q=x0*x0+x6*x6+x1*x1+x9*x9;
     int s=(x0>0)+(x6>0)+(x1>0)+(x9>0);
     int bits=((x0&1)<<0)|((x1&1)<<1)|((x6&1)<<3)|((x9&1)<<5);
     Feat f{s,bits}; ++tmp[f][q]; ++out[u][v].total[f];
   }}
   for(auto const&kv:tmp) out[u][v].q[kv.first]=first8(kv.second);
 }
 return out;
}
static std::vector<std::vector<FeatureLevels>> build_equal(int H){
 std::vector<std::vector<FeatureLevels>> out(H+1,std::vector<FeatureLevels>(H+1));
 for(int u=0;u<=H;++u) for(int v=0;v<=H;++v){
   std::map<Feat,QMap> tmp;
   for(int x=0;x<=std::min(u,v);++x){ int x6=v-x,x9=u-x;
     int q=2*x*x+x6*x6+x9*x9;
     int s=2*(x>0)+(x6>0)+(x9>0);
     int bits=((x&1)<<0)|((x&1)<<1)|((x6&1)<<3)|((x9&1)<<5);
     Feat f{s,bits}; ++tmp[f][q]; ++out[u][v].total[f];
   }
   for(auto const&kv:tmp) out[u][v].q[kv.first]=first8(kv.second);
 }
 return out;
}
static std::vector<std::vector<FeatureLevels>> build_pair(int H){
 std::vector<std::vector<FeatureLevels>> out(H+1);
 for(int w=0;w<=H;++w){ out[w].resize(w+2); for(int L=0;L<=w+1;++L){
   std::map<Feat,QMap> tmp;
   for(int x8=L;x8<=w;++x8){ int x10=w-x8;
     int q=x8*x8+x10*x10, s=(x8>0)+(x10>0), bits=((x8&1)<<4)|((x10&1)<<6);
     Feat f{s,bits}; ++tmp[f][q]; ++out[w][L].total[f];
   }
   for(auto const&kv:tmp) out[w][L].q[kv.first]=first8(kv.second);
 }}
 return out;
}

static void trim_retained(Retained &r){ while(r.levels.size()>8){ auto it=std::prev(r.levels.end()); r.levels.erase(it);} }

static std::map<Base,Retained> compact_range(int H, int blo, int bhi, std::vector<std::vector<FeatureLevels>> const& S, std::vector<std::vector<FeatureLevels>> const& E, std::vector<std::vector<FeatureLevels>> const& P){
 std::map<Base,Retained> out;
 for(int b=blo;b<=bhi;++b) for(int c=0;c<=H;++c) for(int t=0;t<=b+c;++t){
   if((c+t)&1) continue; int ulo=std::max(0,t-c), uhi=std::min(b,t); if(ulo>uhi) continue;
   for(int u=ulo;u<=uhi;++u){ int v=t-u,w=c-t+u,x5=b-u; int adds=(x5>0), addbits=(x5&1)<<2, addq=x5*x5;
     std::array<std::pair<FeatureLevels const*,FeatureLevels const*>,2> branches{}; int nb=0;
     branches[nb++]={&S[u][v],&P[w][0]}; int L=x5+(v>u); if(L<=w) branches[nb++]={&E[u][v],&P[w][L]};
     for(int bi=0;bi<nb;++bi){ auto const&C=*branches[bi].first; auto const&D=*branches[bi].second;
       for(auto const&ct:C.total) for(auto const&dt:D.total){ int support=ct.first.support+dt.first.support+adds, bits=ct.first.bits|dt.first.bits|addbits; int r=(bits&1)^(w&1); Base key{b,c,support,t,r}; out[key].total[bits]+=ct.second*dt.second; }
       for(auto const&cq:C.q) for(auto const&dq:D.q){ int support=cq.first.support+dq.first.support+adds, bits=cq.first.bits|dq.first.bits|addbits; int r=(bits&1)^(w&1); Base key{b,c,support,t,r}; auto &R=out[key];
         for(auto const&q1:cq.second) for(auto const&q2:dq.second) R.levels[addq+q1.first+q2.first][bits]+=q1.second*q2.second;
         trim_retained(R);
       }
     }
   }
 }
 return out;
}
static std::map<Base,Retained> compact(int H){ auto S=build_strict(H); auto E=build_equal(H); auto P=build_pair(H); return compact_range(H,0,H,S,E,P); }

static std::map<Base,Retained> direct(int H){
 std::map<Base,std::map<int,std::map<int,i64>>> full;
 for(int x0=0;x0<=H;++x0) for(int x1=x0;x1<=H;++x1) for(int x5=0;x5<=H;++x5){
   int maxx9=H-x1-x5; if(maxx9<0) break;
   for(int x8=0;x8<=H;++x8){ if(x0==x1&&x5>x8) continue; int rem=H-x0-x8; if(rem<0) break;
     for(int x9=0;x9<=maxx9;++x9){ int b=x1+x5+x9;
       for(int x6=0;x6<=rem;++x6){ if(x0==x1&&x5==x8&&x6>x9) continue;
         for(int x10=0;x10<=rem-x6;++x10){ if((x1+x8+x9+x10)&1) continue; int c=x0+x8+x6+x10;
           int support=(x0>0)+(x1>0)+(x5>0)+(x6>0)+(x8>0)+(x9>0)+(x10>0), t=x0+x1+x6+x9, r=(x0+x8+x10)&1;
           int q=x0*x0+x1*x1+x5*x5+x6*x6+x8*x8+x9*x9+x10*x10;
           int bits=((x0&1)<<0)|((x1&1)<<1)|((x5&1)<<2)|((x6&1)<<3)|((x8&1)<<4)|((x9&1)<<5)|((x10&1)<<6);
           ++full[{b,c,support,t,r}][q][bits];
         }
       }
     }
   }
 }
 std::map<Base,Retained> out;
 for(auto const&bk:full){ auto &R=out[bk.first]; int n=0; for(auto const&qv:bk.second){ for(auto const&bm:qv.second) R.total[bm.first]+=bm.second; if(n<8) R.levels[qv.first]=qv.second; ++n; } }
 return out;
}

static bool same(std::map<Base,Retained> const&A,std::map<Base,Retained> const&B){ if(A.size()!=B.size()) return false; auto ia=A.begin(),ib=B.begin(); for(;ia!=A.end();++ia,++ib){ if(std::tie(ia->first.b,ia->first.c,ia->first.support,ia->first.t,ia->first.r)!=std::tie(ib->first.b,ib->first.c,ib->first.support,ib->first.t,ib->first.r)) return false; if(ia->second.total!=ib->second.total||ia->second.levels!=ib->second.levels) return false;} return true; }

int main(){
 auto c10=compact(10), d10=direct(10); req(same(c10,d10),"H10 compact K8/parity mismatch"); req((int)c10.size()==3800,"H10 state count");
 auto c16=compact(16), d16=direct(16); req(same(c16,d16),"H16 compact K8/parity mismatch"); req((int)c16.size()==16781,"H16 state count");
 long long lev16=0,buck16=0; for(auto const&kv:c16){lev16+=kv.second.levels.size(); for(auto const&q:kv.second.levels) buck16+=q.second.size();}

 int H=96; auto S=build_strict(H); auto E=build_equal(H); auto P=build_pair(H);
 auto b0=compact_range(H,0,0,S,E,P); auto b96=compact_range(H,96,96,S,E,P);
 long long lev0=0,buck0=0,lev96=0,buck96=0;
 for(auto const&kv:b0){lev0+=kv.second.levels.size(); for(auto const&q:kv.second.levels) buck0+=q.second.size();}
 for(auto const&kv:b96){lev96+=kv.second.levels.size(); for(auto const&q:kv.second.levels) buck96+=q.second.size();}
 req((long long)b0.size()==4609,"H96 b=0 state count");
 req(lev0==18189 && buck0==18189,"H96 b=0 K8 profile");
 req((long long)b96.size()==63094,"H96 b=96 state count");
 req(lev96==439932 && buck96==1011820,"H96 b=96 K8 profile");

 std::cout<<"{\n"
 <<"  \"schema\":\"STAGE32_BR204_COMPACT_K8_SYNDROME_PREFLIGHT_V1\",\n"
 <<"  \"status\":\"PASS_ZERO_CREDIT\",\n"
 <<"  \"H10\":{\"base_states\":"<<c10.size()<<",\"direct_equals_compact\":true},\n"
 <<"  \"H16\":{\"base_states\":"<<c16.size()<<",\"direct_equals_compact\":true,\"retained_q_levels\":"<<lev16<<",\"retained_parity_buckets\":"<<buck16<<"},\n"
 <<"  \"H96_scale_smoke\":{\"b0_states\":"<<b0.size()<<",\"b0_q_levels\":"<<lev0<<",\"b0_parity_buckets\":"<<buck0<<",\"b96_states\":"<<b96.size()<<",\"b96_q_levels\":"<<lev96<<",\"b96_parity_buckets\":"<<buck96<<"},\n"
 <<"  \"semantics\":\"first eight distinct qBC levels exact per parity pattern plus all-level parity mass for exact K8 tail reconstruction\",\n"
 <<"  \"streaming\":\"precompute split kernels once; evaluate one b at a time; discard per-b retained map after shard aggregation\",\n"
 <<"  \"credit\":{\"stage32_main\":false,\"full178_complete\":false,\"merge\":false}\n"
 <<"}\n";
 return 0;
}
