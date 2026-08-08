// Stage13-7f: primitive first-harmonic / denominator-channel scaling to B=5,000,000.
// Finite validator only. It decomposes the primitive G-neutral ac-bc gap into
// zero angular mode + first harmonic + higher harmonics, and expands the first
// harmonic normalization 1/(G-1)=sum_{j>=1}G^{-j} through j=8.
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
struct Triple{int u,v,w;};
struct Face{int x,y; double cos4;};
struct Acc{
    long double direct=0, zero=0, h1=0, higher=0, pre_h1=0, primitive_h1_correction=0;
    array<long double,8> channels{}; long double tail8=0;
    unsigned long long shells=0, glued=0, boundary=0;
};
static vector<Triple> triples(int B){
    vector<Triple> out; out.reserve((size_t)(B*2.4));
    int mmax=(int)sqrt((long double)B)+1;
    for(int m=2;m<=mmax;++m){ long long mm=1LL*m*m;
        for(int n=1;n<m;++n){ if(((m-n)&1)==0||gcd(m,n)!=1) continue;
            long long u=mm-1LL*n*n,v=2LL*m*n,w=mm+1LL*n*n; if(w>B) continue; if(u>v) swap(u,v);
            for(int k=1;k<=B/(int)w;++k) out.push_back({(int)(k*u),(int)(k*v),(int)(k*w)});
        }
    } return out;
}
static void add(Acc&a,const Acc&b){
    a.direct+=b.direct;a.zero+=b.zero;a.h1+=b.h1;a.higher+=b.higher;a.pre_h1+=b.pre_h1;
    a.primitive_h1_correction+=b.primitive_h1_correction;a.tail8+=b.tail8;a.shells+=b.shells;a.glued+=b.glued;a.boundary+=b.boundary;
    for(int j=0;j<8;++j)a.channels[j]+=b.channels[j];
}
int main(){
    const int B=5'000'000; const vector<int> cut={100'000,1'000'000,2'000'000,5'000'000};
    auto ts=triples(B); vector<uint8_t> isleg(B+1); for(auto&t:ts)isleg[t.u]=isleg[t.v]=1;
    vector<int> count(B+2); size_t nf=0; for(auto&t:ts)if(isleg[t.w]){++count[t.w];++nf;}
    vector<int> off(B+2); long long run=0; for(int p=0;p<=B+1;++p){off[p]=(int)run;if(p<=B)run+=count[p];}
    vector<Face> faces(nf); vector<int> cur=off;
    for(auto&t:ts)if(isleg[t.w]){long double p=t.w,x=t.u,y=t.v; long double c4=1-8*x*x*y*y/(p*p*p*p);faces[cur[t.w]++]={t.u,t.v,(double)c4};}
    vector<array<Acc,3>> bands(cut.size()); const long double pi=acosl(-1.0L), invsqrt2=1/sqrtl(2.0L);
    for(auto&o:ts){ auto it=lower_bound(cut.begin(),cut.end(),o.w); if(it==cut.end()) continue; int b=(int)(it-cut.begin());
        int ps[2]={o.u,o.v},zs[2]={o.v,o.u};
        for(int side=0;side<2;++side){ int p=ps[side],z=zs[side],R=count[p]; if(!R) continue; int st=(p&1)?1:2;
            long double t=(long double)z/p,k0=0,a1=0;
            if(t<invsqrt2){long double ph=asinl(t);k0=8*ph/pi-1;a1=4*sinl(4*ph)/pi;}
            else if(t<1){long double ph=acosl(t);k0=4*ph/pi;a1=2*sinl(4*ph)/pi;}
            long double signsum=0,sumallc=0,sumprimc=0; int rprim=0; unsigned long long ng=0,boundary=0;
            for(int j=off[p];j<off[p]+R;++j){auto&f=faces[j];sumallc+=f.cos4;++ng;
                if(gcd(gcd(f.x,f.y),z)!=1) continue; ++rprim; sumprimc+=f.cos4;
                if(z<f.x) signsum-=1; else if(f.x<z&&z<f.y) signsum+=1; else if(z==f.x||z==f.y) ++boundary;
            }
            long double direct=signsum/R,zero=k0*rprim/R,pre_h1=a1*sumallc/R,h1=a1*sumprimc/R,higher=direct-zero-h1;
            long double G=2*R+1,TH=2*sumprimc,powG=G,sumch=0; array<long double,8> ch{};
            for(int j=0;j<8;++j){ch[j]=a1*TH/powG;sumch+=ch[j];powG*=G;}
            for(int ss:{0,st}){auto&A=bands[b][ss];A.direct+=direct;A.zero+=zero;A.pre_h1+=pre_h1;A.h1+=h1;A.primitive_h1_correction+=h1-pre_h1;A.higher+=higher;
                for(int j=0;j<8;++j)A.channels[j]+=ch[j];A.tail8+=h1-sumch;A.shells++;A.glued+=ng;A.boundary+=boundary;}
        }
    }
    array<Acc,3> cum{}; const char* names[3]={"ALL","OE","EE"}; cout.precision(15);
    cout<<"{\"diagnostics\":{\"triples\":"<<ts.size()<<",\"face_pairs\":"<<nf<<"},\"rows\":[";
    for(size_t i=0;i<cut.size();++i){for(int s=0;s<3;++s)add(cum[s],bands[i][s]);if(i)cout<<",";cout<<"{\"B\":"<<cut[i];
        for(int s=0;s<3;++s){auto&A=cum[s];cout<<",\""<<names[s]<<"\":{\"direct\":"<<(double)A.direct<<",\"zero_mode\":"<<(double)A.zero<<",\"first_harmonic\":"<<(double)A.h1
            <<",\"higher_harmonics\":"<<(double)A.higher<<",\"preprimitive_first_harmonic\":"<<(double)A.pre_h1<<",\"primitive_first_harmonic_correction\":"<<(double)A.primitive_h1_correction<<",\"normalization_channels\":[";
            for(int j=0;j<8;++j){if(j)cout<<",";cout<<(double)A.channels[j];}cout<<"],\"tail_after_8\":"<<(double)A.tail8<<",\"shells\":"<<A.shells<<",\"glued\":"<<A.glued<<",\"boundary\":"<<A.boundary<<"}";}
        cout<<"}";}
    cout<<"]}\n";
}
