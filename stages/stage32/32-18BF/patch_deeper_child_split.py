import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''    std::vector<uint64_t> child_split_ids_; std::ofstream child_split_out_;\n'''
new=old+'''    bool deep_split_enabled_=false,deep_parent_mode_=false,deep_grandchild_mode_=false;\n    uint64_t deep_split_probe_budget_=0,deep_split_z39_=0,deep_split_parent_id_=0;\n    uint64_t deep_split_parents_seen_=0,deep_split_target_children_seen_=0,deep_split_grandchildren_=0,deep_split_completed_=0,deep_split_capped_=0;\n    uint64_t deep_split_grandchild_index_=0,deep_split_parent_target_seen_=0; bool deep_split_parent_all_complete_=true;\n    std::vector<uint64_t> deep_split_ids_; std::ofstream deep_split_out_;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                        bool child_split_selected = child_split_enabled_ && std::binary_search(child_split_ids_.begin(),child_split_ids_.end(),frontier_states_-1);\n                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n                        if(child_split_selected){\n'''
new='''                        bool deep_split_selected = deep_split_enabled_ && std::binary_search(deep_split_ids_.begin(),deep_split_ids_.end(),frontier_states_-1);\n                        bool child_split_selected = child_split_enabled_ && std::binary_search(child_split_ids_.begin(),child_split_ids_.end(),frontier_states_-1);\n                        bool planner_selected = planner_enabled_ && (planner_ids_.empty() || std::binary_search(planner_ids_.begin(),planner_ids_.end(),frontier_states_-1));\n                        if(deep_split_selected){\n                            ++deep_split_parents_seen_; deep_split_parent_id_=frontier_states_-1; deep_split_grandchild_index_=0;\n                            deep_split_parent_target_seen_=0; deep_split_parent_all_complete_=true; deep_parent_mode_=true;\n                            dfs(i-1,used+term);\n                            deep_parent_mode_=false;\n                            deep_split_out_<<"PARENT,"<<deep_split_parent_id_<<","<<deep_split_z39_<<","<<deep_split_grandchild_index_<<",0,0,"<<(deep_split_parent_all_complete_?1:0)<<","<<deep_split_parent_target_seen_<<"\\n";\n                        } else if(child_split_selected){\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''                    } else if(child_split_mode_ && i==block_cut_){\n'''
new='''                    } else if(deep_parent_mode_ && i==block_cut_){\n                        if(static_cast<uint64_t>(zi)==deep_split_z39_){\n                            ++deep_split_target_children_seen_; ++deep_split_parent_target_seen_;\n                            deep_grandchild_mode_=true; dfs(i-1,used+term); deep_grandchild_mode_=false;\n                        }\n                    } else if(deep_grandchild_mode_ && i==block_cut_-1){\n                        uint64_t saved_budget=planner_probe_budget_;\n                        planner_local_nodes_=0; planner_probe_capped_=false; planner_probe_budget_=deep_split_probe_budget_; planner_mode_=true;\n                        dfs(i-1,used+term);\n                        planner_mode_=false; planner_probe_budget_=saved_budget;\n                        bool complete=!planner_probe_capped_; uint64_t gi=deep_split_grandchild_index_++; ++deep_split_grandchildren_;\n                        if(complete) ++deep_split_completed_; else { ++deep_split_capped_; deep_split_parent_all_complete_=false; }\n                        deep_split_out_<<"GRANDCHILD,"<<deep_split_parent_id_<<","<<deep_split_z39_<<","<<gi<<","<<zi<<","<<planner_local_nodes_<<","<<(complete?1:0)<<",1\\n";\n                    } else if(child_split_mode_ && i==block_cut_){\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"child_split_capped_children\\\": "<<child_split_capped_children_<<",\\n";\n'''
new=old+'''        f<<"  \\\"deep_split_enabled\\\": "<<(deep_split_enabled_?"true":"false")<<",\\n";\n        f<<"  \\\"deep_split_selected_ids\\\": "<<deep_split_ids_.size()<<",\\n";\n        f<<"  \\\"deep_split_z39\\\": "<<deep_split_z39_<<",\\n";\n        f<<"  \\\"deep_split_probe_budget\\\": "<<deep_split_probe_budget_<<",\\n";\n        f<<"  \\\"deep_split_parents_seen\\\": "<<deep_split_parents_seen_<<",\\n";\n        f<<"  \\\"deep_split_target_children_seen\\\": "<<deep_split_target_children_seen_<<",\\n";\n        f<<"  \\\"deep_split_grandchildren\\\": "<<deep_split_grandchildren_<<",\\n";\n        f<<"  \\\"deep_split_completed\\\": "<<deep_split_completed_<<",\\n";\n        f<<"  \\\"deep_split_capped\\\": "<<deep_split_capped_<<",\\n";\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path,uint64_t child_split_probe_budget,const std::string& child_split_path,const std::string& child_split_id_path){\n'''
new='''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int block_cut,uint64_t frontier_cap,uint64_t replay_limit,uint64_t planner_probe_budget,const std::string& planner_path,const std::string& planner_id_path,uint64_t child_split_probe_budget,const std::string& child_split_path,const std::string& child_split_id_path,uint64_t deep_split_probe_budget,const std::string& deep_split_path,const std::string& deep_split_id_path,uint64_t deep_split_z39){\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

anchor='''            child_split_out_<<"record,parent_id,child_index,z_value,probe_nodes,complete\\n"; child_split_enabled_=true;\n        }\n'''
add=anchor+'''        deep_split_probe_budget_=deep_split_probe_budget; deep_split_z39_=deep_split_z39;\n        if(!deep_split_id_path.empty()){\n            std::ifstream ids(deep_split_id_path); if(!ids) throw std::runtime_error("cannot open deep split id file");\n            uint64_t id=0; while(ids>>id) deep_split_ids_.push_back(id);\n            std::sort(deep_split_ids_.begin(),deep_split_ids_.end());\n            deep_split_ids_.erase(std::unique(deep_split_ids_.begin(),deep_split_ids_.end()),deep_split_ids_.end());\n            if(deep_split_ids_.empty() || deep_split_ids_.back()>=5000) throw std::runtime_error("bad deep split id file");\n            if(deep_split_path.empty() || deep_split_probe_budget_==0) throw std::runtime_error("deep split output/budget required");\n            deep_split_out_.open(deep_split_path); if(!deep_split_out_) throw std::runtime_error("cannot open deep split output");\n            deep_split_out_<<"record,parent_id,z39,grandchild_index,z38,probe_nodes,complete,target_child_seen\\n"; deep_split_enabled_=true;\n        }\n'''
assert s.count(anchor)==1
s=s.replace(anchor,add,1)

old='''        std::string input,bundle,output,dump,planner_output,planner_id_file,child_split_output,child_split_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL,child_split_probe_budget=0ULL;\n'''
new='''        std::string input,bundle,output,dump,planner_output,planner_id_file,child_split_output,child_split_id_file,deep_split_output,deep_split_id_file; int bound=6,shard_id=0,shard_count=1,split_i=54,block_cut=31; uint64_t node_cap=100000000ULL,frontier_cap=2000000ULL,replay_limit=0ULL,planner_probe_budget=0ULL,child_split_probe_budget=0ULL,deep_split_probe_budget=0ULL,deep_split_z39=0ULL;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else if(a=="--child-split-probe-budget") child_split_probe_budget=std::stoull(need()); else if(a=="--child-split-output") child_split_output=need(); else if(a=="--child-split-id-file") child_split_id_file=need(); else throw std::runtime_error("unknown arg "+a);\n'''
new='''else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--block-cut") block_cut=std::stoi(need()); else if(a=="--frontier-cap") frontier_cap=std::stoull(need()); else if(a=="--replay-limit") replay_limit=std::stoull(need()); else if(a=="--planner-probe-budget") planner_probe_budget=std::stoull(need()); else if(a=="--planner-output") planner_output=need(); else if(a=="--planner-id-file") planner_id_file=need(); else if(a=="--child-split-probe-budget") child_split_probe_budget=std::stoull(need()); else if(a=="--child-split-output") child_split_output=need(); else if(a=="--child-split-id-file") child_split_id_file=need(); else if(a=="--deep-split-probe-budget") deep_split_probe_budget=std::stoull(need()); else if(a=="--deep-split-output") deep_split_output=need(); else if(a=="--deep-split-id-file") deep_split_id_file=need(); else if(a=="--deep-split-z39") deep_split_z39=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file,child_split_probe_budget,child_split_output,child_split_id_file); e.write_json(output); return 0;\n'''
new='''        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i,block_cut,frontier_cap,replay_limit,planner_probe_budget,planner_output,planner_id_file,child_split_probe_budget,child_split_output,child_split_id_file,deep_split_probe_budget,deep_split_output,deep_split_id_file,deep_split_z39); e.write_json(output); return 0;\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
