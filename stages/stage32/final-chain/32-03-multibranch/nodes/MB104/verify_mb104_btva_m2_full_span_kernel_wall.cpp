#include <bits/stdc++.h>
#include "BTVA-M2-FULL-SPAN-MOD1097-DATA.hpp"
#include "BTVA-M2-FULL-SPAN-MOD1009-DATA.hpp"
using namespace std;

static int MOD;
static int invs[1200];
inline int modp(int x){x%=MOD;if(x<0)x+=MOD;return x;}

struct RowSpace {
    array<uint16_t,156> a{};
    uint8_t r=0;
    bool operator==(RowSpace const&o)const{return r==o.r&&a==o.a;}
};
struct RowSpaceHash {
    size_t operator()(RowSpace const&s) const noexcept {
        uint64_t h=1469598103934665603ULL^s.r;
        for(int i=0;i<156;i++){h^=s.a[i]+0x9e37;h*=1099511628211ULL;}
        return (size_t)h;
    }
};

RowSpace insert_row(RowSpace s,const int*v0){
    int v[13];for(int j=0;j<13;j++)v[j]=v0[j];
    for(int i=0;i<s.r;i++){
        int pc=-1;for(int j=0;j<13;j++)if(s.a[i*13+j]){pc=j;break;}
        int c=v[pc];if(c)for(int j=pc;j<13;j++)v[j]=modp(v[j]-c*(int)s.a[i*13+j]);
    }
    int pc=-1;for(int j=0;j<13;j++)if(v[j]){pc=j;break;}if(pc<0)return s;
    int iv=invs[v[pc]];for(int j=pc;j<13;j++)v[j]=(long long)v[j]*iv%MOD;
    for(int i=0;i<s.r;i++){
        int c=s.a[i*13+pc];if(c)for(int j=pc;j<13;j++)s.a[i*13+j]=modp(s.a[i*13+j]-c*v[j]);
    }
    int pos=s.r;
    for(int i=0;i<s.r;i++){
        int q=-1;for(int j=0;j<13;j++)if(s.a[i*13+j]){q=j;break;}
        if(q>pc){pos=i;break;}
    }
    for(int i=s.r;i>pos;i--)for(int j=0;j<13;j++)s.a[i*13+j]=s.a[(i-1)*13+j];
    for(int j=0;j<13;j++)s.a[pos*13+j]=v[j];
    s.r++;return s;
}

RowSpace add_node(RowSpace s,int n,const int maps[48][3][13]){
    for(int rr=0;rr<3;rr++){s=insert_row(s,maps[n][rr]);if(s.r>11)return s;}return s;
}
bool contained(const RowSpace&s,const int*v){return insert_row(s,v).r==s.r;}

int coordinate_rank(const vector<int>&ids,const int nodes[48][7]){
    int A[7][7]{};int r=0;
    for(int n:ids){
        int v[7];for(int j=0;j<7;j++)v[j]=nodes[n][j];
        for(int i=0;i<r;i++){
            int pc=-1;for(int j=0;j<7;j++)if(A[i][j]){pc=j;break;}
            int c=v[pc];if(c)for(int j=pc;j<7;j++)v[j]=modp(v[j]-c*A[i][j]);
        }
        int pc=-1;for(int j=0;j<7;j++)if(v[j]){pc=j;break;}if(pc<0)continue;
        int iv=invs[v[pc]];for(int j=pc;j<7;j++)v[j]=(long long)v[j]*iv%MOD;
        for(int i=0;i<r;i++){
            int c=A[i][pc];if(c)for(int j=pc;j<7;j++)A[i][j]=modp(A[i][j]-c*v[j]);
        }
        memcpy(A[r++],v,sizeof(v));if(r==7)return 7;
    }
    return r;
}

struct Result{size_t states;int best;array<long long,12> hist;array<int,12> maxcoord;};
Result run_prime(int prime,const int nodes[48][7],const int maps[48][3][13]){
    MOD=prime;
    for(int a=1;a<MOD;a++){
        long long b=a,res=1;int e=MOD-2;
        while(e){if(e&1)res=res*b%MOD;b=b*b%MOD;e>>=1;}
        invs[a]=(int)res;
    }
    unordered_set<RowSpace,RowSpaceHash> all;all.reserve(800000);
    RowSpace z;all.insert(z);vector<RowSpace> frontier{z};
    array<long long,12> hist{};array<int,12> maxcoord{};int best=0;
    while(!frontier.empty()){
        vector<RowSpace> next;
        for(auto const&s:frontier){
            vector<int> comp;
            for(int n=0;n<48;n++){
                bool ok=true;for(int rr=0;rr<3;rr++)if(!contained(s,maps[n][rr])){ok=false;break;}
                if(ok)comp.push_back(n);
            }
            int cr=coordinate_rank(comp,nodes);hist[s.r]++;maxcoord[s.r]=max(maxcoord[s.r],cr);best=max(best,cr);
            if(cr==7) throw runtime_error("rank<=11 extension state has coordinate rank 7");
            for(int n=0;n<48;n++){
                RowSpace t=add_node(s,n,maps);
                if(t.r<=11&&t.r>s.r){auto [it,ins]=all.insert(t);if(ins)next.push_back(t);}
            }
        }
        frontier.swap(next);
    }
    return {all.size(),best,hist,maxcoord};
}

int main(){
    const array<long long,12> EH={1,0,0,48,72,204,1152,2616,8934,27836,118579,452152};
    const array<int,12> EC={0,0,0,1,2,3,3,4,4,5,6,6};
    Result a=run_prime(P,NODES,MAPS);
    Result b=run_prime(P2,NODES2,MAPS2);
    for(auto const&r:{a,b}){
        if(r.states!=611594||r.best!=6||r.hist!=EH||r.maxcoord!=EC)return 3;
    }
    static_assert(1097LL*1009LL > 823543LL, "two-prime product must exceed 7^7");
    cout<<"MB104 BTVA full-span m=2 kernel wall verifier PASS (two primes)\n";
    cout<<"p=1097 and p=1009: states=611594, max compatible coordinate rank=6\n";
    cout<<"1097*1009=1106873 > 7^7=823543\n";
    cout<<"therefore characteristic-zero coordinate rank 7 => m=2 extension rank >=12 => kernel dimension <=1\n";
    cout<<"rank_hist 0:1 3:48 4:72 5:204 6:1152 7:2616 8:8934 9:27836 10:118579 11:452152\n";
    return 0;
}
