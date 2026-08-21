#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

struct LegPair {
    uint32_t shared;
    uint32_t partner;
    bool operator<(const LegPair& o) const {
        return shared < o.shared || (shared == o.shared && partner < o.partner);
    }
    bool operator==(const LegPair& o) const {
        return shared == o.shared && partner == o.partner;
    }
};

static uint64_t isqrt_u64(uint64_t n) {
    uint64_t r = static_cast<uint64_t>(std::sqrt(static_cast<long double>(n)));
    while (static_cast<__uint128_t>(r + 1) * (r + 1) <= n) ++r;
    while (static_cast<__uint128_t>(r) * r > n) --r;
    return r;
}

static bool is_square_u64(uint64_t n) {
    const uint64_t r = isqrt_u64(n);
    return static_cast<__uint128_t>(r) * r == n;
}

static uint64_t ceil_sqrt_u64(uint64_t n) {
    uint64_t r = isqrt_u64(n);
    if (static_cast<__uint128_t>(r) * r < n) ++r;
    return r;
}

static std::vector<uint64_t> default_thresholds(uint64_t bound) {
    const uint64_t raw[] = {
        50, 100, 200, 400, 800, 1000, 1200, 1600, 2000,
        5000, 10000, 20000, 50000, 100000, 200000, 500000,
        1000000, 2000000, 5000000, 10000000
    };
    std::vector<uint64_t> out;
    for (uint64_t x : raw) if (x <= bound) out.push_back(x);
    if (out.empty() || out.back() != bound) out.push_back(bound);
    return out;
}

static void add_event(uint64_t r2, const std::vector<uint64_t>& thresholds, std::vector<uint64_t>& diff) {
    const uint64_t need = ceil_sqrt_u64(r2);
    auto it = std::lower_bound(thresholds.begin(), thresholds.end(), need);
    if (it != thresholds.end()) ++diff[static_cast<size_t>(it - thresholds.begin())];
}

static std::vector<uint64_t> prefix(const std::vector<uint64_t>& diff) {
    std::vector<uint64_t> out(diff.size());
    uint64_t s = 0;
    for (size_t i = 0; i < diff.size(); ++i) {
        s += diff[i];
        out[i] = s;
    }
    return out;
}

static void require_eq(const char* label, uint64_t got, uint64_t want) {
    if (got != want) {
        throw std::runtime_error(std::string(label) + " regression mismatch: got=" +
                                 std::to_string(got) + " want=" + std::to_string(want));
    }
}

