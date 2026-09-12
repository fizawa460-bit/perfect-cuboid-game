#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_28_boundary38_partition as b28

HERE = Path(__file__).resolve().parent
P28 = HERE / "bc2-28-boundary38-partition-checkpoint.json"
PMAN = HERE / "bc2-29-residual-p38-leaf-manifest.json"
PF = HERE / "bc2-29-boundary39-partition-preflight.json"

E28 = "52138e7c417d69814d5007479420b56fcc27031679bf88f432916e6c89c77ec4"
EMAN = "f04ffdd2c34f145e7650208e7fc39d69dbf08530ab699a9884f056db3c4402e4"
EPF = "1ea7f9d509f42ad688a696c8011b858e48e25a7b11909726c92cc9732d8858e9"
EB28 = "5b5f8f927d5445d006eea19de9886b6e628a6150"
BOUNDARY39_LABEL = 39
BC2_28_AUDIT_HEAD = "4221d7f9816590e808976da37ba479880f35dc22"
BC2_28_AUDIT_REVIEW = 5183082213


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    return b28.checked(path, expected)


def git_blob_sha(path: Path) -> str:
    return b28.git_blob_sha(path)


def lock_executable_chain() -> None:
    if git_blob_sha(Path(b28.__file__).resolve()) != EB28:
        raise ValueError("BC2-28 source blob regression")
    b28.lock_executable_chain()


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
    c28 = checked(P28, E28)
    manifest = checked(PMAN, EMAN)
    pf = checked(PF, EPF)
    if c28["result"]["parent_unknown_count"] != 4 or c28["result"]["parent_sat_count"] != 0:
        raise ValueError("BC2-28 parent accounting regression")
    if c28["result"]["p38_leaf_unknown_count"] != 4 or c28["result"]["p38_leaf_sat_count"] != 0:
        raise ValueError("BC2-28 residual p38 accounting regression")
    if c28["interpretation"]["known_parent_unsat_count_lower_bound"] != 7160:
        raise ValueError("BC2-28 lower-bound regression")
    if c28["interpretation"]["unretained_unknown_identity_count"] != 172:
        raise ValueError("BC2-28 unretained identity count regression")

    expected_audit = {
        "bc2_28_hostile_audit_exact_head": BC2_28_AUDIT_HEAD,
        "bc2_28_hostile_audit_review_id": BC2_28_AUDIT_REVIEW,
        "bc2_28_hostile_audit_status": "PASS",
    }
    if pf["audit_consumption"] != expected_audit:
        raise ValueError("BC2-28 hostile-audit PASS receipt regression")

    targets = [
        (int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"]), int(r["p35"]), int(r["p38"]))
        for r in manifest["target"]["residual_unknown_p38_leaves"]
    ]
    expected_targets = [(1048,2,6,1,3,3,1),(1050,2,6,1,3,3,1),(1064,2,6,1,3,3,1),(1103,2,6,0,2,3,2)]
    if targets != expected_targets or len(set(targets)) != 4:
        raise ValueError("BC2-29 audited residual p38 target regression")
    if c28["result"]["residual_unknown_parent_indices"] != [1048,1050,1064,1103]:
        raise ValueError("BC2-28 residual parent identity regression")
    maximum = sum(n2 // 2 + 1 for _, _, n2, _, _, _, _ in targets)
    if maximum != 16 or pf["target"]["maximum_subbranch_checks"] != 16:
        raise ValueError("BC2-29 boundary39 maximum-check regression")
    part = pf["partition"]
    if part["boundary_pairing_label"] != 39 or part["factor_pack"] != [34,35,38,39,42,43] or not part["coverage_exact"] or not part["disjoint"]:
        raise ValueError("BC2-29 partition preflight regression")

    ctx = b28.b27.b26.b25.capture_bc224_setup()
    solver, p, n1, n2 = ctx["solver"], ctx["p"], ctx["n1"], ctx["n2"]
    parents, exceptional_labels = ctx["parents"], ctx["exceptional_labels"]
    x, P, blocks, den = ctx["x"], ctx["P"], ctx["blocks"], int(ctx["den"])
    solver.set(timeout=args.per_subbranch_timeout_ms)

    p38_records = []
    leaf_unsat = leaf_unknown = leaf_sat = 0
    first_sat_witness = None
    for parent_index, n1v, n2v, p33v, p34v, p35v, p38v in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label - 1] == value)
        solver.add(n1 == n1v, n2 == n2v, p[32] == p33v, p[33] == p34v, p[34] == p35v, p[37] == p38v)
        leaves, saw_unknown, saw_sat, witness = [], False, False, None
        for p39v in range(n2v // 2 + 1):
            solver.push()
            solver.add(p[BOUNDARY39_LABEL - 1] == p39v)
            result = solver.check()
            rec = {"p39": p39v, "result": str(result)}
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
                fibres = [
                    2 * pv[32] + sum(pv[j - 1] for j in blocks[0][0]),
                    2 * pv[33] + sum(pv[j - 1] for j in blocks[1][0]),
                    2 * pv[34] + sum(pv[j - 1] for j in blocks[1][1]),
                    2 * pv[37] + sum(pv[j - 1] for j in blocks[1][2]),
                    2 * pv[38] + sum(pv[j - 1] for j in blocks[1][3]),
                ]
                if fibres != [n1v,n2v,n2v,n2v,n2v]:
                    raise ValueError("SAT witness fibre regression")
                if (pv[32],pv[33],pv[34],pv[37],pv[38]) != (p33v,p34v,p35v,p38v,p39v):
                    raise ValueError("SAT witness boundary39 partition regression")
                if pv[48] % den not in allowed:
                    raise ValueError("SAT witness x4 residue regression")
                witness = {"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"p35":p35v,"p38":p38v,"p39":p39v,"picard64_coordinates":xv,"all140_pairings":pv,"all140_pairings_sha256":csha(pv)}
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
            if len(leaves) != n2v // 2 + 1 or any(r["result"] != "unsat" for r in leaves):
                raise ValueError("UNSAT p39 coverage regression")
            outcome = "unsat"
        p38_records.append({"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"p35":p35v,"p38":p38v,"result":outcome,"p39_leaf_count_checked":len(leaves),"p39_leaves":leaves})
        solver.pop()

    def aggregate(keys, records):
        grouped = defaultdict(list)
        for r in records:
            grouped[tuple(r[k] for k in keys)].append(r["result"])
        out = []
        for key in sorted(grouped):
            rec = {k:v for k,v in zip(keys,key)}
            rec["result"] = classify(grouped[key])
            rec["targeted_child_count"] = len(grouped[key])
            out.append(rec)
        return out

    p35_records = aggregate(["parent_index","n1","n2","p33","p34","p35"], p38_records)
    p34_records = aggregate(["parent_index","n1","n2","p33","p34"], p35_records)
    p33_records = aggregate(["parent_index","n1","n2","p33"], p34_records)
    branch_records = aggregate(["parent_index","n1","n2"], p33_records)
    parent_records = aggregate(["parent_index"], branch_records)
    if not all(len(v) == 4 for v in (p38_records,p35_records,p34_records,p33_records,branch_records,parent_records)):
        raise ValueError("BC2-29 aggregate coverage regression")

    newly_unsat = [r["parent_index"] for r in parent_records if r["result"] == "unsat"]
    residual_unknown = [r["parent_index"] for r in parent_records if r["result"] == "unknown"]
    sat_parents = [r["parent_index"] for r in parent_records if r["result"] == "sat"]
    count = lambda records,val: sum(r["result"] == val for r in records)
    parent_unsat, parent_unknown, parent_sat = len(newly_unsat), len(residual_unknown), len(sat_parents)
    known_unsat_lower_bound = 7160 + parent_unsat
    residual_p38 = [{k:r[k] for k in ("parent_index","n1","n2","p33","p34","p35","p38")} for r in p38_records if r["result"] == "unknown"]
    if parent_sat:
        status, next_id = "PASS_BOUNDARY39_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT", "BC2_30_ANALYZE_BOUNDARY39_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status, next_id = "PASS_ALL_4_BC2_28_RETAINED_UNKNOWN_PARENTS_EXACT_UNSAT_BY_BOUNDARY39_PARTITION", "BC2_30_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status, next_id = "BLOCKED_BOUNDARY39_PARTITION_LEAVES_RETAINED_UNKNOWN", "BC2_30_REFINE_RESIDUAL_BY_BOUNDARY42_OR_NEXT_EXACT_PAIRING"

    body = {
        "schema":"STAGE32EX5_BC2_29_BOUNDARY39_PARTITION_V1","stage":"32EX5","unit":"BC2_29_PARTITION_BC2_28_RESIDUAL_P38_UNKNOWN_BY_BOUNDARY39","status":status,
        "source_locks":{"bc2_28_checkpoint":E28,"bc2_29_residual_manifest":EMAN,"preflight":EPF,"bc2_28_source_git_blob_sha":EB28},
        "audit_consumption":{"bc2_28_hostile_audit_status":"PASS","bc2_28_hostile_audit_exact_head":BC2_28_AUDIT_HEAD,"bc2_28_hostile_audit_review_id":BC2_28_AUDIT_REVIEW},
        "partition_certificate":{"boundary_pairing_label":39,"fibre_degree_variable":"n2","per_p38_leaf_values_rule":"p39=0..floor(n2/2)","identity":"n2=2*p39+sum(incident exceptional pairings)","coverage_exact":True,"disjoint":True,"targeted_bc2_28_unknown_p38_leaf_count":4,"maximum_possible_subbranch_count":16},
        "target":{"checked_parent_indices":[1048,1050,1064,1103],"checked_parent_count":4,"checked_bc2_28_unknown_p38_leaf_count":4,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
        "result":{"parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,"newly_unsat_parent_indices":newly_unsat,"residual_unknown_parent_indices":residual_unknown,"sat_parent_indices":sat_parents,"parent_records":parent_records,"branch_unsat_count":count(branch_records,"unsat"),"branch_unknown_count":count(branch_records,"unknown"),"branch_sat_count":count(branch_records,"sat"),"branch_records":branch_records,"p33_subbranch_unsat_count":count(p33_records,"unsat"),"p33_subbranch_unknown_count":count(p33_records,"unknown"),"p33_subbranch_sat_count":count(p33_records,"sat"),"p33_subbranch_records":p33_records,"p34_target_unsat_count":count(p34_records,"unsat"),"p34_target_unknown_count":count(p34_records,"unknown"),"p34_target_sat_count":count(p34_records,"sat"),"p34_target_records":p34_records,"p35_target_unsat_count":count(p35_records,"unsat"),"p35_target_unknown_count":count(p35_records,"unknown"),"p35_target_sat_count":count(p35_records,"sat"),"p35_target_records":p35_records,"p38_target_unsat_count":count(p38_records,"unsat"),"p38_target_unknown_count":count(p38_records,"unknown"),"p38_target_sat_count":count(p38_records,"sat"),"residual_unknown_p38_leaves":residual_p38,"p38_target_records":p38_records,"p39_leaf_unsat_count":leaf_unsat,"p39_leaf_unknown_count":leaf_unknown,"p39_leaf_sat_count":leaf_sat,"first_sat_witness":first_sat_witness,"per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,"z3_version":get_version_string()},
        "interpretation":{"known_parent_unsat_count_lower_bound":known_unsat_lower_bound,"known_retained_unknown_identity_count_after_this_run":parent_unknown,"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False},
        "credit":{"all_4_bc2_28_residual_parents_exact_unsat":parent_unsat==4 and parent_unknown==0 and parent_sat==0,"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
        "firewalls":{"unknown_relabelled_unsat":False,"partition_leaf_unknown_dropped":False,"sat_relabelled_actual_curve":False,"unretained_172_parent_identities_inferred":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status":status,"canonical_sha256":body["canonical_sha256_without_this_field"],"parents":{"unsat":parent_unsat,"unknown":parent_unknown,"sat":parent_sat},"p39":{"unsat":leaf_unsat,"unknown":leaf_unknown,"sat":leaf_sat},"known_parent_unsat_lower_bound":known_unsat_lower_bound,"next":next_id}, sort_keys=True))


if __name__ == "__main__":
    main()
