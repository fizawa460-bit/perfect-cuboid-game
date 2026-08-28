#!/usr/bin/env python3
import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()
perm=[0,1,2,3,4,5,6,7,8,9,10,11,12,16,17,18,19,20,24,25,26,27,29,15,21,31,22,32,38,39,47,23,30,46,14,13,41,33,40,35,42,28,34,37,36,45,43,44]+list(range(48,63))
assert sorted(perm)==list(range(63))
assert perm[48:]==list(range(48,63))
plist=','.join(map(str,perm))
lower=','.join(map(str,perm[:48]))

anchor='static long long floor_rat(const cpp_rational& x){\n'
assert s.count(anchor)==1
helper=f'''static void apply_lower48_activity_permutation(Problem& p, Bundle& s){{
    static const int perm[63] = {{{plist}}};
    for(int i=48;i<63;i++) if(perm[i]!=i) throw std::runtime_error("partition coordinate moved");
    auto q0=p.q; auto plin0=p.lin; auto slin0=s.lin;
    for(int i=0;i<63;i++) for(int j=0;j<63;j++) p.q[i][j]=q0[perm[i]][perm[j]];
    for(int r=0;r<p.m;r++) for(int i=0;i<63;i++) p.lin[r][i]=plin0[r][perm[i]];
    for(int r=0;r<s.k;r++) for(int i=0;i<63;i++) s.lin[r][i]=slin0[r][perm[i]];
}}

'''
s=s.replace(anchor,helper+anchor,1)
old='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
new='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); apply_lower48_activity_permutation(p,s); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
assert s.count(old)==1
s=s.replace(old,new,1)
meta='        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";\n'
assert s.count(meta)==1
extra=(meta+
       '        f<<"  \\"coordinate_order_redirection\\": \\"lower48_cap_activity_v1\\",\\n";\n'+
       '        f<<"  \\"coordinate_relabeling_semantics_only\\": true,\\n";\n'+
       '        f<<"  \\"partition_coordinates_48_62_fixed\\": true,\\n";\n'+
       f'        f<<"  \\"lower48_permutation\\": [{lower}],\\n";\n')
s=s.replace(meta,extra,1)
p.write_text(s)
