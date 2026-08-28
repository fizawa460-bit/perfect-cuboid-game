import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    std::ofstream planner_out_;
'''
new='''    std::ofstream planner_out_;
    std::vector<uint64_t> planner_ids_;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                        if(planner_enabled_){
                            planner_local_nodes_=0;
'''
new='''                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));
                        if(planner_selected){
                            planner_local_nodes_=0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;
        planner_probe_budget_=planner_probe_budget; planner_enabled_=!planner_path.empty();
'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;
        planner_probe_budget_=planner_probe_budget; planner_enabled_=!planner_path.empty();
        if(!planner_id_path.empty()){
            std::ifstream ids(planner_id_path);
            if(!ids) throw std::runtime_error("cannot open planner id file");
            uint64_t id=0;
            while(ids>>id) planner_ids_.push_back(id);
            std::sort(planner_ids_.begin(),planner_ids_.end());
            planner_ids_.erase(std::unique(planner_ids_.begin(),planner_ids_.end()),planner_ids_.end());
            if(planner_ids_.empty()) throw std::runtime_error("empty planner id file");
            if(planner_ids_.back()>=5000) throw std::runtime_error("planner id out of range");
        }
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"planner_capped\\\": "<<planner_capped_<<",\\n";
'''
new=old+'''        f<<"  \\\"planner_selected_ids\\\": "<<planner_ids_.size()<<",\\n";
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        std::string input,bundle,output,dump,planner_output; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;
'''
new='''        std::string input,bundle,output,dump,planner_output,planner_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else throw std::runtime_error("unknown arg "+a);
'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else throw std::runtime_error("unknown arg "+a);
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output); e.write_json(output); return 0;
'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file); e.write_json(output); return 0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
