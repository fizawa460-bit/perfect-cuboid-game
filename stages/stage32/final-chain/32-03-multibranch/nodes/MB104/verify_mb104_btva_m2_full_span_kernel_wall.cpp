#include <bits/stdc++.h>
#include "BTVA-M2-FULL-SPAN-MOD1097-DATA.hpp"
using namespace std;

// Exhaustive finite-field verifier for the Stage32 MB104 full-span m=2 wall.
// The DATA header is the p=1097 reduction of the exact 48 node coordinates
// and exact 3x13 local m=2 extension maps retained by the parent adapter.

static int invs[P];
inline int modp(int x) { x %= P; if (x < 0) x += P; return x; }

struct RowSpace {
    // Rank <= 12 is enough while exploring the forbidden rank <= 11 locus.
    array<uint16_t, 156> a{}; // 12 x 13 RREF storage
    uint8_t r = 0;
    bool operator==(RowSpace const& o) const { return r == o.r && a == o.a; }
};
struct RowSpaceHash {
    size_t operator()(RowSpace const& s) const noexcept {
        uint64_t h = 1469598103934665603ULL ^ s.r;
        for (int i = 0; i < 156; ++i) {
            h ^= s.a[i] + 0x9e37;
            h *= 1099511628211ULL;
        }
        return (size_t)h;
    }
};

RowSpace insert_row(RowSpace s, const int* vin) {
    int v[13]; for (int j = 0; j < 13; ++j) v[j] = vin[j];
    for (int i = 0; i < s.r; ++i) {
        int pc = -1; for (int j = 0; j < 13; ++j) if (s.a[i*13+j]) { pc = j; break; }
        int c = v[pc];
        if (c) for (int j = pc; j < 13; ++j) v[j] = modp(v[j] - c * (int)s.a[i*13+j]);
    }
    int pc = -1; for (int j = 0; j < 13; ++j) if (v[j]) { pc = j; break; }
    if (pc < 0) return s;
    int iv = invs[v[pc]];
    for (int j = pc; j < 13; ++j) v[j] = (long long)v[j] * iv % P;
    for (int i = 0; i < s.r; ++i) {
        int c = s.a[i*13+pc];
        if (c) for (int j = pc; j < 13; ++j) s.a[i*13+j] = modp(s.a[i*13+j] - c * v[j]);
    }
    int pos = s.r;
    for (int i = 0; i < s.r; ++i) {
        int q = -1; for (int j = 0; j < 13; ++j) if (s.a[i*13+j]) { q = j; break; }
        if (q > pc) { pos = i; break; }
    }
    for (int i = s.r; i > pos; --i) for (int j = 0; j < 13; ++j) s.a[i*13+j] = s.a[(i-1)*13+j];
    for (int j = 0; j < 13; ++j) s.a[pos*13+j] = v[j];
    ++s.r;
    return s;
}

RowSpace add_node(RowSpace s, int n) {
    for (int rr = 0; rr < 3; ++rr) {
        s = insert_row(s, MAPS[n][rr]);
        if (s.r > 11) return s;
    }
    return s;
}

bool row_contained(const RowSpace& s, const int* v) {
    return insert_row(s, v).r == s.r;
}

int coordinate_rank(const vector<int>& ids) {
    int A[7][7]{}; int r = 0;
    for (int n : ids) {
        int v[7]; for (int j = 0; j < 7; ++j) v[j] = NODES[n][j];
        for (int i = 0; i < r; ++i) {
            int pc = -1; for (int j = 0; j < 7; ++j) if (A[i][j]) { pc = j; break; }
            int c = v[pc];
            if (c) for (int j = pc; j < 7; ++j) v[j] = modp(v[j] - c * A[i][j]);
        }
        int pc = -1; for (int j = 0; j < 7; ++j) if (v[j]) { pc = j; break; }
        if (pc < 0) continue;
        int iv = invs[v[pc]];
        for (int j = pc; j < 7; ++j) v[j] = (long long)v[j] * iv % P;
        for (int i = 0; i < r; ++i) {
            int c = A[i][pc];
            if (c) for (int j = pc; j < 7; ++j) A[i][j] = modp(A[i][j] - c * v[j]);
        }
        memcpy(A[r++], v, sizeof(v));
        if (r == 7) return 7;
    }
    return r;
}

int main() {
    for (int a = 1; a < P; ++a) {
        long long b = a, res = 1; int e = P - 2;
        while (e) { if (e & 1) res = res * b % P; b = b * b % P; e >>= 1; }
        invs[a] = (int)res;
    }

    const long long EXPECT_RANK_HIST[12] = {
        1,0,0,48,72,204,1152,2616,8934,27836,118579,452152
    };
    const int EXPECT_MAX_COORD[12] = {
        0,0,0,1,2,3,3,4,4,5,6,6
    };

    unordered_set<RowSpace, RowSpaceHash> all;
    all.reserve(800000);
    RowSpace zero;
    all.insert(zero);
    vector<RowSpace> frontier{zero};
    long long rank_hist[12]{};
    int max_coord_by_rank[12]{};
    int best_coord = 0;

    while (!frontier.empty()) {
        vector<RowSpace> next;
        for (const auto& s : frontier) {
            vector<int> compatible;
            for (int n = 0; n < 48; ++n) {
                bool ok = true;
                for (int rr = 0; rr < 3; ++rr) if (!row_contained(s, MAPS[n][rr])) { ok = false; break; }
                if (ok) compatible.push_back(n);
            }
            int cr = coordinate_rank(compatible);
            rank_hist[s.r]++;
            max_coord_by_rank[s.r] = max(max_coord_by_rank[s.r], cr);
            best_coord = max(best_coord, cr);
            if (cr == 7) {
                cerr << "FAIL: extension rank <=11 state supports coordinate rank 7\n";
                return 2;
            }
            for (int n = 0; n < 48; ++n) {
                RowSpace t = add_node(s, n);
                if (t.r <= 11 && t.r > s.r) {
                    auto [it, inserted] = all.insert(t);
                    if (inserted) next.push_back(t);
                }
            }
        }
        frontier.swap(next);
    }

    if (all.size() != 611594 || best_coord != 6) return 3;
    for (int r = 0; r <= 11; ++r) {
        if (rank_hist[r] != EXPECT_RANK_HIST[r]) return 4;
        if (max_coord_by_rank[r] != EXPECT_MAX_COORD[r]) return 5;
    }

    cout << "MB104 BTVA full-span m=2 kernel wall verifier PASS\n";
    cout << "reachable extension rowspaces rank<=11: 611594\n";
    cout << "max coordinate rank among their compatible node sets: 6\n";
    cout << "therefore coordinate-rank-7 node support => extension rank >=12 => kernel dimension <=1\n";
    cout << "rank_hist 0:1 3:48 4:72 5:204 6:1152 7:2616 8:8934 9:27836 10:118579 11:452152\n";
    return 0;
}
