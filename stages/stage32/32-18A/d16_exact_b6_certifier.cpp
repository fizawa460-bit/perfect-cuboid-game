#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using boost::multiprecision::cpp_rational;
using i128 = __int128_t;

struct Problem {
    int n=0,m=0;
    std::string core_sha,source_blob,input_sha;
    std::vector<std::vector<long long>> q;
    std::vector<long long> p0,cap;
    std::vector<std::vector<long long>> lin;
};

static Problem load_problem(const std::string& path) {
    std::ifstream f(path); if(!f) throw std::runtime_error("cannot open Hperp input");
    std::string magic; std::getline(f,magic);
    if(magic!="S32_D16_AUT_CANON_HPERP_V1") throw std::runtime_error("bad Hperp magic");
    Problem p; std::getline(f,p.core_sha); std::getline(f,p.source_blob); std::getline(f,p.input_sha);
    f>>p.n>>p.m; if(p.n!=63||p.m!=140) throw std::runtime_error("unexpected Hperp dimensions");
    p.q.assign(p.n,std::vector<long long>(p.n));
    for(int i=0;i<p.n;i++) for(int j=0;j<p.n;j++) f>>p.q[i][j];
    p.p0.resize(p.m); p.cap.resize(p.m); p.lin.assign(p.m,std::vector<long long>(p.n));
    for(int r=0;r<p.m;r++){ f>>p.p0[r]>>p.cap[r]; for(int j=0;j<p.n;j++) f>>p.lin[r][j]; }
    if(!f) throw std::runtime_error("truncated Hperp input");
    return p;
}

struct Bundle {
    int n=0,m=0,k=0,group_order=0;
    std::string input_sha,aut_sha,bundle_sha,seed;
    std::vector<long long> weights,c0;
    std::vector<std::vector<long long>> lin;
    std::vector<std::array<unsigned char,140>> group;
};

static Bundle load_bundle(const std::string& path,const Problem& p){
    std::ifstream f(path); if(!f) throw std::runtime_error("cannot open bundle");
    std::string magic; std::getline(f,magic);
    if(magic!="S32_D16_AUT_CANONICAL_BUNDLE_V1") throw std::runtime_error("bad bundle magic");
    Bundle s; std::getline(f,s.input_sha); std::getline(f,s.aut_sha); std::getline(f,s.bundle_sha); std::getline(f,s.seed);
    f>>s.n>>s.m>>s.k>>s.group_order;
    if(s.input_sha!=p.input_sha||s.n!=63||s.m!=140||s.k!=64||s.group_order!=1536) throw std::runtime_error("bundle mismatch");
    s.weights.resize(s.m); for(auto&x:s.weights) f>>x;
    s.c0.resize(s.k); s.lin.assign(s.k,std::vector<long long>(s.n));
    for(int r=0;r<s.k;r++){ f>>s.c0[r]; for(int j=0;j<s.n;j++) f>>s.lin[r][j]; }
    s.group.resize(s.group_order);
    for(int g=0;g<s.group_order;g++){
        std::array<bool,140> seen{};
        for(int i=0;i<s.m;i++){ int x; f>>x; if(x<0||x>=s.m||seen[x]) throw std::runtime_error("bad permutation"); seen[x]=true; s.group[g][i]=static_cast<unsigned char>(x); }
    }
    if(!f) throw std::runtime_error("truncated bundle");
    return s;
}

static long long floor_rat(const cpp_rational& x){
    cpp_int n=numerator(x), d=denominator(x);
    if(d<=0) throw std::runtime_error("bad rational denominator");
    cpp_int q=n/d, r=n%d; if(n<0 && r!=0) --q;
    return q.convert_to<long long>();
}
static long long ceil_rat(const cpp_rational& x){ return -floor_rat(-x); }

