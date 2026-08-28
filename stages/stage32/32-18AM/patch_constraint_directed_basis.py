import os
from pathlib import Path
p=Path(os.environ['SRC'])
s=p.read_text()
mode=os.environ['MODE']
modes={'window2','window4','window8','global','cap-forward','cap-reverse','sym-forward','sym-reverse','mixed-forward','mixed-reverse','mixed-zigzag','mixed-two-pass'}
assert mode in modes
anchor='static long long floor_rat(const cpp_rational& x){\n'
assert s.count(anchor)==1
helper=r'''static long long nearest_div18am(long long a,long long b){
    if(b<=0) throw std::runtime_error("nonpositive diagonal");
    long long k=llround(-static_cast<long double>(a)/static_cast<long double>(b));
    if(k>3) k=3; if(k<-3) k=-3; return k;
}
static void shear18am(Problem& p,Bundle& s,int i,int j,long long k){
    if(i<0||i>=48||j<0||j>=48||i==j||k==0) return;
    auto qii=p.q[i][i],qij=p.q[i][j],qjj=p.q[j][j];
    for(int r=0;r<63;r++) if(r!=i){ auto v=p.q[r][i]+k*p.q[r][j]; p.q[r][i]=v; p.q[i][r]=v; }
    p.q[i][i]=qii+2*k*qij+k*k*qjj;
    for(int r=0;r<p.m;r++) p.lin[r][i]+=k*p.lin[r][j];
    for(int r=0;r<s.k;r++) s.lin[r][i]+=k*s.lin[r][j];
}
static long double activity18am(const Problem& p,const Bundle& s,int j,int kind){
    long double a=0;
    if(kind==1||kind==3) for(int r=0;r<p.m;r++) a+=fabsl(static_cast<long double>(p.lin[r][j]));
    if(kind==2||kind==3) for(int r=0;r<s.k;r++) a+=fabsl(static_cast<long double>(s.lin[r][j]));
    return a;
}
static bool reduce18am(Problem& p,Bundle& s,int i,int dir,int window,int kind){
    int bj=-1; long long bk=0; long double best=-1;
    for(int j=0;j<48;j++){
        if(j==i) continue;
        if(dir>0 && j>=i) continue; if(dir<0 && j<=i) continue;
        if(window>0 && std::abs(i-j)>window) continue;
        long long k=nearest_div18am(p.q[i][j],p.q[j][j]); if(!k) continue;
        auto cand=p.q[i][i]+2*k*p.q[i][j]+k*k*p.q[j][j];
        if(cand>=p.q[i][i]) continue;
        long double gain=(p.q[i][i]-cand).convert_to<long double>();
        long double score=gain*(1.0L+1e-9L*activity18am(p,s,j,kind));
        if(score>best){best=score;bj=j;bk=k;}
    }
    if(bj>=0){shear18am(p,s,i,bj,bk);return true;} return false;
}
static void apply18am(Problem& p,Bundle& s,const std::string& mode){
    int window=0,kind=0; bool rev=false,zig=false,two=false;
    if(mode=="window2") window=2; else if(mode=="window4") window=4; else if(mode=="window8") window=8; else if(mode=="global") window=0;
    else if(mode=="cap-forward") kind=1; else if(mode=="cap-reverse"){kind=1;rev=true;}
    else if(mode=="sym-forward") kind=2; else if(mode=="sym-reverse"){kind=2;rev=true;}
    else if(mode=="mixed-forward") kind=3; else if(mode=="mixed-reverse"){kind=3;rev=true;}
    else if(mode=="mixed-zigzag"){kind=3;zig=true;} else if(mode=="mixed-two-pass"){kind=3;two=true;}
    auto sweep=[&](bool r){ if(!r){for(int i=1;i<48;i++) reduce18am(p,s,i,1,window,kind);} else {for(int i=46;i>=0;i--) reduce18am(p,s,i,-1,window,kind);} };
    if(zig){ for(int i=1;i<48;i+=2) reduce18am(p,s,i,1,0,3); for(int i=46;i>=0;i-=2) reduce18am(p,s,i,-1,0,3); }
    else if(two){ sweep(false); sweep(true); }
    else sweep(rev);
}
'''
s=s.replace(anchor,helper+anchor,1)
old='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
new=f'Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); apply18am(p,s,"{mode}"); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
assert s.count(old)==1
s=s.replace(old,new,1)
meta='        f<<"  \\\"split_coordinate\\\": "<<split_i_<<",\\n";\n'
assert s.count(meta)==1
s=s.replace(meta,meta+f'        f<<"  \\\"breakthrough_scout_mode\\\": \\\"{mode}\\\",\\n";\n        f<<"  \\\"partition_coordinates_48_62_fixed\\\": true,\\n";\n        f<<"  \\\"integer_lattice_bijection\\\": true,\\n";\n',1)
p.write_text(s)
