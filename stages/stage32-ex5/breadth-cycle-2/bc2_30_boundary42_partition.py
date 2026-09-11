#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_29_boundary39_partition as b29

HERE = Path(__file__).resolve().parent
P29 = HERE / "bc2-29-boundary39-partition-checkpoint.json"
PMAN = HERE / "bc2-30-residual-p39-leaf-manifest.json"
PF = HERE / "bc2-30-boundary42-partition-preflight.json"

E29 = "e02b94819d44d0d74e5ce393746efcc4b069075f98c4c00ad2895246e941fe1d"
EMAN = "c984fa8cb1b2d64fe3ae16dee56f521d25341ae08200898b8baec4739ca1ca64"
EPF = "771ef6c2fb29b0aaf7612820d8892ba32e477814819219304880f6d83c6fcd4e"
EB29 = "5586ca655d0fb87cc9fabb2511b11699aa0ca298"
BOUNDARY42_LABEL = 42
BC2_29_AUDIT_HEAD = "ca8e0ea7209b898d24d5f647dcce11be1aff03b2"
BC2_29_AUDIT_REVIEW = 5183342658


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked(path: Path, expected: str) -> dict:
    return b29.checked(path, expected)


def git_blob_sha(path: Path) -> str:
    return b29.git_blob_sha(path)


