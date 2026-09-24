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

static void req(bool ok, const char* msg) {
    if (!ok) {
        std::cerr << "FAIL: " << msg << "\n";
        std::exit(1);
    }
}

struct Feat {
    int support;
    int bits;
    bool operator<(Feat const& o) const {
        return std::tie(support, bits) < std::tie(o.support, o.bits);
    }
};
struct Base {
    int b, c, support, t, r;
    bool operator<(Base const& o) const {
        return std::tie(b, c, support, t, r) < std::tie(o.b, o.c, o.support, o.t, o.r);
    }
};
using QMap = std::map<int, i64>;
struct FeatureLevels {
    std::map<Feat, QMap> q;
    std::map<Feat, i64> total;
};
struct Retained {
    std::map<int, std::map<int, i64>> levels;
    std::map<int, i64> total;
};

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
    int b, c, support, t, r;
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

static int mu_for(Syn syndrome) {
    for (const auto& entry : BR203_MU_TABLE) {
        if (entry.syndrome == syndrome) return entry.mu;
    }
    return -1;
}

static Syn bc_syndrome_from_bits(int bits) {
    Syn s = 0;
    if (bits & (1 << 0)) s ^= BR203_S_X0;
    if (bits & (1 << 1)) s ^= BR203_S_X1;
    if (bits & (1 << 2)) s ^= BR203_S_X5;
    if (bits & (1 << 3)) s ^= BR203_S_X6;
    if (bits & (1 << 4)) s ^= BR203_S_X8;
    if (bits & (1 << 5)) s ^= BR203_S_X9;
    if (bits & (1 << 6)) s ^= BR203_S_X10;
    return s;
}

static QMap first8(QMap const& in) {
    QMap out;
    int n = 0;
    for (auto const& kv : in) {
        if (n++ == 8) break;
        out.insert(kv);
    }
    return out;
}

static std::vector<std::vector<FeatureLevels>> build_strict(int H) {
    std::vector<std::vector<FeatureLevels>> out(H + 1, std::vector<FeatureLevels>(H + 1));
    for (int u = 0; u <= H; ++u) for (int v = 0; v <= H; ++v) {
        std::map<Feat, QMap> tmp;
        for (int x0 = 0; x0 <= v; ++x0) {
            int x6 = v - x0;
            for (int x1 = x0 + 1; x1 <= u; ++x1) {
                int x9 = u - x1;
                int q = x0*x0 + x6*x6 + x1*x1 + x9*x9;
                int support = (x0 > 0) + (x6 > 0) + (x1 > 0) + (x9 > 0);
                int bits = ((x0 & 1) << 0) | ((x1 & 1) << 1)
                         | ((x6 & 1) << 3) | ((x9 & 1) << 5);
                Feat f{support, bits};
                ++tmp[f][q];
                ++out[u][v].total[f];
            }
        }
        for (auto const& kv : tmp) out[u][v].q[kv.first] = first8(kv.second);
    }
    return out;
}

static std::vector<std::vector<FeatureLevels>> build_equal(int H) {
    std::vector<std::vector<FeatureLevels>> out(H + 1, std::vector<FeatureLevels>(H + 1));
    for (int u = 0; u <= H; ++u) for (int v = 0; v <= H; ++v) {
        std::map<Feat, QMap> tmp;
        for (int x = 0; x <= std::min(u, v); ++x) {
            int x6 = v - x;
            int x9 = u - x;
            int q = 2*x*x + x6*x6 + x9*x9;
            int support = 2*(x > 0) + (x6 > 0) + (x9 > 0);
            int bits = ((x & 1) << 0) | ((x & 1) << 1)
                     | ((x6 & 1) << 3) | ((x9 & 1) << 5);
            Feat f{support, bits};
            ++tmp[f][q];
            ++out[u][v].total[f];
        }
        for (auto const& kv : tmp) out[u][v].q[kv.first] = first8(kv.second);
    }
    return out;
}

static std::vector<std::vector<FeatureLevels>> build_pair(int H) {
    std::vector<std::vector<FeatureLevels>> out(H + 1);
    for (int w = 0; w <= H; ++w) {
        out[w].resize(w + 2);
        for (int L = 0; L <= w + 1; ++L) {
            std::map<Feat, QMap> tmp;
            for (int x8 = L; x8 <= w; ++x8) {
                int x10 = w - x8;
                int q = x8*x8 + x10*x10;
                int support = (x8 > 0) + (x10 > 0);
                int bits = ((x8 & 1) << 4) | ((x10 & 1) << 6);
                Feat f{support, bits};
                ++tmp[f][q];
                ++out[w][L].total[f];
            }
            for (auto const& kv : tmp) out[w][L].q[kv.first] = first8(kv.second);
        }
    }
    return out;
}

