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

struct Problem {
    int n = 0, m = 0;
    std::string core_sha, source_blob, input_sha;
    std::vector<std::vector<long long>> q;
    std::vector<long long> p0, cap;
    std::vector<std::vector<long long>> lin;
};

static Problem load_problem(const std::string& path) {
    std::ifstream f(path);
    if (!f) throw std::runtime_error("cannot open Hperp input");
    std::string magic;
    std::getline(f, magic);
    if (magic != "S32_D16_AUT_CANON_HPERP_V1") throw std::runtime_error("bad Hperp magic");
    Problem p;
    std::getline(f, p.core_sha);
    std::getline(f, p.source_blob);
    std::getline(f, p.input_sha);
    f >> p.n >> p.m;
    if (p.n != 63 || p.m != 140) throw std::runtime_error("unexpected Hperp dimensions");
    p.q.assign(p.n, std::vector<long long>(p.n));
    for (int i=0;i<p.n;i++) for (int j=0;j<p.n;j++) f >> p.q[i][j];
    p.p0.resize(p.m); p.cap.resize(p.m);
    p.lin.assign(p.m, std::vector<long long>(p.n));
    for (int r=0;r<p.m;r++) {
        f >> p.p0[r] >> p.cap[r];
        for (int j=0;j<p.n;j++) f >> p.lin[r][j];
    }
    if (!f) throw std::runtime_error("truncated Hperp input");
    return p;
}

struct CanonicalBundle {
    int n = 0, m = 0, k = 0, group_order = 0;
    std::string input_sha, aut_sha, bundle_sha, seed;
    std::vector<long long> weights, c0;
    std::vector<std::vector<long long>> lin;
    std::vector<std::array<unsigned char,140>> group;
};

static CanonicalBundle load_bundle(const std::string& path, const Problem& p) {
    std::ifstream f(path);
    if (!f) throw std::runtime_error("cannot open Aut canonical bundle");
    std::string magic;
    std::getline(f, magic);
    if (magic != "S32_D16_AUT_CANONICAL_BUNDLE_V1") throw std::runtime_error("bad bundle magic");
    CanonicalBundle s;
    std::getline(f, s.input_sha);
    std::getline(f, s.aut_sha);
    std::getline(f, s.bundle_sha);
    std::getline(f, s.seed);
    f >> s.n >> s.m >> s.k >> s.group_order;
    if (s.input_sha != p.input_sha) throw std::runtime_error("bundle/Hperp input SHA mismatch");
    if (s.n != p.n || s.m != p.m || s.k != 64 || s.group_order != 1536)
        throw std::runtime_error("unexpected canonical bundle dimensions");
    s.weights.resize(s.m);
    for (int i=0;i<s.m;i++) f >> s.weights[i];
    s.c0.resize(s.k);
    s.lin.assign(s.k, std::vector<long long>(s.n));
    for (int r=0;r<s.k;r++) {
        f >> s.c0[r];
        for (int j=0;j<s.n;j++) f >> s.lin[r][j];
    }
    s.group.resize(s.group_order);
    for (int g=0;g<s.group_order;g++) {
        std::array<bool,140> seen{};
        for (int i=0;i<s.m;i++) {
            int x; f >> x;
            if (x < 0 || x >= s.m || seen[x]) throw std::runtime_error("bad Aut permutation in bundle");
            seen[x] = true;
            s.group[g][i] = static_cast<unsigned char>(x);
        }
    }
    if (!f) throw std::runtime_error("truncated canonical bundle");
    return s;
}

struct TierResult {
    int bound = 0;
    std::string status = "COMPLETE";
    uint64_t nodes = 0, coordinate_trials = 0, constraint_prunes = 0, symmetry_prunes = 0;
    uint64_t leaves = 0, precanonical_survivors = 0, canonical_rejects = 0;
    uint64_t canonical_survivors = 0, canonical_nonzero = 0;
    uint64_t checksum = 1469598103934665603ULL;
    double seconds = 0.0;
    std::array<uint64_t,35> norm_hist{};
};

