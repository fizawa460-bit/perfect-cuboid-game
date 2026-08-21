// Stage29-num3 exact aggregated M2 counter.
//
// For a fixed shared edge e, let X_e be all positive integer x such that
// e^2+x^2 is a square.  An unordered pair {x,y} with x!=y, R^2=e^2+x^2+y^2
// <=B^2 and gcd(e,x,y)=1 is one shared-edge incidence of a primitive cuboid
// with at least two integral faces.  Exactly-two cuboids have one such
// incidence; Euler cuboids have exactly three.  Hence
//
//   M2(B) = G(B) - 3*M3(B),
//
// where G is the primitive shared-edge incidence count and M3 is the exact
// primitive Euler-cuboid count under the same physical cutoff.
//
// We do not enumerate O(M2) pairs.  For each e, Mobius inversion gives
//
//   1_{gcd(e,x,y)=1} = sum_{d|e, d|x, d|y} mu(d).
//
// For each squarefree d|e, the number of d-divisible partner pairs satisfying
// the Euclidean cutoff is counted in linear time by two pointers.  Pythagorean
// partners themselves are generated completely from divisors of a square:
//
// odd e:  dq=e^2, d<e, x=(q-d)/2;
// even e: t=e/2, dq=t^2, d<t, x=q-d.
//
// This file counts one endpoint B.  M3(B) is supplied as a separately frozen
// exact input and is subtracted only after G is independently computed.

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
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
constexpr const char* kAlgorithm = "stage29-num3-shared-edge-mobius-v1";

struct Factor {
    std::uint32_t p;
    std::uint8_t e;
};

int factor_any(u64 x, const std::vector<std::uint16_t>& spf, Factor* out) {
    int nf = 0;
    if ((x & 1ULL) == 0) {
        std::uint8_t e = 0;
        do { x >>= 1; ++e; } while ((x & 1ULL) == 0 && x > 0);
        out[nf++] = {2, e};
    }
    while (x > 1) {
        u64 p = spf[x >> 1];
        if (p == 0) p = x;
        std::uint8_t e = 0;
        do { x /= p; ++e; } while (x > 1 && x % p == 0);
        out[nf++] = {static_cast<std::uint32_t>(p), e};
    }
    return nf;
}

void divisors_of_square(const Factor* f, int nf, int i, u64 cur, std::vector<u64>& out) {
    if (i == nf) { out.push_back(cur); return; }
    u64 pw = 1;
    for (int a = 0; a <= 2 * f[i].e; ++a) {
        divisors_of_square(f, nf, i + 1, cur * pw, out);
        pw *= f[i].p;
    }
}

void squarefree_divisors(const Factor* f, int nf, int i, u64 cur, int mu,
                         std::vector<std::pair<u64,int>>& out) {
    if (i == nf) { out.emplace_back(cur, mu); return; }
    squarefree_divisors(f, nf, i + 1, cur, mu, out);
    squarefree_divisors(f, nf, i + 1, cur * f[i].p, -mu, out);
}

u64 count_within(const std::vector<u64>& v, std::size_t lo, std::size_t hi, u128 limit) {
    if (hi <= lo + 1) return 0;
    std::size_t i = lo, j = hi - 1;
    u64 ans = 0;
    while (i < j) {
        const u128 s = static_cast<u128>(v[i]) * v[i] + static_cast<u128>(v[j]) * v[j];
        if (s <= limit) {
            ans += static_cast<u64>(j - i);
            ++i;
        } else {
            --j;
        }
    }
    return ans;
}

u64 count_cross(const std::vector<u64>& v, std::size_t mid, u128 limit) {
    if (mid == 0 || mid == v.size()) return 0;
    std::size_t j = v.size();
    u64 ans = 0;
    for (std::size_t i = 0; i < mid; ++i) {
        while (j > mid) {
            const u128 s = static_cast<u128>(v[i]) * v[i] + static_cast<u128>(v[j - 1]) * v[j - 1];
            if (s <= limit) break;
            --j;
        }
        ans += static_cast<u64>(j - mid);
    }
    return ans;
}
} // namespace

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        std::cerr << "usage: m2_mobius_count B M3 [THREADS]\n";
        return 2;
    }
    const u64 B = std::stoull(argv[1]);
    const u64 M3 = std::stoull(argv[2]);
    if (B < 50 || B > 1000000000ULL) {
        std::cerr << "B outside 50..1e9\n";
        return 2;
    }
    int threads = 1;
#ifdef _OPENMP
    threads = argc == 4 ? std::stoi(argv[3]) : omp_get_max_threads();
    omp_set_num_threads(threads);
#else
    if (argc == 4 && std::stoi(argv[3]) != 1) {
        std::cerr << "binary lacks OpenMP\n";
        return 2;
    }
#endif

    const auto started = std::chrono::steady_clock::now();

    // Compact SPF for odd integers.  A composite n<=1e9 has smallest prime
    // factor <=31623, so uint16_t stores every nonzero SPF entry safely.
    std::vector<std::uint16_t> spf(static_cast<std::size_t>(B / 2 + 1), 0);
    const u64 lim = static_cast<u64>(std::sqrt(static_cast<long double>(B)));
    for (u64 p = 3; p <= lim; p += 2) {
        if (spf[p >> 1] != 0) continue;
        for (u64 n = p * p; n <= B; n += 2 * p) {
            auto& s = spf[n >> 1];
            if (s == 0) s = static_cast<std::uint16_t>(p);
        }
    }
    const auto sieve_done = std::chrono::steady_clock::now();

    const u128 B2 = static_cast<u128>(B) * B;
    u64 G = 0, Ga = 0, Gb = 0, Gc = 0;
    u64 eligible_edges = 0, partner_records = 0, mobius_terms = 0, filtered_visits = 0;
    int error_flag = 0;