static void trim_retained(Retained& r) {
    while (r.levels.size() > 8) {
        auto it = std::prev(r.levels.end());
        r.levels.erase(it);
    }
}

static std::map<Base, Retained> compact_range(
    int H, int blo, int bhi,
    std::vector<std::vector<FeatureLevels>> const& S,
    std::vector<std::vector<FeatureLevels>> const& E,
    std::vector<std::vector<FeatureLevels>> const& P
) {
    std::map<Base, Retained> out;
    for (int b = blo; b <= bhi; ++b) {
        for (int c = 0; c <= H; ++c) {
            for (int t = 0; t <= b + c; ++t) {
                if ((c + t) & 1) continue;
                int ulo = std::max(0, t - c);
                int uhi = std::min(b, t);
                if (ulo > uhi) continue;
                for (int u = ulo; u <= uhi; ++u) {
                    int v = t - u;
                    int w = c - t + u;
                    int x5 = b - u;
                    int adds = (x5 > 0);
                    int addbits = (x5 & 1) << 2;
                    int addq = x5*x5;
                    std::array<std::pair<FeatureLevels const*, FeatureLevels const*>, 2> branches{};
                    int nb = 0;
                    branches[nb++] = {&S[u][v], &P[w][0]};
                    int L = x5 + (v > u);
                    if (L <= w) branches[nb++] = {&E[u][v], &P[w][L]};
                    for (int bi = 0; bi < nb; ++bi) {
                        auto const& C = *branches[bi].first;
                        auto const& D = *branches[bi].second;
                        for (auto const& ct : C.total) for (auto const& dt : D.total) {
                            int support = ct.first.support + dt.first.support + adds;
                            int bits = ct.first.bits | dt.first.bits | addbits;
                            int r = (bits & 1) ^ (w & 1);
                            Base key{b, c, support, t, r};
                            out[key].total[bits] += ct.second * dt.second;
                        }
                        for (auto const& cq : C.q) for (auto const& dq : D.q) {
                            int support = cq.first.support + dq.first.support + adds;
                            int bits = cq.first.bits | dq.first.bits | addbits;
                            int r = (bits & 1) ^ (w & 1);
                            Base key{b, c, support, t, r};
                            auto& R = out[key];
                            for (auto const& q1 : cq.second) for (auto const& q2 : dq.second) {
                                R.levels[addq + q1.first + q2.first][bits] += q1.second * q2.second;
                            }
                            trim_retained(R);
                        }
                    }
                }
            }
        }
    }
    return out;
}

static K8Part make_part(int q, const std::map<int, i64>& by_bits) {
    K8Part part;
    part.q = q;
    for (const auto& [bits, mult] : by_bits) {
        part.total_mult += mult;
        Syn bc_syn = bc_syndrome_from_bits(bits);
        for (int a_id = 0; a_id < 8; ++a_id) {
            int mu = mu_for(BR203_A_SYNDROMES[a_id] ^ bc_syn);
            if (mu >= 0) part.good_mult[a_id][mu] += mult;
        }
    }
    return part;
}

static std::vector<K8Part> parts_from_retained(const Retained& R) {
    std::vector<std::pair<int, std::map<int, i64>>> levels(R.levels.begin(), R.levels.end());
    std::map<int, i64> first7_sum;
    i64 total_mass = 0;
    i64 retained_mass = 0;
    for (const auto& [bits, mult] : R.total) total_mass += mult;
    for (const auto& qv : levels) for (const auto& [bits, mult] : qv.second) retained_mass += mult;

    std::vector<K8Part> parts;
    if (retained_mass == total_mass) {
        for (const auto& qv : levels) parts.push_back(make_part(qv.first, qv.second));
        return parts;
    }

    req(levels.size() == 8, "tail exists but fewer than eight retained q levels");
    for (int i = 0; i < 7; ++i) {
        parts.push_back(make_part(levels[i].first, levels[i].second));
        for (const auto& [bits, mult] : levels[i].second) first7_sum[bits] += mult;
    }
    std::map<int, i64> tail;
    for (const auto& [bits, mult] : R.total) {
        i64 rest = mult - first7_sum[bits];
        req(rest >= 0, "negative K8 tail multiplicity");
        if (rest) tail[bits] = rest;
    }
    i64 first7_mass = 0;
    for (const auto& [bits, mult] : first7_sum) first7_mass += mult;
    i64 tail_mass = 0;
    for (const auto& [bits, mult] : tail) tail_mass += mult;
    req(tail_mass == total_mass - first7_mass, "K8 tail mass mismatch");
    parts.push_back(make_part(levels[7].first, tail));
    return parts;
}

