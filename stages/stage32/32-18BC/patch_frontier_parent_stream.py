import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    std::ofstream planner_out_;\n    std::vector<uint64_t> planner_ids_;\n'''
new='''    std::ofstream planner_out_;\n    std::vector<uint64_t> planner_ids_;\n    std::ofstream frontier_stream_out_;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                        ++frontier_states_;\n                        if(frontier_states_>frontier_cap_) throw std::runtime_error("block frontier cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));\n                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n'''
new='''                        ++frontier_states_;\n                        if(frontier_states_>frontier_cap_) throw std::runtime_error("block frontier cap exceeded nodes="+std::to_string(nodes_)+" frontier="+std::to_string(frontier_states_)+" replay_started="+std::to_string(replay_started_)+" replay_completed="+std::to_string(replay_completed_)+" replay_nodes="+std::to_string(replay_nodes_));\n                        if(frontier_stream_out_){\n                            frontier_stream_out_<<(frontier_states_-1);\n                            for(int k=block_cut_+1;k<n_;k++) frontier_stream_out_<<","<<z_[k];\n                            frontier_stream_out_<<"\\n";\n                        }\n                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path){\n        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;\n'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path,const std::string& frontier_stream_path){\n        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; block_cut_=block_cut; frontier_cap_=frontier_cap; replay_limit_=replay_limit;\n        if(!frontier_stream_path.empty()){ frontier_stream_out_.open(frontier_stream_path); if(!frontier_stream_out_) throw std::runtime_error("cannot open frontier stream output"); }\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        std::string input,bundle,output,dump,planner_output,planner_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;\n'''
new='''        std::string input,bundle,output,dump,planner_output,planner_id_file,frontier_stream_output; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else throw std::runtime_error("unknown arg "+a);\n'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else if(a=="--frontier-stream-output") frontier_stream_output=need(); else throw std::runtime_error("unknown arg "+a);\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file); e.write_json(output); return 0;\n'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file,frontier_stream_output); e.write_json(output); return 0;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
