#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int P=97, R=896, C=1464;
using Row=vector<uint8_t>;
int inv(int a){for(int b=1;b<P;b++)if(a*b%P==1)return b;throw runtime_error("zero inverse");}
vector<uint8_t> read(const string&name){ifstream f(name,ios::binary);return vector<uint8_t>((istreambuf_iterator<char>(f)),{});}
int main(int argc,char**argv){
  string root=argc>1?argv[1]:".";
  auto raw=read(root+"/A97.bin"), ev=read(root+"/evaluations97.bin");
  if(raw.size()!=R*C||ev.size()!=2*C)throw runtime_error("input size");
  vector<Row>a(R+1,Row(C+1));vector<int>original(R+1);iota(original.begin(),original.end(),0);
  for(int r=0;r<R;r++)copy_n(raw.begin()+r*C,C,a[r].begin());
  copy_n(ev.begin(),C,a[R].begin());a[R][C]=1;
  uint8_t product[P][P];for(int i=0;i<P;i++)for(int j=0;j<P;j++)product[i][j]=i*j%P;
  vector<int>pivots,pivot_rows;int rank=0,rank_base=-1;int determinant=1,swap_sign=1;
  for(int col=0;col<C;col++){
    int pivot=-1;
    // Do not pivot on the extra evaluation row until all base rows are exhausted.
    for(int r=rank;r<R;r++)if(a[r][col]){pivot=r;break;}
    if(pivot<0)continue;
    if(pivot!=rank){swap(a[pivot],a[rank]);swap(original[pivot],original[rank]);swap_sign=-swap_sign;}
    determinant=determinant*a[rank][col]%P;
    int scale=inv(a[rank][col]);for(int k=col;k<=C;k++)a[rank][k]=product[scale][a[rank][k]];
    for(int r=rank+1;r<=R;r++)if(a[r][col]){
      int factor=a[r][col];a[r][col]=0;
      for(int k=col+1;k<=C;k++){int v=a[r][k]-product[factor][a[rank][k]];a[r][k]=v<0?v+P:v;}
    }
    pivots.push_back(col);pivot_rows.push_back(original[rank]);rank++;
  }
  rank_base=rank;
  int eval_col=-1;for(int c=0;c<C;c++)if(a[R][c]){eval_col=c;break;}
  cout<<"base_rank="<<rank_base<<" evaluation_increment="<<(eval_col>=0)<<" determinant="<<(swap_sign<0?(P-determinant)%P:determinant)<<"\n";
  if(eval_col<0)throw runtime_error("evaluation is dependent");
  swap(a[rank],a[R]);int s=inv(a[rank][eval_col]);for(int k=eval_col;k<=C;k++)a[rank][k]=product[s][a[rank][k]];
  pivots.push_back(eval_col);rank++;
  vector<int>free_cols;vector<bool>ispivot(C);for(int c:pivots)ispivot[c]=true;
  for(int c=0;c<C;c++)if(!ispivot[c])free_cols.push_back(c);
  mt19937 rng(610028);ofstream samples(root+"/samples97.bin",ios::binary);
  for(int trial=0;trial<32;trial++){
    Row x(C);for(int c:free_cols)x[c]=rng()%P;
    for(int r=rank-1;r>=0;r--){int col=pivots[r],v=a[r][C];for(int k=col+1;k<C;k++)v=(v-product[a[r][k]][x[k]]+P)%P;x[col]=v;}
    samples.write(reinterpret_cast<char*>(x.data()),C);
  }
  ofstream info(root+"/rank97.txt");
  info<<rank_base<<" "<<rank<<" "<<determinant<<" "<<swap_sign<<"\n";
  for(int r:pivot_rows)info<<r<<" ";info<<"\n";
  for(int c:pivots)info<<c<<" ";info<<"\n";
  info<<"extra_eval_original_row "<<R<<"\n";
}
