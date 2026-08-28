import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    uint64_t replay_limit_=0,replay_started_=0,replay_completed_=0,replay_nodes_=0;
'''
new=old+'''    bool planner_enabled_=false,planner_mode_=false,planner_probe_capped_=false;
    uint64_t planner_probe_budget_=0,planner_local_nodes_=0,planner_total_nodes_=0,planner_completed_=0,planner_capped_=0;
    std::ofstream planner_out_;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));
'''
new='''        if(planner_mode_){
            if(planner_probe_capped_) return;
            if(planner_local_nodes_>=planner_probe_budget_){ planner_probe_capped_=true; return; }
            ++planner_local_nodes_; ++planner_total_nodes_;
        } else {
            if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));
        }
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                        if(replay_started_<replay_limit_){
                            ++replay_started_;
                            uint64_t before=nodes_;
                            dfs(i-1,used+term);
                            replay_nodes_ += nodes_-before;
                            ++replay_completed_;
                        }
'''
new='''                        if(planner_enabled_){
                            planner_local_nodes_=0;
                            planner_probe_capped_=false;
                            planner_mode_=true;
                            dfs(i-1,used+term);
                            planner_mode_=false;
                            bool complete=!planner_probe_capped_;
                            if(complete) ++planner_completed_; else ++planner_capped_;
                            planner_out_<<(frontier_states_-1)<<","<<planner_local_nodes_<<","<<(complete?1:0)<<"\\n";
                        } else if(replay_started_<replay_limit_){
                            ++replay_started_;
                            uint64_t before=nodes_;
                            dfs(i-1,used+term);
                            replay_nodes_ += nodes_-before;
                            ++replay_completed_;
                        }
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"replay_nodes\\\": "<<replay_nodes_<<",\\n";
'''
new=old+'''        f<<"  \\\"planner_probe_budget\\\": "<<planner_probe_budget_<<",\\n";
        f<<"  \\\"planner_total_nodes\\\": "<<planner_total_nodes_<<",\\n";
        f<<"  \\\"planner_completed\\\": "<<planner_completed_<<",\\n";
        f<<"  \\\"planner_capped\\\": "<<planner_capped_<<",\\n";
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;
'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;
        planner_probe_budget_=planner_probe_budget; planner_enabled_=!planner_path.empty();
        if(planner_enabled_){
            if(planner_probe_budget_==0) throw std::runtime_error("planner probe budget must be positive");
            planner_out_.open(planner_path);
            if(!planner_out_) throw std::runtime_error("cannot open planner output");
            planner_out_<<"frontier_id,probe_nodes,complete\\n";
        }
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL;
'''
new='''        std::string input,bundle,output,dump,planner_output; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);
'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else throw std::runtime_error("unknown arg "+a);
'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit); e.write_json(output); return 0;
'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output); e.write_json(output); return 0;
'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
