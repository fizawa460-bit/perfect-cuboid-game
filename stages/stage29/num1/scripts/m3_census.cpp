// Stage29-num1 exact primitive canonical Euler-cuboid census.
//
// Completeness route (no parametrized-family restriction): every primitive
// Euler cuboid has exactly one odd edge a.  For a fixed odd a, every even y
// with a^2+y^2 a square is obtained uniquely from a divisor d<a of a^2:
//
//   y = (a^2/d - d)/2.
//
// We enumerate all such y, pair them, test y1^2+y2^2 by exact integer-square
// arithmetic, impose gcd(a,y1,y2)=1, and finally impose the physical cutoff
// R^2=a^2+y1^2+y2^2 <= B^2.  Fixing the unique odd edge means a primitive
// canonical cuboid is generated exactly once.
//
// The modulo-4096 table is only a rejection prefilter.  Every accepted square
// is certified by an adjusted integer sqrt check.  No floating comparison is
// used for acceptance.

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace {
constexpr const char* kAlgorithmVersion = "stage29-num1-odd-edge-divisor-v2";
bool square_mod_4096[4096];

bool is_square(u64 n) {
    if (!square_mod_4096[n & 4095ULL]) return false;
    u64 r = static_cast<u64>(std::sqrt(static_cast<long double>(n)));
    while (static_cast<u128>(r) * r < n) ++r;
    while (static_cast<u128>(r) * r > n) --r;
    return static_cast<u128>(r) * r == n;
}

struct Factor {
    std::uint32_t p;
    std::uint8_t e;
};

int factor_odd(u64 x, const std::vector<std::uint16_t>& spf, Factor* out) {
    int nf = 0;
    while (x > 1) {
        u64 p = spf[x >> 1];
        if (p == 0) p = x;
        std::uint8_t e = 0;
        do {
            x /= p;
            ++e;
        } while (x > 1 && x % p == 0);
        out[nf++] = {static_cast<std::uint32_t>(p), e};
    }
    return nf;
}

void divisors_of_square(const Factor* f, int nf, int i, u64 current,
                        std::vector<u64>& out) {
    if (i == nf) {
        out.push_back(current);
        return;
    }
    u64 power = 1;
    for (int e = 0; e <= 2 * f[i].e; ++e) {
        divisors_of_square(f, nf, i + 1, current * power, out);
        power *= f[i].p;
    }
}
}  // namespace

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) {
        std::cerr << "usage: m3_census MAX_B [THREADS]\n";
        return 2;
    }
    const u64 B = std::stoull(argv[1]);
    if (B < 3 || B > 1000000000ULL) {
        std::cerr << "MAX_B must satisfy 3 <= B <= 1000000000\n";
        return 2;
    }

    int threads = 1;
#ifdef _OPENMP
    threads = argc == 3 ? std::stoi(argv[2]) : omp_get_max_threads();
    omp_set_num_threads(threads);
#else
    if (argc == 3 && std::stoi(argv[2]) != 1) {
        std::cerr << "binary was built without OpenMP; THREADS must be 1\n";
        return 2;
    }
#endif

    for (int r = 0; r < 4096; ++r) square_mod_4096[r] = false;
    for (u64 r = 0; r < 4096; ++r) square_mod_4096[(r * r) & 4095ULL] = true;

    const auto started = std::chrono::steady_clock::now();

    // Odd-only SPF.  For any composite n<=B its smallest prime factor is
    // <=sqrt(B)<=31623 at B<=1e9, so uint16_t is sufficient.
    std::vector<std::uint16_t> spf(static_cast<std::size_t>(B / 2 + 1), 0);
    const u64 limit = static_cast<u64>(std::sqrt(static_cast<long double>(B)));
    for (u64 p = 3; p <= limit; p += 2) {
        if (spf[p >> 1] != 0) continue;
        for (u64 n = p * p; n <= B; n += 2 * p) {
            auto& slot = spf[n >> 1];
            if (slot == 0) slot = static_cast<std::uint16_t>(p);
        }
    }
    const auto sieve_done = std::chrono::steady_clock::now();

    const u128 B2 = static_cast<u128>(B) * B;
    u64 m3 = 0;
    u64 perfect_hits = 0;
    u64 tested_pairs = 0;
    u64 candidate_even_edges = 0;
    u64 odd_edges_with_two_candidates = 0;

#pragma omp parallel reduction(+:m3,perfect_hits,tested_pairs,candidate_even_edges,odd_edges_with_two_candidates) if(threads > 1)
    {
        std::vector<u64> divisors;
        std::vector<u64> ys;
        divisors.reserve(4096);
        ys.reserve(2048);
        Factor factors[10];

#pragma omp for schedule(dynamic,65536)
        for (u64 i = 1; i <= (B - 1) / 2; ++i) {
            const u64 a = 2 * i + 1;
            const int nf = factor_odd(a, spf, factors);
            u64 tau_a2 = 1;
            for (int j = 0; j < nf; ++j) tau_a2 *= 2 * factors[j].e + 1;
            if (tau_a2 < 5) continue;  // fewer than two positive partners

            divisors.clear();
            divisors_of_square(factors, nf, 0, 1, divisors);
            ys.clear();
            const u64 a2 = a * a;
            for (u64 d : divisors) {
                if (d >= a) continue;
                const u64 y = (a2 / d - d) / 2;
                if (y > B) continue;
                if (static_cast<u128>(a2) + static_cast<u128>(y) * y >= B2) continue;
                ys.push_back(y);
            }
            if (ys.size() < 2) continue;

            ++odd_edges_with_two_candidates;
            candidate_even_edges += ys.size();
            std::sort(ys.begin(), ys.end());

            for (std::size_t j = 0; j < ys.size(); ++j) {
                const u64 b = ys[j];
                const u64 b2 = b * b;
                for (std::size_t k = j + 1; k < ys.size(); ++k) {
                    const u64 c = ys[k];
                    const u128 r2 = static_cast<u128>(a2) + b2 + static_cast<u128>(c) * c;
                    if (r2 > B2) break;
                    ++tested_pairs;
                    if (!is_square(b2 + c * c)) continue;
                    if (std::gcd(a, std::gcd(b, c)) != 1) continue;
                    ++m3;
                    if (is_square(static_cast<u64>(r2))) ++perfect_hits;
                }
            }
        }
    }

    const auto finished = std::chrono::steady_clock::now();
    const double sieve_sec = std::chrono::duration<double>(sieve_done - started).count();
    const double runtime_sec = std::chrono::duration<double>(finished - started).count();

    std::cout << "{\n"
              << "  \"algorithm\": \"" << kAlgorithmVersion << "\",\n"
              << "  \"B\": " << B << ",\n"
              << "  \"M3\": " << m3 << ",\n"
              << "  \"perfect_cuboid_hits\": " << perfect_hits << ",\n"
              << "  \"tested_pairs\": " << tested_pairs << ",\n"
              << "  \"candidate_even_edges\": " << candidate_even_edges << ",\n"
              << "  \"odd_edges_with_two_candidates\": " << odd_edges_with_two_candidates << ",\n"
              << "  \"sieve_sec\": " << sieve_sec << ",\n"
              << "  \"runtime_sec\": " << runtime_sec << ",\n"
              << "  \"threads\": " << threads << ",\n"
              << "  \"finite_data_is_not_asymptotic_theorem\": true,\n"
              << "  \"perfect_cuboid_nonexistence_claim\": false\n"
              << "}\n";
    return 0;
}
