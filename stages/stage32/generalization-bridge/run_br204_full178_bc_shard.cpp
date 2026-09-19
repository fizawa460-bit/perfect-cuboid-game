// Stage32 BR204 FULL178 durable b-unit producer.
// Heavy-only execution surface. This translation unit reuses the hostile-audited
// bounded BR204 semantics and adds exact per-b global-LP bin emission plus
// qBC K8-tail attribution required by the BR205 transition gate.
#define main br204_bounded_replay_main
#include "verify_br204_compact_mu_bounded_equivalence.cpp"
#undef main

#include <fstream>
#include <sstream>
#include <string>

static constexpr int BR204_H = 96;
static constexpr std::pair<int,int> BR204_D_BANDS[] = {{8,54}, {56,100}, {102,146}, {148,192}};
static constexpr const char* BR204_BASE_BLOB = "b7fc7e0c6c889c92cb152d4e8b54d05d2b71a5d1";

struct WBC {
    Base key;
    std::vector<K8Part> parts;
    i64 total_mult = 0;
    bool has_tail = false; // exact qBC level count > 8; final K8 part is the level-8+ relaxed slot.
};

static std::string arg_value(int argc, char** argv, const std::string& key) {
    for (int i = 1; i + 1 < argc; ++i) {
        if (argv[i] == key) return argv[i + 1];
    }
    return "";
}

static i128 cap_product(i64 a, i64 b, int B) {
    return (i128)a * (i128)b * (i128)B;
}

static i128 obj_product(i64 a, i64 b, int s) {
    return (i128)a * (i128)b * (i128)s;
}

