#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_26_boundary34_partition as b26

HERE = Path(__file__).resolve().parent
P26 = HERE / "bc2-26-boundary34-partition-checkpoint.json"
PMAN = HERE / "bc2-27-residual-p34-leaf-manifest.json"
PF = HERE / "bc2-27-boundary35-partition-preflight.json"

E26 = "b97d61c0d20cec1742831a07595429024cb9bb272d383cfb98d968278d8d330a"
EMAN = "c723b63c1f61dc8f637b69cbca5888e16b6f3fb94f6bb71a8f9c57e7822a4cf1"
EPF = "1767c15cfd1064863f79f20af413651a818e1009bf37b7b471471ef89f60160b"
EB26 = "f795dcf24ea77a99c6c4a85bec64910ca02f65f9"
BOUNDARY35_LABEL = 35


def checked(path: Path, expected: str) -> dict:
    return b26.checked(path, expected)


def git_blob_sha(path: Path) -> str:
    return b26.git_blob_sha(path)


def lock_executable_chain() -> None:
    if git_blob_sha(Path(b26.__file__).resolve()) != EB26:
        raise ValueError("BC2-26 source blob regression")
    b26.lock_executable_chain()


def classify(vals: list[str]) -> str:
    if "sat" in vals:
        return "sat"
    if "unknown" in vals:
        return "unknown"
    return "unsat"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-subbranch-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_subbranch_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    lock_executable_chain()
    c26 = checked(P26, E26)
    manifest = checked(PMAN, EMAN)
    pf = checked(PF, EPF)

    if c26["result"]["parent_unknown_count"] != 12:
        raise ValueError("BC2-26 parent UNKNOWN accounting regression")
    if c26["result"]["branch_unknown_count"] != 20 or c26["result"]["p33_subbranch_unknown_count"] != 20:
        raise ValueError("BC2-26 hierarchy UNKNOWN accounting regression")
    if c26["result"]["p34_leaf_unknown_count"] != 23:
        raise ValueError("BC2-26 p34 UNKNOWN accounting regression")
    if c26["interpretation"]["known_parent_unsat_count_lower_bound"] != 7152:
        raise ValueError("BC2-26 lower-bound regression")
    if c26["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("BC2-26 unretained identity count regression")

    targets = [(int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"])) for r in manifest["target"]["residual_unknown_p34_leaves"]]
    raw_targets = [(int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"])) for r in c26["result"]["residual_unknown_p34_leaves"]]
    if targets != raw_targets or len(targets) != 23 or len(set(targets)) != 23:
        raise ValueError("BC2-27 residual p34 target regression")
    parents_targeted = sorted({r[0] for r in targets})
    if parents_targeted != [1000,1003,1014,1048,1050,1064,1066,1103,1117,1133,1198,1243]:
        raise ValueError("BC2-27 residual parent set regression")
    branches_targeted = sorted({r[:3] for r in targets})
    p33_targeted = sorted({r[:4] for r in targets})
    if len(branches_targeted) != 20 or len(p33_targeted) != 20:
        raise ValueError("BC2-27 residual hierarchy regression")
    maximum = sum(n2 // 2 + 1 for _, _, n2, _, _ in targets)
    if maximum != 70 or pf["partition"]["maximum_subbranch_checks"] != 70:
        raise ValueError("BC2-27 boundary35 leaf-count regression")

    ctx = b26.b25.capture_bc224_setup()
    solver = ctx["solver"]
    p = ctx["p"]
    n1 = ctx["n1"]
    n2 = ctx["n2"]
    parents = ctx["parents"]
    exceptional_labels = ctx["exceptional_labels"]
    x = ctx["x"]
    P = ctx["P"]
    blocks = ctx["blocks"]
    den = int(ctx["den"])
    solver.set(timeout=args.per_subbranch_timeout_ms)

    p34_records = []
    leaf_unsat = leaf_unknown = leaf_sat = 0
    first_sat_witness = None

    for parent_index, n1v, n2v, p33v, p34v in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label - 1] == value)
        solver.add(n1 == n1v)
        solver.add(n2 == n2v)
        solver.add(p[32] == p33v)
        solver.add(p[33] == p34v)
        leaves = []
        saw_unknown = saw_sat = False
        witness = None
        for p35v in range(n2v // 2 + 1):
            solver.push()
            solver.add(p[BOUNDARY35_LABEL - 1] == p35v)
            result = solver.check()
            rec = {"p35": p35v, "result": str(result)}
            if result == unsat:
                leaf_unsat += 1
            elif result == unknown:
                leaf_unknown += 1
                saw_unknown = True
                rec["reason_unknown"] = solver.reason_unknown()
            elif result == sat:
                leaf_sat += 1
                saw_sat = True
                model = solver.model()
                xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
                pv = [sum(int(P[i, j]) * xv[j] for j in range(64)) for i in range(140)]
                n1m = 2 * pv[32] + sum(pv[j - 1] for j in blocks[0][0])
                n2m = 2 * pv[33] + sum(pv[j - 1] for j in blocks[1][0])
                n2m35 = 2 * pv[34] + sum(pv[j - 1] for j in blocks[1][1])
                if n1m != n1v or n2m != n2v or n2m35 != n2v:
                    raise ValueError("SAT witness fibre regression")
                if pv[32] != p33v or pv[33] != p34v or pv[34] != p35v:
                    raise ValueError("SAT witness boundary35 partition regression")
                if pv[48] % den not in allowed:
                    raise ValueError("SAT witness x4 residue regression")
                witness = {"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"p35":p35v,"picard64_coordinates":xv,"all140_pairings":pv,"all140_pairings_sha256":b26.b25.b24.csha(pv)}
                rec["all140_pairings_sha256"] = witness["all140_pairings_sha256"]
            else:
                raise ValueError("unexpected solver result")
            leaves.append(rec)
            solver.pop()
            if saw_sat:
                break
        if saw_sat:
            outcome = "sat"
            if first_sat_witness is None:
                first_sat_witness = witness
        elif saw_unknown:
            outcome = "unknown"
        else:
            expected = n2v // 2 + 1
            if len(leaves) != expected or any(r["result"] != "unsat" for r in leaves):
                raise ValueError("UNSAT p35 coverage regression")
            outcome = "unsat"
        p34_records.append({"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"result":outcome,"p35_leaf_count_checked":len(leaves),"p35_leaves":leaves})
        solver.pop()

    def aggregate(keys, records):
        grouped = defaultdict(list)
        for r in records:
            grouped[tuple(r[k] for k in keys)].append(r["result"])
        out = []
        for key in sorted(grouped):
            vals = grouped[key]
            rec = {k: v for k, v in zip(keys, key)}
            rec["result"] = classify(vals)
            rec["targeted_child_count"] = len(vals)
            out.append(rec)
        return out

    p33_records = aggregate(["parent_index","n1","n2","p33"], p34_records)
    branch_records = aggregate(["parent_index","n1","n2"], p33_records)
    parent_records = aggregate(["parent_index"], branch_records)
    if len(p33_records) != 20 or len(branch_records) != 20 or len(parent_records) != 12:
        raise ValueError("BC2-27 aggregate coverage regression")

    newly_unsat = [r["parent_index"] for r in parent_records if r["result"] == "unsat"]
    residual_unknown = [r["parent_index"] for r in parent_records if r["result"] == "unknown"]
    sat_parents = [r["parent_index"] for r in parent_records if r["result"] == "sat"]
    p34_unsat = sum(r["result"] == "unsat" for r in p34_records)
    p34_unknown = sum(r["result"] == "unknown" for r in p34_records)
    p34_sat = sum(r["result"] == "sat" for r in p34_records)
    p33_unsat = sum(r["result"] == "unsat" for r in p33_records)
    p33_unknown = sum(r["result"] == "unknown" for r in p33_records)
    p33_sat = sum(r["result"] == "sat" for r in p33_records)
    branch_unsat = sum(r["result"] == "unsat" for r in branch_records)
    branch_unknown = sum(r["result"] == "unknown" for r in branch_records)
    branch_sat = sum(r["result"] == "sat" for r in branch_records)
    parent_unsat = len(newly_unsat)
    parent_unknown = len(residual_unknown)
    parent_sat = len(sat_parents)
    known_unsat_lower_bound = 7152 + parent_unsat
    residual_p34 = [{k:r[k] for k in ("parent_index","n1","n2","p33","p34")} for r in p34_records if r["result"] == "unknown"]
    residual_p33 = [{k:r[k] for k in ("parent_index","n1","n2","p33")} for r in p33_records if r["result"] == "unknown"]
    residual_branches = [{k:r[k] for k in ("parent_index","n1","n2")} for r in branch_records if r["result"] == "unknown"]

    if parent_sat:
        status = "PASS_BOUNDARY35_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_28_ANALYZE_BOUNDARY35_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_ALL_12_BC2_26_RETAINED_UNKNOWN_PARENTS_EXACT_UNSAT_BY_BOUNDARY35_PARTITION"
        next_id = "BC2_28_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_BOUNDARY35_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_28_REFINE_RESIDUAL_BY_X4_OR_NEXT_EXACT_PAIRING"

    body = {
        "schema":"STAGE32EX5_BC2_27_BOUNDARY35_PARTITION_V1","stage":"32EX5","unit":"BC2_27_PARTITION_BC2_26_RESIDUAL_P34_UNKNOWN_BY_BOUNDARY35","status":status,
        "source_locks":{"bc2_26_checkpoint":E26,"bc2_27_residual_manifest":EMAN,"preflight":EPF,"bc2_26_source_git_blob_sha":EB26},
        "audit_consumption":{"bc2_26_hostile_audit_status":"PASS","bc2_26_hostile_audit_exact_head":"34d6b030095b97c738f6faf6b9045f366622592c","bc2_26_hostile_audit_review_id":5177919212},
        "partition_certificate":{"boundary_pairing_label":35,"fibre_degree_variable":"n2","per_p34_leaf_values_rule":"p35=0..floor(n2/2)","identity":"n2=2*p35+sum(incident exceptional pairings)","coverage_exact":True,"disjoint":True,"targeted_bc2_26_unknown_p34_leaf_count":23,"maximum_possible_subbranch_count":70},
        "target":{"checked_parent_indices":parents_targeted,"checked_parent_count":12,"checked_bc2_26_unknown_branch_count":20,"checked_bc2_26_unknown_p33_subbranch_count":20,"checked_bc2_26_unknown_p34_leaf_count":23,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
        "result":{"parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,"newly_unsat_parent_indices":newly_unsat,"residual_unknown_parent_indices":residual_unknown,"sat_parent_indices":sat_parents,"parent_records":parent_records,"branch_unsat_count":branch_unsat,"branch_unknown_count":branch_unknown,"branch_sat_count":branch_sat,"residual_unknown_branches":residual_branches,"branch_records":branch_records,"p33_subbranch_unsat_count":p33_unsat,"p33_subbranch_unknown_count":p33_unknown,"p33_subbranch_sat_count":p33_sat,"residual_unknown_p33_subbranches":residual_p33,"p33_subbranch_records":p33_records,"p34_target_unsat_count":p34_unsat,"p34_target_unknown_count":p34_unknown,"p34_target_sat_count":p34_sat,"residual_unknown_p34_leaves":residual_p34,"p34_target_records":p34_records,"p35_leaf_unsat_count":leaf_unsat,"p35_leaf_unknown_count":leaf_unknown,"p35_leaf_sat_count":leaf_sat,"per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,"solver":"Z3_QF_LIA_N355_REDUNDANT_CUTS_PLUS_EXACT_N1_N2_P33_P34_PLUS_BOUNDARY35_PARTITION","z3_version":get_version_string()},
        "sat_witness":first_sat_witness,
        "interpretation":{"known_parent_unsat_count_lower_bound":known_unsat_lower_bound,"known_retained_unknown_identity_count_after_this_run":parent_unknown,"remaining_target_unknown_branch_count":branch_unknown,"remaining_target_unknown_p33_subbranch_count":p33_unknown,"remaining_target_unknown_p34_leaf_count":p34_unknown,"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False},
        "credit":{"all_12_bc2_26_residual_parents_exact_unsat":parent_sat == 0 and parent_unknown == 0,"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
        "firewalls":{"unretained_172_parent_identities_inferred":False,"unknown_relabelled_unsat":False,"partition_leaf_unknown_dropped":False,"sat_relabelled_actual_curve":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False},
    }
    body["canonical_sha256_without_this_field"] = b26.b25.b24.csha(body)
    args.output.write_text(json.dumps(body,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"canonical":body["canonical_sha256_without_this_field"],"status":status,"parent_unsat":parent_unsat,"parent_unknown":parent_unknown,"parent_sat":parent_sat,"branch_unknown":branch_unknown,"p33_unknown":p33_unknown,"p34_unknown":p34_unknown,"p35_leaf_unknown":leaf_unknown,"known_unsat_lower_bound":known_unsat_lower_bound,"next":next_id},sort_keys=True))


if __name__ == "__main__":
    main()
