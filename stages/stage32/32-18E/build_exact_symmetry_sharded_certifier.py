#!/usr/bin/env python3
from __future__ import annotations
import argparse
import pathlib

OLD_SCHEMA = "STAGE32_18C_D16_EXACT_SHARDED_TRAVERSAL_CERT_V1"
NEW_SCHEMA = "STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {n}")
    return text.replace(old, new, 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    ap.add_argument("--breaker-count", type=int, default=256)
    args = ap.parse_args()
    if args.breaker_count != 256:
        raise RuntimeError("Stage32-18E is intentionally locked to 256 exact Aut score breakers")

    text = args.source.read_text()
    text = replace_once(text, OLD_SCHEMA, NEW_SCHEMA, "schema")
    text = replace_once(
        text,
        'if(s.input_sha!=p.input_sha||s.n!=63||s.m!=140||s.k!=64||s.group_order!=1536) throw std::runtime_error("bundle mismatch");',
        'if(s.input_sha!=p.input_sha||s.n!=63||s.m!=140||s.k!=256||s.group_order!=1536) throw std::runtime_error("bundle mismatch");',
        "bundle breaker lock",
    )
    text = replace_once(
        text,
        '        for(int r=0;r<m_;r++) build_dual_row(p_.lin[r],cap_a_[r],cap_dual_[r],cap_af_[r],cap_dualf_[r]);\n\n        order_.reserve(m_);',
        '        for(int r=0;r<m_;r++) build_dual_row(p_.lin[r],cap_a_[r],cap_dual_[r],cap_af_[r],cap_dualf_[r]);\n\n'
        '        sym_a_.assign(s_.k,std::vector<cpp_rational>(n_,0));\n'
        '        sym_dual_.assign(s_.k,std::vector<cpp_rational>(n_,0));\n'
        '        sym_af_.assign(s_.k,std::vector<long double>(n_,0));\n'
        '        sym_dualf_.assign(s_.k,std::vector<long double>(n_,0));\n'
        '        for(int r=0;r<s_.k;r++) build_dual_row(s_.lin[r],sym_a_[r],sym_dual_[r],sym_af_[r],sym_dualf_[r]);\n\n'
        '        order_.reserve(m_);',
        "symmetry dual construction",
    )
    text = replace_once(
        text,
        '        z_.assign(n_,0); t_.assign(n_,0); tf_.assign(n_,0);\n        cap_assignedf_.assign(m_,0);\n',
        '        z_.assign(n_,0); t_.assign(n_,0); tf_.assign(n_,0);\n'
        '        cap_assignedf_.assign(m_,0);\n'
        '        sym_assignedf_.assign(s_.k,0);\n',
        "symmetry approximate state",
    )
    text = replace_once(
        text,
        '        if(caps_possible(n_-1,cpp_rational(bound_))) dfs(n_-1,cpp_rational(0));\n',
        '        if(caps_possible(n_-1,cpp_rational(bound_)) && symmetry_possible(n_-1,cpp_rational(bound_))) dfs(n_-1,cpp_rational(0));\n',
        "root symmetry gate",
    )
    text = replace_once(
        text,
        '        f<<"  \\"symmetry_breakers_evaluated_only_by_exact_integer_leaf_tests\\": true,\\n";\n',
        '        f<<"  \\"symmetry_breakers_evaluated_by_exact_branch_and_leaf_tests\\": true,\\n";\n'
        '        f<<"  \\"all_symmetry_branch_rejections_exact_rational_cauchy_schwarz\\": true,\\n";\n'
        '        f<<"  \\"selected_breakers_are_actual_full_aut_score_inequalities\\": true,\\n";\n',
        "json symmetry semantics",
    )
    text = replace_once(
        text,
        '        f<<"  \\"exact_symmetry_prunes\\": 0,\\n";\n',
        '        f<<"  \\"exact_symmetry_prune_checks\\": "<<exact_symmetry_prune_checks_<<",\\n";\n'
        '        f<<"  \\"exact_symmetry_prunes\\": "<<symmetry_prunes_<<",\\n";\n',
        "json symmetry counters",
    )
    text = replace_once(
        text,
        '        f<<"  \\"cap_survivors_before_symmetry\\": "<<cap_survivors_<<",\\n";\n',
        '        f<<"  \\"leaf_cap_survivors_after_branch_symmetry\\": "<<cap_survivors_<<",\\n";\n',
        "json cap survivor semantics",
    )
    text = replace_once(
        text,
        '    std::vector<std::vector<cpp_rational>> cap_a_,cap_dual_;\n'
        '    std::vector<std::vector<long double>> cap_af_,cap_dualf_;\n'
        '    std::vector<long long>z_; std::vector<cpp_rational>t_; std::vector<long double>tf_;\n'
        '    std::vector<long double>cap_assignedf_; std::vector<int>order_;\n',
        '    std::vector<std::vector<cpp_rational>> cap_a_,cap_dual_,sym_a_,sym_dual_;\n'
        '    std::vector<std::vector<long double>> cap_af_,cap_dualf_,sym_af_,sym_dualf_;\n'
        '    std::vector<long long>z_; std::vector<cpp_rational>t_; std::vector<long double>tf_;\n'
        '    std::vector<long double>cap_assignedf_,sym_assignedf_; std::vector<int>order_;\n',
        "symmetry member arrays",
    )
    text = replace_once(
        text,
        '    uint64_t exact_prune_checks_=0,constraint_prunes_=0;\n',
        '    uint64_t exact_prune_checks_=0,constraint_prunes_=0,exact_symmetry_prune_checks_=0,symmetry_prunes_=0;\n',
        "symmetry counter members",
    )
    symmetry_method = r'''
    bool symmetry_possible(int last_remaining,const cpp_rational& budget) {
        const long double bf=std::max<long double>(0,budget.convert_to<long double>());
        for(int r=0;r<s_.k;r++){
            long double center=static_cast<long double>(s_.c0[r])+sym_assignedf_[r];
            if(center>=0) continue;
            long double dual=last_remaining>=0?sym_dualf_[r][last_remaining]:0;
            long double reach=std::sqrt(std::max<long double>(0,bf*dual));
            // Floating arithmetic only schedules an exact proof attempt. A missed
            // attempt can cost runtime but cannot discard a branch. The 1.25
            // margin deliberately favors obviously impossible prefixes.
            if(reach==0 || -center>1.25L*reach){
                ++exact_symmetry_prune_checks_;
                cpp_rational exact=exact_center(s_.c0[r],sym_a_[r],last_remaining);
                if(exact<0){
                    cpp_rational reach2=last_remaining>=0?budget*sym_dual_[r][last_remaining]:cpp_rational(0);
                    if(exact*exact>reach2){ ++symmetry_prunes_; return false; }
                }
            }
        }
        return true;
    }
'''
    text = replace_once(
        text,
        '        return true;\n    }\n\n    bool is_canonical',
        '        return true;\n    }\n' + symmetry_method + '\n    bool is_canonical',
        "symmetry possible method",
    )
    text = replace_once(
        text,
        '            for(int r=0;r<m_;r++) cap_assignedf_[r]+=cap_af_[r][i]*tf_[i];\n'
        '            cpp_rational newrem=rem-term;\n'
        '            if(caps_possible(i-1,newrem)){\n',
        '            for(int r=0;r<m_;r++) cap_assignedf_[r]+=cap_af_[r][i]*tf_[i];\n'
        '            for(int r=0;r<s_.k;r++) sym_assignedf_[r]+=sym_af_[r][i]*tf_[i];\n'
        '            cpp_rational newrem=rem-term;\n'
        '            if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem)){\n',
        "DFS symmetry update/gate",
    )
    text = replace_once(
        text,
        '            for(int r=0;r<m_;r++) cap_assignedf_[r]-=cap_af_[r][i]*tf_[i];\n'
        '            t_[i]=0; tf_[i]=0;\n',
        '            for(int r=0;r<m_;r++) cap_assignedf_[r]-=cap_af_[r][i]*tf_[i];\n'
        '            for(int r=0;r<s_.k;r++) sym_assignedf_[r]-=sym_af_[r][i]*tf_[i];\n'
        '            t_[i]=0; tf_[i]=0;\n',
        "DFS symmetry restore",
    )
    args.output.write_text(text)
    print({"schema": NEW_SCHEMA, "breaker_count": args.breaker_count, "exact_branch_symmetry": True, "schedule_margin": 1.25})


if __name__ == "__main__":
    main()