static std::string dec_i128(i128 v) {
    req(v >= 0, "negative i128 serialization");
    if (v == 0) return "0";
    std::string s;
    while (v > 0) {
        int digit = (int)(v % 10);
        s.push_back((char)('0' + digit));
        v /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

int main(int argc, char** argv) {
    if (argc == 2 && std::string(argv[1]) == "--self-test") {
        return br204_bounded_replay_main();
    }

    std::string b_s = arg_value(argc, argv, "--b");
    std::string d_lo_s = arg_value(argc, argv, "--d-lo");
    std::string d_hi_s = arg_value(argc, argv, "--d-hi");
    std::string out_path = arg_value(argc, argv, "--out");
    std::string worker_blob = arg_value(argc, argv, "--worker-blob");
    std::string bc_shard_index_s = arg_value(argc, argv, "--bc-shard-index");
    std::string bc_shard_count_s = arg_value(argc, argv, "--bc-shard-count");
    req(!b_s.empty(), "missing --b");
    req(!d_lo_s.empty() && !d_hi_s.empty(), "missing --d-lo/--d-hi");
    req(!out_path.empty(), "missing --out");
    req(worker_blob.size() == 40, "missing/invalid --worker-blob");
    int only_b = std::stoi(b_s);
    int d_lo = std::stoi(d_lo_s), d_hi = std::stoi(d_hi_s);
    int bc_shard_count = bc_shard_count_s.empty() ? 1 : std::stoi(bc_shard_count_s);
    int bc_shard_index = bc_shard_index_s.empty() ? 0 : std::stoi(bc_shard_index_s);
    req(0 <= only_b && only_b <= BR204_H, "b outside 0..96");
    req(d_lo <= d_hi && (d_lo % 2) == 0 && (d_hi % 2) == 0, "invalid even d range");
    bool approved_band = false;
    for (const auto& band : BR204_D_BANDS)
        if (band.first <= d_lo && d_hi <= band.second) approved_band = true;
    req(approved_band, "d range is not contained in one approved BR204 resume band");
    req(d_hi >= std::max(8, 2 * only_b), "d range has no admissible d for this b");
    req(bc_shard_count >= 1 && bc_shard_count <= 256, "invalid --bc-shard-count");
    req(0 <= bc_shard_index && bc_shard_index < bc_shard_count, "invalid --bc-shard-index");

    auto S = build_strict(BR204_H);
    auto E = build_equal(BR204_H);
    auto P = build_pair(BR204_H);
    auto raw = compact_range(BR204_H, only_b, only_b, S, E, P);
    auto A = build_a(BR204_H);

    std::vector<std::vector<ARec>> A_by_a(BR204_H + 1);
    for (const auto& rec : A) A_by_a[rec.a].push_back(rec);

    std::vector<WBC> BC;
    BC.reserve(raw.size());
    i64 bc_assignment_mass = 0;
    i64 bc_tail_slot_assignment_mass = 0;
    i64 bc_tail_base_states = 0;
    std::size_t raw_index = 0;
    i64 shard_raw_states = 0;
    for (const auto& [key, R] : raw) {
        std::size_t this_index = raw_index++;
        if ((int)(this_index % (std::size_t)bc_shard_count) != bc_shard_index) continue;
        WBC w;
        w.key = key;
        for (const auto& [bits, mult] : R.total) w.total_mult += mult;
        i64 retained_mass = 0;
        for (const auto& [q, by_bits] : R.levels)
            for (const auto& [bits, mult] : by_bits) retained_mass += mult;
        w.has_tail = retained_mass < w.total_mult;
        w.parts = parts_from_retained(R);
        i64 reconstructed = 0;
        for (const auto& p : w.parts) reconstructed += p.total_mult;
        req(reconstructed == w.total_mult, "K8 part reconstruction changed BC mass");
        if (w.has_tail) {
            req(w.parts.size() == 8, "L>8 state without eight K8 parts");
            ++bc_tail_base_states;
            // The last K8 part contains exact level 8 plus all deeper levels, evaluated at q8.
            bc_tail_slot_assignment_mass += w.parts.back().total_mult;
        }
        bc_assignment_mass += w.total_mult;
        BC.push_back(std::move(w));
    }

    using Key = std::pair<int,int>; // (survivor count s, normal-block size B)
    std::map<Key, i128> k8_bins;
    std::map<Key, i128> mu_bins;
    std::map<Key, i128> mu_tail_slot_bins;

    i128 k8_positive_capacity = 0;
    i128 mu_positive_capacity = 0;
    i128 mu_tail_slot_positive_capacity = 0;
    unsigned long long evaluated_state_parts = 0;
    unsigned long long tail_slot_evaluation_cells = 0;

    i128 k8_lgt8_raw_objective = 0;
    i128 k8_tail_slot_raw_objective = 0;
    i128 mu_lgt8_raw_objective = 0;
    i128 mu_tail_slot_raw_objective = 0;
    i128 k8_lgt8_positive_capacity = 0;
    i128 k8_tail_slot_positive_capacity = 0;
    i128 mu_lgt8_positive_capacity = 0;
    i128 mu_tail_slot_positive_capacity_check = 0;

    for (int g : {0, 1}) {
        for (int d = d_lo; d <= d_hi; d += 2) {
            int h = d / 2;
            if (only_b > h) continue;
            int legacy = (g == 0) ? 8 : 4;
            int required_support = ceil_div4(d - 16*g + 16);
            for (const auto& W : BC) {
                const auto& Bc = W.key;
                if (Bc.b != only_b || Bc.b > h || Bc.c > h) continue;
                int c3 = component3(d, Bc.b, Bc.c);
                if (c3 < 0) continue;
                for (int a = 0; a <= h && a <= BR204_H; ++a) {
                    int ca = component_a(d, a);
                    if (ca < 0) continue;
                    int exceptional_mass = a + Bc.b + Bc.c;
                    int support_remainder = std::min(16, d) + ca + c3;
                    for (const auto& AR : A_by_a[a]) {
                        int support = Bc.support + AR.support;
                        int qneed = required_support - support;
                        if (qneed > 0 && support_remainder < qneed) continue;

                        int base_lower = std::max({
                            legacy, required_support, d - 4*g + 4,
                            exceptional_mass,
                            exceptional_mass + std::max(0, qneed)
                        });
                        int upper = std::min({
                            19*d/5, 3*d, 3*d - (Bc.b - Bc.c)
                        });
                        if (base_lower > upper) continue;

                        int excluded1 = -1, excluded2 = -1;
                        int e_n358 = 3*d - (Bc.b - Bc.c);
                        if (Bc.b <= h - 5
                            && support + support_remainder == required_support
                            && e_n358 - exceptional_mass >= support_remainder)
                            excluded1 = e_n358;
                        if (g == 1 && d == 8) excluded2 = 8;

                        for (std::size_t pi = 0; pi < W.parts.size(); ++pi) {
                            const auto& part = W.parts[pi];
                            ++evaluated_state_parts;
                            int q = AR.q + part.q;
                            bool is_lgt8_state = W.has_tail;
                            bool is_tail_slot = W.has_tail && (pi + 1 == W.parts.size());
                            if (is_tail_slot) ++tail_slot_evaluation_cells;

                            int lo0 = (base_lower & 1) ? base_lower + 1 : base_lower;
                            for (int e = lo0; e <= upper; e += 2) {
                                if (e == excluded1 || e == excluded2) continue;
                                int s = one_x4_count(d, g, Bc.t, Bc.r, q, e);
                                if (!s) continue;
                                int block = 19*d - 5*e + 1;
                                req(block > 0, "nonpositive normal block");
                                i128 cap = cap_product(AR.mult, part.total_mult, block);
                                i128 obj = obj_product(AR.mult, part.total_mult, s);
                                k8_bins[{s, block}] += cap;
                                k8_positive_capacity += cap;
                                if (is_lgt8_state) {
                                    k8_lgt8_raw_objective += obj;
                                    k8_lgt8_positive_capacity += cap;
                                }
                                if (is_tail_slot) {
                                    k8_tail_slot_raw_objective += obj;
                                    k8_tail_slot_positive_capacity += cap;
                                }
                            }

                            i64 mu_mass_sum = 0;
                            for (int mu = 0; mu <= 2; ++mu)
                                mu_mass_sum += part.good_mult[AR.syndrome_id][mu];
                            req(mu_mass_sum == part.total_mult, "mu partition changed K8 part mass");

                            for (int mu = 0; mu <= 2; ++mu) {
                                i64 mult = part.good_mult[AR.syndrome_id][mu];
                                if (!mult) continue;
                                int lower = std::max(base_lower, exceptional_mass + mu);
                                int lo = (lower & 1) ? lower + 1 : lower;
                                for (int e = lo; e <= upper; e += 2) {
                                    if (e == excluded1 || e == excluded2) continue;
                                    int s = one_x4_count(d, g, Bc.t, Bc.r, q, e);
                                    if (!s) continue;
                                    int block = 19*d - 5*e + 1;
                                    req(block > 0, "nonpositive normal block");
                                    i128 cap = cap_product(AR.mult, mult, block);
                                    i128 obj = obj_product(AR.mult, mult, s);
                                    mu_bins[{s, block}] += cap;
                                    mu_positive_capacity += cap;
                                    if (is_lgt8_state) {
                                        mu_lgt8_raw_objective += obj;
                                        mu_lgt8_positive_capacity += cap;
                                    }
                                    if (is_tail_slot) {
                                        mu_tail_slot_bins[{s, block}] += cap;
                                        mu_tail_slot_positive_capacity += cap;
                                        mu_tail_slot_raw_objective += obj;
                                        mu_tail_slot_positive_capacity_check += cap;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    req(mu_tail_slot_positive_capacity == mu_tail_slot_positive_capacity_check,
        "tail-slot capacity counter drift");
    for (const auto& [key, cap] : mu_bins) {
        auto it = k8_bins.find(key);
        req(it != k8_bins.end() && cap <= it->second, "mu bin exceeds K8 bin");
    }
    for (const auto& [key, cap] : mu_tail_slot_bins) {
        auto it = mu_bins.find(key);
        req(it != mu_bins.end() && cap <= it->second, "tail-slot bin exceeds mu bin");
    }
    req(mu_lgt8_raw_objective <= k8_lgt8_raw_objective, "mu L>8 raw objective exceeds K8");
    req(mu_tail_slot_raw_objective <= k8_tail_slot_raw_objective, "mu tail-slot raw objective exceeds K8");
    req(mu_lgt8_positive_capacity <= k8_lgt8_positive_capacity, "mu L>8 capacity exceeds K8");
    req(mu_tail_slot_positive_capacity <= k8_tail_slot_positive_capacity, "mu tail-slot capacity exceeds K8");

    std::ofstream out(out_path, std::ios::binary);
    req((bool)out, "cannot open --out");
    out << "META\t" << only_b
        << "\t" << d_lo
        << "\t" << d_hi
        << "\t" << shard_raw_states
        << "\t" << bc_assignment_mass
        << "\t" << bc_tail_slot_assignment_mass
        << "\t" << worker_blob
        << "\t" << BR204_BASE_BLOB
        << "\t" << BR203_MU_TABLE_SHA256
        << "\t" << BR203_TERMINAL_SHA256
        << "\t" << evaluated_state_parts
        << "\n";
    if (bc_shard_count > 1)
        out << "PART\tBC_MOD\t" << bc_shard_index << "\t" << bc_shard_count << "\n";
    for (const auto& [key, cap] : k8_bins)
        out << "K\t" << key.first << "\t" << key.second << "\t" << dec_i128(cap) << "\n";
    for (const auto& [key, cap] : mu_bins) {
        i128 tail = 0;
        auto ti = mu_tail_slot_bins.find(key);
        if (ti != mu_tail_slot_bins.end()) tail = ti->second;
        out << "M\t" << key.first << "\t" << key.second << "\t"
            << dec_i128(cap) << "\t" << dec_i128(tail) << "\n";
    }
    out << "TAIL\t" << bc_tail_base_states
        << "\t" << (shard_raw_states - bc_tail_base_states)
        << "\t" << bc_tail_slot_assignment_mass
        << "\t" << tail_slot_evaluation_cells
        << "\t" << dec_i128(k8_lgt8_raw_objective)
        << "\t" << dec_i128(k8_tail_slot_raw_objective)
        << "\t" << dec_i128(mu_lgt8_raw_objective)
        << "\t" << dec_i128(mu_tail_slot_raw_objective)
        << "\t" << dec_i128(k8_lgt8_positive_capacity)
        << "\t" << dec_i128(k8_tail_slot_positive_capacity)
        << "\t" << dec_i128(mu_lgt8_positive_capacity)
        << "\t" << dec_i128(mu_tail_slot_positive_capacity)
        << "\n";
    out << "SUM\t" << dec_i128(k8_positive_capacity) << "\t"
        << dec_i128(mu_positive_capacity) << "\t"
        << dec_i128(mu_tail_slot_positive_capacity) << "\n";
    out.close();
    req((bool)out, "write failure");

    std::cerr << "BR204_B_UNIT_COMPLETE b=" << only_b
              << " states=" << shard_raw_states
              << " assignments=" << bc_assignment_mass
              << " tail_states=" << bc_tail_base_states
              << " Kbins=" << k8_bins.size()
              << " Mbins=" << mu_bins.size()
              << " bc_shard=" << bc_shard_index << "/" << bc_shard_count
              << "\n";
    return 0;
}
