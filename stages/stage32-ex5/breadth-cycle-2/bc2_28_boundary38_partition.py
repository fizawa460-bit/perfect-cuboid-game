#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_27_boundary35_partition as b27

HERE = Path(__file__).resolve().parent
P27 = HERE / "bc2-27-boundary35-partition-checkpoint.json"
PMAN = HERE / "bc2-28-residual-p35-leaf-manifest.json"
PF = HERE / "bc2-28-boundary38-partition-preflight.json"

E27 = "0f9278799809fd1a48c187f9a9668631422ab3136478cb3f9f64fd423df71462"
EMAN = "635bc832c61c539333f39f3732edd9f82397f8dc3d4a8c0a00406b2c79572477"
EPF = "afd747ef826fe0c0287d0188f5cdc7e38ae704cc50709014f1b10b7db1a471e0"
EB27 = "864f9dd0955d244cdba8f0efd3471f6505e883e8"
BOUNDARY38_LABEL = 38
BC2_27_AUDIT_HEAD = "b70bc51909f5ed78641ee3b727a2258382ef950c"
BC2_27_AUDIT_REVIEW = 5179488973


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    return b27.checked(path, expected)


def git_blob_sha(path: Path) -> str:
    return b27.git_blob_sha(path)


def lock_executable_chain() -> None:
    if git_blob_sha(Path(b27.__file__).resolve()) != EB27:
        raise ValueError("BC2-27 source blob regression")
    b27.lock_executable_chain()


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
    c27 = checked(P27, E27)
    manifest = checked(PMAN, EMAN)
    pf = checked(PF, EPF)

    if c27["result"]["parent_unknown_count"] != 9 or c27["result"]["parent_sat_count"] != 0:
        raise ValueError("BC2-27 parent accounting regression")
    if c27["result"]["p34_target_unknown_count"] != 13 or c27["result"]["p35_leaf_unknown_count"] != 13:
        raise ValueError("BC2-27 residual p34/p35 UNKNOWN accounting regression")
    if c27["interpretation"]["known_parent_unsat_count_lower_bound"] != 7155:
        raise ValueError("BC2-27 lower-bound regression")
    if c27["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("BC2-27 unretained identity count regression")

    a = pf["audit_consumption"]
    expected_audit = {
        "bc2_27_hostile_audit_exact_head": BC2_27_AUDIT_HEAD,
        "bc2_27_hostile_audit_review_id": BC2_27_AUDIT_REVIEW,
        "bc2_27_hostile_audit_status": "PASS",
    }
    if a != expected_audit:
        raise ValueError("BC2-27 hostile-audit PASS receipt regression")

    targets = [
        (int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"]), int(r["p35"]))
        for r in manifest["target"]["residual_unknown_p35_leaves"]
    ]
    if len(targets) != 13 or len(set(targets)) != 13:
        raise ValueError("BC2-28 target leaf identity regression")
    p34_targets = [r[:5] for r in targets]
    predecessor_p34 = [
        (int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"]))
        for r in c27["result"]["residual_unknown_p34_leaves"]
    ]
    if p34_targets != predecessor_p34 or len(set(p34_targets)) != 13:
        raise ValueError("BC2-28 target p34 coverage does not exactly equal BC2-27 residual p34 leaves")
    parents_targeted = sorted({r[0] for r in targets})
    if parents_targeted != [1000,1003,1014,1048,1050,1064,1103,1198,1243]:
        raise ValueError("BC2-28 target parent set regression")
    maximum = sum(n2 // 2 + 1 for _, _, n2, _, _, _ in targets)
    if maximum != 42 or pf["target"]["maximum_subbranch_checks"] != 42:
        raise ValueError("BC2-28 boundary38 maximum-check regression")
    part = pf["partition"]
    if part["boundary_pairing_label"] != 38 or part["factor_pack"] != [34,35,38,39,42,43] or not part["coverage_exact"] or not part["disjoint"]:
        raise ValueError("BC2-28 partition preflight regression")

    ctx = b27.b26.b25.capture_bc224_setup()
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

    p35_records = []
    leaf_unsat = leaf_unknown = leaf_sat = 0
    first_sat_witness = None

    for parent_index, n1v, n2v, p33v, p34v, p35v in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label - 1] == value)
        solver.add(n1 == n1v)
        solver.add(n2 == n2v)
        solver.add(p[32] == p33v)
        solver.add(p[33] == p34v)
        solver.add(p[34] == p35v)
        leaves = []
        saw_unknown = saw_sat = False
        witness = None
        for p38v in range(n2v // 2 + 1):
            solver.push()
            solver.add(p[BOUNDARY38_LABEL - 1] == p38v)
            result = solver.check()
            rec = {"p38": p38v, "result": str(result)}
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
                n2m34 = 2 * pv[33] + sum(pv[j - 1] for j in blocks[1][0])
                n2m35 = 2 * pv[34] + sum(pv[j - 1] for j in blocks[1][1])
                n2m38 = 2 * pv[37] + sum(pv[j - 1] for j in blocks[1][2])
                if n1m != n1v or n2m34 != n2v or n2m35 != n2v or n2m38 != n2v:
                    raise ValueError("SAT witness fibre regression")
                if pv[32] != p33v or pv[33] != p34v or pv[34] != p35v or pv[37] != p38v:
                    raise ValueError("SAT witness boundary38 partition regression")
                if pv[48] % den not in allowed:
                    raise ValueError("SAT witness x4 residue regression")
                witness = {
                    "parent_index": parent_index, "n1": n1v, "n2": n2v,
                    "p33": p33v, "p34": p34v, "p35": p35v, "p38": p38v,
                    "picard64_coordinates": xv, "all140_pairings": pv,
                    "all140_pairings_sha256": csha(pv),
                }
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
                raise ValueError("UNSAT p38 coverage regression")
            outcome = "unsat"
        p35_records.append({
            "parent_index": parent_index, "n1": n1v, "n2": n2v,
            "p33": p33v, "p34": p34v, "p35": p35v,
            "result": outcome, "p38_leaf_count_checked": len(leaves), "p38_leaves": leaves,
        })
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

    p34_records = aggregate(["parent_index","n1","n2","p33","p34"], p35_records)
    p33_records = aggregate(["parent_index","n1","n2","p33"], p34_records)
    branch_records = aggregate(["parent_index","n1","n2"], p33_records)
    parent_records = aggregate(["parent_index"], branch_records)
    if len(p34_records) != 13 or len(p33_records) != 13 or len(branch_records) != 13 or len(parent_records) != 9:
        raise ValueError("BC2-28 aggregate coverage regression")

    newly_unsat = [r["parent_index"] for r in parent_records if r["result"] == "unsat"]
    residual_unknown = [r["parent_index"] for r in parent_records if r["result"] == "unknown"]
    sat_parents = [r["parent_index"] for r in parent_records if r["result"] == "sat"]
    def count(records, val):
        return sum(r["result"] == val for r in records)
    parent_unsat, parent_unknown, parent_sat = len(newly_unsat), len(residual_unknown), len(sat_parents)
    known_unsat_lower_bound = 7155 + parent_unsat
    residual_p35 = [{k:r[k] for k in ("parent_index","n1","n2","p33","p34","p35")} for r in p35_records if r["result"] == "unknown"]
    residual_p34 = [{k:r[k] for k in ("parent_index","n1","n2","p33","p34")} for r in p34_records if r["result"] == "unknown"]
    residual_p33 = [{k:r[k] for k in ("parent_index","n1","n2","p33")} for r in p33_records if r["result"] == "unknown"]
    residual_branches = [{k:r[k] for k in ("parent_index","n1","n2")} for r in branch_records if r["result"] == "unknown"]

    if parent_sat:
        status = "PASS_BOUNDARY38_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_29_ANALYZE_BOUNDARY38_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_ALL_9_BC2_27_RETAINED_UNKNOWN_PARENTS_EXACT_UNSAT_BY_BOUNDARY38_PARTITION"
        next_id = "BC2_29_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_BOUNDARY38_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_29_REFINE_RESIDUAL_BY_BOUNDARY39_OR_NEXT_EXACT_PAIRING"

    body = {
        "schema":"STAGE32EX5_BC2_28_BOUNDARY38_PARTITION_V1","stage":"32EX5",
        "unit":"BC2_28_PARTITION_BC2_27_RESIDUAL_P35_UNKNOWN_BY_BOUNDARY38","status":status,
        "source_locks":{"bc2_27_checkpoint":E27,"bc2_28_residual_manifest":EMAN,"preflight":EPF,"bc2_27_source_git_blob_sha":EB27},
        "audit_consumption":{"bc2_27_hostile_audit_status":"PASS","bc2_27_hostile_audit_exact_head":BC2_27_AUDIT_HEAD,"bc2_27_hostile_audit_review_id":BC2_27_AUDIT_REVIEW},
        "partition_certificate":{"boundary_pairing_label":38,"fibre_degree_variable":"n2","per_p35_leaf_values_rule":"p38=0..floor(n2/2)","identity":"n2=2*p38+sum(incident exceptional pairings)","coverage_exact":True,"disjoint":True,"targeted_bc2_27_unknown_p35_leaf_count":13,"maximum_possible_subbranch_count":42},
        "target":{"checked_parent_indices":parents_targeted,"checked_parent_count":9,"checked_bc2_27_unknown_branch_count":13,"checked_bc2_27_unknown_p33_subbranch_count":13,"checked_bc2_27_unknown_p34_leaf_count":13,"checked_bc2_27_unknown_p35_leaf_count":13,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
        "result":{
            "parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,"newly_unsat_parent_indices":newly_unsat,"residual_unknown_parent_indices":residual_unknown,"sat_parent_indices":sat_parents,"parent_records":parent_records,
            "branch_unsat_count":count(branch_records,"unsat"),"branch_unknown_count":count(branch_records,"unknown"),"branch_sat_count":count(branch_records,"sat"),"residual_unknown_branches":residual_branches,"branch_records":branch_records,
            "p33_subbranch_unsat_count":count(p33_records,"unsat"),"p33_subbranch_unknown_count":count(p33_records,"unknown"),"p33_subbranch_sat_count":count(p33_records,"sat"),"residual_unknown_p33_subbranches":residual_p33,"p33_subbranch_records":p33_records,
            "p34_target_unsat_count":count(p34_records,"unsat"),"p34_target_unknown_count":count(p34_records,"unknown"),"p34_target_sat_count":count(p34_records,"sat"),"residual_unknown_p34_leaves":residual_p34,"p34_target_records":p34_records,
            "p35_target_unsat_count":count(p35_records,"unsat"),"p35_target_unknown_count":count(p35_records,"unknown"),"p35_target_sat_count":count(p35_records,"sat"),"residual_unknown_p35_leaves":residual_p35,"p35_target_records":p35_records,
            "p38_leaf_unsat_count":leaf_unsat,"p38_leaf_unknown_count":leaf_unknown,"p38_leaf_sat_count":leaf_sat,"per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,"solver":"Z3_QF_LIA_N355_REDUNDANT_CUTS_PLUS_EXACT_N1_N2_P33_P34_P35_PLUS_BOUNDARY38_PARTITION","z3_version":get_version_string()
        },
        "sat_witness":first_sat_witness,
        "interpretation":{"known_parent_unsat_count_lower_bound":known_unsat_lower_bound,"known_retained_unknown_identity_count_after_this_run":parent_unknown,"remaining_target_unknown_branch_count":count(branch_records,"unknown"),"remaining_target_unknown_p33_subbranch_count":count(p33_records,"unknown"),"remaining_target_unknown_p34_leaf_count":count(p34_records,"unknown"),"remaining_target_unknown_p35_leaf_count":count(p35_records,"unknown"),"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False},
        "credit":{"all_9_bc2_27_residual_parents_exact_unsat":parent_sat == 0 and parent_unknown == 0,"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
        "firewalls":{"unretained_172_parent_identities_inferred":False,"unknown_relabelled_unsat":False,"partition_leaf_unknown_dropped":False,"sat_relabelled_actual_curve":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False}
    }
    result = {**body, "canonical_sha256_without_this_field": csha(body)}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
