#!/usr/bin/env python3
from __future__ import annotations
import argparse
import pathlib

OLD_SCHEMA = "STAGE32_18I_D16_EXACT_TWO_STAGE_SHARDED_TRAVERSAL_CERT_V1"
NEW_SCHEMA = "STAGE32_18J_D16_EXACT_THREE_STAGE_SHARDED_TRAVERSAL_CERT_V1"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()
    text = args.source.read_text()
    text = replace_once(text, OLD_SCHEMA, NEW_SCHEMA, "schema")

    old = '''                bool take=true;
                if(i==54){
                    uint64_t h=1469598103934665603ULL;
                    for(int k=54;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    take=static_cast<int>(h%1024ULL)==26;
                }
                if(take && shard_count_>1 && i==split_i_){
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
'''
    new = '''                bool take=true;
                if(i==54){
                    uint64_t h=1469598103934665603ULL;
                    for(int k=54;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    take=static_cast<int>(h%1024ULL)==26;
                }
                if(take && i==45){
                    ++secondary_split_prefixes_;
                    uint64_t h=1469598103934665603ULL;
                    for(int k=45;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    take=static_cast<int>(h%32ULL)==5;
                    if(take) ++secondary_owned_prefixes_;
                }
                if(take && shard_count_>1 && i==split_i_){
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
'''
    text = replace_once(text, old, new, "three-stage DFS partition")

    old_meta = '''        f<<"  \\"shard_id\\": "<<shard_id_<<",\\n";
        f<<"  \\"shard_count\\": "<<shard_count_<<",\\n";
        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";
        f<<"  \\"two_stage_partition\\": true,\\n";
        f<<"  \\"primary_split_coordinate\\": 54,\\n";
        f<<"  \\"primary_shard_count\\": 1024,\\n";
        f<<"  \\"primary_shard_id\\": 26,\\n";
        f<<"  \\"secondary_split_coordinate\\": "<<split_i_<<",\\n";
        f<<"  \\"secondary_shard_count\\": "<<shard_count_<<",\\n";
        f<<"  \\"secondary_shard_id\\": "<<shard_id_<<",\\n";
        f<<"  \\"split_prefixes_seen\\": "<<split_prefixes_<<",\\n";
        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";
'''
    new_meta = '''        f<<"  \\"shard_id\\": "<<shard_id_<<",\\n";
        f<<"  \\"shard_count\\": "<<shard_count_<<",\\n";
        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";
        f<<"  \\"three_stage_partition\\": true,\\n";
        f<<"  \\"primary_split_coordinate\\": 54,\\n";
        f<<"  \\"primary_shard_count\\": 1024,\\n";
        f<<"  \\"primary_shard_id\\": 26,\\n";
        f<<"  \\"secondary_split_coordinate\\": 45,\\n";
        f<<"  \\"secondary_shard_count\\": 32,\\n";
        f<<"  \\"secondary_shard_id\\": 5,\\n";
        f<<"  \\"secondary_split_prefixes_seen\\": "<<secondary_split_prefixes_<<",\\n";
        f<<"  \\"secondary_owned_prefixes\\": "<<secondary_owned_prefixes_<<",\\n";
        f<<"  \\"tertiary_split_coordinate\\": "<<split_i_<<",\\n";
        f<<"  \\"tertiary_shard_count\\": "<<shard_count_<<",\\n";
        f<<"  \\"tertiary_shard_id\\": "<<shard_id_<<",\\n";
        f<<"  \\"split_prefixes_seen\\": "<<split_prefixes_<<",\\n";
        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";
'''
    text = replace_once(text, old_meta, new_meta, "three-stage metadata")

    old_members = '    int shard_id_=0,shard_count_=1,split_i_=54; uint64_t split_prefixes_=0,owned_prefixes_=0;\n'
    new_members = '    int shard_id_=0,shard_count_=1,split_i_=54; uint64_t split_prefixes_=0,owned_prefixes_=0,secondary_split_prefixes_=0,secondary_owned_prefixes_=0;\n'
    text = replace_once(text, old_members, new_members, "secondary counters")

    args.output.write_text(text)
    print({"schema": NEW_SCHEMA, "primary": [54,26,1024], "secondary": [45,5,32], "tertiary_cli": True})


if __name__ == "__main__":
    main()
