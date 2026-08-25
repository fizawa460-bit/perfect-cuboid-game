#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using i128 = __int128_t;
using Clock = std::chrono::steady_clock;
static constexpr int RANK=63, TOTAL=142, CUT1=140, CUT2=141;

struct Problem{
    int n=0,m=0; std::string core_sha,source_blob,input_sha;
    std::vector<std::vector<long long>> q,lin; std::vector<long long> p0,cap;
};
static Problem load_problem(const std::string&path){
    std::ifstream f(path); if(!f) throw std::runtime_error("cannot open input");
    std::string magic; std::getline(f,magic);
    if(magic!="S32_D16_CONSTRAINED_HPERP_PARENT_CUTS_V1") throw std::runtime_error("bad magic");
    Problem p; std::getline(f,p.core_sha); std::getline(f,p.source_blob); std::getline(f,p.input_sha);
    f>>p.n>>p.m; if(p.n!=RANK||p.m!=TOTAL) throw std::runtime_error("unexpected dimensions");
    p.q.assign(p.n,std::vector<long long>(p.n));
    for(int i=0;i<p.n;i++)for(int j=0;j<p.n;j++)f>>p.q[i][j];
    p.p0.resize(p.m);p.cap.resize(p.m);p.lin.assign(p.m,std::vector<long long>(p.n));
    for(int r=0;r<p.m;r++){f>>p.p0[r]>>p.cap[r];for(int j=0;j<p.n;j++)f>>p.lin[r][j];}
    if(!f) throw std::runtime_error("truncated input");
    if(p.cap[CUT1]!=8||p.cap[CUT2]!=40) throw std::runtime_error("bad parent-cut caps");
    return p;
}
struct Tier{
    int bound=0;std::string status="COMPLETE";
    uint64_t nodes=0,trials=0,prunes=0,cut1_prunes=0,cut2_prunes=0,leaves=0,survivors=0,nonzero=0;
    uint64_t checksum=1469598103934665603ULL;double seconds=0;std::array<uint64_t,35> hist{};
};
class Enum{
    const Problem&p;int n,m,bound=0;std::vector<std::vector<long double>>L,A,dual;
    std::vector<long double>D,assigned;std::vector<long long>z;std::vector<int>order;Tier out;
    bool stop=false;double maxsec=0;uint64_t nodecap=0,survcap=0;Clock::time_point started;
public:
    explicit Enum(const Problem&pp):p(pp),n(pp.n),m(pp.m){
        L.assign(n,std::vector<long double>(n,0));D.assign(n,0);
        for(int i=0;i<n;i++){
            L[i][i]=1;long double di=(long double)p.q[i][i];
            for(int k=0;k<i;k++)di-=L[i][k]*L[i][k]*D[k];
            if(!(di>0))throw std::runtime_error("LDL lost positive definiteness");D[i]=di;
            for(int j=i+1;j<n;j++){
                long double v=(long double)p.q[j][i];for(int k=0;k<i;k++)v-=L[j][k]*L[i][k]*D[k];L[j][i]=v/D[i];
            }
        }
        A.assign(m,std::vector<long double>(n,0));dual.assign(m,std::vector<long double>(n,0));
        for(int r=0;r<m;r++){
            for(int i=0;i<n;i++){long double v=(long double)p.lin[r][i];for(int k=0;k<i;k++)v-=L[i][k]*A[r][k];A[r][i]=v;}
            long double s=0;for(int i=0;i<n;i++){s+=A[r][i]*A[r][i]/D[i];dual[r][i]=s;}
        }
        order={CUT1,CUT2};for(int r=92;r<140;r++)order.push_back(r);for(int r=0;r<92;r++)order.push_back(r);
        z.assign(n,0);assigned.assign(m,0);
    }
    Tier run(int b,double sec,uint64_t nc,uint64_t sc){
        bound=b;maxsec=sec;nodecap=nc;survcap=sc;out=Tier{};out.bound=b;std::fill(z.begin(),z.end(),0);std::fill(assigned.begin(),assigned.end(),0);
        stop=false;started=Clock::now();if(possible(n-1,(long double)b))dfs(n-1,0);out.seconds=std::chrono::duration<double>(Clock::now()-started).count();return out;
    }
private:
    bool limits(){
        if(stop)return true;if(out.nodes>=nodecap){out.status="NODE_CAP";stop=true;return true;}
        if(out.survivors>=survcap){out.status="SURVIVOR_CAP";stop=true;return true;}
        if((out.nodes&16383ULL)==0&&std::chrono::duration<double>(Clock::now()-started).count()>=maxsec){out.status="TIMEOUT";stop=true;return true;}return false;
    }
    bool possible(int last,long double budget){
        if(budget<0)budget=0;
        for(int r:order){
            long double center=(long double)p.p0[r]+assigned[r],dist=0;
            if(center<0)dist=-center;else if(center>(long double)p.cap[r])dist=center-(long double)p.cap[r];
            if(dist==0)continue;long double reach=std::sqrt(std::max((long double)0,budget*(last>=0?dual[r][last]:0)));
            long double guard=1e-8L*(1+std::fabs(center)+reach);
            if(dist>reach+guard){if(r==CUT1)out.cut1_prunes++;if(r==CUT2)out.cut2_prunes++;return false;}
        }return true;
    }
    void dfs(int i,long double used){
        out.nodes++;if(limits())return;if(i<0){leaf();return;}long double rem=(long double)bound-used;if(rem<-1e-10L)return;if(rem<0)rem=0;
        long double shift=0;for(int j=i+1;j<n;j++)shift+=L[j][i]*(long double)z[j];long double radius=std::sqrt(std::max((long double)0,rem/D[i]));
        long double pad=1e-9L*(1+std::fabs(shift)+radius);long long lo=(long long)std::ceil(-shift-radius-pad),hi=(long long)std::floor(-shift+radius+pad);
        for(long long zi=lo;zi<=hi;zi++){
            if(stop)return;out.trials++;long double ti=(long double)zi+shift,newused=used+D[i]*ti*ti;if(newused>(long double)bound+1e-8L)continue;
            z[i]=zi;for(int r=0;r<m;r++)assigned[r]+=A[r][i]*ti;long double newrem=(long double)bound-newused;
            if(possible(i-1,newrem))dfs(i-1,newused);else out.prunes++;for(int r=0;r<m;r++)assigned[r]-=A[r][i]*ti;
        }z[i]=0;
    }
    void leaf(){
        out.leaves++;i128 norm=0;for(int i=0;i<n;i++)for(int j=0;j<n;j++)norm+=(i128)z[i]*(i128)p.q[i][j]*(i128)z[j];if(norm<0||norm>bound)return;
        for(int r=0;r<m;r++){i128 v=p.p0[r];for(int j=0;j<n;j++)v+=(i128)p.lin[r][j]*(i128)z[j];if(v<0||v>p.cap[r])return;}
        out.survivors++;if(norm!=0)out.nonzero++;int ni=(int)norm;if(0<=ni&&ni<35)out.hist[ni]++;
        for(long long v:z){uint64_t x=(uint64_t)v;for(int b=0;b<8;b++){out.checksum^=(x>>(8*b))&255ULL;out.checksum*=1099511628211ULL;}}
    }
};
static std::vector<int> parse_bounds(const std::string&s){std::vector<int>v;std::stringstream ss(s);std::string x;while(std::getline(ss,x,','))if(!x.empty())v.push_back(std::stoi(x));if(v.empty())throw std::runtime_error("empty bounds");return v;}
int main(int argc,char**argv){
    try{
        std::string input,output,bounds_s="2,4,6,8,10,12,16,20,26,34";double per=90;uint64_t nodecap=250000000ULL,survcap=5000000ULL;
        for(int i=1;i<argc;i++){std::string a=argv[i];auto need=[&](){if(++i>=argc)throw std::runtime_error("missing arg");return std::string(argv[i]);};
            if(a=="--input")input=need();else if(a=="--output")output=need();else if(a=="--bounds")bounds_s=need();else if(a=="--per-bound-seconds")per=std::stod(need());else if(a=="--node-cap")nodecap=std::stoull(need());else if(a=="--survivor-cap")survcap=std::stoull(need());else throw std::runtime_error("unknown arg "+a);}
        if(input.empty()||output.empty())throw std::runtime_error("input/output required");Problem p=load_problem(input);Enum en(p);std::vector<Tier>tiers;bool regression=true;
        for(int b:parse_bounds(bounds_s)){Tier t=en.run(b,per,nodecap,survcap);tiers.push_back(t);std::cerr<<"bound="<<b<<" status="<<t.status<<" nodes="<<t.nodes<<" cut1="<<t.cut1_prunes<<" cut2="<<t.cut2_prunes<<" surv="<<t.survivors<<" sec="<<t.seconds<<"\n";
            if(b==2&&!(t.status=="COMPLETE"&&t.survivors==49&&t.nonzero==48))regression=false;if(b==4&&!(t.status=="COMPLETE"&&t.survivors==1177&&t.nonzero==1176))regression=false;if((b==2||b==4)&&!regression)break;if(t.status!="COMPLETE")break;}
        std::ofstream f(output);if(!f)throw std::runtime_error("cannot open output");
        f<<"{\n  \"schema\": \"STAGE32_SCOUT_D16_PARENT_POLYTOPE_CUTS_V1\",\n  \"scope\": \"SCOUT_ONLY_NO_CREDIT\",\n";
        f<<"  \"source_core_canonical_sha256\": \""<<p.core_sha<<"\",\n  \"source_blob_sha1\": \""<<p.source_blob<<"\",\n  \"prepared_input_sha256\": \""<<p.input_sha<<"\",\n";
        f<<"  \"architecture\": {\"direction\": \"H_PERP_PLUS_140_CAPS_PLUS_EXACT_282_PARENT_POLYTOPE_CUTS_PLUS_NORM_ONE_TREE\", \"floating_pruning_is_scout_only\": true, \"exact_integer_leaf_recheck\": true, \"materialized_branch_count_constructed\": 0},\n";
        f<<"  \"regression\": {\"bound2_expected\":49,\"bound4_expected\":1177,\"pass\":"<<(regression?"true":"false")<<"},\n  \"tiers\": [\n";
        for(size_t k=0;k<tiers.size();k++){auto&t=tiers[k];f<<"    {\"bound\":"<<t.bound<<",\"status\":\""<<t.status<<"\",\"nodes\":"<<t.nodes<<",\"coordinate_trials\":"<<t.trials<<",\"constraint_prunes\":"<<t.prunes<<",\"parent_band_prunes\":"<<t.cut1_prunes<<",\"parent_lower_envelope_prunes\":"<<t.cut2_prunes<<",\"exact_leaves\":"<<t.leaves<<",\"exact_survivors_including_zero\":"<<t.survivors<<",\"nonzero_survivors\":"<<t.nonzero<<",\"elapsed_seconds\":"<<std::fixed<<std::setprecision(6)<<t.seconds<<",\"checksum_fnv64\":\""<<std::hex<<t.checksum<<std::dec<<"\",\"norm_histogram\":{";bool first=true;for(int n=0;n<35;n++)if(t.hist[n]){if(!first)f<<",";first=false;f<<"\""<<n<<"\":"<<t.hist[n];}f<<"}}"<<(k+1<tiers.size()?",":"")<<"\n";}
        f<<"  ],\n  \"THEOREM_CREDIT\": false,\n  \"RECEIVER_CREDIT\": false,\n  \"FULL_D16_G0_ROW_COMPLETE\": false,\n  \"FULL_D176_D192_NUMERICAL_ORBIT_CENSUS\": false,\n  \"R29_LG2_NUMERICAL_COMPONENT_COMPLETE\": false,\n  \"R29_LG2\": \"NOT_DISCHARGED\",\n  \"G10_LOWGENUS_PICARD\": \"AMBER\"\n}\n";
        return regression?0:2;
    }catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<"\n";return 1;}
}
