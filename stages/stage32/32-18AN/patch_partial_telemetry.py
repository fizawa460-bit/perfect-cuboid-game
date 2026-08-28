import os
from pathlib import Path
p=Path(os.environ['SRC']); s=p.read_text()
old='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;'
new='Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); try { e.run(bound,node_cap,dump,shard_id,shard_count,split_i); } catch(const std::runtime_error& ex) { if(std::string(ex.what())=="exact traversal node cap exceeded") { e.write_json(output); std::cerr<<ex.what()<<"\\n"; return 3; } throw; } e.write_json(output); return 0;'
assert s.count(old)==1
s=s.replace(old,new,1)
p.write_text(s)