#pragma omp parallel reduction(+:G,Ga,Gb,Gc,eligible_edges,partner_records,mobius_terms,filtered_visits) reduction(|:error_flag) if(threads > 1)
    {
        Factor ft[12], fe[12];
        std::vector<u64> divisors, partners, sub;
        std::vector<std::pair<u64,int>> sf;
        divisors.reserve(8192);
        partners.reserve(4096);
        sub.reserve(4096);
        sf.reserve(1024);

#pragma omp for schedule(dynamic,8192)
        for (u64 e = 1; e < B; ++e) {
            const u64 t = (e & 1ULL) ? e : (e >> 1);
            if (t <= 1) continue;
            const int nft = factor_any(t, spf, ft);
            u64 tau2 = 1;
            for (int i = 0; i < nft; ++i) tau2 *= 2 * ft[i].e + 1;
            if (tau2 < 5) continue; // fewer than two positive partners before cutoff

            divisors.clear();
            divisors_of_square(ft, nft, 0, 1, divisors);
            partners.clear();
            const u64 t2 = t * t;
            const u128 e2 = static_cast<u128>(e) * e;
            const u128 room = B2 - e2;
            for (u64 d : divisors) {
                if (d >= t) continue;
                const u64 q = t2 / d;
                const u64 x = (e & 1ULL) ? ((q - d) >> 1) : (q - d);
                if (x == 0 || x >= B) continue;
                if (static_cast<u128>(x) * x >= room) continue;
                partners.push_back(x);
            }
            if (partners.size() < 2) continue;
            std::sort(partners.begin(), partners.end());
            if (std::adjacent_find(partners.begin(), partners.end()) != partners.end()) {
                error_flag = 1;
                continue;
            }
            ++eligible_edges;
            partner_records += partners.size();

            // Factor e for the squarefree Mobius divisors.  Deriving from t
            // would also work, but this explicit factorization is simple and
            // independently protects the 2-adic case.
            const int nfe = factor_any(e, spf, fe);
            sf.clear();
            squarefree_divisors(fe, nfe, 0, 1, +1, sf);

            long long local_a = 0, local_b = 0, local_c = 0;
            for (const auto& dm : sf) {
                const u64 d = dm.first;
                const int mu = dm.second;
                sub.clear();
                for (u64 x : partners) if (x % d == 0) sub.push_back(x);
                filtered_visits += partners.size();
                if (sub.size() < 2) continue;
                ++mobius_terms;
                const std::size_t mid = static_cast<std::size_t>(
                    std::lower_bound(sub.begin(), sub.end(), e) - sub.begin());
                const u64 c_low = count_within(sub, 0, mid, room);
                const u64 c_high = count_within(sub, mid, sub.size(), room);
                const u64 c_cross = count_cross(sub, mid, room);
                // shared e largest -> canonical c; middle -> b; smallest -> a
                local_a += static_cast<long long>(mu) * static_cast<long long>(c_high);
                local_b += static_cast<long long>(mu) * static_cast<long long>(c_cross);
                local_c += static_cast<long long>(mu) * static_cast<long long>(c_low);
            }
            if (local_a < 0 || local_b < 0 || local_c < 0) {
                error_flag = 1;
                continue;
            }
            const u64 la = static_cast<u64>(local_a);
            const u64 lb = static_cast<u64>(local_b);
            const u64 lc = static_cast<u64>(local_c);
            Ga += la; Gb += lb; Gc += lc; G += la + lb + lc;
        }
    }

    if (error_flag) {
        std::cerr << "internal partner/Mobius invariant failure\n";
        return 3;
    }
    if (G < 3 * M3 || Ga < M3 || Gb < M3 || Gc < M3) {
        std::cerr << "M3 subtraction underflow\n";
        return 3;
    }
    const u64 M2 = G - 3 * M3;
    const u64 M2a = Ga - M3;
    const u64 M2b = Gb - M3;
    const u64 M2c = Gc - M3;
    if (M2a + M2b + M2c != M2) {
        std::cerr << "direction sum failure\n";
        return 3;
    }

    const auto finished = std::chrono::steady_clock::now();
    const double sieve_sec = std::chrono::duration<double>(sieve_done - started).count();
    const double runtime_sec = std::chrono::duration<double>(finished - started).count();

    std::cout << "{\n"
              << "  \"algorithm\": \"" << kAlgorithm << "\",\n"
              << "  \"B\": " << B << ",\n"
              << "  \"M3_input\": " << M3 << ",\n"
              << "  \"G_at_least_two_shared_edge_incidences\": " << G << ",\n"
              << "  \"G_direction_a_b_c\": [" << Ga << "," << Gb << "," << Gc << "],\n"
              << "  \"M2\": " << M2 << ",\n"
              << "  \"M2_direction_a_b_c\": [" << M2a << "," << M2b << "," << M2c << "],\n"
              << "  \"eligible_shared_edges\": " << eligible_edges << ",\n"
              << "  \"partner_records\": " << partner_records << ",\n"
              << "  \"mobius_terms_with_two_plus_partners\": " << mobius_terms << ",\n"
              << "  \"filtered_partner_visits\": " << filtered_visits << ",\n"
              << "  \"sieve_seconds\": " << sieve_sec << ",\n"
              << "  \"runtime_seconds\": " << runtime_sec << ",\n"
              << "  \"threads\": " << threads << ",\n"
              << "  \"identity\": \"M2=G-3*M3; directional M2_j=G_j-M3\",\n"
              << "  \"finite_data_is_not_asymptotic_theorem\": true,\n"
              << "  \"perfect_cuboid_nonexistence_claim\": false\n"
              << "}\n";
    return 0;
}
