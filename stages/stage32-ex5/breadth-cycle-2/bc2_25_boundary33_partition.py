#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import linecache
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_24_explicit_fibre_degree_partition as b24

HERE = Path(__file__).resolve().parent
P24 = HERE / "bc2-24-explicit-fibre-degree-partition-checkpoint.json"
PMAN = HERE / "bc2-25-residual-branch-manifest.json"
PF = HERE / "bc2-25-boundary33-partition-preflight.json"

E24 = "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f"
EMAN = "9a057a80c47b6babcec3d8ff12b4163d09bb88ccdf734ea95c5c8c344bad65b0"
EPF = "49ae6b46ce0d7e6e634d0bce2e2f3375b48514afe125895d89c9b8bceccf6be1"
EB24 = "fea28d97abd21c4ee1a8a4604e38785045f4c7f5"
BOUNDARY_LABEL = 33
TARGET_D = 8


class _SetupCaptured(Exception):
    pass


def capture_bc224_setup() -> dict:
    if b24.git_blob_sha(Path(b24.__file__).resolve()) != EB24:
        raise ValueError("BC2-24 source blob regression")
    captured: dict = {}

    def tracer(frame, event, arg):
        if frame.f_code is b24.main.__code__ and event == "line":
            text = linecache.getline(frame.f_code.co_filename, frame.f_lineno).strip()
            if text == "parent_records = []":
                captured.update(frame.f_locals)
                raise _SetupCaptured
        return tracer

    old_argv = sys.argv[:]
    old_trace = sys.gettrace()
    try:
        with tempfile.TemporaryDirectory() as td:
            sys.argv = [
                str(b24.__file__),
                "--per-branch-timeout-ms",
                "1",
                "--output",
                str(Path(td) / "unused.json"),
            ]
            sys.settrace(tracer)
            try:
                b24.main()
            except _SetupCaptured:
                pass
    finally:
        sys.settrace(old_trace)
        sys.argv = old_argv
    need = {"solver","p","n1","n2","parents","exceptional_labels","x","P","blocks","den","targets"}
    if not need.issubset(captured):
        raise ValueError(f"BC2-24 setup capture regression: missing {sorted(need-set(captured))}")
    return captured


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-subbranch-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_subbranch_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    c24 = b24.checked(P24, E24)
    manifest = b24.checked(PMAN, EMAN)
    pf = b24.checked(PF, EPF)
    targets = [int(v) for v in c24["result"]["residual_unknown_parent_indices"]]
    expected_targets = [584,1000,1003,1014,1030,1048,1050,1056,1064,1066,1103,1106,1117,1119,1133,1198,1218,1224,1243]
    if targets != expected_targets or manifest["target"]["retained_unknown_parent_indices"] != targets:
        raise ValueError("BC2-24 residual parent regression")
    branch_targets = [
        (int(parent), int(n1), TARGET_D-int(n1))
        for parent, n1 in manifest["target"]["residual_unknown_branch_pairs_parent_n1"]
    ]
    if len(branch_targets) != 60 or len(set(branch_targets)) != 60:
        raise ValueError("residual branch manifest regression")
    if sum(n1//2+1 for _,n1,_ in branch_targets) != 166:
        raise ValueError("boundary33 subbranch count regression")
    if pf["partition"]["maximum_subbranch_checks"] != 166:
        raise ValueError("preflight branch count regression")
    if c24["interpretation"]["known_parent_unsat_count_lower_bound"] != 7145:
        raise ValueError("BC2-24 lower bound regression")
    if c24["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("unretained identity count regression")

    ctx = capture_bc224_setup()
    if [int(v) for v in ctx["targets"]] != [
        80,458,584,1000,1003,1014,1030,1032,1048,1050,1056,1064,1066,1103,1106,1108,1117,1119,1133,1198,1218,1224,1243
    ]:
        raise ValueError("captured BC2-24 source target regression")

    solver = ctx["solver"]
    p = ctx["p"]
    n1 = ctx["n1"]
    parents = ctx["parents"]
    exceptional_labels = ctx["exceptional_labels"]
    x = ctx["x"]
    P = ctx["P"]
    blocks = ctx["blocks"]
    den = int(ctx["den"])
    solver.set(timeout=args.per_subbranch_timeout_ms)

    target_by_parent: dict[int, list[tuple[int,int]]] = defaultdict(list)
    for parent_index, n1v, n2v in branch_targets:
        target_by_parent[parent_index].append((n1v,n2v))

    branch_records = []
    branch_unsat = branch_unknown = branch_sat = 0
    sub_unsat = sub_unknown = sub_sat = 0
    first_sat_witness = None

    for parent_index in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label-1] == value)
        for n1v, n2v in sorted(target_by_parent[parent_index]):
            solver.push()
            solver.add(n1 == n1v)
            subrecords = []
            saw_sat = saw_unknown = False
            witness = None
            for p33v in range(n1v//2+1):
                solver.push()
                solver.add(p[BOUNDARY_LABEL-1] == p33v)
                result = solver.check()
                rec = {"p33":p33v,"result":str(result)}
                if result == unsat:
                    sub_unsat += 1
                elif result == unknown:
                    sub_unknown += 1
                    saw_unknown = True
                    rec["reason_unknown"] = solver.reason_unknown()
                elif result == sat:
                    sub_sat += 1
                    saw_sat = True
                    model = solver.model()
                    xv = [int(model.eval(q,model_completion=True).as_long()) for q in x]
                    pv = [sum(int(P[i,j])*xv[j] for j in range(64)) for i in range(140)]
                    n1m = 2*pv[32] + sum(pv[j-1] for j in blocks[0][0])
                    n2m = 2*pv[33] + sum(pv[j-1] for j in blocks[1][0])
                    if n1m != n1v or n2m != n2v or pv[32] != p33v:
                        raise ValueError("SAT witness partition regression")
                    if pv[48] % den not in allowed:
                        raise ValueError("SAT witness x4 residue regression")
                    witness = {
                        "parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,
                        "picard64_coordinates":xv,
                        "all140_pairings":pv,
                        "all140_pairings_sha256":b24.csha(pv),
                    }
                    rec["all140_pairings_sha256"] = witness["all140_pairings_sha256"]
                else:
                    raise ValueError("unexpected solver result")
                subrecords.append(rec)
                solver.pop()
                if saw_sat:
                    break
            if saw_sat:
                branch_result = "sat"; branch_sat += 1
                if first_sat_witness is None:
                    first_sat_witness = witness
            elif saw_unknown:
                branch_result = "unknown"; branch_unknown += 1
            else:
                expected = n1v//2+1
                if len(subrecords) != expected or any(r["result"]!="unsat" for r in subrecords):
                    raise ValueError("UNSAT subbranch coverage regression")
                branch_result = "unsat"; branch_unsat += 1
            branch_records.append({
                "parent_index":parent_index,"n1":n1v,"n2":n2v,"result":branch_result,
                "subbranch_count_checked":len(subrecords),"subbranches":subrecords,
            })
            solver.pop()
        solver.pop()

    by_parent: dict[int,list[str]] = defaultdict(list)
    for rec in branch_records:
        by_parent[int(rec["parent_index"])].append(rec["result"])
    parent_records = []
    newly_unsat = []; residual_unknown = []; sat_parents = []
    for parent_index in targets:
        vals = by_parent[parent_index]
        if len(vals) != len(target_by_parent[parent_index]):
            raise ValueError("parent coverage regression")
        if "sat" in vals:
            result = "sat"; sat_parents.append(parent_index)
        elif "unknown" in vals:
            result = "unknown"; residual_unknown.append(parent_index)
        else:
            result = "unsat"; newly_unsat.append(parent_index)
        parent_records.append({
            "parent_index":parent_index,"result":result,
            "targeted_bc2_24_unknown_branch_count":len(vals),
        })

    parent_unsat = len(newly_unsat)
    parent_unknown = len(residual_unknown)
    parent_sat = len(sat_parents)
    known_unsat_lower_bound = 7145 + parent_unsat
    residual_branches = [
        {"parent_index":r["parent_index"],"n1":r["n1"],"n2":r["n2"]}
        for r in branch_records if r["result"]=="unknown"
    ]
    if parent_sat:
        status = "PASS_BOUNDARY33_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_26_ANALYZE_BOUNDARY33_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_ALL_19_BC2_24_RETAINED_UNKNOWN_PARENTS_EXACT_UNSAT_BY_BOUNDARY33_PARTITION"
        next_id = "BC2_26_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_BOUNDARY33_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_26_PARTITION_RESIDUAL_BY_SECOND_BOUNDARY_PAIRING_OR_X4"

    body = {
        "schema":"STAGE32EX5_BC2_25_BOUNDARY33_PARTITION_V1",
        "stage":"32EX5",
        "unit":"BC2_25_PARTITION_BC2_24_RESIDUAL_TIMEOUT_BRANCHES_BY_BOUNDARY33",
        "status":status,
        "source_locks":{
            "bc2_24_checkpoint":E24,"bc2_25_residual_manifest":EMAN,"preflight":EPF,
            "bc2_24_source_git_blob_sha":EB24,
        },
        "partition_certificate":{
            "boundary_pairing_label":33,"fibre_degree_variable":"n1",
            "per_branch_values_rule":"p33=0..floor(n1/2)",
            "identity":"n1=2*p33+sum(incident exceptional pairings)",
            "coverage_exact":True,"disjoint":True,
            "targeted_bc2_24_unknown_branch_count":60,
            "maximum_possible_subbranch_count":166,
        },
        "target":{
            "checked_parent_indices":targets,"checked_parent_count":19,
            "checked_bc2_24_unknown_branch_count":60,
            "unretained_bc2_19_unknown_identity_count":172,
            "unretained_bc2_19_unknown_identities_inferred":False,
        },
        "result":{
            "parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,
            "newly_unsat_parent_indices":newly_unsat,"residual_unknown_parent_indices":residual_unknown,
            "sat_parent_indices":sat_parents,"parent_records":parent_records,
            "branch_unsat_count":branch_unsat,"branch_unknown_count":branch_unknown,"branch_sat_count":branch_sat,
            "residual_unknown_branches":residual_branches,"branch_records":branch_records,
            "subbranch_unsat_count":sub_unsat,"subbranch_unknown_count":sub_unknown,"subbranch_sat_count":sub_sat,
            "per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,
            "solver":"Z3_QF_LIA_N355_REDUNDANT_CUTS_PLUS_EXACT_N1_PLUS_BOUNDARY33_PARTITION",
            "z3_version":get_version_string(),
        },
        "sat_witness":first_sat_witness,
        "interpretation":{
            "known_parent_unsat_count_lower_bound":known_unsat_lower_bound,
            "known_retained_unknown_identity_count_after_this_run":parent_unknown,
            "remaining_target_unknown_branch_count":branch_unknown,
            "unretained_unknown_identity_count":172,
            "whole_first_block_unsat_proved":False,
        },
        "credit":{
            "all_19_bc2_24_residual_parents_exact_unsat":parent_sat==0 and parent_unknown==0,
            "whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,
            "stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,
            "theorem_credit":False,"endpoint_credit":False,
        },
        "firewalls":{
            "unretained_172_parent_identities_inferred":False,"unknown_relabelled_unsat":False,
            "partition_subbranch_unknown_dropped":False,"sat_relabelled_actual_curve":False,
            "main_promotion":False,"merge_authorized":False,
            "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False,
        },
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False},
    }
    body["canonical_sha256_without_this_field"] = b24.csha(body)
    args.output.write_text(json.dumps(body,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
        "canonical":body["canonical_sha256_without_this_field"],"status":status,
        "parent_unsat":parent_unsat,"parent_unknown":parent_unknown,"parent_sat":parent_sat,
        "branch_unsat":branch_unsat,"branch_unknown":branch_unknown,"branch_sat":branch_sat,
        "subbranch_unsat":sub_unsat,"subbranch_unknown":sub_unknown,"subbranch_sat":sub_sat,
        "known_unsat_lower_bound":known_unsat_lower_bound,"next":next_id,
    },sort_keys=True))


if __name__ == "__main__":
    main()
