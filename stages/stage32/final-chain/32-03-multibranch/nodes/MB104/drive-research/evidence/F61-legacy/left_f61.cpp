#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int P=97,R=896,C=1464,W=C+R;
int inv(int a){for(int b=1;b<P;b++)if(a*b%P==1)return b;return 0;}
int main(int argc,char**argv){
 string root=argc>1?argv[1]:".";ifstream f(root+"/A97.bin",ios::binary);
 vector<vector<uint8_t>>a(R,vector<uint8_t>(W));
 for(int r=0;r<R;r++){f.read((char*)a[r].data(),C);a[r][C+r]=1;}
 uint8_t table[P][P];for(int i=0;i<P;i++)for(int j=0;j<P;j++)table[i][j]=i*j%P;
 int rank=0;
 for(int col=0;col<C;col++){
  int p=-1;for(int r=rank;r<R;r++)if(a[r][col]){p=r;break;}if(p<0)continue;
  swap(a[p],a[rank]);int s=inv(a[rank][col]);for(int k=col;k<W;k++)a[rank][k]=table[s][a[rank][k]];
  for(int r=rank+1;r<R;r++)if(a[r][col]){int s=a[r][col];a[r][col]=0;
   for(int k=col+1;k<W;k++){int v=a[r][k]-table[s][a[rank][k]];a[r][k]=v<0?v+P:v;}}
  rank++;
 }
 ofstream out(root+"/left97.bin",ios::binary);
 for(int r=rank;r<R;r++)out.write((char*)a[r].data()+C,R);
 cout<<"rank="<<rank<<" left_relations="<<R-rank<<"\n";
}