class Enumerator {
public:
    Enumerator(const Problem& p, const CanonicalBundle& s): p_(p), s_(s), n_(p.n), m_(p.m) {
        l_.assign(n_, std::vector<long double>(n_, 0));
        d_.assign(n_, 0);
        for (int i=0;i<n_;i++) {
            l_[i][i] = 1;
            long double di = static_cast<long double>(p_.q[i][i]);
            for (int k=0;k<i;k++) di -= l_[i][k]*l_[i][k]*d_[k];
            if (!(di > 0)) throw std::runtime_error("LDL lost positive definiteness");
            d_[i] = di;
            for (int j=i+1;j<n_;j++) {
                long double v = static_cast<long double>(p_.q[j][i]);
                for (int k=0;k<i;k++) v -= l_[j][k]*l_[i][k]*d_[k];
                l_[j][i] = v / d_[i];
            }
        }

        a_.assign(m_, std::vector<long double>(n_, 0));
        remdual_.assign(m_, std::vector<long double>(n_, 0));
        for (int r=0;r<m_;r++) build_dual_row(p_.lin[r], a_[r], remdual_[r]);

        sa_.assign(s_.k, std::vector<long double>(n_, 0));
        sremdual_.assign(s_.k, std::vector<long double>(n_, 0));
        for (int r=0;r<s_.k;r++) build_dual_row(s_.lin[r], sa_[r], sremdual_[r]);

        order_.reserve(m_);
        for (int r=92;r<m_;r++) order_.push_back(r);
        for (int r=0;r<92;r++) order_.push_back(r);
        z_.assign(n_,0);
        assigned_.assign(m_,0);
        sassigned_.assign(s_.k,0);
    }

    TierResult run(int bound, double max_seconds, uint64_t node_cap, uint64_t survivor_cap,
                   std::ofstream* canonical_dump=nullptr) {
        bound_ = bound; max_seconds_=max_seconds; node_cap_=node_cap; survivor_cap_=survivor_cap;
        dump_=canonical_dump;
        result_ = TierResult{}; result_.bound=bound;
        std::fill(z_.begin(),z_.end(),0);
        std::fill(assigned_.begin(),assigned_.end(),0);
        std::fill(sassigned_.begin(),sassigned_.end(),0);
        stop_=false;
        started_=Clock::now();
        long double budget=static_cast<long double>(bound_);
        if (caps_possible(n_-1,budget) && symmetry_possible(n_-1,budget)) dfs(n_-1,0.0L);
        result_.seconds=std::chrono::duration<double>(Clock::now()-started_).count();
        return result_;
    }

private:
    const Problem& p_;
    const CanonicalBundle& s_;
    int n_,m_,bound_=0;
    std::vector<std::vector<long double>> l_,a_,remdual_,sa_,sremdual_;
    std::vector<long double> d_,assigned_,sassigned_;
    std::vector<long long> z_;
    std::vector<int> order_;
    TierResult result_;
    bool stop_=false;
    double max_seconds_=0;
    uint64_t node_cap_=0,survivor_cap_=0;
    Clock::time_point started_;
    std::ofstream* dump_=nullptr;

    void build_dual_row(const std::vector<long long>& row,
                        std::vector<long double>& ar,
                        std::vector<long double>& rem) {
        for (int i=0;i<n_;i++) {
            long double v=static_cast<long double>(row[i]);
            for (int k=0;k<i;k++) v -= l_[i][k]*ar[k];
            ar[i]=v;
        }
        long double sum=0;
        for (int i=0;i<n_;i++) {
            sum += ar[i]*ar[i]/d_[i];
            rem[i]=sum;
        }
    }

    bool limits() {
        if (stop_) return true;
        if (result_.nodes >= node_cap_) { result_.status="NODE_CAP"; stop_=true; return true; }
        if (result_.canonical_survivors >= survivor_cap_) { result_.status="SURVIVOR_CAP"; stop_=true; return true; }
        if ((result_.nodes & 16383ULL)==0) {
            double sec=std::chrono::duration<double>(Clock::now()-started_).count();
            if (sec >= max_seconds_) { result_.status="TIMEOUT"; stop_=true; return true; }
        }
        return false;
    }

