#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>
#include <utility>
#include <vector>

#include "br203_mu_generated.hpp"

using i64 = long long;
using i128 = __int128_t;
using Syn = Br203Syn;

struct ARec {
    int a;
    int support;
    int q;
    int syndrome_id;
    i64 mult;
};

struct K8Part {
    int q;
    i64 total_mult = 0;
    std::array<std::array<i64, 3>, 8> good_mult{};
};

struct BCBase {
    int b;
    int c;
    int support;
    int t;
    int r;
    std::vector<K8Part> parts;
    i64 total_mult = 0;
};

struct EvalResult {
    i128 br202_k8 = 0;
    i128 br203_mu_k8 = 0;
    int a_refined_states = 0;
    int bc_base_states = 0;
    i64 bc_assignments = 0;
};

static void req(bool ok, const char* msg) {
    if (!ok) {
        std::cerr << "FAIL: " << msg << "\n";
        std::exit(1);
    }
}

static int mu_for(Syn syndrome) {
    for (const auto& entry : BR203_MU_TABLE) {
        if (entry.syndrome == syndrome) return entry.mu;
    }
    return -1;
}

static int ceil_div2(int x) {
    int q = x / 2;
    int rem = x % 2;
    if (rem != 0 && x > 0) ++q;
    return q;
}

static int floor_div2(int x) {
    int q = x / 2;
    int rem = x % 2;
    if (rem != 0 && x < 0) --q;
    return q;
}

static int ceil_div4(int x) {
    return x >= 0 ? (x + 3) / 4 : x / 4;
}

static int component_a(int d, int a) {
    int h = d / 2;
    return std::min({13, d - a, d - 2 * a + 4, h + 5});
}

static int component3(int d, int b, int c) {
    return std::min({9, d - b - c, d - 2 * b, d - 2 * c + 1});
}

static std::vector<ARec> build_a(int H) {
    std::map<std::tuple<int, int, int, int>, i64> hist;
    for (int a = 0; a <= H; ++a) {
        for (int x2 = 0; x2 <= a; ++x2) {
            for (int x3 = 0; x3 <= a - x2; ++x3) {
                int x7 = a - x2 - x3;
                int support = (x2 > 0) + (x3 > 0) + (x7 > 0);
                int q = x2 * x2 + x3 * x3 + x7 * x7;
                int syndrome_id = (x2 & 1) | ((x3 & 1) << 1) | ((x7 & 1) << 2);
                ++hist[{a, support, q, syndrome_id}];
            }
        }
    }

    std::vector<ARec> out;
    out.reserve(hist.size());
    for (const auto& kv : hist) {
        auto [a, support, q, syndrome_id] = kv.first;
        out.push_back({a, support, q, syndrome_id, kv.second});
    }
    return out;
}

static Syn bc_syndrome(
    int x0, int x1, int x5, int x6, int x8, int x9, int x10
) {
    return ((x0 & 1) ? BR203_S_X0 : 0ULL)
         ^ ((x1 & 1) ? BR203_S_X1 : 0ULL)
         ^ ((x5 & 1) ? BR203_S_X5 : 0ULL)
         ^ ((x6 & 1) ? BR203_S_X6 : 0ULL)
         ^ ((x8 & 1) ? BR203_S_X8 : 0ULL)
         ^ ((x9 & 1) ? BR203_S_X9 : 0ULL)
         ^ ((x10 & 1) ? BR203_S_X10 : 0ULL);
}

static K8Part make_part(int q, const std::map<Syn, i64>& by_syndrome) {
    K8Part part;
    part.q = q;
    for (const auto& [bc_syn, mult] : by_syndrome) {
        part.total_mult += mult;
        for (int a_id = 0; a_id < 8; ++a_id) {
            // All 46 syndrome coordinates are 0/4 mod 8, hence negation equals
            // identity and target=-(sigma_A+sigma_BC) is exact XOR here.
            int mu = mu_for(BR203_A_SYNDROMES[a_id] ^ bc_syn);
            if (mu >= 0) part.good_mult[a_id][mu] += mult;
        }
    }
    return part;
}

