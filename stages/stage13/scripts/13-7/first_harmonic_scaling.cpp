// Stage13-7e: first nonzero angular harmonic scaling through B=5,000,000.
//
// For each face representation x<y, x^2+y^2=p^2, set theta=asin(x/p).
// The first nonzero cosine moment is M1(p)=average cos(4 theta).
// For an outer shell p^2+z^2=d^2, t=z/p, the ac-bc ordering kernel has
// uniform-angle baseline k0(t) and first Fourier coefficient a1(t).
//
// This program accumulates, separately for ALL/OE/EE strata:
//   direct    primitive G-neutral ac-bc gap,
//   m1        pre-primitive exact G-neutral gap,
//   geom      uniform-inner-angle baseline,
//   h1        first cos(4 theta) harmonic contribution,
//   residual  m1 - geom - h1,
//   primitive direct - m1.
//
// It is a finite diagnostic. It does not prove asymptotic first-harmonic
// dominance or a directional limiting ratio.

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

struct Triple { int u, v, w; };
struct Acc {
    long double direct = 0, m1 = 0, geom = 0, h1 = 0;
    unsigned long long shells = 0, boundary = 0;
};

static vector<Triple> generate_triples(int B) {
    vector<Triple> out;
    out.reserve(static_cast<size_t>(B * 2.4));
    const int mmax = static_cast<int>(sqrt(static_cast<long double>(B))) + 1;
    for (int m = 2; m <= mmax; ++m) {
        const long long mm = 1LL * m * m;
        for (int n = 1; n < m; ++n) {
            if (((m - n) & 1) == 0 || gcd(m, n) != 1) continue;
            long long u = mm - 1LL * n * n;
            long long v = 2LL * m * n;
            const long long w = mm + 1LL * n * n;
            if (w > B) continue;
            if (u > v) swap(u, v);
            for (int k = 1; k <= B / static_cast<int>(w); ++k)
                out.push_back({static_cast<int>(k*u), static_cast<int>(k*v), static_cast<int>(k*w)});
        }
    }
    return out;
}

static void add(Acc &a, const Acc &b) {
    a.direct += b.direct; a.m1 += b.m1; a.geom += b.geom; a.h1 += b.h1;
    a.shells += b.shells; a.boundary += b.boundary;
}

int main() {
    const int B = 5'000'000;
    const vector<int> cutoffs = {100'000,500'000,1'000'000,1'500'000,2'000'000,2'500'000,3'000'000,3'500'000,4'000'000,4'500'000,5'000'000};
    const auto triples = generate_triples(B);

    vector<uint8_t> is_leg(B+1);
    for (const auto &t : triples) { is_leg[t.u] = 1; is_leg[t.v] = 1; }

    vector<int> count(B+2);
    vector<double> sum_cos4(B+2);
    size_t face_pair_count = 0;
    for (const auto &t : triples) if (is_leg[t.w]) {
        ++count[t.w]; ++face_pair_count;
        const long double p=t.w, x=t.u, y=t.v;
        const long double cos4 = 1.0L - 8.0L*(x*x*y*y)/(p*p*p*p);
        sum_cos4[t.w] += static_cast<double>(cos4);
    }

    vector<int> offset(B+2); long long running=0;
    for (int p=0; p<=B+1; ++p) { offset[p]=static_cast<int>(running); if (p<=B) running += count[p]; }
    vector<pair<int,int>> faces(face_pair_count); vector<int> cursor=offset;
    for (const auto &t : triples) if (is_leg[t.w]) faces[cursor[t.w]++] = {t.u,t.v};

    vector<array<Acc,3>> bands(cutoffs.size()); // 0 ALL, 1 OE, 2 EE
    unsigned long long glued=0;
    const long double pi=acosl(-1.0L), invsqrt2=1.0L/sqrtl(2.0L);

    for (const auto &outer : triples) {
        const auto it=lower_bound(cutoffs.begin(),cutoffs.end(),outer.w);
        if (it==cutoffs.end()) continue;
        const int band=static_cast<int>(it-cutoffs.begin());
        const int ps[2]={outer.u,outer.v}, zs[2]={outer.v,outer.u};
        for (int side=0; side<2; ++side) {
            const int p=ps[side], z=zs[side], R=count[p];
            if (!R) continue;
            const int stratum=(p&1)?1:2;
            ++bands[band][0].shells; ++bands[band][stratum].shells;

            const long double t=static_cast<long double>(z)/p;
            long double k0=0, a1=0;
            if (t<invsqrt2) { const long double phi=asinl(t); k0=8*phi/pi-1; a1=4*sinl(4*phi)/pi; }
            else if (t<1) { const long double phi=acosl(t); k0=4*phi/pi; a1=2*sinl(4*phi)/pi; }
            const long double h1=a1*(sum_cos4[p]/R);
            bands[band][0].geom += k0; bands[band][stratum].geom += k0;
            bands[band][0].h1 += h1; bands[band][stratum].h1 += h1;

            const long double w=1.0L/R;
            for (int j=offset[p]; j<offset[p]+R; ++j) {
                ++glued; const auto [x,y]=faces[j]; int sign=0;
                if (z<x) sign=-1;
                else if (x<z && z<y) sign=1;
                else if (z==x || z==y) { ++bands[band][0].boundary; ++bands[band][stratum].boundary; continue; }
                const long double value=w*sign;
                bands[band][0].m1 += value; bands[band][stratum].m1 += value;
                if (gcd(gcd(x,y),z)==1) { bands[band][0].direct += value; bands[band][stratum].direct += value; }
            }
        }
    }

    array<Acc,3> cumulative{}; const char *names[3]={"ALL","OE","EE"};
    cout.precision(15);
    cout << "{\"diagnostics\":{\"triples\":" << triples.size() << ",\"face_pairs\":" << face_pair_count << ",\"glued\":" << glued << "},\"rows\":[\n";
    for (size_t i=0; i<cutoffs.size(); ++i) {
        for (int s=0; s<3; ++s) add(cumulative[s],bands[i][s]);
        if (i) cout << ",\n";
        cout << "{\"B\":" << cutoffs[i];
        for (int s=0; s<3; ++s) {
            const auto &a=cumulative[s];
            cout << ",\"" << names[s] << "\":{\"direct\":" << static_cast<double>(a.direct)
                 << ",\"m1\":" << static_cast<double>(a.m1)
                 << ",\"geom\":" << static_cast<double>(a.geom)
                 << ",\"h1\":" << static_cast<double>(a.h1)
                 << ",\"inner\":" << static_cast<double>(a.m1-a.geom)
                 << ",\"residual_after_h1\":" << static_cast<double>(a.m1-a.geom-a.h1)
                 << ",\"primitive\":" << static_cast<double>(a.direct-a.m1)
                 << ",\"shells\":" << a.shells << ",\"boundary\":" << a.boundary << '}';
        }
        cout << '}';
    }
    cout << "\n]}\n";
}