    bool caps_possible(int last_remaining, long double budget) const {
        if (budget < 0) budget=0;
        for (int rr: order_) {
            long double center=static_cast<long double>(p_.p0[rr])+assigned_[rr];
            long double dist=0;
            if (center < 0) dist=-center;
            else if (center > static_cast<long double>(p_.cap[rr])) dist=center-static_cast<long double>(p_.cap[rr]);
            if (dist==0) continue;
            long double dual = last_remaining>=0 ? remdual_[rr][last_remaining] : 0;
            long double reach=std::sqrt(std::max(static_cast<long double>(0),budget*dual));
            long double guard=1e-8L*(1.0L+std::fabs(center)+reach);
            if (dist > reach+guard) return false;
        }
        return true;
    }

    bool symmetry_possible(int last_remaining, long double budget) const {
        if (budget < 0) budget=0;
        for (int r=0;r<s_.k;r++) {
            long double center=static_cast<long double>(s_.c0[r])+sassigned_[r];
            if (center >= 0) continue;
            long double dual = last_remaining>=0 ? sremdual_[r][last_remaining] : 0;
            long double reach=std::sqrt(std::max(static_cast<long double>(0),budget*dual));
            long double guard=1e-8L*(1.0L+std::fabs(center)+reach);
            if (-center > reach+guard) return false;
        }
        return true;
    }

    void dfs(int i, long double used) {
        result_.nodes++;
        if (limits()) return;
        if (i < 0) { exact_leaf(); return; }
        long double rem=static_cast<long double>(bound_)-used;
        if (rem < -1e-10L) return;
        if (rem < 0) rem=0;
        long double shift=0;
        for (int j=i+1;j<n_;j++) shift += l_[j][i]*static_cast<long double>(z_[j]);
        long double radius=std::sqrt(std::max(static_cast<long double>(0),rem/d_[i]));
        long double pad=1e-9L*(1.0L+std::fabs(shift)+radius);
        long long lo=static_cast<long long>(std::ceil(-shift-radius-pad));
        long long hi=static_cast<long long>(std::floor(-shift+radius+pad));
        for (long long zi=lo;zi<=hi;zi++) {
            if (stop_) return;
            result_.coordinate_trials++;
            long double ti=static_cast<long double>(zi)+shift;
            long double newused=used+d_[i]*ti*ti;
            if (newused > static_cast<long double>(bound_)+1e-8L) continue;
            z_[i]=zi;
            for (int r=0;r<m_;r++) assigned_[r]+=a_[r][i]*ti;
            for (int r=0;r<s_.k;r++) sassigned_[r]+=sa_[r][i]*ti;
            long double newrem=static_cast<long double>(bound_)-newused;
            if (!caps_possible(i-1,newrem)) {
                result_.constraint_prunes++;
            } else if (!symmetry_possible(i-1,newrem)) {
                result_.symmetry_prunes++;
            } else {
                dfs(i-1,newused);
            }
            for (int r=0;r<s_.k;r++) sassigned_[r]-=sa_[r][i]*ti;
            for (int r=0;r<m_;r++) assigned_[r]-=a_[r][i]*ti;
        }
        z_[i]=0;
    }

    bool is_canonical(const std::array<unsigned char,140>& pairing) const {
        i128 base_score=0;
        for (int i=0;i<m_;i++) base_score += static_cast<i128>(s_.weights[i]) * static_cast<int>(pairing[i]);
        std::array<unsigned char,140> transformed{};
        for (const auto& p: s_.group) {
            i128 score=0;
            for (int old=0;old<m_;old++)
                score += static_cast<i128>(s_.weights[p[old]]) * static_cast<int>(pairing[old]);
            if (score < base_score) return false;
            if (score != base_score) continue;
            transformed.fill(0);
            for (int old=0;old<m_;old++) transformed[p[old]]=pairing[old];
            if (std::lexicographical_compare(transformed.begin(), transformed.end(), pairing.begin(), pairing.end()))
                return false;
        }
        return true;
    }