class ExactEnumerator {
public:
    ExactEnumerator(const Problem&p,const Bundle&s):p_(p),s_(s),n_(p.n),m_(p.m){
        L_.assign(n_,std::vector<cpp_rational>(n_,0)); D_.assign(n_,0);
        for(int i=0;i<n_;i++){
            L_[i][i]=1;
            cpp_rational di=p_.q[i][i];
            for(int k=0;k<i;k++) di-=L_[i][k]*L_[i][k]*D_[k];
            if(di<=0) throw std::runtime_error("exact LDL lost positive definiteness");
            D_[i]=di;
            for(int j=i+1;j<n_;j++){
                cpp_rational v=p_.q[j][i];
                for(int k=0;k<i;k++) v-=L_[j][k]*L_[i][k]*D_[k];
                L_[j][i]=v/D_[i];
            }
        }
        for(int i=0;i<n_;i++) for(int j=0;j<n_;j++){
            cpp_rational v=0; int lim=std::min(i,j);
            for(int k=0;k<=lim;k++) v+=L_[i][k]*D_[k]*L_[j][k];
            if(v!=cpp_rational(p_.q[i][j])) throw std::runtime_error("exact LDL reconstruction mismatch");
        }

        cap_a_.assign(m_,std::vector<cpp_rational>(n_,0));
        cap_dual_.assign(m_,std::vector<cpp_rational>(n_,0));
        cap_af_.assign(m_,std::vector<long double>(n_,0));
        cap_dualf_.assign(m_,std::vector<long double>(n_,0));
        for(int r=0;r<m_;r++) build_dual_row(p_.lin[r],cap_a_[r],cap_dual_[r],cap_af_[r],cap_dualf_[r]);

        order_.reserve(m_);
        for(int r=92;r<m_;r++) order_.push_back(r);
        for(int r=0;r<92;r++) order_.push_back(r);

        z_.assign(n_,0); t_.assign(n_,0); tf_.assign(n_,0);
        cap_assignedf_.assign(m_,0);
    }

    void run(int bound,uint64_t node_cap,const std::string& dump_path){
        bound_=bound; node_cap_=node_cap;
        std::ofstream dump(dump_path,std::ios::binary); if(!dump) throw std::runtime_error("cannot open dump");
        dump.write("S32D16C1",8); dump_=&dump;
        if(caps_possible(n_-1,cpp_rational(bound_))) dfs(n_-1,cpp_rational(0));
        dump.close(); if(!dump) throw std::runtime_error("dump close failed"); dump_=nullptr;
    }

    void write_json(const std::string& path)const{
        std::ofstream f(path); if(!f) throw std::runtime_error("cannot open output");
        f<<"{\n";
        f<<"  \"schema\": \"STAGE32_18A_D16_EXACT_B6_TRAVERSAL_CERT_V1\",\n";
        f<<"  \"bound\": "<<bound_<<",\n";
        f<<"  \"status\": \"COMPLETE\",\n";
        f<<"  \"prepared_input_sha256\": \""<<p_.input_sha<<"\",\n";
        f<<"  \"stable_aut_content_sha256\": \""<<s_.aut_sha<<"\",\n";
        f<<"  \"canonical_bundle_sha256\": \""<<s_.bundle_sha<<"\",\n";
        f<<"  \"aut_group_order\": "<<s_.group_order<<",\n";
        f<<"  \"dfs_symmetry_breaker_count\": "<<s_.k<<",\n";
        f<<"  \"exact_ldl_reconstructs_integer_gram\": true,\n";
        f<<"  \"floating_arithmetic_used_for_traversal_pruning\": false,\n";
        f<<"  \"floating_arithmetic_used_only_to_schedule_exact_prune_checks\": true,\n";
        f<<"  \"all_cap_branch_rejections_exact_rational_cauchy_schwarz\": true,\n";
        f<<"  \"symmetry_breakers_evaluated_only_by_exact_integer_leaf_tests\": true,\n";
        f<<"  \"norm_ball_coordinate_ranges_are_exact_rational_supersets\": true,\n";
        f<<"  \"every_candidate_coordinate_is_exactly_norm_checked_before_descent\": true,\n";
        f<<"  \"nodes\": "<<nodes_<<",\n";
        f<<"  \"coordinate_trials\": "<<trials_<<",\n";
        f<<"  \"exact_prune_checks\": "<<exact_prune_checks_<<",\n";
        f<<"  \"exact_constraint_prunes\": "<<constraint_prunes_<<",\n";
        f<<"  \"exact_symmetry_prunes\": 0,\n";
        f<<"  \"exact_norm_leaves\": "<<leaves_<<",\n";
        f<<"  \"cap_survivors_before_symmetry\": "<<cap_survivors_<<",\n";
        f<<"  \"precanonical_survivors\": "<<precanonical_<<",\n";
        f<<"  \"canonical_rejects\": "<<canonical_rejects_<<",\n";
        f<<"  \"canonical_survivors_including_zero\": "<<canonical_<<",\n";
        f<<"  \"canonical_nonzero_survivors\": "<<canonical_nonzero_<<",\n";
        f<<"  \"canonical_norm_histogram\": {";
        bool first=true; for(auto [k,v]:hist_){ if(!first) f<<","; first=false; f<<"\""<<k<<"\":"<<v; } f<<"},\n";
        f<<"  \"TRAVERSAL_COMPLETENESS_CERTIFICATE\": true,\n";
        f<<"  \"THEOREM_CREDIT\": false,\n  \"RECEIVER_CREDIT\": false,\n  \"FULL_D16_G0_ROW_COMPLETE\": false\n}\n";
    }

private:
    const Problem&p_; const Bundle&s_; int n_,m_,bound_=0; uint64_t node_cap_=0;
    std::vector<std::vector<cpp_rational>> L_; std::vector<cpp_rational>D_;
    std::vector<std::vector<cpp_rational>> cap_a_,cap_dual_;
    std::vector<std::vector<long double>> cap_af_,cap_dualf_;
    std::vector<long long>z_; std::vector<cpp_rational>t_; std::vector<long double>tf_;
    std::vector<long double>cap_assignedf_; std::vector<int>order_;
    uint64_t nodes_=0,trials_=0,leaves_=0,cap_survivors_=0,precanonical_=0,canonical_rejects_=0,canonical_=0,canonical_nonzero_=0;
    uint64_t exact_prune_checks_=0,constraint_prunes_=0;
    std::map<int,uint64_t>hist_; std::ofstream*dump_=nullptr;

