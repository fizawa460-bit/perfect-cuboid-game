#!/usr/bin/env python3
from __future__ import annotations
import argparse
import pathlib

OLD_SCHEMA="STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
NEW_SCHEMA="STAGE32_18N_D16_EXACT_DESCENDANT_WORK_PROFILE_V1"


def replace_once(text:str, old:str, new:str, label:str)->str:
    n=text.count(old)
    if n!=1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old,new,1)


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    args=ap.parse_args()
    text=args.source.read_text()
    text=replace_once(text,OLD_SCHEMA,NEW_SCHEMA,'schema')

    text=replace_once(text,
'''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i;
        if(shard_count_<1 || shard_id_<0 || shard_id_>=shard_count_) throw std::runtime_error("bad shard parameters");
        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");
''',
'''    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i,int probe_i){
        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i; probe_i_=probe_i;
        if(shard_count_<1 || shard_id_<0 || shard_id_>=shard_count_) throw std::runtime_error("bad shard parameters");
        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");
        if(probe_i_<0 || probe_i_>=split_i_) throw std::runtime_error("bad probe coordinate");
        descendant_nodes_.assign(static_cast<size_t>(shard_count_),0);
        descendant_trials_.assign(static_cast<size_t>(shard_count_),0);
        descendant_constraint_prunes_.assign(static_cast<size_t>(shard_count_),0);
        descendant_symmetry_prunes_.assign(static_cast<size_t>(shard_count_),0);
        descendant_probe_prefixes_.assign(static_cast<size_t>(shard_count_),0);
''','run signature')

    text=replace_once(text,
'    int shard_id_=0,shard_count_=1,split_i_=54; uint64_t split_prefixes_=0,owned_prefixes_=0;\n',
'''    int shard_id_=0,shard_count_=1,split_i_=54,probe_i_=50,active_bucket_=-1; uint64_t split_prefixes_=0,owned_prefixes_=0;
    std::vector<uint64_t> descendant_nodes_,descendant_trials_,descendant_constraint_prunes_,descendant_symmetry_prunes_,descendant_probe_prefixes_;
''','profile members')

    text=replace_once(text,
'                    ++constraint_prunes_; return false;\n',
'                    ++constraint_prunes_; if(active_bucket_>=0) ++descendant_constraint_prunes_[static_cast<size_t>(active_bucket_)]; return false;\n',
'cap prune attribution')

    text=replace_once(text,
'                    if(exact*exact>reach2){ ++symmetry_prunes_; return false; }\n',
'                    if(exact*exact>reach2){ ++symmetry_prunes_; if(active_bucket_>=0) ++descendant_symmetry_prunes_[static_cast<size_t>(active_bucket_)]; return false; }\n',
'symmetry prune attribution')

    text=replace_once(text,
'''    void dfs(int i,const cpp_rational& used){
        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded");
''',
'''    void dfs(int i,const cpp_rational& used){
        if(++nodes_>node_cap_) throw std::runtime_error("exact traversal node cap exceeded");
        if(active_bucket_>=0) ++descendant_nodes_[static_cast<size_t>(active_bucket_)];
''','node attribution')

    text=replace_once(text,
'''        for(long long zi=lo;zi<=hi;zi++){
            ++trials_; cpp_rational ti=cpp_rational(zi)+shift; cpp_rational term=D_[i]*ti*ti;
''',
'''        for(long long zi=lo;zi<=hi;zi++){
            ++trials_; if(active_bucket_>=0) ++descendant_trials_[static_cast<size_t>(active_bucket_)]; cpp_rational ti=cpp_rational(zi)+shift; cpp_rational term=D_[i]*ti*ti;
''','trial attribution')

    old='''            if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem)){
                bool take=true;
                if(shard_count_>1 && i==split_i_){
                    ++split_prefixes_;
                    uint64_t h=1469598103934665603ULL;
                    for(int k=split_i_;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    take=static_cast<int>(h%static_cast<uint64_t>(shard_count_))==shard_id_;
                    if(take) ++owned_prefixes_;
                }
                if(take) dfs(i-1,used+term);
            }
'''
    new='''            if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem)){
                bool take=true;
                int previous_bucket=active_bucket_;
                if(i==split_i_){
                    ++split_prefixes_;
                    uint64_t h=1469598103934665603ULL;
                    for(int k=split_i_;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    active_bucket_=static_cast<int>(h%static_cast<uint64_t>(shard_count_));
                    ++owned_prefixes_;
                }
                if(active_bucket_>=0 && i==probe_i_){
                    ++descendant_probe_prefixes_[static_cast<size_t>(active_bucket_)];
                    take=false;
                }
                if(take) dfs(i-1,used+term);
                active_bucket_=previous_bucket;
            }
'''
    text=replace_once(text,old,new,'descendant DFS attribution and stop')

    text=replace_once(text,
'        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";\n',
'''        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";
        f<<"  \\"descendant_work_profile_only\\": true,\\n";
        f<<"  \\"parent_coordinate\\": "<<split_i_<<",\\n";
        f<<"  \\"probe_coordinate\\": "<<probe_i_<<",\\n";
        f<<"  \\"parent_modulus\\": "<<shard_count_<<",\\n";
        f<<"  \\"descendant_nodes_by_residue\\": ["; for(size_t i=0;i<descendant_nodes_.size();i++){ if(i) f<<","; f<<descendant_nodes_[i]; } f<<"],\\n";
        f<<"  \\"descendant_trials_by_residue\\": ["; for(size_t i=0;i<descendant_trials_.size();i++){ if(i) f<<","; f<<descendant_trials_[i]; } f<<"],\\n";
        f<<"  \\"descendant_constraint_prunes_by_residue\\": ["; for(size_t i=0;i<descendant_constraint_prunes_.size();i++){ if(i) f<<","; f<<descendant_constraint_prunes_[i]; } f<<"],\\n";
        f<<"  \\"descendant_symmetry_prunes_by_residue\\": ["; for(size_t i=0;i<descendant_symmetry_prunes_.size();i++){ if(i) f<<","; f<<descendant_symmetry_prunes_[i]; } f<<"],\\n";
        f<<"  \\"descendant_probe_prefixes_by_residue\\": ["; for(size_t i=0;i<descendant_probe_prefixes_.size();i++){ if(i) f<<","; f<<descendant_probe_prefixes_[i]; } f<<"],\\n";
''','profile JSON')

    text=replace_once(text,
'        f<<"  \\"TRAVERSAL_COMPLETENESS_CERTIFICATE\\": true,\\n";\n',
'''        f<<"  \\"DESCENDANT_WORK_PROFILE_COMPLETE\\": true,\\n";
        f<<"  \\"FULL_BOUND_TRAVERSAL_COMPLETE\\": false,\\n";
        f<<"  \\"TRAVERSAL_COMPLETENESS_CERTIFICATE\\": false,\\n";
        f<<"  \\"NUMERICAL_CREDIT\\": false,\\n";
''','profile firewall')

    text=replace_once(text,
'        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54; uint64_t node_cap=100000000ULL;\n',
'        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54,probe_i=50; uint64_t node_cap=100000000ULL;\n',
'main vars')

    text=replace_once(text,
'else if(a=="--split-coordinate") split_i=std::stoi(need()); else throw std::runtime_error("unknown arg "+a);\n',
'else if(a=="--split-coordinate") split_i=std::stoi(need()); else if(a=="--probe-coordinate") probe_i=std::stoi(need()); else throw std::runtime_error("unknown arg "+a);\n',
'probe arg')

    text=replace_once(text,
'e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;\n',
'e.run(bound,node_cap,dump,shard_id,shard_count,split_i,probe_i); e.write_json(output); return 0;\n',
'run call')

    args.output.write_text(text)
    print({'schema':NEW_SCHEMA,'parent_coordinate_cli':True,'probe_coordinate_cli':True,'per_parent_residue_exact_work':True})


if __name__=='__main__':
    main()