static std::vector<ARec> build_a(int H) {
    std::map<std::tuple<int,int,int,int>, i64> hist;
    for (int a = 0; a <= H; ++a) {
        for (int x2 = 0; x2 <= a; ++x2) {
            for (int x3 = 0; x3 <= a - x2; ++x3) {
                int x7 = a - x2 - x3;
                int support = (x2 > 0) + (x3 > 0) + (x7 > 0);
                int q = x2*x2 + x3*x3 + x7*x7;
                int syndrome_id = (x2 & 1) | ((x3 & 1) << 1) | ((x7 & 1) << 2);
                ++hist[{a, support, q, syndrome_id}];
            }
        }
    }
    std::vector<ARec> out;
    for (const auto& kv : hist) {
        auto [a, support, q, syndrome_id] = kv.first;
        out.push_back({a, support, q, syndrome_id, kv.second});
    }
    return out;
}

static int ceil_div2(int x) {
    int q = x / 2, rem = x % 2;
    if (rem != 0 && x > 0) ++q;
    return q;
}
static int floor_div2(int x) {
    int q = x / 2, rem = x % 2;
    if (rem != 0 && x < 0) --q;
    return q;
}
static int ceil_div4(int x) {
    return x >= 0 ? (x + 3) / 4 : x / 4;
}
static int component_a(int d, int a) {
    int h = d / 2;
    return std::min({13, d - a, d - 2*a + 4, h + 5});
}
static int component3(int d, int b, int c) {
    return std::min({9, d - b - c, d - 2*b, d - 2*c + 1});
}

