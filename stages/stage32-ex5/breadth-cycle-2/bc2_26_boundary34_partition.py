#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from z3 import get_version_string, sat, unknown, unsat

import bc2_25_boundary33_partition as b25

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P25 = HERE / "bc2-25-boundary33-partition-checkpoint.json"
PMAN = HERE / "bc2-26-residual-p33-subbranch-manifest.json"
PF = HERE / "bc2-26-boundary34-partition-preflight.json"

E25 = "fc4e4541a4f349e6c249f7dadd85f91edfd1c0dc1cb56d92b18bbf13054a4518"
EMAN = "39d816977fed0c770e155422ab7209ea3dd98dee49eb96daabb5b30557708a3a"
EPF = "92c6e53d8e2e3f5bf6576983c042667b5c56c154206c5514877ab4f1e6af3bcd"
EB25 = "1c10dcc88059e505ab64cfad90cf1bae19b6e350"
EB24 = "fea28d97abd21c4ee1a8a4604e38785045f4c7f5"
EB18 = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EHPERP = "fb1eb380ca786e42a6b00c5ef454b0e79fdba771"
EPAIR = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
BOUNDARY33_LABEL = 33
BOUNDARY34_LABEL = 34
TARGET_D = 8


def checked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field drift: {path.name}")
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    if b25.b24.csha(q) != expected:
        raise ValueError(f"canonical replay drift: {path.name}")
    return obj


def git_blob_sha(path: Path) -> str:
    return b25.b24.git_blob_sha(path)