    void build_dual_row(const std::vector<long long>& row,
                        std::vector<cpp_rational>& a,std::vector<cpp_rational>& dual,
                        std::vector<long double>& af,std::vector<long double>& dualf){
        cpp_rational sum=0;
        for(int i=0;i<n_;i++){
            cpp_rational v=row[i];
            for(int k=0;k<i;k++) v-=L_[i][k]*a[k];
            a[i]=v; sum += a[i]*a[i]/D_[i]; dual[i]=sum;
            af[i]=a[i].convert_to<long double>(); dualf[i]=sum.convert_to<long double>();
        }
    }

    cpp_rational exact_center(long long base,const std::vector<cpp_rational>& a,int last_remaining) const {
        cpp_rational c=base;
        for(int j=last_remaining+1;j<n_;j++) c+=a[j]*t_[j];
        return c;
    }

    bool exact_outside_interval_impossible(long long base,long long cap,
                                           const std::vector<cpp_rational>& a,
                                           const std::vector<cpp_rational>& dual,
                                           int last_remaining,const cpp_rational& budget) {
        ++exact_prune_checks_;
        cpp_rational center=exact_center(base,a,last_remaining), dist=0;
        if(center<0) dist=-center;
        else if(center>cpp_rational(cap)) dist=center-cpp_rational(cap);
        else return false;
        cpp_rational reach2 = last_remaining>=0 ? budget*dual[last_remaining] : cpp_rational(0);
        return dist*dist > reach2;
    }

    bool caps_possible(int last_remaining,const cpp_rational& budget) {
        const long double bf=std::max<long double>(0,budget.convert_to<long double>());
        for(int rr:order_){
            long double center=static_cast<long double>(p_.p0[rr])+cap_assignedf_[rr], dist=0;
            if(center<0) dist=-center;
            else if(center>static_cast<long double>(p_.cap[rr])) dist=center-static_cast<long double>(p_.cap[rr]);
            else continue;
            long double dual=last_remaining>=0?cap_dualf_[rr][last_remaining]:0;
            long double reach=std::sqrt(std::max<long double>(0,bf*dual));
            if(reach==0 || dist>0.5L*reach){
                if(exact_outside_interval_impossible(p_.p0[rr],p_.cap[rr],cap_a_[rr],cap_dual_[rr],last_remaining,budget)){
                    ++constraint_prunes_; return false;
                }
            }
        }
        return true;
    }

