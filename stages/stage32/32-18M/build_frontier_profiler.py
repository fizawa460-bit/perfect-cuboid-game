#!/usr/bin/env python3
from __future__ import annotations
import argparse
import pathlib

OLD_SCHEMA = "STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"
NEW_SCHEMA = "STAGE32_18M_D16_EXACT_FRONTIER_PROFILE_V1"


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

    text = replace_once(
        text,
        '        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");\n',
        '        if(split_i_<0 || split_i_>=n_) throw std::runtime_error("bad split coordinate");\n'
        '        frontier_counts_.assign(static_cast<size_t>(shard_count_),0);\n',
        "frontier allocation",
    )

    text = replace_once(
        text,
        '    std::map<int,uint64_t>hist_; std::ofstream*dump_=nullptr;\n',
        '    std::map<int,uint64_t>hist_; std::vector<uint64_t> frontier_counts_; std::ofstream*dump_=nullptr;\n',
        "frontier member",
    )

    old = '''                bool take=true;
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
'''
    new = '''                bool take=true;
                if(i==split_i_){
                    ++split_prefixes_;
                    uint64_t h=1469598103934665603ULL;
                    for(int k=split_i_;k<n_;k++){
                        uint64_t u=static_cast<uint64_t>(z_[k]);
                        h^=(u + 0x9e3779b97f4a7c15ULL + (static_cast<uint64_t>(k)<<32));
                        h*=1099511628211ULL;
                    }
                    ++frontier_counts_[static_cast<size_t>(h%static_cast<uint64_t>(shard_count_))];
                    take=false;
                }
                if(take) dfs(i-1,used+term);
'''
    text = replace_once(text, old, new, "frontier stop")

    text = replace_once(
        text,
        '        f<<"  \\"owned_prefixes\\": "<<owned_prefixes_<<",\\n";\n',
        '        f<<"  \\"owned_prefixes\\": 0,\\n";\n'
        '        f<<"  \\"frontier_only\\": true,\\n";\n'
        '        f<<"  \\"frontier_coordinate\\": "<<split_i_<<",\\n";\n'
        '        f<<"  \\"frontier_modulus\\": "<<shard_count_<<",\\n";\n'
        '        f<<"  \\"frontier_total_prefixes\\": "<<split_prefixes_<<",\\n";\n'
        '        f<<"  \\"frontier_counts_by_residue\\": [";\n'
        '        for(size_t i=0;i<frontier_counts_.size();i++){ if(i) f<<","; f<<frontier_counts_[i]; }\n'
        '        f<<"],\\n";\n',
        "frontier json",
    )

    text = replace_once(
        text,
        '        f<<"  \\"TRAVERSAL_COMPLETENESS_CERTIFICATE\\": true,\\n";\n',
        '        f<<"  \\"FRONTIER_PREFIX_ENUMERATION_COMPLETE\\": true,\\n";\n'
        '        f<<"  \\"FULL_BOUND_TRAVERSAL_COMPLETE\\": false,\\n";\n'
        '        f<<"  \\"TRAVERSAL_COMPLETENESS_CERTIFICATE\\": false,\\n";\n'
        '        f<<"  \\"NUMERICAL_CREDIT\\": false,\\n";\n',
        "profile firewall",
    )

    args.output.write_text(text)
    print({"schema": NEW_SCHEMA, "frontier_only": True, "modulus_via_shard_count": True})


if __name__ == "__main__":
    main()
