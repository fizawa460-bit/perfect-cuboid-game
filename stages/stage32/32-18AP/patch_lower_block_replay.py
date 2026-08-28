import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    uint64_t frontier_states_=0,frontier_cap_=2000000;
'''
new='''    uint64_t frontier_states_=0,frontier_cap_=2000000;
    uint64_t replay_limit_=0,replay_started_=0,replay_completed_=0,replay_nodes_=0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_));
'''
new='''        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                    if(i-1==block_cut_){
                        ++frontier_states_;
                        if(frontier_states_>frontier_cap_) throw std::runtime_error("block frontier cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_));
                    } else dfs(i-1,used+term);
'''
new='''                    if(i-1==block_cut_){
                        ++frontier_states_;
                        if(frontier_states_>frontier_cap_) throw std::runtime_error("block frontier cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));
                        if(replay_started_<replay_limit_){
                            ++replay_started_;
                            uint64_t before=nodes_;
                            dfs(i-1,used+term);
                            replay_nodes_ += nodes_-before;
                            ++replay_completed_;
                        }
                    } else dfs(i-1,used+term);
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"frontier_cap\\\": "<<frontier_cap_<<",\\n";
'''
new=old+'''        f<<"  \\\"replay_limit\\\": "<<replay_limit_<<",\\n";
        f<<"  \\\"replay_started\\\": "<<replay_started_<<",\\n";
        f<<"  \\\"replay_completed\\\": "<<replay_completed_<<",\\n";
        f<<"  \\\"replay_nodes\\\": "<<replay_nodes_<<",\\n";
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap;
'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL;
'''
new='''        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);
'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap); e.write_json(output); return 0;
'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit); e.write_json(output); return 0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