def lock_executable_chain() -> None:
    if git_blob_sha(Path(b25.__file__).resolve()) != EB25:
        raise ValueError("BC2-25 source blob regression")
    if git_blob_sha(Path(b25.b24.__file__).resolve()) != EB24:
        raise ValueError("BC2-24 source blob regression")
    if git_blob_sha(Path(b25.b24.d18.__file__).resolve()) != EB18:
        raise ValueError("BC2-18 source blob regression")
    hperp = ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py"
    pairing = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
    if git_blob_sha(hperp) != EHPERP:
        raise ValueError("hperp_integral_adapter source blob regression")
    if git_blob_sha(pairing) != EPAIR:
        raise ValueError("pairing_prefix_engine source blob regression")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-subbranch-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_subbranch_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    lock_executable_chain()
    c25 = checked(P25, E25)
    manifest = checked(PMAN, EMAN)
    pf = checked(PF, EPF)

    if c25["result"]["parent_unknown_count"] != 16 or c25["result"]["branch_unknown_count"] != 36:
        raise ValueError("BC2-25 retained UNKNOWN accounting regression")
    if c25["result"]["subbranch_unknown_count"] != 38:
        raise ValueError("BC2-25 p33 UNKNOWN accounting regression")
    if c25["interpretation"]["known_parent_unsat_count_lower_bound"] != 7148:
        raise ValueError("BC2-25 lower-bound regression")
    if c25["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("BC2-25 unretained identity count regression")

    targets = [(int(r["parent_index"]), int(r["n1"]), int(r["n2"]), int(r["p33"])) for r in manifest["target"]["residual_unknown_p33_subbranches"]]
    if len(targets) != 38 or len(set(targets)) != 38:
        raise ValueError("BC2-26 residual p33 target regression")
    parents_targeted = sorted({p for p, _, _, _ in targets})
    if parents_targeted != [1000,1003,1014,1048,1050,1064,1066,1103,1106,1117,1119,1133,1198,1218,1224,1243]:
        raise ValueError("BC2-26 residual parent set regression")
    branches_targeted = sorted({(p,n1,n2) for p,n1,n2,_ in targets})
    if len(branches_targeted) != 36:
        raise ValueError("BC2-26 residual branch count regression")
    maximum = sum(n2 // 2 + 1 for _, _, n2, _ in targets)
    if maximum != 110 or pf["partition"]["maximum_subbranch_checks"] != 110:
        raise ValueError("BC2-26 boundary34 leaf-count regression")
    if manifest["partition_candidate"]["maximum_subbranch_checks"] != 110:
        raise ValueError("BC2-26 manifest leaf-count regression")

    ctx = b25.capture_bc224_setup()
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

    p33_records = []
    leaf_unsat = leaf_unknown = leaf_sat = 0
    first_sat_witness = None

    for parent_index, n1v, n2v, p33v in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label - 1] == value)
        solver.add(n1 == n1v)
        solver.add(n2 == n2v)
        solver.add(p[BOUNDARY33_LABEL - 1] == p33v)
        leaves = []
        saw_unknown = saw_sat = False
        witness = None
        for p34v in range(n2v // 2 + 1):
            solver.push()
            solver.add(p[BOUNDARY34_LABEL - 1] == p34v)
            result = solver.check()
            rec = {"p34": p34v, "result": str(result)}
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
                if n1m != n1v or n2m != n2v or pv[32] != p33v or pv[33] != p34v:
                    raise ValueError("SAT witness boundary34 partition regression")
                if pv[48] % den not in allowed:
                    raise ValueError("SAT witness x4 residue regression")
                witness = {"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"p34":p34v,"picard64_coordinates":xv,"all140_pairings":pv,"all140_pairings_sha256":b25.b24.csha(pv)}
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
                raise ValueError("UNSAT p34 coverage regression")
            outcome = "unsat"
        p33_records.append({"parent_index":parent_index,"n1":n1v,"n2":n2v,"p33":p33v,"result":outcome,"p34_leaf_count_checked":len(leaves),"p34_leaves":leaves})
        solver.pop()

    by_branch = defaultdict(list)
    for r in p33_records:
        by_branch[(r["parent_index"], r["n1"], r["n2"])].append(r["result"])
    branch_records = []
    branch_unsat = branch_unknown = branch_sat = 0
    for key in branches_targeted:
        vals = by_branch[key]
        if not vals:
            raise ValueError("missing BC2-26 branch coverage")
        if "sat" in vals:
            outcome = "sat"; branch_sat += 1
        elif "unknown" in vals:
            outcome = "unknown"; branch_unknown += 1
        else:
            outcome = "unsat"; branch_unsat += 1
        branch_records.append({"parent_index":key[0],"n1":key[1],"n2":key[2],"result":outcome,"targeted_bc2_25_unknown_p33_subbranch_count":len(vals)})

    by_parent = defaultdict(list)
    for r in branch_records:
        by_parent[r["parent_index"]].append(r["result"])
    parent_records = []
    newly_unsat = []
    residual_unknown = []
    sat_parents = []
    for parent_index in parents_targeted:
        vals = by_parent[parent_index]
        if "sat" in vals:
            outcome = "sat"; sat_parents.append(parent_index)
        elif "unknown" in vals:
            outcome = "unknown"; residual_unknown.append(parent_index)
        else:
            outcome = "unsat"; newly_unsat.append(parent_index)
        parent_records.append({"parent_index":parent_index,"result":outcome,"targeted_bc2_25_unknown_branch_count":len(vals)})

    p33_unsat = sum(r["result"] == "unsat" for r in p33_records)
    p33_unknown = sum(r["result"] == "unknown" for r in p33_records)
    p33_sat = sum(r["result"] == "sat" for r in p33_records)
    parent_unsat = len(newly_unsat)
    parent_unknown = len(residual_unknown)
    parent_sat = len(sat_parents)
    known_unsat_lower_bound = 7148 + parent_unsat
    residual_p33 = [{"parent_index":r["parent_index"],"n1":r["n1"],"n2":r["n2"],"p33":r["p33"]} for r in p33_records if r["result"] == "unknown"]
    residual_branches = [{"parent_index":r["parent_index"],"n1":r["n1"],"n2":r["n2"]} for r in branch_records if r["result"] == "unknown"]

    if parent_sat:
        status = "PASS_BOUNDARY34_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_27_ANALYZE_BOUNDARY34_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_ALL_16_BC2_25_RETAINED_UNKNOWN_PARENTS_EXACT_UNSAT_BY_BOUNDARY34_PARTITION"
        next_id = "BC2_27_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_BOUNDARY34_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_27_REFINE_RESIDUAL_BY_X4_OR_THIRD_EXACT_PAIRING"

    body = {
        "schema":"STAGE32EX5_BC2_26_BOUNDARY34_PARTITION_V1","stage":"32EX5","unit":"BC2_26_PARTITION_BC2_25_RESIDUAL_P33_UNKNOWN_BY_BOUNDARY34","status":status,
        "source_locks":{"bc2_25_checkpoint":E25,"bc2_26_residual_manifest":EMAN,"preflight":EPF,"bc2_25_source_git_blob_sha":EB25,"bc2_24_source_git_blob_sha":EB24,"bc2_18_source_git_blob_sha":EB18,"hperp_integral_adapter_git_blob_sha":EHPERP,"pairing_prefix_engine_git_blob_sha":EPAIR},
        "partition_certificate":{"boundary_pairing_label":34,"fibre_degree_variable":"n2","per_p33_subbranch_values_rule":"p34=0..floor(n2/2)","identity":"n2=2*p34+sum(incident exceptional pairings)","coverage_exact":True,"disjoint":True,"targeted_bc2_25_unknown_p33_subbranch_count":38,"maximum_possible_subbranch_count":110},
        "target":{"checked_parent_indices":parents_targeted,"checked_parent_count":16,"checked_bc2_25_unknown_branch_count":36,"checked_bc2_25_unknown_p33_subbranch_count":38,"unretained_bc2_19_unknown_identity_count":172,"unretained_bc2_19_unknown_identities_inferred":False},
        "result":{"parent_unsat_count":parent_unsat,"parent_unknown_count":parent_unknown,"parent_sat_count":parent_sat,"newly_unsat_parent_indices":newly_unsat,"residual_unknown_parent_indices":residual_unknown,"sat_parent_indices":sat_parents,"parent_records":parent_records,"branch_unsat_count":branch_unsat,"branch_unknown_count":branch_unknown,"branch_sat_count":branch_sat,"residual_unknown_branches":residual_branches,"branch_records":branch_records,"p33_subbranch_unsat_count":p33_unsat,"p33_subbranch_unknown_count":p33_unknown,"p33_subbranch_sat_count":p33_sat,"residual_unknown_p33_subbranches":residual_p33,"p33_subbranch_records":p33_records,"p34_leaf_unsat_count":leaf_unsat,"p34_leaf_unknown_count":leaf_unknown,"p34_leaf_sat_count":leaf_sat,"per_subbranch_timeout_ms":args.per_subbranch_timeout_ms,"solver":"Z3_QF_LIA_N355_REDUNDANT_CUTS_PLUS_EXACT_N1_N2_P33_PLUS_BOUNDARY34_PARTITION","z3_version":get_version_string()},
        "sat_witness":first_sat_witness,
        "interpretation":{"known_parent_unsat_count_lower_bound":known_unsat_lower_bound,"known_retained_unknown_identity_count_after_this_run":parent_unknown,"remaining_target_unknown_branch_count":branch_unknown,"remaining_target_unknown_p33_subbranch_count":p33_unknown,"unretained_unknown_identity_count":172,"whole_first_block_unsat_proved":False},
        "credit":{"all_16_bc2_25_residual_parents_exact_unsat":parent_sat == 0 and parent_unknown == 0,"whole_first_block_unsat":False,"whole_stratum_closed":False,"full178_complete":False,"stage32_main_credit":False,"effectivity_or_actual_curve_existence_proved":False,"theorem_credit":False,"endpoint_credit":False},
        "firewalls":{"unretained_172_parent_identities_inferred":False,"unknown_relabelled_unsat":False,"partition_leaf_unknown_dropped":False,"sat_relabelled_actual_curve":False,"main_promotion":False,"merge_authorized":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
        "next_exact_unit":{"id":next_id,"heavy_scaleout_authorized":False,"main_promotion_authorized":False}
    }
    body["canonical_sha256_without_this_field"] = b25.b24.csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"canonical":body["canonical_sha256_without_this_field"],"status":status,"parent_unsat":parent_unsat,"parent_unknown":parent_unknown,"parent_sat":parent_sat,"branch_unsat":branch_unsat,"branch_unknown":branch_unknown,"branch_sat":branch_sat,"p33_unsat":p33_unsat,"p33_unknown":p33_unknown,"p33_sat":p33_sat,"p34_leaf_unsat":leaf_unsat,"p34_leaf_unknown":leaf_unknown,"p34_leaf_sat":leaf_sat,"known_unsat_lower_bound":known_unsat_lower_bound,"next":next_id}, sort_keys=True))


if __name__ == "__main__":
    main()
