import os
from pathlib import Path
p=Path(os.environ['SRC'])
s=p.read_text()
limit=int(os.environ.get('PAIR_LIMIT','6'))
ratio=os.environ.get('PAIR_RATIO','0.20')
assert 2 <= limit <= 32
old='''    uint64_t exact_prune_checks_=0,constraint_prunes_=0,exact_symmetry_prune_checks_=0,symmetry_prunes_=0;\n'''
new='''    uint64_t exact_prune_checks_=0,constraint_prunes_=0,exact_symmetry_prune_checks_=0,symmetry_prunes_=0;\n    uint64_t pairwise_symmetry_checks_=0,pairwise_symmetry_prunes_=0;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)
anchor='''    bool is_canonical(const std::array<unsigned char,140>& pairing)const{\n'''
fn=f'''    bool pairwise_symmetry_possible(int last_remaining,const cpp_rational& budget) {{
        if(last_remaining<0 || budget<=0) return true;
        const long double bf=std::max<long double>(0,budget.convert_to<long double>());
        struct Cand{{ int r; long double severity; }};
        std::vector<Cand> cand; cand.reserve(32);
        for(int r=0;r<s_.k;r++){{
            long double center=static_cast<long double>(s_.c0[r])+sym_assignedf_[r];
            if(center>=0) continue;
            long double dual=sym_dualf_[r][last_remaining];
            if(dual<=0) continue;
            long double reach=std::sqrt(std::max<long double>(0,bf*dual));
            if(reach<=0) continue;
            long double sev=(-center)/reach;
            if(sev>{ratio}L) cand.push_back({{r,sev}});
        }}
        std::sort(cand.begin(),cand.end(),[](const Cand&a,const Cand&b){{
            if(a.severity!=b.severity) return a.severity>b.severity;
            return a.r<b.r;
        }});
        if(cand.size()>{limit}) cand.resize({limit});
        for(size_t x=0;x<cand.size();x++) for(size_t y=x+1;y<cand.size();y++){{
            int r=cand[x].r, q=cand[y].r; ++pairwise_symmetry_checks_;
            cpp_rational cr=exact_center(s_.c0[r],sym_a_[r],last_remaining);
            cpp_rational cq=exact_center(s_.c0[q],sym_a_[q],last_remaining);
            if(cr>=0 || cq>=0) continue;
            cpp_rational d1=-cr,d2=-cq;
            cpp_rational g11=sym_dual_[r][last_remaining],g22=sym_dual_[q][last_remaining],g12=0;
            for(int j=0;j<=last_remaining;j++) g12+=sym_a_[r][j]*sym_a_[q][j]/D_[j];
            cpp_rational det=g11*g22-g12*g12;
            if(det<=0) continue;
            cpp_rational lam1=(d1*g22-d2*g12)/det;
            cpp_rational lam2=(d2*g11-d1*g12)/det;
            if(lam1<=0 || lam2<=0) continue;
            cpp_rational need=d1*lam1+d2*lam2;
            if(need>budget){{ ++pairwise_symmetry_prunes_; return false; }}
        }}
        return true;
    }}

'''
assert s.count(anchor)==1
s=s.replace(anchor,fn+anchor,1)
# Parent namespace invariant: at the cut39 recording boundary the branch must be
# accepted/rejected by exactly the baseline predicates. Pairwise KKT pruning is
# allowed only after recursion has entered strictly below the recorded parent.
old_branch='''if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem)){'''
new_branch='''if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem) && ((i-1)>=block_cut_ || pairwise_symmetry_possible(i-1,newrem))){'''
assert s.count(old_branch)==1
s=s.replace(old_branch,new_branch,1)
meta='''        f<<"  \\\"exact_symmetry_prunes\\\": "<<symmetry_prunes_<<",\\n";\n'''
add=meta+f'''        f<<"  \\\"pairwise_symmetry_exact_gram_kkt\\\": true,\\n";\n        f<<"  \\\"pairwise_parent_partition_stable\\\": true,\\n";\n        f<<"  \\\"pairwise_strictly_below_block_cut\\\": true,\\n";\n        f<<"  \\\"pairwise_candidate_limit\\\": {limit},\\n";\n        f<<"  \\\"pairwise_schedule_ratio\\\": {ratio},\\n";\n        f<<"  \\\"pairwise_symmetry_checks\\\": "<<pairwise_symmetry_checks_<<",\\n";\n        f<<"  \\\"pairwise_symmetry_prunes\\\": "<<pairwise_symmetry_prunes_<<",\\n";\n'''
assert s.count(meta)==1
s=s.replace(meta,add,1)
p.write_text(s)
