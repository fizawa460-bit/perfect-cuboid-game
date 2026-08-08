// Stage13-7g: exact Stage12-coordinate bridge validator.
//
// Re-enumerates the complete outer Pythagorean gluing population and checks,
// for every shell that survives the primitive face filter, the exact map
//
// OE: r=m-n, s=m+n, h=k,
// EE: r=n,   s=m,   h=2k,
//
// with
//   p=h*r*s,
//   z=h*(s*s-r*r)/2,
//   d=h*(r*r+s*s)/2.
//
// It also splits the primitive G-neutral ac-bc gap into k=1 and k>1 scale
// sectors, retaining the zero / first / higher angular-mode decomposition.
// This is a finite validator, not the coupled-region asymptotic theorem.

#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;

struct Triple { int oddleg, evenleg, w, m, n, k; };
struct Face { int x, y; double cos4; };
struct Acc {
    long double direct=0, zero=0, h1=0, higher=0;
    unsigned long long shells=0;
};

static vector<Triple> generate(int B) {
    vector<Triple> out;
    out.reserve(static_cast<size_t>(B*2.4));
    int mmax=static_cast<int>(sqrt(static_cast<long double>(B)))+1;
    for (int m=2;m<=mmax;++m) {
        long long mm=1LL*m*m;
        for (int n=1;n<m;++n) {
            if (((m-n)&1)==0 || gcd(m,n)!=1) continue;
            long long odd=mm-1LL*n*n, even=2LL*m*n, w=mm+1LL*n*n;
            if (w>B) continue;
            for (int k=1;k<=B/static_cast<int>(w);++k)
                out.push_back({static_cast<int>(k*odd),static_cast<int>(k*even),
                               static_cast<int>(k*w),m,n,k});
        }
    }
    return out;
}

static void add(Acc& a,long double direct,long double zero,long double h1,long double higher) {
    a.direct+=direct; a.zero+=zero; a.h1+=h1; a.higher+=higher; ++a.shells;
}

static void emit(const char* name,const Acc& a) {
    cout << ",\"" << name << "\":{\"direct\":" << static_cast<double>(a.direct)
         << ",\"zero\":" << static_cast<double>(a.zero)
         << ",\"h1\":" << static_cast<double>(a.h1)
         << ",\"higher\":" << static_cast<double>(a.higher)
         << ",\"shells\":" << a.shells << '}';
}

int main(int argc,char** argv) {
    int B=5'000'000;
    if (argc>1) B=stoi(argv[1]);
    auto triples=generate(B);

    vector<uint8_t> isleg(B+1);
    for (const auto& t:triples) { isleg[t.oddleg]=1; isleg[t.evenleg]=1; }

    vector<int> count(B+2);
    size_t face_count=0;
    for (const auto& t:triples) if (isleg[t.w]) { ++count[t.w]; ++face_count; }

    vector<int> offset(B+2);
    long long running=0;
    for (int p=0;p<=B+1;++p) {
        offset[p]=static_cast<int>(running);
        if (p<=B) running+=count[p];
    }

    vector<Face> faces(face_count);
    vector<int> cursor=offset;
    for (const auto& t:triples) if (isleg[t.w]) {
        long double x=min(t.oddleg,t.evenleg), y=max(t.oddleg,t.evenleg), p=t.w;
        long double c4=1.0L-8.0L*x*x*y*y/(p*p*p*p);
        faces[cursor[t.w]++]={static_cast<int>(x),static_cast<int>(y),static_cast<double>(c4)};
    }

    const long double pi=acosl(-1.0L), invsqrt2=1.0L/sqrtl(2.0L);
    array<Acc,3> total{}, k1{}, kgt1{}; // ALL, OE, EE
    unsigned long long mismatches=0,boundaries=0,surviving_shells=0,glued=0;

    for (const auto& outer:triples) {
        int ps[2]={outer.oddleg,outer.evenleg};
        int zs[2]={outer.evenleg,outer.oddleg};
        for (int side=0;side<2;++side) {
            int p=ps[side], z=zs[side], R=count[p];
            if (!R) continue;
            int stratum=(p&1)?1:2;
            long double signsum=0,sumprimcos=0;
            int rprim=0;
            for (int j=offset[p];j<offset[p]+R;++j) {
                const auto& f=faces[j];
                ++glued;
                if (gcd(gcd(f.x,f.y),z)!=1) continue;
                int x=min(f.x,f.y), y=max(f.x,f.y);
                if (z<x) signsum-=1;
                else if (x<z && z<y) signsum+=1;
                else if (z==x || z==y) { ++boundaries; continue; }
                ++rprim;
                sumprimcos+=f.cos4;
            }
            if (!rprim) continue;
            ++surviving_shells;

            if (gcd(p,z)!=outer.k) ++mismatches;
            int r,s,h;
            if (stratum==1) {
                r=outer.m-outer.n; s=outer.m+outer.n; h=outer.k;
                if (side!=0 || !(r&1) || !(s&1) || !(h&1)) ++mismatches;
            } else {
                r=outer.n; s=outer.m; h=2*outer.k;
                if (side!=1 || ((r-s)&1)==0 || h%4!=2) ++mismatches;
            }
            if (gcd(r,s)!=1 || 1LL*h*(r*r+s*s)!=2LL*outer.w ||
                1LL*h*r*s!=p || 1LL*h*(s*s-r*r)/2!=z) ++mismatches;

            long double t=static_cast<long double>(z)/p,k0=0,a1=0;
            if (t<invsqrt2) {
                long double phi=asinl(t);
                k0=8*phi/pi-1; a1=4*sinl(4*phi)/pi;
            } else if (t<1) {
                long double phi=acosl(t);
                k0=4*phi/pi; a1=2*sinl(4*phi)/pi;
            }
            long double direct=signsum/R;
            long double zero=k0*rprim/R;
            long double h1=a1*sumprimcos/R;
            long double higher=direct-zero-h1;

            for (int sidx:{0,stratum}) {
                add(total[sidx],direct,zero,h1,higher);
                if (outer.k==1) add(k1[sidx],direct,zero,h1,higher);
                else add(kgt1[sidx],direct,zero,h1,higher);
            }
        }
    }

    cout.precision(15);
    cout << "{\"B\":" << B
         << ",\"triples\":" << triples.size()
         << ",\"face_pairs\":" << face_count
         << ",\"glued\":" << glued
         << ",\"surviving_shells\":" << surviving_shells
         << ",\"mapping_mismatches\":" << mismatches
         << ",\"boundary_hits\":" << boundaries;
    const char* names[3]={"ALL","OE","EE"};
    for (int sidx=0;sidx<3;++sidx) {
        string a=string(names[sidx])+"_all";
        string b=string(names[sidx])+"_k1";
        string c=string(names[sidx])+"_kgt1";
        emit(a.c_str(),total[sidx]); emit(b.c_str(),k1[sidx]); emit(c.c_str(),kgt1[sidx]);
    }
    cout << "}\n";
}