def lock_executable_chain() -> None:
    if git_blob_sha(Path(b29.__file__).resolve()) != EB29:
        raise ValueError("BC2-29 source blob regression")
    b29.lock_executable_chain()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-subbranch-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_subbranch_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    lock_executable_chain()
    c29 = checked(P29, E29)
    manifest = checked(PMAN, EMAN)
    pf = checked(PF, EPF)

    if c29["result"]["parent_unknown_count"] != 1 or c29["result"]["parent_sat_count"] != 0:
        raise ValueError("BC2-29 parent accounting regression")
    if c29["result"]["p39_leaf_unknown_count"] != 1 or c29["result"]["p39_leaf_sat_count"] != 0:
        raise ValueError("BC2-29 p39 accounting regression")
    if c29["interpretation"]["known_parent_unsat_count_lower_bound"] != 7163:
        raise ValueError("BC2-29 lower-bound regression")
    if c29["interpretation"]["unretained_unknown_identity_count"] != 172:
        raise ValueError("BC2-29 unretained identity count regression")

    expected_audit = {
        "bc2_29_hostile_audit_exact_head": BC2_29_AUDIT_HEAD,
        "bc2_29_hostile_audit_review_id": BC2_29_AUDIT_REVIEW,
        "bc2_29_hostile_audit_status": "PASS",
    }
    if pf["audit_consumption"] != expected_audit:
        raise ValueError("BC2-29 hostile-audit PASS receipt regression")

    targets = [
        (int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"]), int(r["p34"]), int(r["p35"]), int(r["p38"]), int(r["p39"]))
        for r in manifest["target"]["residual_unknown_p39_leaves"]
    ]
    expected_targets = [(1064, 2, 6, 1, 3, 3, 1, 3)]
    if targets != expected_targets:
        raise ValueError("BC2-30 residual p39 target regression")
    if c29["result"]["residual_unknown_parent_indices"] != [1064]:
        raise ValueError("BC2-29 residual parent identity regression")
    if c29["result"]["residual_unknown_p38_leaves"] != [{"parent_index":1064,"n1":2,"n2":6,"p33":1,"p34":3,"p35":3,"p38":1}]:
        raise ValueError("BC2-29 residual p38 identity regression")
    if pf["target"]["maximum_subbranch_checks"] != 4:
        raise ValueError("BC2-30 maximum-check regression")
    part = pf["partition"]
    if part["boundary_pairing_label"] != 42 or part["factor_pack"] != [34,35,38,39,42,43] or not part["coverage_exact"] or not part["disjoint"]:
        raise ValueError("BC2-30 partition preflight regression")

    ctx = b29.b28.b27.b26.b25.capture_bc224_setup()
    solver, p, n1, n2 = ctx["solver"], ctx["p"], ctx["n1"], ctx["n2"]
    parents, exceptional_labels = ctx["parents"], ctx["exceptional_labels"]
    x, P, blocks, den = ctx["x"], ctx["P"], ctx["blocks"], int(ctx["den"])
    solver.set(timeout=args.per_subbranch_timeout_ms)

    parent_index, n1v, n2v, p33v, p34v, p35v, p38v, p39v = targets[0]
    yE, allowed = parents[parent_index]
    solver.push()
    for label, value in zip(exceptional_labels, yE):
        solver.add(p[label - 1] == value)
    solver.add(
        n1 == n1v,
        n2 == n2v,
        p[32] == p33v,
        p[33] == p34v,
        p[34] == p35v,
        p[37] == p38v,
        p[38] == p39v,
    )

    leaves = []
    leaf_unsat = leaf_unknown = leaf_sat = 0
    first_sat_witness = None
    for p42v in range(n2v // 2 + 1):
        solver.push()
        solver.add(p[BOUNDARY42_LABEL - 1] == p42v)
        result = solver.check()
        rec = {"p42": p42v, "result": str(result)}
        if result == unsat:
            leaf_unsat += 1
        elif result == unknown:
            leaf_unknown += 1
            rec["reason_unknown"] = solver.reason_unknown()
        elif result == sat:
            leaf_sat += 1
            model = solver.model()
            xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
            pv = [sum(int(P[i, j]) * xv[j] for j in range(64)) for i in range(140)]
            fibres = [
                2 * pv[32] + sum(pv[j - 1] for j in blocks[0][0]),
                2 * pv[33] + sum(pv[j - 1] for j in blocks[1][0]),
                2 * pv[34] + sum(pv[j - 1] for j in blocks[1][1]),
                2 * pv[37] + sum(pv[j - 1] for j in blocks[1][2]),
                2 * pv[38] + sum(pv[j - 1] for j in blocks[1][3]),
                2 * pv[41] + sum(pv[j - 1] for j in blocks[1][4]),
            ]
            if fibres != [n1v,n2v,n2v,n2v,n2v,n2v]:
                raise ValueError("SAT witness fibre regression")
            if (pv[32],pv[33],pv[34],pv[37],pv[38],pv[41]) != (p33v,p34v,p35v,p38v,p39v,p42v):
                raise ValueError("SAT witness boundary42 partition regression")
            if pv[48] % den not in allowed:
                raise ValueError("SAT witness x4 residue regression")
            first_sat_witness = {
                "parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"p35":p35v,
                "p38":p38v,"p39":p39v,"p42":p42v,"picard64_coordinates":xv,"all140_pairings":pv,
                "all140_pairings_sha256":csha(pv),
            }
            rec["all140_pairings_sha256"] = first_sat_witness["all140_pairings_sha256"]
        else:
            raise ValueError("unexpected solver result")
        leaves.append(rec)
        solver.pop()
        if result == sat:
            break
    solver.pop()

    if leaf_sat:
        parent_result = "sat"
    elif leaf_unknown:
        parent_result = "unknown"
    else:
        if len(leaves) != 4 or any(r["result"] != "unsat" for r in leaves):
            raise ValueError("UNSAT p42 coverage regression")
        parent_result = "unsat"

    parent_unsat = int(parent_result == "unsat")
    parent_unknown = int(parent_result == "unknown")
    parent_sat = int(parent_result == "sat")
    known_unsat_lower_bound = 7163 + parent_unsat
    residual_unknown_p42 = [
        {"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"p35":p35v,"p38":p38v,"p39":p39v,"p42":r["p42"]}
        for r in leaves if r["result"] == "unknown"
    ]

    if parent_sat:
        status = "PASS_BOUNDARY42_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_31_ANALYZE_BOUNDARY42_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_FINAL_BC2_29_RETAINED_UNKNOWN_PARENT_EXACT_UNSAT_BY_BOUNDARY42_PARTITION"
        next_id = "BC2_31_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_BOUNDARY42_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_31_REFINE_RESIDUAL_BY_BOUNDARY43_OR_NEXT_EXACT_PAIRING"

    body = {
        "schema":"STAGE32EX5_BC2_30_BOUNDARY42_PARTITION_V1",
        "stage":"32EX5",
        "unit":"BC2_30_PARTITION_BC2_29_RESIDUAL_P39_UNKNOWN_BY_BOUNDARY42",
        "status":status,
        "source_locks":{"bc2_29_checkpoint":E29,"bc2_30_residual_manifest":EMAN,"preflight":EPF,"bc2_29_source_git_blob_sha":EB29},
        "audit_consumption":expected_audit,
        "partition_certificate":{"boundary_pairing_label":42,"fibre_degree_variable":"n2","per_p39_leaf_values_rule":"p42=0..floor(n2/2)","identity":"n2=2*p42+sum(incident exceptional pairings)","coverage_exact":True,"disjoint":True,"targeted_bc2_29_unknown_p39_leaf_count":1,"maximum_possible_subbranch_count":4},
        "target":{"checked_parent_indices":[1064],"checked_parent_count":1,"checked_bc2_29_unknown_p39_leaf_count":1,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
        "result":{"parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,"newly_unsat_parent_indices":[1064] if parent_unsat else [],"residual_unknown_parent_indices":[1064] if parent_unknown else [],"sat_parent_indices":[1064] if parent_sat else [],"p42_leaf_unsat_count":leaf_unsat,"p42_leaf_unknown_count":leaf_unknown,"p42_leaf_sat_count":leaf_sat,"p42_leaves":leaves,"residual_unknown_p42_leaves":residual_unknown_p42,"first_sat_witness":first_sat_witness,"per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,"z3_version":get_version_string()},
        "interpretation":{"known_parent_unsat_count_lower_bound":known_unsat_lower_bound,"known_retained_unknown_identity_count_after_this_run":parent_unknown,"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False},
        "credit":{"final_bc2_29_residual_parent_exact_unsat":bool(parent_unsat and not parent_unknown and not parent_sat),"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
        "firewalls":{"unknown_relabelled_unsat":False,"partition_leaf_unknown_dropped":False,"sat_relabelled_actual_curve":False,"unretained_172_parent_identities_inferred":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False},
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status":status,"canonical":body["canonical_sha256_without_this_field"],"p42_unsat":leaf_unsat,"p42_unknown":leaf_unknown,"p42_sat":leaf_sat,"known_parent_unsat_lower_bound":known_unsat_lower_bound}, sort_keys=True))


if __name__ == "__main__":
    main()
