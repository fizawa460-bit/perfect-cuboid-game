#include <bits/stdc++.h>
using namespace std; using u64=unsigned long long; using u128=__uint128_t;
static constexpr int H=96, QCAP=4993;
static string s128(u128 x){ if(!x)return"0"; string s; while(x){s.push_back('0'+x%10);x/=10;} reverse(s.begin(),s.end());return s; }
static int cdiv(int a,int b){ return (a+b-1)/b; }
static int caa(int d,int a){return min({13,d-a,d-2*a+4,d/2+5});}
static int c3f(int d,int b,int c){return min({9,d-b-c,d-2*b,d-2*c+1});}
static pair<int,long long> eis(int d,int lower,int upper,int ex1,int ex2){int lo=lower%2?lower+1:lower,hi=upper%2?upper-1:upper;if(lo>hi)return{0,0}; long long n=(hi-lo)/2+1,total=n*(19LL*d+1)-5LL*n*(lo+hi)/2;int cnt=n; set<int> ex; if(ex1>=0)ex.insert(ex1);if(ex2>=0)ex.insert(ex2);for(int e:ex)if(lo<=e&&e<=hi&&e%2==0){total-=19LL*d-5LL*e+1;cnt--;}return{cnt,total};}
static int minsq(int total,int slots,int s){if(s<0||s>slots)return INT_MAX;if(s==0)return total==0?0:INT_MAX;if(total<s)return INT_MAX;int q=total/s,r=total%s;return (s-r)*q*q+r*(q+1)*(q+1);}
static int minbc(int b,int c,int st){int best=INT_MAX;for(int sb=0;sb<=3;sb++){int sc=st-sb;if(sc<0||sc>4)continue;int x=minsq(b,3,sb),y=minsq(c,4,sc);if(x!=INT_MAX&&y!=INT_MAX)best=min(best,x+y);}return best;}
static int minall(int a,int b,int c,int st){int best=INT_MAX;for(int sa=0;sa<=3;sa++){int x=minsq(a,3,sa);if(x==INT_MAX)continue;for(int sb=0;sb<=3;sb++){int sc=st-sa-sb;if(sc<0||sc>4)continue;int y=minsq(b,3,sb),z=minsq(c,4,sc);if(y!=INT_MAX&&z!=INT_MAX)best=min(best,x+y+z);}}return best;}
int main(int argc,char**argv){ if(argc!=3){cerr<<"usage: h8c03a rows.jsonl projection.tsv\n"; return 2;} string rowsPath=argv[1], projectionPath=argv[2];
 // Original N358 BC support census.
 using A2=array<u64,2>;
 vector<array<A2,3>> B(H+1); vector<array<A2,4>> C(H+1);
 for(int g=0;g<=H;g++){for(int x9=0;x9<=g;x9++){int x5=g-x9;B[g][(x5>0)+(x9>0)][x9&1]++;}for(int x8=0;x8<=g;x8++)for(int x10=0;x10<=g-x8;x10++){int x6=g-x8-x10;C[g][(x6>0)+(x8>0)+(x10>0)][(x8+x10)&1]++;}}
 using S6=array<u64,6>; vector<vector<array<S6,2>>> D(H+1, vector<array<S6,2>>(H+1));
 for(int g2=0;g2<=H;g2++)for(int g3=0;g3<=H;g3++)for(int req=0;req<2;req++)for(int sb=0;sb<3;sb++)for(int pb=0;pb<2;pb++){u64 bv=B[g2][sb][pb];if(!bv)continue;for(int sc=0;sc<4;sc++){u64 cv=C[g3][sc][pb^req];if(cv)D[g2][g3][req][sb+sc]+=bv*cv;}}
 using LCell=array<array<u64,2>,6>; vector<vector<LCell>> L(H+1,vector<LCell>(H+1)); vector<array<A2,3>> P(H+1);
 for(int q=0;q<=H;q++)for(int x10=0;x10<=q;x10++){int x6=q-x10;P[q][(x6>0)+(x10>0)][x10&1]++;}
 for(int x5=0;x5<=H;x5++){int s5=x5>0;for(int x8=x5+1;x8<=H;x8++)for(int x9=0;x9<=H-x5;x9++){int g2=x5+x9,s0=s5+1+(x9>0),p0=(x8+x9)&1;for(int q=0;q<=H-x8;q++){int g3=x8+q;for(int sq=0;sq<3;sq++){u64 v0=P[q][sq][0],v1=P[q][sq][1];if(v0)L[g2][g3][s0+sq][p0]+=v0;if(v1)L[g2][g3][s0+sq][p0^1]+=v1;}}}}
 for(int t=0;t<=H;t++){int st=2*(t>0),cap=H-t;for(int x6=0;x6<=cap;x6++)for(int x9=x6;x9<=cap;x9++){int g2=t+x9,base=st+(x6>0)+(x9>0),p0=(t+x9)&1;for(int x10=0;x10<=cap-x6;x10++){int g3=t+x6+x10;L[g2][g3][base+(x10>0)][p0^(x10&1)]++;}}}
 using BCcell=array<u64,8>; vector<vector<BCcell>> BC(H+1,vector<BCcell>(H+1));
 for(int x0=0;x0<=H;x0++){int extra=(x0>0)+1;for(int x1=x0+1;x1<=H;x1++){int req=x1&1;for(int g2=0;g2<=H-x1;g2++){int b=x1+g2;for(int g3=0;g3<=H-x0;g3++){int c=x0+g3;for(int s=0;s<6;s++){u64 v=D[g2][g3][req][s];if(v)BC[b][c][s+extra]+=v;}}}}}
 for(int t=0;t<=H;t++){int extra=2*(t>0),par=t&1,cap=H-t;for(int g2=0;g2<=cap;g2++){int b=t+g2;for(int g3=0;g3<=cap;g3++){int c=t+g3;for(int s=0;s<6;s++){u64 v=L[g2][g3][s][par];if(v)BC[b][c][s+extra]+=v;}}}}
 ofstream projection(projectionPath); for(int b=0;b<=H;b++)for(int c=0;c<=H;c++)for(int s=0;s<8;s++) projection<<b<<"\t"<<c<<"\t"<<s<<"\t"<<BC[b][c][s]<<"\n"; projection.close();
 // N357 witness projection check.
 u64 witness=0;{int g=0,d=100,e=200,h=50,K=cdiv(d+16,4),T=3*d-e;for(int b=0;b<=h;b++)for(int c=0;c<=h;c++){if(b-c>T)continue;for(int a=0;a<=h;a++){int srem=min(16,d)+caa(d,a)+c3f(d,b,c),om=e-a-b-c;if(om<0)continue;for(int sbc=0;sbc<8;sbc++){u64 bv=BC[b][c][sbc];if(!bv)continue;for(int sa=0;sa<4;sa++){u64 ac=0;if(a==0)ac=(sa==0);else if(sa>0&&sa<=3&&sa<=a){ // C(3,sa)C(a-1,sa-1)
 static int comb3[4]={1,3,3,1}; long long choose=1;if(sa==1)choose=1;else if(sa==2)choose=a-1;else choose=1LL*(a-1)*(a-2)/2;ac=comb3[sa]*choose;} if(ac&&sbc+sa+min(srem,om)>=K)witness+=bv*ac;}}}}}
 if(witness!=49030556814634ULL){cerr<<"witness fail "<<witness<<"\n";return 3;}
 // A exact square tail counts: tail[a][s][q] = # tuples with sq > q, q in [-1..QCAP].
 const int QN=QCAP+2; // index q+1, index0 => q=-1
 vector<array<vector<u64>,4>> hist(H+1),tail(H+1);
 for(int a=0;a<=H;a++)for(int s=0;s<4;s++){hist[a][s].assign(QCAP+1,0);tail[a][s].assign(QN,0);}
 for(int a=0;a<=H;a++)for(int x=0;x<=a;x++)for(int y=0;y<=a-x;y++){int z=a-x-y,s=(x>0)+(y>0)+(z>0),q=min(QCAP,x*x+y*y+z*z);hist[a][s][q]++;}
 for(int a=0;a<=H;a++)for(int s=0;s<4;s++){u64 run=0;for(int q=QCAP;q>=0;q--){run+=hist[a][s][q];tail[a][s][q]=run;}tail[a][s][QCAP+1]=0;}
 auto tailgt=[&](int a,int s,int q)->u64{ if(q<0) return tail[a][s][0]; if(q>=QCAP) return 0; return tail[a][s][q+1]; };
 // totals for A support precomputed
 u64 Atot[H+1][4]{};for(int a=0;a<=H;a++)for(int s=0;s<4;s++)for(u64 v:hist[a][s])Atot[a][s]+=v;
 int minBC[H+1][H+1][8];for(int b=0;b<=H;b++)for(int c=0;c<=H;c++)for(int s=0;s<8;s++)minBC[b][c][s]=minbc(b,c,s);
 u128 tot2=0,tot3=0,pre2=0,pre3=0; u128 g2tot[2]={0,0},g3tot[2]={0,0}; int rows2=0,rows3=0,rowsInc=0;ofstream rows(rowsPath);
 for(int g=0;g<=1;g++){int dmax=g?192:176;for(int d=8;d<=dmax;d+=2){int h=d/2,legacy=g?4:8,K=cdiv(d-16*g+16,4);long long thr=3LL*d*d+48LL*d+96-96*g;int Q=thr/24;u128 r2=0,r3=0,p2=0,p3=0;
  for(int b=0;b<=h;b++)for(int c=0;c<=h;c++){int c3=c3f(d,b,c);if(c3<0)continue;bool any=false;for(auto v:BC[b][c])if(v){any=true;break;}if(!any)continue;for(int a=0;a<=h;a++){int ca=caa(d,a);if(ca<0)continue;int M=a+b+c,srem=min(16,d)+ca+c3;
   long long normal[11]; int neArr[11]; fill(begin(normal),end(normal),-1); fill(begin(neArr),end(neArr),0); for(int st=0;st<=10;st++){int qneed=K-st;if(qneed>0&&srem<qneed)continue;int lower=max({legacy,K,d-4*g+4,M,M+max(0,qneed)}),upper=min({19*d/5,3*d,3*d-(b-c)});if(lower>upper)continue;int ex1=-1,ex2=-1,eN=3*d-(b-c);if(b<=h-5&&st+srem==K&&eN-M>=srem)ex1=eN;if(g==1&&d==8)ex2=8;auto [ne,ns]=eis(d,lower,upper,ex1,ex2);if(ne>0){normal[st]=ns; neArr[st]=ne;}}
   for(int sa=0;sa<4;sa++){u64 ac=Atot[a][sa];if(!ac)continue;for(int sbc=0;sbc<8;sbc++){u64 bc=BC[b][c][sbc];if(!bc)continue;int st=sa+sbc;if(normal[st]<0)continue;int ne_for_support=neArr[st];int m2=minall(a,b,c,st);if(m2>Q){ r2+=(u128)ac*bc*(u64)normal[st]; p2+=(u128)ac*bc*(u64)ne_for_support; } int mb=minBC[b][c][sbc];if(mb==INT_MAX)continue;u64 ac3=tailgt(a,sa,Q-mb);if(ac3){ r3+=(u128)ac3*bc*(u64)normal[st]; p3+=(u128)ac3*bc*(u64)ne_for_support; }}}
  }}
  if(r2)rows2++;if(r3)rows3++;if(r3>r2)rowsInc++;tot2+=r2;tot3+=r3;pre2+=p2;pre3+=p3;g2tot[g]+=r2;g3tot[g]+=r3;rows<<"{\"g\":"<<g<<",\"d\":"<<d<<",\"h8c02_prefixes\":"<<s128(p2)<<",\"h8c03a_prefixes\":"<<s128(p3)<<",\"h8c02_terms\":"<<s128(r2)<<",\"h8c03a_terms\":"<<s128(r3)<<",\"incremental_vs_h8c02\":"<<s128(r3-r2)<<"}\n";
 }}
 rows.close();cout<<"{\"n357_witness\":"<<witness<<",\"h8c02_rejected_terminals\":"<<s128(tot2)<<",\"h8c03a_rejected_terminals\":"<<s128(tot3)<<",\"incremental_vs_h8c02\":"<<s128(tot3-tot2)<<",\"h8c02_prefixes\":"<<s128(pre2)<<",\"h8c03a_prefixes\":"<<s128(pre3)<<",\"h8c03a_genus0_terms\":"<<s128(g3tot[0])<<",\"h8c03a_genus1_terms\":"<<s128(g3tot[1])<<",\"h8c02_rows\":"<<rows2<<",\"h8c03a_rows\":"<<rows3<<",\"incremental_rows\":"<<rowsInc<<"}\n";
}
