#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int P=97,R=896,C=1464;
int inv(int a){for(int b=1;b<P;b++)if(a*b%P==1)return b;throw runtime_error("inverse");}
vector<uint8_t> read(const string&f){ifstream s(f,ios::binary);return vector<uint8_t>((istreambuf_iterator<char>(s)),{});}
int determinant(vector<vector<uint8_t>> a){
  int n=a.size(),det=1;uint8_t table[P][P];for(int i=0;i<P;i++)for(int j=0;j<P;j++)table[i][j]=i*j%P;
  for(int c=0;c<n;c++){
    int k=c;while(k<n&&!a[k][c])k++;if(k==n)return 0;
    if(k!=c){swap(a[k],a[c]);det=(P-det)%P;}
    int pivot=a[c][c];det=det*pivot%P;int v=inv(pivot);
    for(int r=c+1;r<n;r++)if(a[r][c]){
      int f=table[a[r][c]][v];for(int j=c+1;j<n;j++){int x=a[r][j]-table[f][a[c][j]];a[r][j]=x<0?x+P:x;}
      a[r][c]=0;
    }
  }
  return det;
}
int main(int argc,char**argv){
 string root=argv[1];auto raw=read(root+"/A97.bin"),ev=read(root+"/evaluations97.bin");
 if(raw.size()!=R*C||ev.size()!=2*C)throw runtime_error("size");
 ifstream in(root+"/rank97.txt");int rank,aug,old_det,sign;in>>rank>>aug>>old_det>>sign;
 vector<int>rows(rank),cols(aug);for(int&x:rows)in>>x;for(int&x:cols)in>>x;
 if(rank!=892||aug!=893)throw runtime_error("rank sizes");
 vector<vector<uint8_t>>m(rank,vector<uint8_t>(rank)),ma(aug,vector<uint8_t>(aug));
 for(int r=0;r<rank;r++)for(int c=0;c<aug;c++){
   int v=raw.at(rows.at(r)*C+cols.at(c));ma[r][c]=v;if(c<rank)m[r][c]=v;
 }
 for(int c=0;c<aug;c++)ma[rank][c]=ev.at(cols[c]);
 int d=determinant(m),da=determinant(ma);if(!d||!da)throw runtime_error("singular minor");
 cout<<"{\"prime\":97,\"rank_892_minor_determinant\":"<<d<<",\"evaluation_893_minor_determinant\":"<<da<<"}\n";
}
