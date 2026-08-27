#!/usr/bin/env python3
from __future__ import annotations
import argparse,pathlib
OLD_SCHEMA='STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1'
NEW_SCHEMA='STAGE32_18X_D16_B16_TWO_STAGE_SHARD_V1'

def once(text:str,old:str,new:str,label:str)->str:
    n=text.count(old)
    if n!=1: raise RuntimeError(f'{label}: expected one occurrence, got {n}')
    return text.replace(old,new,1)

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=pathlib.Path,required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    ap.add_argument('--primary-id',type=int,required=True)
    a=ap.parse_args(); pid=a.primary_id
    if not 0<=pid<1024: raise RuntimeError('primary id outside 0..1023')
    text=a.source.read_text()
    text=once(text,OLD_SCHEMA,NEW_SCHEMA,'schema')
    old='''                bool take=true;\n                if(shard_count_>1 && i==split_i_){\n                    ++split_prefixes_;\n                    uint64_t h=1469598103934665603ULL;\n                    for(int k=split_i_;k<n_;k++){\n                        uint64_t u=static_cast<uint64_t>(z_[k]);\n                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));\n                        h*=1099511628211ULL;\n                    }\n                    take=static_cast<int>(h%static_cast<uint64_t>(shard_count_))==shard_id_;\n                    if(take) ++owned_prefixes_;\n                }\n                if(take) dfs(i-1,used+term);\n'''
    new=f'''                bool take=true;\n                if(i==54){{\n                    uint64_t h=1469598103934665603ULL;\n                    for(int k=54;k<n_;k++){{\n                        uint64_t u=static_cast<uint64_t>(z_[k]);\n                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));\n                        h*=1099511628211ULL;\n                    }}\n                    take=static_cast<int>(h%1024ULL)=={pid};\n                }}\n                if(take && shard_count_>1 && i==split_i_){{\n                    ++split_prefixes_;\n                    uint64_t h=1469598103934665603ULL;\n                    for(int k=split_i_;k<n_;k++){{\n                        uint64_t u=static_cast<uint64_t>(z_[k]);\n                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));\n                        h*=1099511628211ULL;\n                    }}\n                    take=static_cast<int>(h%static_cast<uint64_t>(shard_count_))==shard_id_;\n                    if(take) ++owned_prefixes_;\n                }}\n                if(take) dfs(i-1,used+term);\n'''
    text=once(text,old,new,'two-stage DFS')
    oldm='        f<<"  \\"split_coordinate\\": "<<split_i_<<",\\n";\n'
    newm=oldm+('        f<<"  \\"two_stage_partition\\": true,\\n";\n'
               +'        f<<"  \\"primary_split_coordinate\\": 54,\\n";\n'
               +'        f<<"  \\"primary_shard_count\\": 1024,\\n";\n'
               +f'        f<<"  \\"primary_shard_id\\": {pid},\\n";\n'
               +'        f<<"  \\"secondary_split_coordinate\\": "<<split_i_<<",\\n";\n'
               +'        f<<"  \\"secondary_shard_count\\": "<<shard_count_<<",\\n";\n'
               +'        f<<"  \\"secondary_shard_id\\": "<<shard_id_<<",\\n";\n')
    text=once(text,oldm,newm,'metadata')
    a.output.write_text(text)

if __name__=='__main__': main()
