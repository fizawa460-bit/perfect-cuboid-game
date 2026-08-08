// Stage13-7d: finite scaling of the exact analytic reduction through B=5,000,000.
//
// For each oriented outer Pythagorean shell (p,z,d), let R=R_all(p) be the
// number of unordered positive face representations x<y with x^2+y^2=p^2.
// The Stage13 G-neutral observable is the primitive strict-order category count
// weighted by 1/R.
//
// This program splits that observable into three exact finite layers:
//
//   direct = geom + inner_angular_discrepancy + primitive_correction,
//
// where
//   direct : primitive G-neutral weights,
//   m1     : all-face (primitive filter removed) weights,
//   geom   : uniform-inner-angle shell baseline,
//   inner_angular_discrepancy = m1 - geom,
//   primitive_correction      = direct - m1.
//
// The separate Python validator analytic_reduction.py verifies at B=100000
// that primitive_correction is exactly the Möbius sum over m|gcd(p,z).
// This C++ extension tracks the same finite decomposition through 5m without
// redoing the divisor expansion at every shell.
//
// Example:
//   g++ -O3 -std=c++17 analytic_reduction_scaling.cpp -o analytic_reduction_scaling
//   ./analytic_reduction_scaling 5000000 > analytic_reduction_scaling_report.json

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

struct Bucket {
    long double direct[3]{};
    long double m1[3]{};
    long double geom[3]{};
};

