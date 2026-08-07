// Stage13-7c: parity-resolved pure-G scaling through B=5,000,000.
//
// Complete Pythagorean gluing enumeration for primitive canonical objects:
//     x^2 + y^2 = p^2,
//     p^2 + z^2 = d^2,
// with a<b<c, gcd(a,b,c)=1.
//
// For every raw face incidence the program also accumulates
//   * exact-one counts,
//   * G-neutral weight 1/R_all(p),
//   * shell-neutral weight 1/R_prim(p,z,d),
//   * parity-resolved G-neutral OE/EE weights.
//
// The default cutoffs are 1.0m, 1.5m, ..., 5.0m.  The output is JSON.
// This is a finite diagnostic, not an asymptotic theorem.
//
// Example:
//   g++ -O3 -std=c++17 parity_g_scaling.cpp -o parity_g_scaling
//   ./parity_g_scaling 5000000 > parity_g_scaling.json

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

struct Triple {
    int u, v, w;
};

struct Accumulator {
    long long raw[3]{};
    long long exact_one[3]{};
    long double g_neutral[3]{};
    long double shell_neutral[3]{};
    long double g_oe[3]{};
    long double g_ee[3]{};
};

static vector<Triple> generate_triples(int bound) {
    vector<Triple> triples;
    triples.reserve(static_cast<size_t>(bound * 2.4));

    const int m_max = static_cast<int>(sqrt(static_cast<long double>(bound))) + 1;
    for (int m = 2; m <= m_max; ++m) {
        const long long mm = 1LL * m * m;
        for (int n = 1; n < m; ++n) {
            if (((m - n) & 1) == 0 || gcd(m, n) != 1) continue;

            long long u = mm - 1LL * n * n;
            long long v = 2LL * m * n;
            const long long w = mm + 1LL * n * n;
            if (w > bound) continue;
            if (u > v) swap(u, v);

            for (int k = 1; k <= bound / static_cast<int>(w); ++k) {
                triples.push_back({static_cast<int>(k * u), static_cast<int>(k * v),
                                   static_cast<int>(k * w)});
            }
        }
    }
    return triples;
}

static bool is_square(long long n) {
    long long r = static_cast<long long>(sqrt(static_cast<long double>(n)));
    while ((r + 1) * (r + 1) <= n) ++r;
    while (r * r > n) --r;
    return r * r == n;
}

static int classify_incidence(int x, int y, int z, bool &exact_one) {
    int a = x, b = y, c = z;
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (a > b) swap(a, b);
    if (!(a < b && b < c)) return -1;

    const int lo = min(x, y);
    const int hi = max(x, y);
    int cat = -1;
    if (lo == a && hi == b) cat = 0;
    else if (lo == a && hi == c) cat = 1;
    else if (lo == b && hi == c) cat = 2;
    else return -2;

    const long long face_sq[3] = {
        1LL * a * a + 1LL * b * b,
        1LL * a * a + 1LL * c * c,
        1LL * b * b + 1LL * c * c,
    };
    exact_one = true;
    for (int i = 0; i < 3; ++i) {
        if (i != cat && is_square(face_sq[i])) {
            exact_one = false;
            break;
        }
    }
    return cat;
}

static void add(Accumulator &dst, const Accumulator &src) {
    for (int c = 0; c < 3; ++c) {
        dst.raw[c] += src.raw[c];
        dst.exact_one[c] += src.exact_one[c];
        dst.g_neutral[c] += src.g_neutral[c];
        dst.shell_neutral[c] += src.shell_neutral[c];
        dst.g_oe[c] += src.g_oe[c];
        dst.g_ee[c] += src.g_ee[c];
    }
}