static std::vector<BCBase> build_bc(int H) {
    using BaseKey = std::tuple<int, int, int, int, int>;
    using SyndromeHist = std::map<Syn, i64>;
    std::map<BaseKey, std::map<int, SyndromeHist>> hist;

    for (int x0 = 0; x0 <= H; ++x0) {
        for (int x1 = x0; x1 <= H; ++x1) {
            for (int x5 = 0; x5 <= H; ++x5) {
                int max_x9 = H - x1 - x5;
                if (max_x9 < 0) break;
                for (int x8 = 0; x8 <= H; ++x8) {
                    if (x0 == x1 && x5 > x8) continue;
                    int rem_c = H - x0 - x8;
                    if (rem_c < 0) break;
                    for (int x9 = 0; x9 <= max_x9; ++x9) {
                        int b = x1 + x5 + x9;
                        for (int x6 = 0; x6 <= rem_c; ++x6) {
                            if (x0 == x1 && x5 == x8 && x6 > x9) continue;
                            for (int x10 = 0; x10 <= rem_c - x6; ++x10) {
                                if ((x1 + x8 + x9 + x10) & 1) continue;
                                int c = x0 + x8 + x6 + x10;
                                int support = (x0 > 0) + (x1 > 0) + (x5 > 0)
                                            + (x6 > 0) + (x8 > 0) + (x9 > 0)
                                            + (x10 > 0);
                                int t = x0 + x1 + x6 + x9;
                                int r = (x0 + x8 + x10) & 1;
                                int q = x0 * x0 + x1 * x1 + x5 * x5 + x6 * x6
                                      + x8 * x8 + x9 * x9 + x10 * x10;
                                ++hist[{b, c, support, t, r}][q][bc_syndrome(
                                    x0, x1, x5, x6, x8, x9, x10
                                )];
                            }
                        }
                    }
                }
            }
        }
    }

    std::vector<BCBase> out;
    out.reserve(hist.size());
    for (const auto& kv : hist) {
        auto [b, c, support, t, r] = kv.first;
        BCBase base{b, c, support, t, r, {}, 0};
        std::vector<std::pair<int, SyndromeHist>> levels;
        levels.reserve(kv.second.size());
        for (const auto& qv : kv.second) {
            levels.push_back(qv);
            for (const auto& sm : qv.second) base.total_mult += sm.second;
        }

        // Preserve BR202 K8 semantics exactly. If there are >8 q-levels,
        // levels 0..6 stay exact and all levels >=7 are charged at q_7.
        if (levels.size() <= 8) {
            for (const auto& qv : levels) {
                base.parts.push_back(make_part(qv.first, qv.second));
            }
        } else {
            for (int i = 0; i < 7; ++i) {
                base.parts.push_back(make_part(levels[i].first, levels[i].second));
            }
            SyndromeHist tail;
            for (std::size_t i = 7; i < levels.size(); ++i) {
                for (const auto& [syn, mult] : levels[i].second) tail[syn] += mult;
            }
            base.parts.push_back(make_part(levels[7].first, tail));
        }
        out.push_back(std::move(base));
    }
    return out;
}

static int one_x4_count(int d, int g, int t, int r, int q, int e) {
    if (e < 0 || (e & 1) || e > 19 * d / 5) return 0;
    int j = e / 2;
    int n = 19 * d - 10 * j;
    int rhs = 3 * d * d + 48 * d + 96 - 96 * g;
    int rem = rhs - 24 * q;
    if (n < 0 || rem < 0) return 0;
    int root = (int)std::floor(std::sqrt((double)(rem / 4)));
    while ((root + 1) * (root + 1) <= rem / 4) ++root;
    while (root * root > rem / 4) --root;
    int D = d / 2 - t;
    int lo = std::max(0, ceil_div2(D - root));
    int hi0 = floor_div2(D + root);
    int hi = std::min(n, hi0);
    if (lo > hi) return 0;
    int first = ((lo & 1) == r) ? lo : lo + 1;
    if (first > hi) return 0;
    return (hi - first) / 2 + 1;
}

