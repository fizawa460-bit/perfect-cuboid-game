#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using i128 = __int128_t;
using Clock = std::chrono::steady_clock;

static std::string i128s(i128 x) {
    if (x == 0) return "0";
    bool neg = x < 0;
    if (neg) x = -x;
    std::string s;
    while (x) { s.push_back(char('0' + int(x % 10))); x /= 10; }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

struct Problem {
    int n = 0, m = 0;
    std::string core_sha, source_blob, input_sha;
    std::vector<std::vector<long long>> q;
    std::vector<long long> p0, cap;
    std::vector<std::vector<long long>> lin;
};

static Problem load_problem(const std::string& path) {
    std::ifstream f(path);
    if (!f) throw std::runtime_error("cannot open input");
    std::string magic;
    std::getline(f, magic);
    if (magic != "S32_D16_CONSTRAINED_HPERP_V1") throw std::runtime_error("bad magic");
    Problem p;
    std::getline(f, p.core_sha);
    std::getline(f, p.source_blob);
    std::getline(f, p.input_sha);
    f >> p.n >> p.m;
    if (p.n != 63 || p.m != 140) throw std::runtime_error("unexpected dimensions");
    p.q.assign(p.n, std::vector<long long>(p.n));
    for (int i=0;i<p.n;i++) for (int j=0;j<p.n;j++) f >> p.q[i][j];
    p.p0.resize(p.m); p.cap.resize(p.m);
    p.lin.assign(p.m, std::vector<long long>(p.n));
    for (int r=0;r<p.m;r++) {
        f >> p.p0[r] >> p.cap[r];
        for (int j=0;j<p.n;j++) f >> p.lin[r][j];
    }
    if (!f) throw std::runtime_error("truncated input");
    return p;
}

struct TierResult {
    int bound = 0;
    std::string status = "COMPLETE";
    uint64_t nodes = 0, coordinate_trials = 0, constraint_prunes = 0;
    uint64_t leaves = 0, exact_survivors = 0, nonzero_survivors = 0;
    uint64_t checksum = 1469598103934665603ULL;
    double seconds = 0.0;
    std::array<uint64_t,35> norm_hist{};
};

class Enumerator {
public:
    explicit Enumerator(const Problem& p): p_(p), n_(p.n), m_(p.m) {
        l_.assign(n_, std::vector<long double>(n_, 0));
        d_.assign(n_, 0);
        // Numeric LDL^T of the exact, LLL-reduced positive definite Gram matrix.
        for (int i=0;i<n_;i++) {
            l_[i][i] = 1;
            long double di = (long double)p_.q[i][i];
            for (int k=0;k<i;k++) di -= l_[i][k]*l_[i][k]*d_[k];
            if (!(di > 0)) throw std::runtime_error("LDL lost positive definiteness");
            d_[i] = di;
            for (int j=i+1;j<n_;j++) {
                long double v = (long double)p_.q[j][i];
                for (int k=0;k<i;k++) v -= l_[j][k]*l_[i][k]*d_[k];
                l_[j][i] = v / d_[i];
            }
        }

        // a = L^{-1} lin, so lin.z = a.t for t=L^T z.
        a_.assign(m_, std::vector<long double>(n_, 0));
        remdual_.assign(m_, std::vector<long double>(n_, 0));
        for (int r=0;r<m_;r++) {
            for (int i=0;i<n_;i++) {
                long double v = (long double)p_.lin[r][i];
                for (int k=0;k<i;k++) v -= l_[i][k]*a_[r][k];
                a_[r][i] = v;
            }
            long double s=0;
            for (int i=0;i<n_;i++) {
                s += a_[r][i]*a_[r][i]/d_[i];
                remdual_[r][i]=s;
            }
        }
        order_.reserve(m_);
        for (int r=92;r<m_;r++) order_.push_back(r); // tighter exceptional caps first
        for (int r=0;r<92;r++) order_.push_back(r);
        z_.assign(n_,0);
        t_.assign(n_,0);
        assigned_.assign(m_,0);
    }

    TierResult run(int bound, double max_seconds, uint64_t node_cap, uint64_t survivor_cap,
                   std::ofstream* survivor_dump=nullptr) {
        bound_ = bound; max_seconds_=max_seconds; node_cap_=node_cap; survivor_cap_=survivor_cap;
        dump_=survivor_dump;
        result_ = TierResult{}; result_.bound=bound;
        std::fill(z_.begin(),z_.end(),0);
        std::fill(t_.begin(),t_.end(),0);
        std::fill(assigned_.begin(),assigned_.end(),0);
        stop_=false;
        started_=Clock::now();
        if (constraints_possible(n_-1,(long double)bound_)) dfs(n_-1,0.0L);
        result_.seconds=std::chrono::duration<double>(Clock::now()-started_).count();
        return result_;
    }

private:
    const Problem& p_; int n_,m_,bound_=0;
    std::vector<std::vector<long double>> l_,a_,remdual_;
    std::vector<long double> d_,t_,assigned_;
    std::vector<long long> z_;
    std::vector<int> order_;
    TierResult result_;
    bool stop_=false;
    double max_seconds_=0; uint64_t node_cap_=0,survivor_cap_=0;
    Clock::time_point started_;
    std::ofstream* dump_=nullptr;

    bool limits() {
        if (stop_) return true;
        if (result_.nodes >= node_cap_) { result_.status="NODE_CAP"; stop_=true; return true; }
        if (result_.exact_survivors >= survivor_cap_) { result_.status="SURVIVOR_CAP"; stop_=true; return true; }
        if ((result_.nodes & 16383ULL)==0) {
            double s=std::chrono::duration<double>(Clock::now()-started_).count();
            if (s >= max_seconds_) { result_.status="TIMEOUT"; stop_=true; return true; }
        }
        return false;
    }

    bool constraints_possible(int last_remaining, long double budget) {
        if (budget < 0) budget=0;
        for (int rr: order_) {
            long double center=(long double)p_.p0[rr]+assigned_[rr];
            long double dist=0;
            if (center < 0) dist=-center;
            else if (center > (long double)p_.cap[rr]) dist=center-(long double)p_.cap[rr];
            if (dist==0) continue;
            long double dual = last_remaining>=0 ? remdual_[rr][last_remaining] : 0;
            long double reach=std::sqrt(std::max((long double)0,budget*dual));
            // Deliberately conservative floating guard: borderline nodes are retained.
            long double guard=1e-8L*(1.0L+std::fabs(center)+reach);
            if (dist > reach+guard) return false;
        }
        return true;
    }

    void dfs(int i, long double used) {
        result_.nodes++;
        if (limits()) return;
        if (i < 0) { exact_leaf(); return; }
        long double rem=(long double)bound_-used;
        if (rem < -1e-10L) return;
        if (rem < 0) rem=0;
        long double shift=0;
        for (int j=i+1;j<n_;j++) shift += l_[j][i]*(long double)z_[j];
        long double radius=std::sqrt(std::max((long double)0,rem/d_[i]));
        long double pad=1e-9L*(1.0L+std::fabs(shift)+radius);
        long long lo=(long long)std::ceil(-shift-radius-pad);
        long long hi=(long long)std::floor(-shift+radius+pad);
        for (long long zi=lo;zi<=hi;zi++) {
            if (stop_) return;
            result_.coordinate_trials++;
            long double ti=(long double)zi+shift;
            long double newused=used+d_[i]*ti*ti;
            if (newused > (long double)bound_+1e-8L) continue;
            z_[i]=zi; t_[i]=ti;
            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;
            long double newrem=(long double)bound_-newused;
            if (constraints_possible(i-1,newrem)) dfs(i-1,newused);
            else result_.constraint_prunes++;
            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;
        }
        z_[i]=0; t_[i]=0;
    }

    void exact_leaf() {
        result_.leaves++;
        i128 norm=0;
        for (int i=0;i<n_;i++) for (int j=0;j<n_;j++)
            norm += (i128)z_[i]*(i128)p_.q[i][j]*(i128)z_[j];
        if (norm < 0 || norm > bound_) return;
        std::array<unsigned char,140> pairing{};
        for (int r=0;r<m_;r++) {
            i128 v=p_.p0[r];
            for (int j=0;j<n_;j++) v += (i128)p_.lin[r][j]*(i128)z_[j];
            if (v < 0 || v > p_.cap[r]) return;
            pairing[r]=(unsigned char)((int)v);
        }
        result_.exact_survivors++;
        if (norm != 0) result_.nonzero_survivors++;
        int ni=(int)norm;
        if (0<=ni && ni<35) result_.norm_hist[ni]++;
        if (dump_) {
            unsigned char nb=(unsigned char)ni;
            dump_->write(reinterpret_cast<const char*>(&nb),1);
            dump_->write(reinterpret_cast<const char*>(pairing.data()),pairing.size());
            if (!*dump_) throw std::runtime_error("survivor dump write failed");
        }
        // Deterministic compact scout checksum, explicitly non-cryptographic.
        for (long long v:z_) {
            uint64_t x=(uint64_t)v;
            for (int b=0;b<8;b++) { result_.checksum ^= (x>>(8*b))&255ULL; result_.checksum *= 1099511628211ULL; }
        }
    }
};

static std::vector<int> parse_bounds(const std::string& s) {
    std::vector<int> v; std::stringstream ss(s); std::string x;
    while (std::getline(ss,x,',')) if (!x.empty()) v.push_back(std::stoi(x));
    if (v.empty()) throw std::runtime_error("empty bounds");
    return v;
}

int main(int argc,char**argv) {
    try {
        std::string input,output,bounds_s="2,4,6,8,12,16,20,26,34",dump_path;
        double per_bound=90.0; uint64_t node_cap=100000000ULL,survivor_cap=5000000ULL;
        for (int i=1;i<argc;i++) {
            std::string a=argv[i];
            auto need=[&](){ if (++i>=argc) throw std::runtime_error("missing argument"); return std::string(argv[i]); };
            if (a=="--input") input=need(); else if (a=="--output") output=need();
            else if (a=="--bounds") bounds_s=need(); else if (a=="--per-bound-seconds") per_bound=std::stod(need());
            else if (a=="--node-cap") node_cap=std::stoull(need()); else if (a=="--survivor-cap") survivor_cap=std::stoull(need());
            else if (a=="--dump-survivors") dump_path=need();
            else throw std::runtime_error("unknown arg "+a);
        }
        if (input.empty()||output.empty()) throw std::runtime_error("--input/--output required");
        Problem p=load_problem(input);
        Enumerator en(p);
        auto bounds=parse_bounds(bounds_s);
        if (!dump_path.empty() && bounds.size()!=1) throw std::runtime_error("survivor dump requires exactly one bound");
        std::ofstream dump;
        if (!dump_path.empty()) {
            dump.open(dump_path,std::ios::binary);
            if (!dump) throw std::runtime_error("cannot open survivor dump");
            dump.write("S32D16V1",8);
        }
        std::vector<TierResult> tiers;
        bool regression_pass=true;
        for (int b:bounds) {
            TierResult r=en.run(b,per_bound,node_cap,survivor_cap,dump_path.empty()?nullptr:&dump);
            tiers.push_back(r);
            std::cerr << "bound="<<b<<" status="<<r.status<<" nodes="<<r.nodes<<" survivors="<<r.exact_survivors<<" nonzero="<<r.nonzero_survivors<<" sec="<<r.seconds<<"\n";
            if (b==2 && !(r.status=="COMPLETE" && r.exact_survivors==49 && r.nonzero_survivors==48)) regression_pass=false;
            if (b==4 && !(r.status=="COMPLETE" && r.exact_survivors==1177 && r.nonzero_survivors==1176)) regression_pass=false;
            if ((b==2||b==4) && !regression_pass) break;
            if (r.status!="COMPLETE") break;
        }
        if (dump.is_open()) { dump.close(); if (!dump) throw std::runtime_error("survivor dump close failed"); }
        std::ofstream f(output);
        if (!f) throw std::runtime_error("cannot open output");
        f << "{\n";
        f << "  \"schema\": \"STAGE32_SCOUT_D16_CONSTRAINED_HPERP_V1\",\n";
        f << "  \"scope\": \"SCOUT_ONLY_NO_CREDIT\",\n";
        f << "  \"source_core_canonical_sha256\": \""<<p.core_sha<<"\",\n";
        f << "  \"source_blob_sha1\": \""<<p.source_blob<<"\",\n";
        f << "  \"prepared_input_sha256\": \""<<p.input_sha<<"\",\n";
        f << "  \"architecture\": {\"direction\": \"H_PERP_COORDINATES_PLUS_140_CAPS_PLUS_NORM_IN_ONE_BRANCH_AND_BOUND\", \"enumerator\": \"CUSTOM_LLL_LDL_FINCKE_POHST_WITH_ELLIPSOID_LINEAR_REACH_PRUNING\", \"floating_pruning_is_scout_only\": true, \"exact_integer_leaf_recheck\": true, \"materialized_branch_count_constructed\": 0, \"exact_pairing_dump_supported\": true},\n";
        f << "  \"regression\": {\"expected_bound2_total_including_zero\": 49, \"expected_bound4_total_including_zero\": 1177, \"pass\": "<<(regression_pass?"true":"false")<<"},\n";
        f << "  \"tiers\": [\n";
        for (size_t k=0;k<tiers.size();k++) {
            auto&r=tiers[k];
            f << "    {\"bound\": "<<r.bound<<", \"status\": \""<<r.status<<"\", \"nodes\": "<<r.nodes<<", \"coordinate_trials\": "<<r.coordinate_trials<<", \"constraint_prunes\": "<<r.constraint_prunes<<", \"exact_leaves\": "<<r.leaves<<", \"exact_survivors_including_zero\": "<<r.exact_survivors<<", \"nonzero_survivors\": "<<r.nonzero_survivors<<", \"elapsed_seconds\": "<<std::fixed<<std::setprecision(6)<<r.seconds<<", \"survivor_checksum_fnv64\": \""<<std::hex<<r.checksum<<std::dec<<"\", \"norm_histogram\": {";
            bool first=true; for (int n=0;n<35;n++) if (r.norm_hist[n]) { if(!first)f<<","; first=false; f<<"\""<<n<<"\":"<<r.norm_hist[n]; }
            f << "}}"<<(k+1<tiers.size()?",":"")<<"\n";
        }
        f << "  ],\n";
        f << "  \"THEOREM_CREDIT\": false,\n  \"RECEIVER_CREDIT\": false,\n  \"FULL_D16_G0_ROW_COMPLETE\": false,\n  \"FULL_D176_D192_NUMERICAL_ORBIT_CENSUS\": false,\n  \"R29_LG2_NUMERICAL_COMPONENT_COMPLETE\": false,\n  \"R29_LG2\": \"NOT_DISCHARGED\",\n  \"G10_LOWGENUS_PICARD\": \"AMBER\"\n}\n";
        if (!regression_pass) return 2;
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "ERROR: "<<e.what()<<"\n";
        return 1;
    }
}