static void emit_stats(const Accumulator &a) {
    const long double raw_total = a.raw[0] + a.raw[1] + a.raw[2];
    const long double exact_total = a.exact_one[0] + a.exact_one[1] + a.exact_one[2];
    const long double g_total = a.g_neutral[0] + a.g_neutral[1] + a.g_neutral[2];

    const long double raw_ac_bc = static_cast<long double>(a.raw[1]) / a.raw[2];
    const long double exact_ac_bc = static_cast<long double>(a.exact_one[1]) / a.exact_one[2];
    const long double g_ac_bc = a.g_neutral[1] / a.g_neutral[2];
    const long double shell_ac_bc = a.shell_neutral[1] / a.shell_neutral[2];

    const long double raw_alpha = a.raw[0] / raw_total - 0.5L;
    const long double raw_beta = (a.raw[1] - a.raw[2]) / (2.0L * raw_total);
    const long double exact_alpha = a.exact_one[0] / exact_total - 0.5L;
    const long double exact_beta = (a.exact_one[1] - a.exact_one[2]) / (2.0L * exact_total);
    const long double g_alpha = a.g_neutral[0] / g_total - 0.5L;
    const long double g_beta = (a.g_neutral[1] - a.g_neutral[2]) / (2.0L * g_total);

    const long double oe_ratio = a.g_oe[1] / a.g_oe[2];
    const long double ee_ratio = a.g_ee[1] / a.g_ee[2];
    const long double oe_gap = a.g_oe[1] - a.g_oe[2];
    const long double ee_gap = a.g_ee[1] - a.g_ee[2];
    const long double total_gap = oe_gap + ee_gap;
    const long double cancellation =
        (oe_gap * ee_gap < 0)
            ? 1.0L - fabsl(total_gap) / (fabsl(oe_gap) + fabsl(ee_gap))
            : 0.0L;

    cout << "{\"raw\":[" << a.raw[0] << ',' << a.raw[1] << ',' << a.raw[2] << ']'
         << ",\"exact_one\":[" << a.exact_one[0] << ',' << a.exact_one[1] << ','
         << a.exact_one[2] << ']'
         << ",\"raw_ac_bc\":" << static_cast<double>(raw_ac_bc)
         << ",\"exact_ac_bc\":" << static_cast<double>(exact_ac_bc)
         << ",\"raw_alpha\":" << static_cast<double>(raw_alpha)
         << ",\"raw_beta\":" << static_cast<double>(raw_beta)
         << ",\"exact_alpha\":" << static_cast<double>(exact_alpha)
         << ",\"exact_beta\":" << static_cast<double>(exact_beta)
         << ",\"G_ab_bc\":" << static_cast<double>(a.g_neutral[0] / a.g_neutral[2])
         << ",\"G_ac_bc\":" << static_cast<double>(g_ac_bc)
         << ",\"G_alpha\":" << static_cast<double>(g_alpha)
         << ",\"G_beta\":" << static_cast<double>(g_beta)
         << ",\"shell_ac_bc\":" << static_cast<double>(shell_ac_bc)
         << ",\"F_prim\":" << static_cast<double>(shell_ac_bc / g_ac_bc)
         << ",\"F_shell\":" << static_cast<double>(raw_ac_bc / shell_ac_bc)
         << ",\"G_OE_ac_bc\":" << static_cast<double>(oe_ratio)
         << ",\"G_EE_ac_bc\":" << static_cast<double>(ee_ratio)
         << ",\"G_OE_gap\":" << static_cast<double>(oe_gap)
         << ",\"G_EE_gap\":" << static_cast<double>(ee_gap)
         << ",\"cancellation_efficiency\":" << static_cast<double>(cancellation)
         << '}';
}

