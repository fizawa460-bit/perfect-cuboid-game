#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int R=896,C=1464,W=C+R;
int main(int argc,char**argv){
 string root=argv[1];int P=stoi(argv[2]);
 auto inv=[P](int a){for(int b=1;b<P;b++)if(a*b%P==1)return b;return 0;};
 ifstream f(root+"/A97.bin",ios::binary);
 vector<vector<uint16_t>>a(R,vector<uint16_t>(W));
 for(int r=0;r<R;r++){if(P<256){vector<uint8_t>tmp(C);f.read((char*)tmp.data(),C);copy(tmp.begin(),tmp.end(),a[r].begin());}else f.read((char*)a[r].data(),2*C);a[r][C+r]=1;}
 vector<vector<uint16_t>>table(P,vector<uint16_t>(P));for(int i=0;i<P;i++)for(int j=0;j<P;j++)table[i][j]=i*j%P;
 int rank=0;
 for(int col=0;col<C;col++){
  int p=-1;for(int r=rank;r<R;r++)if(a[r][col]){p=r;break;}if(p<0)continue;
  swap(a[p],a[rank]);int s=inv(a[rank][col]);for(int k=col;k<W;k++)a[rank][k]=table[s][a[rank][k]];
  for(int r=rank+1;r<R;r++)if(a[r][col]){int s=a[r][col];a[r][col]=0;
   for(int k=col+1;k<W;k++){int v=a[r][k]-table[s][a[rank][k]];a[r][k]=v<0?v+P:v;}}
  rank++;
 }
 vector<vector<uint16_t>>left;for(int r=rank;r<R;r++)left.emplace_back(a[r].begin()+C,a[r].end());
 vector<int>pivots;int k=0;
 for(int col=0;col<R&&k<(int)left.size();col++){
  int p=-1;for(int r=k;r<(int)left.size();r++)if(left[r][col]){p=r;break;}if(p<0)continue;
  swap(left[p],left[k]);int s=inv(left[k][col]);for(int j=0;j<R;j++)left[k][j]=table[s][left[k][j]];
  for(int r=0;r<(int)left.size();r++)if(r!=k&&left[r][col]){int s=left[r][col];for(int j=0;j<R;j++){int v=left[r][j]-table[s][left[k][j]];left[r][j]=v<0?v+P:v;}}
  pivots.push_back(col);k++;
 }
 ofstream out(root+"/canonical_left.bin",ios::binary);for(auto&row:left)out.write((char*)row.data(),2*R);
 ofstream info(root+"/canonical_left.txt");info<<rank<<"\n";for(int c:pivots)info<<c<<" ";info<<"\n";
 cout<<"p="<<P<<" rank="<<rank<<"\n";
}
