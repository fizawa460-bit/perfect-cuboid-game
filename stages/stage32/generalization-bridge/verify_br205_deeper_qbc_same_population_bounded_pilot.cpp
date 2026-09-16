#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using i64 = long long;
using i128 = __int128_t;
struct ARec { int a, sa, q; i64 mult; };
struct BCBase { int b,c,support,t,r; std::vector<std::pair<int,i64>> levels; i64 total_mult; };
static int ceil_div2(int x){int q=x/2, rem=x%2; if(rem!=0&&x>0)++q;return q;}
static int floor_div2(int x){int q=x/2, rem=x%2; if(rem!=0&&x<0)--q;return q;}
static int ceil_div4(int x){return x>=0?(x+3)/4:x/4;}
static int component_a(int d,int a){int h=d/2;return std::min({13,d-a,d-2*a+4,h+5});}
static int component3(int d,int b,int c){return std::min({9,d-b-c,d-2*b,d-2*c+1});}
static std::vector<ARec> build_a(int H){
 std::map<std::tuple<int,int,int>,i64> hist;
 for(int a=0;a<=H;++a) for(int x2=0;x2<=a;++x2) for(int x3=0;x3<=a-x2;++x3){
   int x7=a-x2-x3; int support=(x2>0)+(x3>0)+(x7>0); int q=x2*x2+x3*x3+x7*x7; ++hist[{a,support,q}];
 }
 std::vector<ARec> out; for(auto const&kv:hist){auto[a,s,q]=kv.first;out.push_back({a,s,q,kv.second});} return out;
}
static std::vector<BCBase> build_bc(int H){
 std::map<std::tuple<int,int,int,int,int>,std::map<int,i64>> hist;
 for(int x0=0;x0<=H;++x0) for(int x1=x0;x1<=H;++x1) for(int x5=0;x5<=H;++x5){
   int max_x9=H-x1-x5; if(max_x9<0)break;
   for(int x8=0;x8<=H;++x8){
     if(x0==x1&&x5>x8) continue;
     int rem_c=H-x0-x8; if(rem_c<0)break;
     for(int x9=0;x9<=max_x9;++x9){
       int b=x1+x5+x9;
       for(int x6=0;x6<=rem_c;++x6){
         if(x0==x1&&x5==x8&&x6>x9) continue;
         for(int x10=0;x10<=rem_c-x6;++x10){
           if((x1+x8+x9+x10)&1) continue;
           int c=x0+x8+x6+x10;
           int support=(x0>0)+(x1>0)+(x5>0)+(x6>0)+(x8>0)+(x9>0)+(x10>0);
           int t=x0+x1+x6+x9; int r=(x0+x8+x10)&1;
           int q=x0*x0+x1*x1+x5*x5+x6*x6+x8*x8+x9*x9+x10*x10;
           ++hist[{b,c,support,t,r}][q];
         }
       }
     }
   }
 }
 std::vector<BCBase> out; out.reserve(hist.size());
 for(auto const&kv:hist){auto[b,c,s,t,r]=kv.first;BCBase z{b,c,s,t,r,{},0};for(auto const&qm:kv.second){z.levels.push_back(qm);z.total_mult+=qm.second;}out.push_back(std::move(z));}
 return out;
}
static int one_x4_count(int d,int g,int t,int r,int q,int e){
 if(e<0||(e&1)||e>19*d/5)return 0; int j=e/2;int n=19*d-10*j;int rhs=3*d*d+48*d+96-96*g;int rem=rhs-24*q;if(n<0||rem<0)return 0;
 int root=(int)std::floor(std::sqrt((double)(rem/4)));while((root+1)*(root+1)<=rem/4)++root;while(root*root>rem/4)--root;
 int D=d/2-t;int lo=std::max(0,ceil_div2(D-root));int hi0=floor_div2(D+root);int hi=std::min(n,hi0);if(lo>hi)return 0;int first=((lo&1)==r)?lo:lo+1;if(first>hi)return 0;return(hi-first)/2+1;
}
static i64 x4_prefix(int d,int g,int t,int r,int q,int J){
 if(J<0)return 0; int maxJ=(19*d/5)/2;J=std::min(J,maxJ);int rhs=3*d*d+48*d+96-96*g;int rem=rhs-24*q;if(rem<0)return 0;
 int root=(int)std::floor(std::sqrt((double)(rem/4)));while((root+1)*(root+1)<=rem/4)++root;while(root*root>rem/4)--root;
 int D=d/2-t;int lo=std::max(0,ceil_div2(D-root));int hi0=floor_div2(D+root);int first=((lo&1)==r)?lo:lo+1;if(hi0<first)return 0;
 int switch_j=(19*d-hi0)/10;i64 constant_count=(hi0-first)/2+1,total=0;int constant_end=std::min(J,switch_j);if(constant_end>=0)total+=(i64)(constant_end+1)*constant_count;
 int a=std::max(0,switch_j+1);if(a<=J){i64 base=(19*d-first)/2+1;int b=std::min<i64>(J,(base-1)/5);if(a<=b){i64 count=b-a+1;total+=count*base-5LL*(a+b)*count/2;}}
 return total;
}
static i64 sum_x4_over_even_e(int d,int g,int t,int r,int q,int lower,int upper,int excluded1,int excluded2){
 int lo=(lower&1)?lower+1:lower;int hi=(upper&1)?upper-1:upper;if(lo>hi)return 0;
 i64 total=x4_prefix(d,g,t,r,q,hi/2)-x4_prefix(d,g,t,r,q,lo/2-1);
 if(excluded1>=lo&&excluded1<=hi&&!(excluded1&1)) total-=one_x4_count(d,g,t,r,q,excluded1);
 if(excluded2>=lo&&excluded2<=hi&&!(excluded2&1)&&excluded2!=excluded1) total-=one_x4_count(d,g,t,r,q,excluded2);
 return total;
}
static void req(bool ok,const char* msg){if(!ok){std::cerr<<"FAIL: "<<msg<<"\n";std::exit(1);}}
int main(){
 const int H=16,maxD=32; const std::array<int,6> Ks{1,2,4,8,16,32};
 auto A=build_a(H);auto BC=build_bc(H);
 std::vector<std::vector<ARec>> A_by_a(H+1);for(auto const&a:A)A_by_a[a.a].push_back(a);
 std::array<i128,6> ans{};i128 full=0; i128 active_tail_mass=0; i64 active_cells=0, maxlevels=0; std::map<int,i64> level_hist;
 for(auto const&B:BC){maxlevels=std::max<i64>(maxlevels,B.levels.size());++level_hist[(int)B.levels.size()];}
 for(int g:{0,1}) for(int d=8;d<=maxD;d+=2){
   int h=d/2, legacy=(g==0)?8:4, required_support=ceil_div4(d-16*g+16);
   for(auto const&B:BC){
    if(B.b>h||B.c>h)continue;int c3=component3(d,B.b,B.c);if(c3<0)continue;
    int L=B.levels.size();
    for(int a=0;a<=h&&a<=H;++a){int ca=component_a(d,a);if(ca<0)continue;int exceptional_mass=a+B.b+B.c;int support_remainder=std::min(16,d)+ca+c3;
      for(auto const&AR:A_by_a[a]){
       int support=B.support+AR.sa;int qneed=required_support-support;if(qneed>0&&support_remainder<qneed)continue;
       int lower=std::max({legacy,required_support,d-4*g+4,exceptional_mass,exceptional_mass+std::max(0,qneed)});
       int upper=std::min({19*d/5,3*d,3*d-(B.b-B.c)});if(lower>upper)continue;
       int ex1=-1,ex2=-1;int e_n358=3*d-(B.b-B.c);
       if(B.b<=h-5&&support+support_remainder==required_support&&e_n358-exceptional_mass>=support_remainder)ex1=e_n358;
       if(g==1&&d==8)ex2=8;
       std::vector<i64> f(L);std::vector<i64> pm(L+1);std::vector<i128> ep(L+1);
       for(int i=0;i<L;++i){auto[qb,mb]=B.levels[i];f[i]=sum_x4_over_even_e(d,g,B.t,B.r,AR.q+qb,lower,upper,ex1,ex2);pm[i+1]=pm[i]+mb;ep[i+1]=ep[i]+(i128)mb*f[i];}
       full+=(i128)AR.mult*ep[L];
       if(L>8 && f[7]!=f[L-1]){++active_cells; active_tail_mass+=(i128)AR.mult*(B.total_mult-pm[7]);}
       for(int kk=0;kk<6;++kk){int K=Ks[kk];i128 bc;if(L<=K)bc=ep[L];else{int j=K-1;bc=ep[j]+(i128)(B.total_mult-pm[j])*f[j];}ans[kk]+=(i128)AR.mult*bc;}
      }
    }
   }
 }
 i64 tail_base_states=0;
 for(auto const&kv:level_hist) if(kv.first>8) tail_base_states += kv.second;
 const std::array<i64,6> expected{304596475910LL,290611516997LL,264256534379LL,230521553871LL,201104867976LL,191878707884LL};
 req(A.size()==196,"H16 A-state regression");
 req(BC.size()==16781,"H16 BC-base-state regression");
 for(int i=0;i<6;++i) req(ans[i]==(i128)expected[i],"qBC tier survivor regression");
 req(full==(i128)191776755135LL,"full qBC survivor regression");
 req(maxlevels==80,"max qBC level regression");
 req(tail_base_states==7840,"K8 tail base-state regression");
 req(active_cells==2396203,"active K8-tail evaluation-cell regression");
 req(active_tail_mass==(i128)931400934LL,"active K8-tail multiplicity regression");
 req(ans[3]>ans[4] && ans[4]>ans[5] && ans[5]>full,"deeper qBC must strictly tighten");
 std::cout
   <<"{\n"
   <<"  \"schema\":\"STAGE32_BR205_DEEPER_QBC_SAME_POPULATION_BOUNDED_PILOT_V1\",\n"
   <<"  \"status\":\"PASS_STRICT_DEEPER_QBC_BOUNDED_ZERO_CREDIT\",\n"
   <<"  \"scope\":{\"H\":16,\"max_d\":32,\"population\":\"BR202_P1_SAME_POPULATION\"},\n"
   <<"  \"regression\":{\"A_states\":196,\"BC_base_states\":16781,\"K1\":304596475910,\"K2\":290611516997,\"K4\":264256534379,\"K8\":230521553871},\n"
   <<"  \"deeper_qBC\":{\"K16\":201104867976,\"K32\":191878707884,\"FULL\":191776755135,\"K8_minus_K16\":29416685895,\"K8_minus_K32\":38642845987,\"K8_minus_FULL\":38744798736},\n"
   <<"  \"tail_activity\":{\"max_qBC_levels\":80,\"BC_base_states_with_more_than_8_levels\":7840,\"active_K8_tail_evaluation_cells\":2396203,\"active_K8_tail_multiplicity\":931400934},\n"
   <<"  \"gate\":{\"same_population_strict_improvement\":true,\"qBC_K8_truncation_active_on_nonzero_retained_mass\":true,\"BR205_authorized\":false,\"requires_BR204_exact_FULL178_slack_attribution\":true},\n"
   <<"  \"credit\":{\"stage32_main\":false,\"full178_complete\":false,\"theorem\":false,\"effectivity\":false,\"receiver\":false,\"endpoint\":false,\"merge\":false}\n"
   <<"}\n";
}
