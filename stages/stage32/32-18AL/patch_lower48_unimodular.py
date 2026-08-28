import os
from pathlib import Path
p=Path(os.environ['SRC'])
s=p.read_text()
mode=os.environ['BASIS_MODE']
assert mode in {'forward-greedy','reverse-greedy','alternating2'}
anchor='static long long floor_rat(const cpp_rational& x){\n'
assert s.count(anchor)==1
helper=r'''static long long nearest_div_ll(long long a,long long b){
    if(b<=0) throw std::runtime_error("nonpositive diagonal in basis reduction");
    long double x=-static_cast<long double>(a)/static_cast<long double>(b);
    long long k=llround(x);
    if(k>2) k=2; if(k<-2) k=-2;
    return k;
}

static void elementary_lower48_shear(Problem& p, Bundle& s, int i, int j, long long k){
    if(i<0||i>=48||j<0||j>=48||i==j||k==0) return;
    auto qii=p.q[i][i], qij=p.q[i][j], qjj=p.q[j][j];
    for(int r=0;r<63;r++) if(r!=i){
        auto v=p.q[r][i] + k*p.q[r][j];
        p.q[r][i]=v; p.q[i][r]=v;
    }
    p.q[i][i]=qii + 2*k*qij + k*k*qjj;
    for(int r=0;r<p.m;r++) p.lin[r][i]+=k*p.lin[r][j];
    for(int r=0;r<s.k;r++) s.lin[r][i]+=k*s.lin[r][j];
}

static bool greedy_reduce_one(Problem& p, Bundle& s, int i, bool reverse){
    long long bestk=0; int bestj=-1; auto best=p.q[i][i];
    for(int j=0;j<48;j++){
        if(j==i) continue;
        if(!reverse && j>=i) continue;
        if(reverse && j<=i) continue;
        long long k=nearest_div_ll(p.q[i][j],p.q[j][j]);
        if(k==0) continue;
        auto cand=p.q[i][i]+2*k*p.q[i][j]+k*k*p.q[j][j];
        if(cand<best){ best=cand; bestj=j; bestk=k; }
    }
    if(bestj>=0){ elementary_lower48_shear(p,s,i,bestj,bestk); return true; }
    return false;
}

static void apply_lower48_unimodular_basis(Problem& p, Bundle& s, const std::string& mode){
    if(mode=="forward-greedy"){
        for(int i=1;i<48;i++) greedy_reduce_one(p,s,i,false);
    }else if(mode=="reverse-greedy"){
        for(int i=46;i>=0;i--) greedy_reduce_one(p,s,i,true);
    }else if(mode=="alternating2"){
        for(int pass=0;pass<2;pass++){
            for(int i=1;i<48;i++) greedy_reduce_one(p,s,i,false);
            for(int i=46;i>=0;i--) greedy_reduce_one(p,s,i,true);
        }
    }else throw std::runtime_error("unknown lower48 basis mode");
}

'''
s=s.replace(anchor,helper+anchor,1)
old='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
new=f'Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); apply_lower48_unimodular_basis(p,s,"{mode}"); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
assert s.count(old)==1
s=s.replace(old,new,1)
meta='        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";\n'
assert s.count(meta)==1
extra=meta+f'        f<<"  \\"lower48_unimodular_basis\\": \\"{mode}\\",\\n";\n        f<<"  \\"partition_coordinates_48_62_fixed\\": true,\\n";\n        f<<"  \\"integer_lattice_bijection\\": true,\\n";\n'
s=s.replace(meta,extra,1)
p.write_text(s)
