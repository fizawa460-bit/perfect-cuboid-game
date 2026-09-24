#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <tuple>

using i64 = long long;
using i128 = __int128_t;

struct Key {
    int b, c, support, t, r;
    bool operator<(const Key& o) const {
        return std::tie(b,c,support,t,r) < std::tie(o.b,o.c,o.support,o.t,o.r);
    }
    bool operator==(const Key& o) const {
        return b==o.b && c==o.c && support==o.support && t==o.t && r==o.r;
    }
};

static void req(bool ok, const char* msg) {
    if (!ok) {
        std::cerr << "FAIL: " << msg << "\n";
        std::exit(1);
    }
}

static int count_parity(int lo, int hi, int p) {
    if (lo > hi) return 0;
    int first = ((lo & 1) == p) ? lo : lo + 1;
    if (first > hi) return 0;
    return (hi - first) / 2 + 1;
}

static i64 sum_parity(int lo, int hi, int p) {
    int n = count_parity(lo, hi, p);
    if (!n) return 0;
    int first = ((lo & 1) == p) ? lo : lo + 1;
    int last = first + 2 * (n - 1);
    return (i64)n * (first + last) / 2;
}

static void add_split(
    std::array<std::array<i128,2>,8>& cell,
    int base_support, int xpar, int w, int lo_x8, i128 mult = 1
) {
    if (lo_x8 > w) return;
    int r = xpar ^ (w & 1);
    if (w == 0) {
        if (lo_x8 <= 0 && base_support <= 7) cell[base_support][r] += mult;
        return;
    }
    if (lo_x8 == 0 && base_support + 1 <= 7) cell[base_support + 1][r] += mult;
    if (base_support + 1 <= 7) cell[base_support + 1][r] += mult;
    int L = std::max(1, lo_x8);
    int n2 = std::max(0, w - L);
    if (n2 && base_support + 2 <= 7) cell[base_support + 2][r] += mult * n2;
}

static void add_strict(
    std::array<std::array<i128,2>,8>& cell,
    int u, int v, int w, int fixed_support
) {
    if (u <= 0) return;
    int m = std::min(v, u - 1);
    if (m < 0) return;

    {
        int A = (v > 0);
        add_split(cell, fixed_support + A + 1, 0, w, 0, 1);
        i64 n = u - 1;
        if (n > 0) add_split(cell, fixed_support + A + 2, 0, w, 0, n);
    }

    int generic_hi = m;
    bool has_v_endpoint = (v > 0 && v <= u - 1);
    if (has_v_endpoint) generic_hi = v - 1;
    if (generic_hi >= 1) {
        for (int p = 0; p < 2; ++p) {
            i64 cnt = count_parity(1, generic_hi, p);
            i64 sx = sum_parity(1, generic_hi, p);
            if (cnt) {
                add_split(cell, fixed_support + 3, p, w, 0, cnt);
                i64 n = cnt * (u - 1) - sx;
                if (n > 0) add_split(cell, fixed_support + 4, p, w, 0, n);
            }
        }
    }

    if (has_v_endpoint) {
        int p = v & 1;
        add_split(cell, fixed_support + 2, p, w, 0, 1);
        i64 n = u - v - 1;
        if (n > 0) add_split(cell, fixed_support + 3, p, w, 0, n);
    }
}

static void add_equal(
    std::array<std::array<i128,2>,8>& cell,
    int u, int v, int w, int x5
) {
    int L = x5 + (v > u ? 1 : 0);
    if (L > w) return;
    int fixed = (x5 > 0);
    int m = std::min(u, v);

    {
        int base = fixed + (u > 0) + (v > 0);
        add_split(cell, base, 0, w, L, 1);
    }
    if (m == 0) return;

    if (m >= 2) {
        int base = fixed + 4;
        for (int p = 0; p < 2; ++p) {
            int cnt = count_parity(1, m - 1, p);
            if (cnt) add_split(cell, base, p, w, L, cnt);
        }
    }

    {
        int base = 2 + fixed + (u > m) + (v > m);
        add_split(cell, base, m & 1, w, L, 1);
    }
}

static std::map<Key,i128> compact_map(int H) {
    std::map<Key,i128> out;
    for (int b = 0; b <= H; ++b) {
        for (int c = 0; c <= H; ++c) {
            for (int t = 0; t <= b + c; ++t) {
                if ((c + t) & 1) continue;
                int ulo = std::max(0, t - c);
                int uhi = std::min(b, t);
                if (ulo > uhi) continue;
                std::array<std::array<i128,2>,8> cell{};
                for (int u = ulo; u <= uhi; ++u) {
                    int v = t - u;
                    int w = c - t + u;
                    int x5 = b - u;
                    add_strict(cell, u, v, w, x5 > 0);
                    add_equal(cell, u, v, w, x5);
                }
                for (int s = 0; s < 8; ++s) {
                    for (int r = 0; r < 2; ++r) {
                        if (cell[s][r]) out[{b,c,s,t,r}] = cell[s][r];
                    }
                }
            }
        }
    }
    return out;
}

