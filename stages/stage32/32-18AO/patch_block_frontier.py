import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i;
'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");
'''
new='''        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");
        if(block_cut_<0 || block_cut_>=split_i_-1) throw std::runtime_error("bad block cut");
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"status\\\": \\\"COMPLETE\\\",\\n";
'''
new='''        f<<"  \\\"status\\\": \\\"FRONTIER_COMPLETE\\\",\\n";
'''
assert s.count(old)==1
s=s.replace(old,new,1)

anchor='''        f<<"  \\\"owned_prefixes\\\": "<<owned_prefixes_<<",\\n";
'''
add=anchor+'''        f<<"  \\\"block_cut_coordinate\\\": "<<block_cut_<<",\\n";
        f<<"  \\\"frontier_states\\\": "<<frontier_states_<<",\\n";
        f<<"  \\\"frontier_cap\\\": "<<frontier_cap_<<",\\n";
        f<<"  \\\"LOWER_BLOCK_ENUMERATED\\\": false,\\n";
        f<<"  \\\"MITM_JOIN_IMPLEMENTED\\\": false,\\n";
'''
assert s.count(anchor)==1
s=s.replace(anchor,add,1)

old='''    int shard_id_=0,shard_count_=1,split_i_=54; uint64_t split_prefixes_=0,owned_prefixes_=0;
'''
new='''    int shard_id_=0,shard_count_=1,split_i_=54,block_cut_=31; uint64_t split_prefixes_=0,owned_prefixes_=0;
    uint64_t frontier_states_=0,frontier_cap_=2000000;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded");
'''
new='''        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_));
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                if(take) dfs(i-1,used+term);
'''
new='''                if(take){
                    if(i-1==block_cut_){
                        ++frontier_states_;
                        if(frontier_states_>frontier_cap_) throw std::runtime_error("block frontier cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_));
                    } else dfs(i-1,used+term);
                }
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54; uint64_t node_cap=100000000ULL;
'''
new='''        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else throw std::runtime_error("unknown arg "+a);
'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;
'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap); e.write_json(output); return 0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
