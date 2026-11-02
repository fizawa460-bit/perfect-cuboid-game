#include <array>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
const int P=97;
int power(int a,int n){int v=1;while(n){if(n&1)v=v*a%P;a=a*a%P;n/=2;}return v;}
int inv(int a){return power(a,95);}
struct Leg{int j,a,b;};
struct Col{Leg z,w;int f,g;};
struct Point{int r,u,v;};
int mon(Leg l,Point p){return power(p.r,l.j)*power(p.u,l.a)%P*power(p.v,l.b)%P;}
int derivative(Leg l,Point p){int unit=(l.j*inv(p.r)+l.a*power(p.r,3)*inv(2*p.u*p.u%P)+l.b*power(p.r,3)*inv(2*p.v*p.v%P))%P;return mon(l,p)*unit%P;}
int main(int argc,char**argv){
 string root=argv[1];ifstream f(root+"/scan-input97.txt");vector<Col>cols;Col c;
 while(f>>c.z.j>>c.z.a>>c.z.b>>c.w.j>>c.w.a>>c.w.b>>c.f>>c.g)cols.push_back(c);
 if(cols.size()!=1464)return 2;
 vector<Point>pts;
 for(int r=1;r<P;r++)for(int u=1;u<P;u++)if(4*u*u%P==(power(r,4)+4)%P)
  for(int v=1;v<P;v++)if(4*v*v%P==(power(r,4)+P-4)%P)pts.push_back({r,u,v});
 vector<vector<int>>zv(pts.size(),vector<int>(cols.size())),wv=zv;
 for(int k=0;k<(int)pts.size();k++)for(int j=0;j<(int)cols.size();j++){zv[k][j]=mon(cols[j].z,pts[k]);wv[k][j]=mon(cols[j].w,pts[k]);}
 int count=0;cout<<"{\"prime\":97,\"nonbranch_curve_points\":"<<pts.size()<<",\"simple_basepoints\":[";
 for(int z=0;z<(int)pts.size();z++)for(int w=0;w<(int)pts.size();w++){
  int f0=0,g0=0;for(int j=0;j<(int)cols.size();j++){int a=zv[z][j]*wv[w][j]%P;f0=(f0+cols[j].f*a)%P;g0=(g0+cols[j].g*a)%P;}
  if(f0||g0)continue;
  int fz=0,fw=0,gz=0,gw=0;
  for(int j=0;j<(int)cols.size();j++){int a=derivative(cols[j].z,pts[z])*wv[w][j]%P,b=zv[z][j]*derivative(cols[j].w,pts[w])%P;
   fz=(fz+cols[j].f*a)%P;fw=(fw+cols[j].f*b)%P;gz=(gz+cols[j].g*a)%P;gw=(gw+cols[j].g*b)%P;}
  int determinant=(fz*gw-fw*gz+P*P)%P;if(!determinant)continue;
  if(count++)cout<<",";auto a=pts[z],b=pts[w];cout<<"{\"z\":["<<a.r<<","<<a.u<<","<<a.v<<"],\"w\":["<<b.r<<","<<b.u<<","<<b.v<<"],\"values\":[0,0],\"jacobian\":["<<fz<<","<<fw<<","<<gz<<","<<gw<<"],\"determinant\":"<<determinant<<"}";
 }
 cout<<"],\"count\":"<<count<<"}\n";
}