static std::map<Key,i128> direct_map(int H) {
    std::map<Key,i128> out;
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
                                int support = (x0>0)+(x1>0)+(x5>0)+(x6>0)
                                            +(x8>0)+(x9>0)+(x10>0);
                                int t = x0 + x1 + x6 + x9;
                                int r = (x0 + x8 + x10) & 1;
                                ++out[{b,c,support,t,r}];
                            }
                        }
                    }
                }
            }
        }
    }
    return out;
}

struct Summary {
    long long states = 0;
    long long cells = 0;
    i128 assignments = 0;
    std::array<long long,8> shard_states{};
    std::array<long long,8> shard_cells{};
};

static int shard_for_b(int b) {
    if (b <= 83) return b / 12;
    return 7;
}

static Summary summarize_compact(int H) {
    Summary z;
    for (int b = 0; b <= H; ++b) {
        for (int c = 0; c <= H; ++c) {
            for (int t = 0; t <= b + c; ++t) {
                if ((c + t) & 1) continue;
                int ulo = std::max(0, t - c);
                int uhi = std::min(b, t);
                if (ulo > uhi) continue;
                std::array<std::array<i128,2>,8> cell{};
                for (int u = ulo; u <= uhi; ++u) {
                    int v = t - u;
                    int w = c - t + u;
                    int x5 = b - u;
                    add_strict(cell, u, v, w, x5 > 0);
                    add_equal(cell, u, v, w, x5);
                }
                long long nstate = 0;
                i128 mass = 0;
                for (int s = 0; s < 8; ++s) {
                    for (int r = 0; r < 2; ++r) {
                        if (cell[s][r]) ++nstate;
                        mass += cell[s][r];
                    }
                }
                if (nstate) {
                    int sh = shard_for_b(b);
                    ++z.cells;
                    ++z.shard_cells[sh];
                    z.states += nstate;
                    z.shard_states[sh] += nstate;
                    z.assignments += mass;
                }
            }
        }
    }
    return z;
}

static std::string dec(i128 x) {
    if (x == 0) return "0";
    bool neg = x < 0;
    if (neg) x = -x;
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    if (neg) s.push_back('-');
    std::reverse(s.begin(), s.end());
    return s;
}

int main() {
    auto c10 = compact_map(10);
    auto d10 = direct_map(10);
    req(c10 == d10, "H10 compact/direct multiplicity mismatch");
    req((long long)c10.size() == 3800, "H10 refined-state regression");

    auto c16 = compact_map(16);
    auto d16 = direct_map(16);
    req(c16 == d16, "H16 compact/direct multiplicity mismatch");
    req((long long)c16.size() == 16781, "H16 refined-state regression");

    auto h96 = summarize_compact(96);
    const std::array<long long,8> expected_states{
        249095,345921,409990,473976,537010,600154,663730,790834
    };
    const std::array<long long,8> expected_cells{
        31590,38598,45510,52422,59334,66246,73158,87079
    };
    req(h96.states == 4070710, "H96 refined-state count");
    req(h96.cells == 453937, "H96 bct-cell count");
    req(h96.shard_states == expected_states, "H96 shard refined-state counts");
    req(h96.shard_cells == expected_cells, "H96 shard bct-cell counts");

    std::cout
        << "{\n"
        << "  \"schema\": \"STAGE32_BR204_COMPACT_ROUTING_SURFACE_PREFLIGHT_V1\",\n"
        << "  \"status\": \"PASS_ZERO_CREDIT\",\n"
        << "  \"H10_direct_equals_compact\": true,\n"
        << "  \"H16_direct_equals_compact\": true,\n"
        << "  \"H96\": {\"refined_states\":" << h96.states
        << ",\"bct_cells\":" << h96.cells
        << ",\"assignment_mass\":\"" << dec(h96.assignments) << "\"},\n"
        << "  \"shard_states\": [";
    for (int i = 0; i < 8; ++i) {
        if (i) std::cout << ",";
        std::cout << h96.shard_states[i];
    }
    std::cout << "],\n  \"shard_cells\": [";
    for (int i = 0; i < 8; ++i) {
        if (i) std::cout << ",";
        std::cout << h96.shard_cells[i];
    }
    std::cout
        << "],\n"
        << "  \"credit\": {\"stage32_main\":false,\"theorem\":false,"
           "\"full178_complete\":false,\"merge\":false}\n"
        << "}\n";
    return 0;
}
