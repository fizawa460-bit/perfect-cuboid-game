#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using i64 = long long;
using i128 = __int128_t;

struct ARec { int a, sa, q; i64 mult; };
struct BCBase {
    int b, c, support, t, r;
    std::vector<std::pair<int, i64>> levels;
    i64 total_mult;
};

static void req(bool ok, const char* msg) {
    if (!ok) {
        std::cerr << "FAIL: " << msg << "\n";
        std::exit(1);
    }
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
    return std::min({13, d - a, d - 2 * a + 4, h + 5});
}

static int component3(int d, int b, int c) {
    return std::min({9, d - b - c, d - 2 * b, d - 2 * c + 1});
}

static std::vector<ARec> build_a(int H) {
    std::map<std::tuple<int,int,int>, i64> hist;
    for (int a = 0; a <= H; ++a) {
        for (int x2 = 0; x2 <= a; ++x2) {
            for (int x3 = 0; x3 <= a - x2; ++x3) {
                int x7 = a - x2 - x3;
                int support = (x2 > 0) + (x3 > 0) + (x7 > 0);
                int q = x2*x2 + x3*x3 + x7*x7;
                ++hist[{a, support, q}];
            }
        }
    }
    std::vector<ARec> out;
    for (const auto& kv : hist) {
        auto [a, support, q] = kv.first;
        out.push_back({a, support, q, kv.second});
    }
    return out;
}

static std::vector<BCBase> build_bc(int H) {
    std::map<std::tuple<int,int,int,int,int>, std::map<int,i64>> hist;
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
                                int support = (x0>0)+(x1>0)+(x5>0)+(x6>0)+(x8>0)+(x9>0)+(x10>0);
                                int t = x0 + x1 + x6 + x9;
                                int r = (x0 + x8 + x10) & 1;
                                int q = x0*x0+x1*x1+x5*x5+x6*x6+x8*x8+x9*x9+x10*x10;
                                ++hist[{b,c,support,t,r}][q];
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
        auto [b,c,support,t,r] = kv.first;
        BCBase base{b,c,support,t,r,{},0};
        for (const auto& qm : kv.second) {
            base.levels.push_back(qm);
            base.total_mult += qm.second;
        }
        out.push_back(std::move(base));
    }
    return out;
}