    void exact_leaf() {
        result_.leaves++;
        i128 norm=0;
        for (int i=0;i<n_;i++) for (int j=0;j<n_;j++)
            norm += static_cast<i128>(z_[i])*static_cast<i128>(p_.q[i][j])*static_cast<i128>(z_[j]);
        if (norm < 0 || norm > bound_) return;
        std::array<unsigned char,140> pairing{};
        for (int r=0;r<m_;r++) {
            i128 v=p_.p0[r];
            for (int j=0;j<n_;j++) v += static_cast<i128>(p_.lin[r][j])*static_cast<i128>(z_[j]);
            if (v < 0 || v > p_.cap[r]) return;
            pairing[r]=static_cast<unsigned char>(static_cast<int>(v));
        }
        for (int r=0;r<s_.k;r++) {
            i128 v=s_.c0[r];
            for (int j=0;j<n_;j++) v += static_cast<i128>(s_.lin[r][j])*static_cast<i128>(z_[j]);
            if (v < 0) return;
        }
        result_.precanonical_survivors++;
        if (!is_canonical(pairing)) {
            result_.canonical_rejects++;
            return;
        }
        result_.canonical_survivors++;
        if (norm != 0) result_.canonical_nonzero++;
        int ni=static_cast<int>(norm);
        if (0<=ni && ni<35) result_.norm_hist[ni]++;
        if (dump_) {
            unsigned char nb=static_cast<unsigned char>(ni);
            dump_->write(reinterpret_cast<const char*>(&nb),1);
            dump_->write(reinterpret_cast<const char*>(pairing.data()),pairing.size());
            if (!*dump_) throw std::runtime_error("canonical dump write failed");
        }
        for (long long v:z_) {
            uint64_t x=static_cast<uint64_t>(v);
            for (int b=0;b<8;b++) { result_.checksum ^= (x>>(8*b))&255ULL; result_.checksum *= 1099511628211ULL; }
        }
    }
};