struct ParityBuckets {
    Bucket all, oe, ee;
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

// x<y is the distinguished face representation.  Strict canonical order gives
//   ab iff y<z, ac iff x<z<y, bc iff z<x.
static int classify(int x, int y, int z) {
    if (!(x < y)) return -2;
    if (z > y) return 0;
    if (x < z && z < y) return 1;
    if (z < x) return 2;
    return -1;  // repeated-edge boundary, excluded by a<b<c
}

// Uniform inner angle theta in (0,pi/4), with t=z/p.
static void geometry_probabilities(long double t, long double out[3]) {
    const long double pi = acosl(-1.0L);
    const long double invsqrt2 = 1.0L / sqrtl(2.0L);

    if (t < invsqrt2) {
        const long double ac = 4.0L * asinl(t) / pi;
        out[0] = 0.0L;
        out[1] = ac;
        out[2] = 1.0L - ac;
    } else if (t < 1.0L) {
        const long double ac = 4.0L * acosl(t) / pi;
        out[0] = 1.0L - ac;
        out[1] = ac;
        out[2] = 0.0L;
    } else {
        out[0] = 1.0L;
        out[1] = out[2] = 0.0L;
    }
}

static void add_bucket(Bucket &dst, const Bucket &src) {
    for (int i = 0; i < 3; ++i) {
        dst.direct[i] += src.direct[i];
        dst.m1[i] += src.m1[i];
        dst.geom[i] += src.geom[i];
    }
}

static void add(ParityBuckets &dst, const ParityBuckets &src) {
    add_bucket(dst.all, src.all);
    add_bucket(dst.oe, src.oe);
    add_bucket(dst.ee, src.ee);
}

static void accumulate_shell(Bucket &b, const int primitive[3], const int all[3],
                             int R, const long double geom[3]) {
    const long double w = 1.0L / R;
    for (int i = 0; i < 3; ++i) {
        b.direct[i] += w * primitive[i];
        b.m1[i] += w * all[i];
        b.geom[i] += geom[i];
    }
}

static void emit_vector(const long double v[3]) {
    cout << '[' << static_cast<double>(v[0]) << ',' << static_cast<double>(v[1]) << ','
         << static_cast<double>(v[2]) << ']';
}

static void emit_bucket(const Bucket &b) {
    const long double direct_gap = b.direct[1] - b.direct[2];
    const long double m1_gap = b.m1[1] - b.m1[2];
    const long double geom_gap = b.geom[1] - b.geom[2];
    const long double primitive_correction_gap = direct_gap - m1_gap;
    const long double inner_angular_discrepancy_gap = m1_gap - geom_gap;

    cout << "{\"direct\":";
    emit_vector(b.direct);
    cout << ",\"m1\":";
    emit_vector(b.m1);
    cout << ",\"geom\":";
    emit_vector(b.geom);
    cout << ",\"direct_ac_bc\":" << static_cast<double>(b.direct[1] / b.direct[2])
         << ",\"direct_gap\":" << static_cast<double>(direct_gap)
         << ",\"m1_gap\":" << static_cast<double>(m1_gap)
         << ",\"geom_gap\":" << static_cast<double>(geom_gap)
         << ",\"inner_angular_discrepancy_gap\":"
         << static_cast<double>(inner_angular_discrepancy_gap)
         << ",\"primitive_correction_gap\":"
         << static_cast<double>(primitive_correction_gap) << '}';
}

int main(int argc, char **argv) {
    int bound = 5'000'000;
    if (argc > 1) bound = stoi(argv[1]);

    vector<int> cutoffs = {100'000, 500'000, 1'000'000, 1'500'000, 2'000'000, 2'500'000,
                           3'000'000, 3'500'000, 4'000'000, 4'500'000, 5'000'000};
    while (!cutoffs.empty() && cutoffs.back() > bound) cutoffs.pop_back();
    if (cutoffs.empty()) return 2;

    const auto triples = generate_triples(bound);

    vector<uint8_t> is_leg(static_cast<size_t>(bound) + 1);
    for (const auto &t : triples) {
        is_leg[t.u] = is_leg[t.v] = 1;
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

    vector<ParityBuckets> bands(cutoffs.size());
    unsigned long long glued_records = 0;
    unsigned long long oriented_shells = 0;
    unsigned long long boundary_hits = 0;
    unsigned long long primitive_outer_parity_failures = 0;

    for (const auto &outer : triples) {
        const auto it = lower_bound(cutoffs.begin(), cutoffs.end(), outer.w);
        if (it == cutoffs.end()) continue;
        const int band = static_cast<int>(it - cutoffs.begin());

        const int p_values[2] = {outer.u, outer.v};
        const int z_values[2] = {outer.v, outer.u};
        for (int side = 0; side < 2; ++side) {
            const int p = p_values[side];
            const int z = z_values[side];
            const int R = count[p];
            if (!R) continue;
            ++oriented_shells;

            int local_all[3]{};
            int local_primitive[3]{};
            for (int j = offset[p]; j < offset[p] + R; ++j) {
                const auto [x, y] = faces[j];
                ++glued_records;
                const int category = classify(x, y, z);
                if (category < 0) {
                    if (category == -1) ++boundary_hits;
                    continue;
                }
                ++local_all[category];
                if (gcd(gcd(x, y), z) == 1) ++local_primitive[category];
            }

            const int primitive_total =
                local_primitive[0] + local_primitive[1] + local_primitive[2];
            if (primitive_total && ((p & 1) == (z & 1))) {
                ++primitive_outer_parity_failures;
            }

            long double geom[3];
            geometry_probabilities(static_cast<long double>(z) / p, geom);
            accumulate_shell(bands[band].all, local_primitive, local_all, R, geom);
            if (p & 1) {
                accumulate_shell(bands[band].oe, local_primitive, local_all, R, geom);
            } else {
                accumulate_shell(bands[band].ee, local_primitive, local_all, R, geom);
            }
        }
    }

    cout.precision(15);
    cout << "{\"diagnostics\":{\"triples\":" << triples.size()
         << ",\"face_pairs\":" << face_pair_count
         << ",\"oriented_shells\":" << oriented_shells
         << ",\"glued\":" << glued_records
         << ",\"boundary_hits\":" << boundary_hits
         << ",\"primitive_outer_parity_failures\":" << primitive_outer_parity_failures
         << "},\"rows\":[";

    ParityBuckets cumulative;
    for (size_t i = 0; i < cutoffs.size(); ++i) {
        add(cumulative, bands[i]);
        if (i) cout << ',';
        cout << "{\"B\":" << cutoffs[i] << ",\"ALL\":";
        emit_bucket(cumulative.all);
        cout << ",\"OE\":";
        emit_bucket(cumulative.oe);
        cout << ",\"EE\":";
        emit_bucket(cumulative.ee);
        cout << '}';
    }
    cout << "]}\n";
    return 0;
}