static int one_x4_count(int d, int g, int t, int r, int q, int e) {
    if (e < 0 || (e & 1) || e > 19*d/5) return 0;
    int j = e / 2;
    int n = 19*d - 10*j;
    int rhs = 3*d*d + 48*d + 96 - 96*g;
    int rem = rhs - 24*q;
    if (n < 0 || rem < 0) return 0;
    int root = (int)std::floor(std::sqrt((double)(rem / 4)));
    while ((root+1)*(root+1) <= rem/4) ++root;
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
    while ((root+1)*(root+1) <= rem/4) ++root;
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

static std::array<i128,4> evaluate(int H, int maxD, int* out_a_states, int* out_bc_states, i64* out_bc_assignments) {
    const std::array<int,4> Ks{1,2,4,8};
    auto A = build_a(H);
    auto BC = build_bc(H);
    *out_a_states = (int)A.size();
    *out_bc_states = (int)BC.size();
    *out_bc_assignments = 0;
    for (const auto& b : BC) *out_bc_assignments += b.total_mult;

    std::vector<std::vector<ARec>> A_by_a(H + 1);
    for (const auto& a : A) A_by_a[a.a].push_back(a);
    std::array<i128,4> ans{0,0,0,0};

    for (int g : {0,1}) {
        for (int d = 8; d <= maxD; d += 2) {
            int h = d / 2;
            int legacy = (g == 0) ? 8 : 4;
            int required_support = ceil_div4(d - 16*g + 16);
            for (const auto& B : BC) {
                if (B.b > h || B.c > h) continue;
                int c3 = component3(d, B.b, B.c);
                if (c3 < 0) continue;
                int level_count = (int)B.levels.size();
                int upto = std::min(level_count, 8);

                for (int a = 0; a <= h && a <= H; ++a) {
                    int ca = component_a(d, a);
                    if (ca < 0) continue;
                    int exceptional_mass = a + B.b + B.c;
                    int support_remainder = std::min(16,d) + ca + c3;

                    for (const auto& AR : A_by_a[a]) {
                        int support = B.support + AR.sa;
                        int qneed = required_support - support;
                        if (qneed > 0 && support_remainder < qneed) continue;

                        int lower = std::max({legacy, required_support, d - 4*g + 4,
                                              exceptional_mass,
                                              exceptional_mass + std::max(0,qneed)});
                        int upper = std::min({19*d/5, 3*d, 3*d - (B.b - B.c)});
                        if (lower > upper) continue;

                        int excluded1 = -1, excluded2 = -1;
                        int e_n358 = 3*d - (B.b - B.c);
                        if (B.b <= h - 5 && support + support_remainder == required_support
                            && e_n358 - exceptional_mass >= support_remainder)
                            excluded1 = e_n358;
                        if (g == 1 && d == 8) excluded2 = 8;

                        std::array<i64,8> f{};
                        std::array<i64,9> prefix_mult{};
                        std::array<i128,9> exact_prefix{};
                        for (int i = 0; i < upto; ++i) {
                            int qb = B.levels[i].first;
                            i64 mb = B.levels[i].second;
                            f[i] = sum_x4_over_even_e(d,g,B.t,B.r,AR.q + qb,
                                                     lower,upper,excluded1,excluded2);
                            prefix_mult[i+1] = prefix_mult[i] + mb;
                            exact_prefix[i+1] = exact_prefix[i] + (i128)mb * f[i];
                        }

                        for (int kk = 0; kk < 4; ++kk) {
                            int K = Ks[kk];
                            i128 bc_contribution;
                            if (level_count <= K) {
                                bc_contribution = exact_prefix[level_count];
                            } else {
                                int j = K - 1;
                                bc_contribution = exact_prefix[j]
                                    + (i128)(B.total_mult - prefix_mult[j]) * f[j];
                            }
                            ans[kk] += (i128)AR.mult * bc_contribution;
                        }
                    }
                }
            }
        }
    }
    return ans;
}

static i64 narrow(i128 x) {
    req(x >= 0 && x <= (i128)9223372036854775807LL, "result outside int64 range");
    return (i64)x;
}

int main() {
    int a10=0, bc10=0, a16=0, bc16=0;
    i64 assignments10=0, assignments16=0;
    auto h10 = evaluate(10,20,&a10,&bc10,&assignments10);
    auto h16 = evaluate(16,32,&a16,&bc16,&assignments16);

    const std::array<i64,4> expected10{
        2499907264LL, 2315905432LL, 2059154207LL, 1878715345LL
    };
    const std::array<i64,4> expected16{
        304596475910LL, 290611516997LL, 264256534379LL, 230521553871LL
    };
    req(a10 == 66, "H10 A-state regression");
    req(bc10 == 3800, "H10 BC-base-state regression");
    req(assignments10 == 78945, "H10 BC assignment regression");
    req(a16 == 196, "H16 A-state regression");
    req(bc16 == 16781, "H16 BC-base-state regression");
    req(assignments16 == 1305021, "H16 BC assignment regression");
    for (int i=0;i<4;++i) {
        req(narrow(h10[i]) == expected10[i], "H10 P1 tier survivor regression");
        req(narrow(h16[i]) == expected16[i], "H16 P1 tier survivor regression");
    }

    std::cout
      << "{\n"
      << "  \"schema\": \"STAGE32_BR202_P1_K8_FULL_QA_KERNEL_V1\",\n"
      << "  \"status\": \"PASS_ZERO_CREDIT\",\n"
      << "  \"H10_d20\": {\"A_states\":66,\"BC_base_states\":3800,\"BC_assignments\":78945,"
         "\"K1\":2499907264,\"K2\":2315905432,\"K4\":2059154207,\"K8\":1878715345},\n"
      << "  \"H16_d32\": {\"A_states\":196,\"BC_base_states\":16781,\"BC_assignments\":1305021,"
         "\"K1\":304596475910,\"K2\":290611516997,\"K4\":264256534379,\"K8\":230521553871},\n"
      << "  \"credit\": {\"stage32_main\":false,\"theorem\":false,\"effectivity\":false,"
         "\"receiver\":false,\"endpoint\":false,\"perfect_cuboid\":false,\"merge\":false}\n"
      << "}\n";
    return 0;
}