int main(int argc, char** argv) {
    uint64_t bound = 1000000;
    std::string output = "m2-count.json";
    for (int i = 1; i < argc; ++i) {
        std::string a = argv[i];
        if (a == "--bound" && i + 1 < argc) bound = std::strtoull(argv[++i], nullptr, 10);
        else if (a == "--output" && i + 1 < argc) output = argv[++i];
        else throw std::runtime_error("usage: m2_shared_edge_count --bound B --output FILE");
    }
    if (bound < 2000 || bound > 1000000000ULL) throw std::runtime_error("bound outside audited integer range");

    const auto t0 = std::chrono::steady_clock::now();
    const uint64_t B2 = bound * bound;
    std::vector<LegPair> legs;
    const uint64_t reserve_guess = std::min<uint64_t>(bound * 8ULL, 200000000ULL);
    legs.reserve(static_cast<size_t>(reserve_guess));
    uint64_t primitive_triples = 0;
    uint64_t scaled_triangles = 0;

    for (uint64_t m = 2; m * m + 1 <= bound; ++m) {
        for (uint64_t n = 1; n < m; ++n) {
            if (((m - n) & 1ULL) == 0 || std::gcd(m, n) != 1) continue;
            const uint64_t h0 = m * m + n * n;
            if (h0 > bound) break;
            const uint64_t u0 = m * m - n * n;
            const uint64_t v0 = 2 * m * n;
            ++primitive_triples;
            const uint64_t kmax = bound / h0;
            scaled_triangles += kmax;
            for (uint64_t k = 1; k <= kmax; ++k) {
                const uint64_t u = k * u0;
                const uint64_t v = k * v0;
                legs.push_back({static_cast<uint32_t>(u), static_cast<uint32_t>(v)});
                legs.push_back({static_cast<uint32_t>(v), static_cast<uint32_t>(u)});
            }
        }
    }
    std::sort(legs.begin(), legs.end());
    if (std::adjacent_find(legs.begin(), legs.end()) != legs.end()) {
        throw std::runtime_error("duplicate Pythagorean leg-partner record");
    }
    const auto t_generated = std::chrono::steady_clock::now();

    const auto thresholds = default_thresholds(bound);
    const size_t K = thresholds.size();
    std::vector<uint64_t> m2_diff(K), n2_diff(K), m3_inc_diff(K), perfect_inc_diff(K);
    std::vector<std::vector<uint64_t>> m2_dir_diff(3, std::vector<uint64_t>(K));
    std::vector<std::vector<uint64_t>> n2_dir_diff(3, std::vector<uint64_t>(K));

    uint64_t shared_groups = 0;
    uint64_t pair_tests = 0;
    uint64_t cutoff_breaks = 0;
    uint64_t primitive_rejects = 0;
    uint64_t accepted_exact_two = 0;
    uint64_t triple_incidences = 0;
    uint64_t n2_endpoint = 0;

    size_t lo = 0;
    while (lo < legs.size()) {
        size_t hi = lo + 1;
        while (hi < legs.size() && legs[hi].shared == legs[lo].shared) ++hi;
        const uint64_t e = legs[lo].shared;
        if (hi - lo >= 2) ++shared_groups;
        const uint64_t e2 = e * e;

        for (size_t i = lo; i + 1 < hi; ++i) {
            const uint64_t x = legs[i].partner;
            const uint64_t x2 = x * x;
            for (size_t j = i + 1; j < hi; ++j) {
                const uint64_t y = legs[j].partner;
                const uint64_t r2 = e2 + x2 + y * y;
                ++pair_tests;
                if (r2 > B2) {
                    ++cutoff_breaks;
                    break;
                }
                if (std::gcd(e, std::gcd(x, y)) != 1) {
                    ++primitive_rejects;
                    continue;
                }

                const bool third_square = is_square_u64(x2 + y * y);
                if (third_square) {
                    ++triple_incidences;
                    add_event(r2, thresholds, m3_inc_diff);
                    if (is_square_u64(r2)) add_event(r2, thresholds, perfect_inc_diff);
                    continue;
                }

                ++accepted_exact_two;
                add_event(r2, thresholds, m2_diff);
                int dir = (e < x) ? 0 : ((e < y) ? 1 : 2);
                add_event(r2, thresholds, m2_dir_diff[dir]);
                if (is_square_u64(r2)) {
                    ++n2_endpoint;
                    add_event(r2, thresholds, n2_diff);
                    add_event(r2, thresholds, n2_dir_diff[dir]);
                }
            }
        }
        lo = hi;
    }

    const auto m2 = prefix(m2_diff);
    const auto n2 = prefix(n2_diff);
    const auto m3inc = prefix(m3_inc_diff);
    const auto pinc = prefix(perfect_inc_diff);
    std::vector<std::vector<uint64_t>> m2dir(3), n2dir(3);
    for (int d = 0; d < 3; ++d) {
        m2dir[d] = prefix(m2_dir_diff[d]);
        n2dir[d] = prefix(n2_dir_diff[d]);
    }

    // Stage18 / Stage15 exact finite locks.
    const std::vector<std::pair<uint64_t,uint64_t>> m2_locks = {
        {50,16},{100,56},{200,172},{400,494},{800,1347},{1000,1838},
        {1200,2350},{1600,3536},{2000,4812},{5000,16710},{10000,41666},
        {20000,102522},{50000,331731},{100000,796698}
    };
    const std::vector<std::pair<uint64_t,uint64_t>> n2_locks = {
        {1000,2},{2000,5},{5000,15},{10000,25},{20000,42},{50000,62},{100000,89}
    };
    const std::vector<std::pair<uint64_t,uint64_t>> m3_locks = {
        {10000,18},{50000,42},{200000,82},{1000000,219}
    };
    for (auto [b,w] : m2_locks) if (b <= bound) {
        auto it = std::lower_bound(thresholds.begin(), thresholds.end(), b);
        if (it == thresholds.end() || *it != b) throw std::runtime_error("missing M2 regression threshold");
        require_eq("M2", m2[it-thresholds.begin()], w);
    }
    for (auto [b,w] : n2_locks) if (b <= bound) {
        auto it = std::lower_bound(thresholds.begin(), thresholds.end(), b);
        require_eq("N2", n2[it-thresholds.begin()], w);
    }
    for (auto [b,w] : m3_locks) if (b <= bound) {
        auto it = std::lower_bound(thresholds.begin(), thresholds.end(), b);
        const uint64_t inc = m3inc[it-thresholds.begin()];
        if (inc % 3 != 0) throw std::runtime_error("M3 incidence multiplicity not divisible by 3");
        require_eq("M3", inc / 3, w);
    }
    for (size_t i = 0; i < K; ++i) {
        if (m3inc[i] % 3 != 0 || pinc[i] % 3 != 0) throw std::runtime_error("triple incidence multiplicity failure");
        if (m2dir[0][i] + m2dir[1][i] + m2dir[2][i] != m2[i]) throw std::runtime_error("M2 direction sum mismatch");
        if (n2dir[0][i] + n2dir[1][i] + n2dir[2][i] != n2[i]) throw std::runtime_error("N2 direction sum mismatch");
    }

    const auto t1 = std::chrono::steady_clock::now();
    const double generate_sec = std::chrono::duration<double>(t_generated - t0).count();
    const double total_sec = std::chrono::duration<double>(t1 - t0).count();

    std::ofstream f(output);
    if (!f) throw std::runtime_error("cannot open output");
    f << "{\n";
    f << "  \"track\": \"Stage29-num3\",\n";
    f << "  \"algorithm\": \"stage29-num3-shared-edge-stream-count-v1\",\n";
    f << "  \"contract\": {\"population\": \"primitive canonical exactly-two-face cuboids\", \"space_diagonal_required\": false, \"cutoff\": \"R^2=a^2+b^2+c^2<=B^2\"},\n";
    f << "  \"bound\": " << bound << ",\n";
    f << "  \"profile\": {\"primitive_pythagorean_triples\": " << primitive_triples
      << ", \"scaled_triangles\": " << scaled_triangles
      << ", \"leg_partner_records\": " << legs.size()
      << ", \"shared_groups_with_two_plus_partners\": " << shared_groups
      << ", \"pair_tests\": " << pair_tests
      << ", \"cutoff_breaks\": " << cutoff_breaks
      << ", \"primitive_rejects\": " << primitive_rejects
      << ", \"endpoint_exact_two\": " << accepted_exact_two
      << ", \"endpoint_triple_incidences\": " << triple_incidences
      << ", \"endpoint_N2\": " << n2_endpoint
      << ", \"generation_seconds\": " << generate_sec
      << ", \"total_seconds\": " << total_sec << "},\n";
    f << "  \"checkpoints\": [\n";
    for (size_t i = 0; i < K; ++i) {
        f << "    {\"B\": " << thresholds[i]
          << ", \"M2\": " << m2[i]
          << ", \"M2_direction\": [" << m2dir[0][i] << "," << m2dir[1][i] << "," << m2dir[2][i] << "]"
          << ", \"N2\": " << n2[i]
          << ", \"N2_direction\": [" << n2dir[0][i] << "," << n2dir[1][i] << "," << n2dir[2][i] << "]"
          << ", \"M3\": " << (m3inc[i] / 3)
          << ", \"P\": " << (pinc[i] / 3) << "}";
        if (i + 1 != K) f << ",";
        f << "\n";
    }
    f << "  ],\n";
    f << "  \"guards\": {\"NUM_REUSE_PREFLIGHT\": \"PASS\", \"FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM\": true, \"PERFECT_CUBOID_NONEXISTENCE_CLAIM\": false, \"M2_ASYMPTOTIC_INFERRED_FROM_CENSUS\": false}\n";
    f << "}\n";
    f.close();

    std::cout << "STAGE29_NUM3_OK B=" << bound
              << " M2=" << m2.back()
              << " N2=" << n2.back()
              << " M3=" << (m3inc.back()/3)
              << " P=" << (pinc.back()/3)
              << " total_seconds=" << total_sec << "\n";
    return 0;
}
