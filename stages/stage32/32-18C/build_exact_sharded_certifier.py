#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib

OLD_SCHEMA="STAGE32_18A_D16_EXACT_B6_TRAVERSAL_CERT_V1"
NEW_SCHEMA="STAGE32_18C_D16_EXACT_SHARDED_TRAVERSAL_CERT_V1"
OLD_LOCK='        if(bound!=6) throw std::runtime_error("Stage32-18A certifier is intentionally locked to b6");\n'

def replace_once(text:str, old:str, new:str, label:str)->str:
    n=text.count(old)
    if n!=1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old,new,1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=pathlib.Path,required=True)
    ap.add_argument("--output",type=pathlib.Path,required=True)
    args=ap.parse_args()
    text=args.source.read_text()
    text=replace_once(text,OLD_SCHEMA,NEW_SCHEMA,"schema")
    text=replace_once(text,OLD_LOCK,"","b6 lock")
    text=replace_once(
        text,
        '    void run(int bound,uint64_t node_cap,const std::string& dump_path){\n        bound_=bound; node_cap_=node_cap;\n',
        '    void run(int bound,uint64_t node_cap,const std::string& dump_path,int shard_id,int shard_count,int split_i){\n'
        '        bound_=bound; node_cap_=node_cap; shard_id_=shard_id; shard_count_=shard_count; split_i_=split_i;\n'
        '        if(shard_count_<1 || shard_id_<0 || shard_id_>=shard_count_) throw std::runtime_error("bad shard parameters");\n'
        '        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");\n',
        "run signature")
    text=replace_once(
        text,
        '    uint64_t nodes_=0,trials_=0,leaves_=0,cap_survivors_=0,precanonical_=0,canonical_rejects_=0,canonical_=0,canonical_nonzero_=0;\n',
        '    int shard_id_=0,shard_count_=1,split_i_=54; uint64_t split_prefixes_=0,owned_prefixes_=0;\n'
        '    uint64_t nodes_=0,trials_=0,leaves_=0,cap_survivors_=0,precanonical_=0,canonical_rejects_=0,canonical_=0,canonical_nonzero_=0;\n',
        "member insertion")
    text=replace_once(
        text,
        '        f<<"  \\"exact_symmetry_prunes\\": 0,\\n";\n',
        '        f<<"  \\"exact_symmetry_prunes\\": 0,\\n";\n'
        '        f<<"  \\"shard_id\\": "<<shard_id_<<",\\n";\n'
        '        f<<"  \\"shard_count\\": "<<shard_count_<<",\\n";\n'
        '        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";\n'
        '        f<<"  \\"split_prefixes_seen\\": "<<split_prefixes_<<",\\n";\n'
        '        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";\n',
        "json shard metadata")
    replacement = '''            if(caps_possible(i-1,newrem)){
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
    text=replace_once(
        text,
        '            if(caps_possible(i-1,newrem)) dfs(i-1,used+term);\n',
        replacement,
        "DFS shard partition")
    text=replace_once(
        text,
        '        std::string input,bundle,output,dump; int bound=6; uint64_t node_cap=100000000ULL;\n',
        '        std::string input,bundle,output,dump; int bound=6,shard_id=0,shard_count=1,split_i=54; uint64_t node_cap=100000000ULL;\n',
        "main vars")
    text=replace_once(
        text,
        '            if(a=="--input") input=need(); else if(a=="--bundle") bundle=need(); else if(a=="--output") output=need(); else if(a=="--dump-canonical") dump=need(); else if(a=="--bound") bound=std::stoi(need()); else if(a=="--node-cap") node_cap=std::stoull(need()); else throw std::runtime_error("unknown arg "+a);\n',
        '            if(a=="--input") input=need(); else if(a=="--bundle") bundle=need(); else if(a=="--output") output=need(); else if(a=="--dump-canonical") dump=need(); else if(a=="--bound") bound=std::stoi(need()); else if(a=="--node-cap") node_cap=std::stoull(need()); else if(a=="--shard-id") shard_id=std::stoi(need()); else if(a=="--shard-count") shard_count=std::stoi(need()); else if(a=="--split-coordinate") split_i=std::stoi(need()); else throw std::runtime_error("unknown arg "+a);\n',
        "arg parse")
    text=replace_once(
        text,
        '        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump); e.write_json(output); return 0;\n',
        '        Problem p=load_problem(input); Bundle s=load_bundle(bundle,p); ExactEnumerator e(p,s); e.run(bound,node_cap,dump,shard_id,shard_count,split_i); e.write_json(output); return 0;\n',
        "run call")
    args.output.write_text(text)
    print({"schema":NEW_SCHEMA,"sharded":True,"partition":"FNV64_PREFIX_VECTOR","split_default":54})

if __name__=="__main__":
    main()