    bool is_canonical(const std::array<unsigned char,140>& pairing)const{
        i128 base=0; for(int i=0;i<m_;i++) base+=static_cast<i128>(s_.weights[i])*static_cast<int>(pairing[i]);
        std::array<unsigned char,140> transformed{};
        for(const auto&p:s_.group){
            i128 score=0; for(int old=0;old<m_;old++) score+=static_cast<i128>(s_.weights[p[old]])*static_cast<int>(pairing[old]);
            if(score<base) return false;
            if(score!=base) continue;
            transformed.fill(0); for(int old=0;old<m_;old++) transformed[p[old]]=pairing[old];
            if(std::lexicographical_compare(transformed.begin(),transformed.end(),pairing.begin(),pairing.end())) return false;
        }
        return true;
    }

    void dfs(int i,const cpp_rational& used){
        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded");
        if(i<0){ exact_leaf(); return; }
        cpp_rational rem=cpp_rational(bound_)-used; if(rem<0) return;
        cpp_rational shift=0; for(int j=i+1;j<n_;j++) shift+=L_[j][i]*z_[j];
        cpp_rational ratio=rem/D_[i]; if(ratio<0) return;
        long long R=0; while(cpp_rational(R)*R<=ratio) ++R;
        long long lo=ceil_rat(-shift-cpp_rational(R)), hi=floor_rat(-shift+cpp_rational(R));
        for(long long zi=lo;zi<=hi;zi++){
            ++trials_; cpp_rational ti=cpp_rational(zi)+shift; cpp_rational term=D_[i]*ti*ti;
            if(term>rem) continue;
            z_[i]=zi; t_[i]=ti; tf_[i]=ti.convert_to<long double>();
            for(int r=0;r<m_;r++) cap_assignedf_[r]+=cap_af_[r][i]*tf_[i];
            cpp_rational newrem=rem-term;
            if(caps_possible(i-1,newrem)) dfs(i-1,used+term);
            for(int r=0;r<m_;r++) cap_assignedf_[r]-=cap_af_[r][i]*tf_[i];
            t_[i]=0; tf_[i]=0;
        }
        z_[i]=0;
    }

    void exact_leaf(){
        ++leaves_;
        i128 norm=0; for(int i=0;i<n_;i++) for(int j=0;j<n_;j++) norm+=static_cast<i128>(z_[i])*p_.q[i][j]*static_cast<i128>(z_[j]);
        if(norm<0||norm>bound_) throw std::runtime_error("exact norm traversal inconsistency");
        std::array<unsigned char,140> pairing{};
        for(int r=0;r<m_;r++){
            i128 v=p_.p0[r]; for(int j=0;j<n_;j++) v+=static_cast<i128>(p_.lin[r][j])*z_[j];
            if(v<0||v>p_.cap[r]) return;
            pairing[r]=static_cast<unsigned char>(static_cast<int>(v));
        }
        ++cap_survivors_;
        for(int r=0;r<s_.k;r++){
            i128 v=s_.c0[r]; for(int j=0;j<n_;j++) v+=static_cast<i128>(s_.lin[r][j])*z_[j];
            if(v<0) return;
        }
        ++precanonical_;
        if(!is_canonical(pairing)){ ++canonical_rejects_; return; }
        ++canonical_; int ni=static_cast<int>(norm); if(ni) ++canonical_nonzero_; hist_[ni]++;
        unsigned char nb=static_cast<unsigned char>(ni); dump_->write(reinterpret_cast<const char*>(&nb),1); dump_->write(reinterpret_cast<const char*>(pairing.data()),pairing.size());
        if(!*dump_) throw std::runtime_error("dump write failed");
    }
};

int main(int argc,char**argv){
    try{
        std::string input,bundle,output,dump; int bound=6; uint64_t node_cap=100000000ULL;
        for(int i=1;i<argc;i++){
            std::string a=argv[i]; auto need=[&](){ if(++i>=argc) throw std::runtime_error("missing arg"); return std::string(argv[i]); };
            if(a=="--input") input=need(); else if(a=="--bundle") bundle=need(); else if(a=="--output") output=need(); else if(a=="--dump-canonical") dump=need(); else if(a=="--bound") bound=std::stoi(need()); else if(a=="--node-cap") node_cap=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);
        }
        if(input.empty()||bundle.empty()||output.empty()||dump.empty()) throw std::runtime_error("required args missing");
        if(bound!=6) throw std::runtime_error("Stage32-18A certifier is intentionally locked to b6");
        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump); e.write_json(output); return 0;
    }catch(const std::exception&e){ std::cerr<<"ERROR: "<<e.what()<<"\n"; return 1; }
}
