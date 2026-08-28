import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    std::vector<uint64_t> planner_ids_;\n'''
new='''    std::vector<uint64_t> planner_ids_;\n    bool child_split_enabled_=false,child_split_mode_=false;\n    uint64_t child_split_probe_budget_=0,child_split_parent_id_=0,child_split_parent_nodes_=0;\n    uint64_t child_split_parents_seen_=0,child_split_children_=0,child_split_completed_children_=0,child_split_capped_children_=0;\n    uint64_t child_split_child_index_=0; bool child_split_parent_all_complete_=true;\n    std::vector<uint64_t> child_split_ids_; std::ofstream child_split_out_;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n                        if(planner_selected){\n'''
new='''                        bool child_split_selected = child_split_enabled_ && std::binary_search(child_split_ids_.begin(),child_split_ids_.end(),frontier_states_-1);\n                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n                        if(child_split_selected){\n                            ++child_split_parents_seen_; child_split_parent_id_=frontier_states_-1; child_split_parent_nodes_=0;\n                            child_split_child_index_=0; child_split_parent_all_complete_=true; child_split_mode_=true;\n                            dfs(i-1,used+term);\n                            child_split_mode_=false;\n                            child_split_out_<<"PARENT,"<<child_split_parent_id_<<","<<child_split_child_index_<<",0,"<<child_split_parent_nodes_<<","<<(child_split_parent_all_complete_?1:0)<<"\\n";\n                        } else if(planner_selected){\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                    } else dfs(i-1,used+term);\n'''
new='''                    } else if(child_split_mode_ && i==block_cut_){\n                        uint64_t saved_budget=planner_probe_budget_;\n                        planner_local_nodes_=0; planner_probe_capped_=false; planner_probe_budget_=child_split_probe_budget_; planner_mode_=true;\n                        dfs(i-1,used+term);\n                        planner_mode_=false; planner_probe_budget_=saved_budget;\n                        bool complete=!planner_probe_capped_;\n                        uint64_t ci=child_split_child_index_++; child_split_parent_nodes_+=planner_local_nodes_; ++child_split_children_;\n                        if(complete) ++child_split_completed_children_; else { ++child_split_capped_children_; child_split_parent_all_complete_=false; }\n                        child_split_out_<<"CHILD,"<<child_split_parent_id_<<","<<ci<<","<<zi<<","<<planner_local_nodes_<<","<<(complete?1:0)<<"\\n";\n                    } else dfs(i-1,used+term);\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"planner_selected_ids\\\": "<<planner_ids_.size()<<",\\n";\n'''
new=old+'''        f<<"  \\\"child_split_enabled\\\": "<<(child_split_enabled_?"true":"false")<<",\\n";\n        f<<"  \\\"child_split_selected_ids\\\": "<<child_split_ids_.size()<<",\\n";\n        f<<"  \\\"child_split_probe_budget\\\": "<<child_split_probe_budget_<<",\\n";\n        f<<"  \\\"child_split_parents_seen\\\": "<<child_split_parents_seen_<<",\\n";\n        f<<"  \\\"child_split_children\\\": "<<child_split_children_<<",\\n";\n        f<<"  \\\"child_split_completed_children\\\": "<<child_split_completed_children_<<",\\n";\n        f<<"  \\\"child_split_capped_children\\\": "<<child_split_capped_children_<<",\\n";\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path){\n'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path,uint64_t child_split_probe_budget,const std::string& child_split_path,const std::string& child_split_id_path){\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

anchor='''            if(planner_ids_.back()>=5000) throw std::runtime_error("planner id out of range");\n        }\n'''
add=anchor+'''        child_split_probe_budget_=child_split_probe_budget;\n        if(!child_split_id_path.empty()){\n            std::ifstream ids(child_split_id_path); if(!ids) throw std::runtime_error("cannot open child split id file");\n            uint64_t id=0; while(ids>>id) child_split_ids_.push_back(id);\n            std::sort(child_split_ids_.begin(),child_split_ids_.end());\n            child_split_ids_.erase(std::unique(child_split_ids_.begin(),child_split_ids_.end()),child_split_ids_.end());\n            if(child_split_ids_.empty() || child_split_ids_.back()>=5000) throw std::runtime_error("bad child split id file");\n            if(child_split_path.empty() || child_split_probe_budget_==0) throw std::runtime_error("child split output/budget required");\n            child_split_out_.open(child_split_path); if(!child_split_out_) throw std::runtime_error("cannot open child split output");\n            child_split_out_<<"record,parent_id,child_index,z_value,probe_nodes,complete\\n"; child_split_enabled_=true;\n        }\n'''
assert s.count(anchor)==1
s=s.replace(anchor,add,1)

old='''        std::string input,bundle,output,dump,planner_output,planner_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL;\n'''
new='''        std::string input,bundle,output,dump,planner_output,planner_id_file,child_split_output,child_split_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL,child_split_probe_budget=0ULL;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else throw std::runtime_error("unknown arg "+a);\n'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else if(a=="--child-split-probe-budget") child_split_probe_budget=std::stoull(need()); else if(a=="--child-split-output") child_split_output=need(); else if(a=="--child-split-id-file") child_split_id_file=need(); else throw std::runtime_error("unknown arg "+a);\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file); e.write_json(output); return 0;\n'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file,child_split_probe_budget,child_split_output,child_split_id_file); e.write_json(output); return 0;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