static int one_x4_count(int d, int g, int t, int r, int q, int e) {
    if (e < 0 || (e & 1) || e > 19*d/5) return 0;
    int j = e / 2;
    int n = 19*d - 10*j;
    int rhs = 3*d*d + 48*d + 96 - 96*g;
    int rem = rhs - 24*q;
    if (n < 0 || rem < 0) return 0;
    int root = (int)std::floor(std::sqrt((double)(rem / 4)));
    while ((root + 1)*(root + 1) <= rem/4) ++root;
    while (root*root > rem/4) --root;
    int D = d/2 - t;
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
    int maxJ = (19*d/5) / 2;
    J = std::min(J, maxJ);
    int rhs = 3*d*d + 48*d + 96 - 96*g;
    int rem = rhs - 24*q;
    if (rem < 0) return 0;
    int root = (int)std::floor(std::sqrt((double)(rem / 4)));
    while ((root + 1)*(root + 1) <= rem/4) ++root;
    while (root*root > rem/4) --root;
    int D = d/2 - t;
    int lo = std::max(0, ceil_div2(D - root));
    int hi0 = floor_div2(D + root);
    int first = ((lo & 1) == r) ? lo : lo + 1;
    if (hi0 < first) return 0;

    int switch_j = (19*d - hi0) / 10;
    i64 constant_count = (hi0 - first) / 2 + 1;
    i64 total = 0;
    int constant_end = std::min(J, switch_j);
    if (constant_end >= 0) total += (i64)(constant_end + 1) * constant_count;

    int a = std::max(0, switch_j + 1);
    if (a <= J) {
        i64 base = (19*d - first) / 2 + 1;
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
    i64 total = x4_prefix(d,g,t,r,q,hi/2) - x4_prefix(d,g,t,r,q,lo/2 - 1);
    if (excluded1 >= lo && excluded1 <= hi && !(excluded1 & 1))
        total -= one_x4_count(d,g,t,r,q,excluded1);
    if (excluded2 >= lo && excluded2 <= hi && !(excluded2 & 1) && excluded2 != excluded1)
        total -= one_x4_count(d,g,t,r,q,excluded2);
    return total;
}

static EvalResult evaluate_compact(int H, int maxD) {
    auto S = build_strict(H);
    auto E = build_equal(H);
    auto P = build_pair(H);
    auto raw = compact_range(H, 0, H, S, E, P);
    auto A = build_a(H);

    std::vector<BCBase> BC;
    BC.reserve(raw.size());
    EvalResult out;
    out.a_refined_states = (int)A.size();
    out.bc_base_states = (int)raw.size();

    for (const auto& [key, R] : raw) {
        BCBase base{key.b, key.c, key.support, key.t, key.r, {}, 0};
        for (const auto& [bits, mult] : R.total) base.total_mult += mult;
        base.parts = parts_from_retained(R);
        i64 part_mass = 0;
        for (const auto& part : base.parts) part_mass += part.total_mult;
        req(part_mass == base.total_mult, "part reconstruction changed BC multiplicity");
        out.bc_assignments += base.total_mult;
        BC.push_back(std::move(base));
    }

    std::vector<std::vector<ARec>> A_by_a(H + 1);
    for (const auto& rec : A) A_by_a[rec.a].push_back(rec);

    for (int g : {0, 1}) {
        for (int d = 8; d <= maxD; d += 2) {
            int h = d / 2;
            int legacy = (g == 0) ? 8 : 4;
            int required_support = ceil_div4(d - 16*g + 16);
            for (const auto& B : BC) {
                if (B.b > h || B.c > h) continue;
                int c3 = component3(d, B.b, B.c);
                if (c3 < 0) continue;
                for (int a = 0; a <= h && a <= H; ++a) {
                    int ca = component_a(d, a);
                    if (ca < 0) continue;
                    int exceptional_mass = a + B.b + B.c;
                    int support_remainder = std::min(16, d) + ca + c3;
                    for (const auto& AR : A_by_a[a]) {
                        int support = B.support + AR.support;
                        int qneed = required_support - support;
                        if (qneed > 0 && support_remainder < qneed) continue;

                        int base_lower = std::max({
                            legacy, required_support, d - 4*g + 4,
                            exceptional_mass,
                            exceptional_mass + std::max(0, qneed)
                        });
                        int upper = std::min({
                            19*d/5, 3*d, 3*d - (B.b - B.c)
                        });
                        if (base_lower > upper) continue;

                        int excluded1 = -1, excluded2 = -1;
                        int e_n358 = 3*d - (B.b - B.c);
                        if (B.b <= h - 5
                            && support + support_remainder == required_support
                            && e_n358 - exceptional_mass >= support_remainder)
                            excluded1 = e_n358;
                        if (g == 1 && d == 8) excluded2 = 8;

                        for (const auto& part : B.parts) {
                            int q = AR.q + part.q;
                            i64 f0 = sum_x4_over_even_e(
                                d,g,B.t,B.r,q,base_lower,upper,excluded1,excluded2
                            );
                            out.br202_k8 += (i128)AR.mult * part.total_mult * f0;
                            for (int mu = 0; mu <= 2; ++mu) {
                                i64 mult = part.good_mult[AR.syndrome_id][mu];
                                if (!mult) continue;
                                int lower = std::max(base_lower, exceptional_mass + mu);
                                i64 f = sum_x4_over_even_e(
                                    d,g,B.t,B.r,q,lower,upper,excluded1,excluded2
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
    req(x >= 0 && x <= (i128)9223372036854775807LL, "result outside int64");
    return (i64)x;
}

int main() {
    auto h10 = evaluate_compact(10, 20);
    auto h16 = evaluate_compact(16, 32);

    req(h10.a_refined_states == 152, "H10 A refined state count");
    req(h16.a_refined_states == 462, "H16 A refined state count");
    req(h10.bc_base_states == 3800 && h10.bc_assignments == 78945, "H10 BC population");
    req(h16.bc_base_states == 16781 && h16.bc_assignments == 1305021, "H16 BC population");

    req(narrow(h10.br202_k8) == 1878715345LL, "H10 BR202 compact replay");
    req(narrow(h10.br203_mu_k8) == 1853108432LL, "H10 BR203 compact mu replay");
    req(narrow(h16.br202_k8) == 230521553871LL, "H16 BR202 compact replay");
    req(narrow(h16.br203_mu_k8) == 229209796641LL, "H16 BR203 compact mu replay");

    std::cout
        << "{\n"
        << "  \"schema\":\"STAGE32_BR204_COMPACT_MU_BOUNDED_EQUIVALENCE_V1\",\n"
        << "  \"status\":\"PASS_ZERO_CREDIT\",\n"
        << "  \"mu_table_sha256\":\"" << BR203_MU_TABLE_SHA256 << "\",\n"
        << "  \"terminal_syndrome_sha256\":\"" << BR203_TERMINAL_SHA256 << "\",\n"
        << "  \"H10\":{\"BR202_K8\":1878715345,\"BR203_mu_K8\":1853108432,\"direct_reference_match\":true},\n"
        << "  \"H16\":{\"BR202_K8\":230521553871,\"BR203_mu_K8\":229209796641,\"direct_reference_match\":true},\n"
        << "  \"producer\":\"aggregate split kernels -> first8 qBC levels + all-level 7-bit parity mass -> exact 46-bit syndrome/mu tail reconstruction\",\n"
        << "  \"credit\":{\"stage32_main\":false,\"theorem\":false,\"full178_complete\":false,\"merge\":false}\n"
        << "}\n";
    return 0;
}