int main(int argc,char**argv) {
    try {
        std::string input,bundle,output,dump_path;
        int bound=6;
        double max_seconds=30.0;
        uint64_t node_cap=10000000ULL,survivor_cap=100000ULL;
        for (int i=1;i<argc;i++) {
            std::string a=argv[i];
            auto need=[&](){ if (++i>=argc) throw std::runtime_error("missing argument"); return std::string(argv[i]); };
            if (a=="--input") input=need();
            else if (a=="--bundle") bundle=need();
            else if (a=="--output") output=need();
            else if (a=="--bound") bound=std::stoi(need());
            else if (a=="--max-seconds") max_seconds=std::stod(need());
            else if (a=="--node-cap") node_cap=std::stoull(need());
            else if (a=="--survivor-cap") survivor_cap=std::stoull(need());
            else if (a=="--dump-canonical") dump_path=need();
            else throw std::runtime_error("unknown arg "+a);
        }
        if (input.empty()||bundle.empty()||output.empty()) throw std::runtime_error("--input/--bundle/--output required");
        if (bound < 0 || bound > 34) throw std::runtime_error("bound outside Stage32 d16 implementation window");

        Problem p=load_problem(input);
        CanonicalBundle s=load_bundle(bundle,p);
        Enumerator en(p,s);
        std::ofstream dump;
        if (!dump_path.empty()) {
            dump.open(dump_path,std::ios::binary);
            if (!dump) throw std::runtime_error("cannot open canonical dump");
            dump.write("S32D16C1",8);
        }
        TierResult r=en.run(bound,max_seconds,node_cap,survivor_cap,dump_path.empty()?nullptr:&dump);
        if (dump.is_open()) { dump.close(); if (!dump) throw std::runtime_error("canonical dump close failed"); }

        std::cerr << "bound="<<bound<<" status="<<r.status<<" nodes="<<r.nodes
                  <<" precanonical="<<r.precanonical_survivors<<" canonical="<<r.canonical_survivors
                  <<" canonical_rejects="<<r.canonical_rejects<<" sym_prunes="<<r.symmetry_prunes
                  <<" sec="<<r.seconds<<"\n";

        std::ofstream f(output);
        if (!f) throw std::runtime_error("cannot open output");
        f << "{\n";
        f << "  \"schema\": \"STAGE32_18_D16_AUT_CANONICAL_ENUM_V1\",\n";
        f << "  \"scope\": \"MAIN_IMPLEMENTATION_CHECKPOINT_NO_NUMERICAL_ROW_CREDIT\",\n";
        f << "  \"source_core_canonical_sha256\": \""<<p.core_sha<<"\",\n";
        f << "  \"source_blob_sha1\": \""<<p.source_blob<<"\",\n";
        f << "  \"prepared_input_sha256\": \""<<p.input_sha<<"\",\n";
        f << "  \"aut_canonical_sha256\": \""<<s.aut_sha<<"\",\n";
        f << "  \"canonical_bundle_sha256\": \""<<s.bundle_sha<<"\",\n";
        f << "  \"canonical_seed\": \""<<s.seed<<"\",\n";
        f << "  \"aut_group_order\": "<<s.group_order<<",\n";
        f << "  \"dfs_symmetry_breaker_count\": "<<s.k<<",\n";
        f << "  \"canonical_rule\": \"MIN_EXACT_SHA_SCORE_THEN_LEX_PAIRING_OVER_FULL_AUT_ORBIT\",\n";
        f << "  \"pairing_injectivity_required\": true,\n";
        f << "  \"floating_reach_pruning_completeness_audit_pending\": true,\n";
        f << "  \"bound\": "<<r.bound<<",\n";
        f << "  \"status\": \""<<r.status<<"\",\n";
        f << "  \"nodes\": "<<r.nodes<<",\n";
        f << "  \"coordinate_trials\": "<<r.coordinate_trials<<",\n";
        f << "  \"constraint_prunes\": "<<r.constraint_prunes<<",\n";
        f << "  \"symmetry_prunes\": "<<r.symmetry_prunes<<",\n";
        f << "  \"exact_leaves\": "<<r.leaves<<",\n";
        f << "  \"precanonical_survivors\": "<<r.precanonical_survivors<<",\n";
        f << "  \"canonical_rejects\": "<<r.canonical_rejects<<",\n";
        f << "  \"canonical_survivors_including_zero\": "<<r.canonical_survivors<<",\n";
        f << "  \"canonical_nonzero_survivors\": "<<r.canonical_nonzero<<",\n";
        f << "  \"elapsed_seconds\": "<<std::fixed<<std::setprecision(6)<<r.seconds<<",\n";
        f << "  \"canonical_survivor_checksum_fnv64\": \""<<std::hex<<r.checksum<<std::dec<<"\",\n";
        f << "  \"canonical_norm_histogram\": {";
        bool first=true;
        for (int n=0;n<35;n++) if (r.norm_hist[n]) { if(!first)f<<","; first=false; f<<"\""<<n<<"\":"<<r.norm_hist[n]; }
        f << "},\n";
        f << "  \"THEOREM_CREDIT\": false,\n";
        f << "  \"RECEIVER_CREDIT\": false,\n";
        f << "  \"FULL_D16_G0_ROW_COMPLETE\": false,\n";
        f << "  \"FULL_D176_D192_NUMERICAL_ORBIT_CENSUS\": false,\n";
        f << "  \"R29_LG2_NUMERICAL_COMPONENT_COMPLETE\": false,\n";
        f << "  \"R29_LG2\": \"NOT_DISCHARGED\",\n";
        f << "  \"G10_LOWGENUS_PICARD\": \"AMBER\"\n";
        f << "}\n";
        return r.status=="COMPLETE" ? 0 : 2;
    } catch (const std::exception& e) {
        std::cerr << "ERROR: "<<e.what()<<"\n";
        return 1;
    }
}