int main(int argc, char **argv) {
    int bound = 5'000'000;
    if (argc > 1) bound = stoi(argv[1]);

    vector<int> cutoffs = {1'000'000, 1'500'000, 2'000'000, 2'500'000, 3'000'000,
                           3'500'000, 4'000'000, 4'500'000, 5'000'000};
    while (!cutoffs.empty() && cutoffs.back() > bound) cutoffs.pop_back();
    if (cutoffs.empty()) return 2;

    const auto triples = generate_triples(bound);

    vector<uint8_t> is_leg(static_cast<size_t>(bound) + 1);
    for (const auto &t : triples) {
        is_leg[t.u] = 1;
        is_leg[t.v] = 1;
    }

    vector<int> count(static_cast<size_t>(bound) + 2);
    size_t face_pair_count = 0;
    for (const auto &t : triples) {
        if (is_leg[t.w]) {
            ++count[t.w];
            ++face_pair_count;
        }
    }

    vector<int> offset(static_cast<size_t>(bound) + 2);
    long long running = 0;
    for (int p = 0; p <= bound + 1; ++p) {
        offset[p] = static_cast<int>(running);
        if (p <= bound) running += count[p];
    }

    vector<pair<int, int>> faces(face_pair_count);
    vector<int> cursor = offset;
    for (const auto &t : triples) {
        if (is_leg[t.w]) faces[cursor[t.w]++] = {t.u, t.v};
    }

    vector<Accumulator> bands(cutoffs.size());
    unsigned long long glued_records = 0;
    unsigned long long primitive_incidences = 0;
    unsigned long long supported_shells = 0;

    for (const auto &outer : triples) {
        const auto it = lower_bound(cutoffs.begin(), cutoffs.end(), outer.w);
        if (it == cutoffs.end()) continue;
        const int band = static_cast<int>(it - cutoffs.begin());

        const int p_values[2] = {outer.u, outer.v};
        const int z_values[2] = {outer.v, outer.u};
        for (int side = 0; side < 2; ++side) {
            const int p = p_values[side];
            const int z = z_values[side];
            const int r_all = count[p];
            if (!r_all) continue;

            int local[3]{};
            int local_exact[3]{};
            int local_oe[3]{};
            int local_ee[3]{};

            for (int j = offset[p]; j < offset[p] + r_all; ++j) {
                const auto [x, y] = faces[j];
                ++glued_records;
                if (gcd(gcd(x, y), z) != 1) continue;

                bool exact_one = false;
                const int cat = classify_incidence(x, y, z, exact_one);
                if (cat < 0) continue;

                ++primitive_incidences;
                ++local[cat];
                if (exact_one) ++local_exact[cat];
                if ((x ^ y) & 1) ++local_oe[cat];
                else ++local_ee[cat];
            }

            const int r_prim = local[0] + local[1] + local[2];
            if (!r_prim) continue;
            ++supported_shells;

            const long double w_g = 1.0L / r_all;
            const long double w_shell = 1.0L / r_prim;
            for (int cat = 0; cat < 3; ++cat) {
                bands[band].raw[cat] += local[cat];
                bands[band].exact_one[cat] += local_exact[cat];
                bands[band].g_neutral[cat] += w_g * local[cat];
                bands[band].shell_neutral[cat] += w_shell * local[cat];
                bands[band].g_oe[cat] += w_g * local_oe[cat];
                bands[band].g_ee[cat] += w_g * local_ee[cat];
            }
        }
    }

    cout.precision(15);
    cout << "{\"diagnostics\":{\"integer_pythagorean_triples\":" << triples.size()
         << ",\"indexed_face_pairs\":" << face_pair_count
         << ",\"glued_records\":" << glued_records
         << ",\"primitive_raw_incidences\":" << primitive_incidences
         << ",\"supported_shells\":" << supported_shells << "},\"rows\":[";

    Accumulator cumulative;
    for (size_t i = 0; i < cutoffs.size(); ++i) {
        add(cumulative, bands[i]);
        if (i) cout << ',';
        cout << "{\"B\":" << cutoffs[i] << ",\"cumulative\":";
        emit_stats(cumulative);
        cout << ",\"band\":";
        emit_stats(bands[i]);
        cout << '}';
    }
    cout << "]}\n";
    return 0;
}