static i64 x4_prefix(int d, int g, int t, int r, int q, int J) {
    if (J < 0) return 0;
    int maxJ = (19 * d / 5) / 2;
    J = std::min(J, maxJ);
    int rhs = 3 * d * d + 48 * d + 96 - 96 * g;
    int rem = rhs - 24 * q;
    if (rem < 0) return 0;
    int root = (int)std::floor(std::sqrt((double)(rem / 4)));
    while ((root + 1) * (root + 1) <= rem / 4) ++root;
    while (root * root > rem / 4) --root;
    int D = d / 2 - t;
    int lo = std::max(0, ceil_div2(D - root));
    int hi0 = floor_div2(D + root);
    int first = ((lo & 1) == r) ? lo : lo + 1;
    if (hi0 < first) return 0;

    int switch_j = (19 * d - hi0) / 10;
    i64 constant_count = (hi0 - first) / 2 + 1;
    i64 total = 0;
    int constant_end = std::min(J, switch_j);
    if (constant_end >= 0) total += (i64)(constant_end + 1) * constant_count;

    int a = std::max(0, switch_j + 1);
    if (a <= J) {
        i64 base = (19 * d - first) / 2 + 1;
        int b = std::min<i64>(J, (base - 1) / 5);
        if (a <= b) {
            i64 count = b - a + 1;
            total += count * base - 5LL * (a + b) * count / 2;
        }
    }
    return total;
}

static i64 sum_x4_over_even_e(
    int d, int g, int t, int r, int q,
    int lower, int upper, int excluded1, int excluded2
) {
    int lo = (lower & 1) ? lower + 1 : lower;
    int hi = (upper & 1) ? upper - 1 : upper;
    if (lo > hi) return 0;
    i64 total = x4_prefix(d, g, t, r, q, hi / 2)
              - x4_prefix(d, g, t, r, q, lo / 2 - 1);
    if (excluded1 >= lo && excluded1 <= hi && !(excluded1 & 1)) {
        total -= one_x4_count(d, g, t, r, q, excluded1);
    }
    if (excluded2 >= lo && excluded2 <= hi && !(excluded2 & 1)
        && excluded2 != excluded1) {
        total -= one_x4_count(d, g, t, r, q, excluded2);
    }
    return total;
}

static EvalResult evaluate(int H, int maxD) {
    auto A = build_a(H);
    auto BC = build_bc(H);
    EvalResult out;
    out.a_refined_states = (int)A.size();
    out.bc_base_states = (int)BC.size();
    for (const auto& base : BC) out.bc_assignments += base.total_mult;

    std::vector<std::vector<ARec>> A_by_a(H + 1);
    for (const auto& rec : A) A_by_a[rec.a].push_back(rec);

    for (int g : {0, 1}) {
        for (int d = 8; d <= maxD; d += 2) {
            int h = d / 2;
            int legacy = (g == 0) ? 8 : 4;
            int required_support = ceil_div4(d - 16 * g + 16);
            for (const auto& B : BC) {
                if (B.b > h || B.c > h) continue;
                int c_3 = component3(d, B.b, B.c);
                if (c_3 < 0) continue;

                for (int a = 0; a <= h && a <= H; ++a) {
                    int c_a = component_a(d, a);
                    if (c_a < 0) continue;
                    int exceptional_mass = a + B.b + B.c;
                    int support_remainder = std::min(16, d) + c_a + c_3;

                    for (const auto& AR : A_by_a[a]) {
                        int support = B.support + AR.support;
                        int qneed = required_support - support;
                        if (qneed > 0 && support_remainder < qneed) continue;

                        int base_lower = std::max({
                            legacy,
                            required_support,
                            d - 4 * g + 4,
                            exceptional_mass,
                            exceptional_mass + std::max(0, qneed),
                        });
                        int upper = std::min({
                            19 * d / 5,
                            3 * d,
                            3 * d - (B.b - B.c),
                        });
                        if (base_lower > upper) continue;

                        int excluded1 = -1;
                        int excluded2 = -1;
                        int e_n358 = 3 * d - (B.b - B.c);
                        if (B.b <= h - 5
                            && support + support_remainder == required_support
                            && e_n358 - exceptional_mass >= support_remainder) {
                            excluded1 = e_n358;
                        }
                        if (g == 1 && d == 8) excluded2 = 8;

                        for (const auto& part : B.parts) {
                            int q = AR.q + part.q;
                            i64 f0 = sum_x4_over_even_e(
                                d, g, B.t, B.r, q,
                                base_lower, upper, excluded1, excluded2
                            );
                            out.br202_k8 += (i128)AR.mult * part.total_mult * f0;

                            for (int mu = 0; mu <= 2; ++mu) {
                                i64 mult = part.good_mult[AR.syndrome_id][mu];
                                if (mult == 0) continue;
                                int lower = std::max(base_lower, exceptional_mass + mu);
                                i64 f = sum_x4_over_even_e(
                                    d, g, B.t, B.r, q,
                                    lower, upper, excluded1, excluded2
                                );
                                out.br203_mu_k8 += (i128)AR.mult * mult * f;
                            }
                        }
                    }
                }
            }
        }
    }
    return out;
}

