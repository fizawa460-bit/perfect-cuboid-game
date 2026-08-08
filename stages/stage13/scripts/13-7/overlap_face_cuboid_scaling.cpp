// Stage13-7jc: complete finite overlap / face-cuboid scaling diagnostic.
//
// Enumerate primitive canonical raw incidences by gluing
//
//   x^2+y^2=p^2,   p^2+z^2=d^2,
//
// but retain a cuboid only when at least one of the two *other* face
// diagonals is also integral.  This avoids storing the overwhelmingly larger
// exact-one population and permits a complete audit through B=5,000,000.
//
// The output is a finite diagnostic only.  It is not used as proof of the
// required face-cuboid bound F(B)=o(B(log B)^3).

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

struct KeyHash {
  size_t operator()(const array<int,4>& a) const noexcept {
    size_t h = 0;
    for (int x : a) h = h * 1000003u + static_cast<unsigned>(x);
    return h;
  }
};

static bool is_square(long long n) {
  if (n < 0) return false;
  long long r = static_cast<long long>(sqrt(static_cast<long double>(n)));
  while ((r + 1) * (r + 1) <= n) ++r;
  while (r * r > n) --r;
  return r * r == n;
}

int main(int argc, char** argv) {
  int B = 5000000;
  if (argc >= 2) B = stoi(argv[1]);
  if (B <= 0) return 2;

  vector<vector<pair<int,int>>> hyp(B + 1), leg(B + 1);
  vector<long long> raw_by_d(B + 1, 0);
  long long integer_triples = 0;

  int mmax = static_cast<int>(sqrt(static_cast<long double>(B))) + 2;
  for (int m = 2; m <= mmax; ++m) {
    for (int n = 1; n < m; ++n) {
      if (((m - n) & 1) == 0 || gcd(m, n) != 1) continue;
      long long u = 1LL * m * m - 1LL * n * n;
      long long v = 2LL * m * n;
      long long w = 1LL * m * m + 1LL * n * n;
      if (w > B) continue;
      if (u > v) swap(u, v);
      for (long long k = 1; k * w <= B; ++k) {
        int x = static_cast<int>(k * u);
        int y = static_cast<int>(k * v);
        int d = static_cast<int>(k * w);
        hyp[d].push_back({x, y});
        leg[x].push_back({y, d});
        leg[y].push_back({x, d});
        ++integer_triples;
      }
    }
  }

  unordered_map<array<int,4>, unsigned char, KeyHash> overlap_masks;
  overlap_masks.reserve(4096);
  long long glued_records = 0;
  long long primitive_raw_incidences = 0;

  for (int p = 1; p <= B; ++p) {
    if (hyp[p].empty() || leg[p].empty()) continue;
    for (auto [x, y] : hyp[p]) {
      for (auto [z, d] : leg[p]) {
        ++glued_records;
        if (gcd(gcd(x, y), z) != 1) continue;

        array<int,3> e = {x, y, z};
        sort(e.begin(), e.end());
        if (e[0] == e[1] || e[1] == e[2]) continue;

        ++primitive_raw_incidences;
        ++raw_by_d[d];

        // The distinguished face x-y is already integral.  An overlap can
        // occur only if one of x-z or y-z is also integral.
        if (!is_square(1LL * x * x + 1LL * z * z) &&
            !is_square(1LL * y * y + 1LL * z * z)) {
          continue;
        }

        array<int,4> key = {e[0], e[1], e[2], d};
        long long vals[3] = {
          1LL * e[0] * e[0] + 1LL * e[1] * e[1],
          1LL * e[0] * e[0] + 1LL * e[2] * e[2],
          1LL * e[1] * e[1] + 1LL * e[2] * e[2]
        };
        unsigned char mask = 0;
        for (int i = 0; i < 3; ++i) {
          if (is_square(vals[i])) mask |= static_cast<unsigned char>(1u << i);
        }
        if (__builtin_popcount(static_cast<unsigned>(mask)) < 2) {
          cerr << "overlap candidate lost second face\n";
          return 3;
        }
        overlap_masks[key] = mask;
      }
    }
  }

  vector<long long> raw_prefix(B + 1, 0);
  for (int d = 1; d <= B; ++d) raw_prefix[d] = raw_prefix[d - 1] + raw_by_d[d];

  const vector<int> requested = {100000, 200000, 500000, 1000000, 2000000, 5000000};

  cout << "{\n";
  cout << "  \"metadata\": {\"stage\": \"13-7jc\", \"scope\": \"finite complete overlap diagnostic only\"},\n";
  cout << "  \"diagnostics\": {\"bound\": " << B
       << ", \"integer_pythagorean_triples\": " << integer_triples
       << ", \"glued_records\": " << glued_records
       << ", \"primitive_raw_incidences\": " << primitive_raw_incidences
       << ", \"stored_face_cuboids\": " << overlap_masks.size() << "},\n";
  cout << "  \"rows\": [\n";

  bool first = true;
  for (int bb : requested) {
    if (bb > B) continue;
    long long o_ab_ac = 0, o_ab_bc = 0, o_ac_bc = 0, triple = 0;
    for (const auto& kv : overlap_masks) {
      if (kv.first[3] > bb) continue;
      unsigned char m = kv.second;
      if ((m & 1) && (m & 2)) ++o_ab_ac;
      if ((m & 1) && (m & 4)) ++o_ab_bc;
      if ((m & 2) && (m & 4)) ++o_ac_bc;
      if (m == 7) ++triple;
    }
    long long pair_sum = o_ab_ac + o_ab_bc + o_ac_bc;
    long long face_cuboids = pair_sum - 2 * triple;
    long long raw_total = raw_prefix[bb];
    long double logb = log(static_cast<long double>(bb));

    if (!first) cout << ",\n";
    first = false;
    cout << "    {\"B\": " << bb
         << ", \"overlap\": {\"ab_ac\": " << o_ab_ac
         << ", \"ab_bc\": " << o_ab_bc
         << ", \"ac_bc\": " << o_ac_bc
         << ", \"three_face\": " << triple << "}"
         << ", \"pair_overlap_sum\": " << pair_sum
         << ", \"face_cuboid_count\": " << face_cuboids
         << ", \"raw_incidence_total\": " << raw_total
         << ", \"face_cuboid_over_raw\": " << static_cast<double>(face_cuboids / static_cast<long double>(raw_total))
         << ", \"pair_sum_over_sqrt_B\": " << static_cast<double>(pair_sum / sqrt(static_cast<long double>(bb)))
         << ", \"pair_sum_over_B_logB_cubed\": " << static_cast<double>(pair_sum / (bb * logb * logb * logb))
         << "}";
  }
  cout << "\n  ],\n";
  cout << "  \"warning\": \"The apparent sqrt(B)-scale stability is a finite observation only; no asymptotic exponent is inferred.\"\n";
  cout << "}\n";
  return 0;
}