static i64 narrow(i128 x) {
    req(x >= 0 && x <= (i128)9223372036854775807LL, "result outside int64 range");
    return (i64)x;
}

int main() {
    constexpr i64 EXPECTED_H10_BR202_K8 = 1878715345LL;
    constexpr i64 EXPECTED_H16_BR202_K8 = 230521553871LL;

    auto h10 = evaluate(10, 20);
    auto h16 = evaluate(16, 32);

    req(narrow(h10.br202_k8) == EXPECTED_H10_BR202_K8,
        "H10 syndrome-refined replay changed BR202 K8 semantics");
    req(narrow(h16.br202_k8) == EXPECTED_H16_BR202_K8,
        "H16 syndrome-refined replay changed BR202 K8 semantics");
    req(h10.bc_base_states == 3800 && h10.bc_assignments == 78945,
        "H10 BC compact population regression");
    req(h16.bc_base_states == 16781 && h16.bc_assignments == 1305021,
        "H16 BC compact population regression");
    req(h10.br203_mu_k8 <= h10.br202_k8 && h16.br203_mu_k8 <= h16.br202_k8,
        "BR203 mu intersection enlarged the BR202 bound");

    i64 h10_mu = narrow(h10.br203_mu_k8);
    i64 h16_mu = narrow(h16.br203_mu_k8);
    std::cout
        << "{\n"
        << "  \"schema\": \"STAGE32_BR203_BOUNDED_MU_INTERSECTION_KERNEL_V1\",\n"
        << "  \"status\": \"PASS_ZERO_CREDIT\",\n"
        << "  \"mu_table_sha256\": \"" << BR203_MU_TABLE_SHA256 << "\",\n"
        << "  \"terminal_syndrome_sha256\": \"" << BR203_TERMINAL_SHA256 << "\",\n"
        << "  \"baseline_semantics\": \"BR202_K8_EXACT_REPLAY_AFTER_SYNDROME_REFINEMENT\",\n"
        << "  \"H10_d20\": {\"A_refined_states\":" << h10.a_refined_states
        << ",\"BC_base_states\":" << h10.bc_base_states
        << ",\"BC_assignments\":" << h10.bc_assignments
        << ",\"BR202_K8\":" << EXPECTED_H10_BR202_K8
        << ",\"BR203_mu_K8\":" << h10_mu
        << ",\"tightening\":" << (EXPECTED_H10_BR202_K8 - h10_mu) << "},\n"
        << "  \"H16_d32\": {\"A_refined_states\":" << h16.a_refined_states
        << ",\"BC_base_states\":" << h16.bc_base_states
        << ",\"BC_assignments\":" << h16.bc_assignments
        << ",\"BR202_K8\":" << EXPECTED_H16_BR202_K8
        << ",\"BR203_mu_K8\":" << h16_mu
        << ",\"tightening\":" << (EXPECTED_H16_BR202_K8 - h16_mu) << "},\n"
        << "  \"credit\": {\"stage32_main\":false,\"theorem\":false,\"effectivity\":false,"
           "\"receiver\":false,\"endpoint\":false,\"full178_complete\":false,"
           "\"perfect_cuboid\":false,\"merge\":false}\n"
        << "}\n";
    return 0;
}
