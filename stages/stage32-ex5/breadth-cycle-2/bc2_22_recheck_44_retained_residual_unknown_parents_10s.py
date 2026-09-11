#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

HERE = Path(__file__).resolve().parent
BC2_17 = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
BC2_18 = HERE / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
BC2_19 = HERE / "bc2-19-n354-survivor-normal-positivity-mass-checkpoint.json"
BC2_21 = HERE / "bc2-21-first64-unknown-parent-slice-checkpoint.json"

EXPECTED_BC2_17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC2_18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_BC2_19 = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_BC2_21 = "8b40a6b0ee650897d276fb7e543d6f31ef3f76af6f3e923e109b8d02ecd46f4f"
EXPECTED_D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXPECTED_FEASIBLE_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
EXPECTED_PARENT_COUNT = 7336
EXPECTED_ENUMERATED_PARENT_COUNT = 177100
NORMAL_COUNT = 92
ALL140_COUNT = 140
PICARD_RANK = 64
NORMAL_MASS = 112
TARGET_E = 8
X4_LABEL = 49

def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def checked(path: Path, expected: str, *, replay: bool = True) -> dict:
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field drift: {path.name}")
    if replay:
        cp = dict(obj)
        cp.pop("canonical_sha256_without_this_field", None)
        if csha(cp) != expected:
            raise ValueError(f"canonical replay drift: {path.name}")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=10000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_D18_BLOB:
        raise ValueError("BC2-18 enumerator source blob regression")

    c17 = checked(BC2_17, EXPECTED_BC2_17)
    c18 = checked(BC2_18, EXPECTED_BC2_18, replay=False)
    c19 = checked(BC2_19, EXPECTED_BC2_19)
    c21 = checked(BC2_21, EXPECTED_BC2_21)

    if c18["exact_decomposition"]["enumerated_parent_count"] != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("BC2-18 enumeration count regression")
    if c18["exact_decomposition"]["mod8_extendable_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent count regression")
    if c18["exact_decomposition"]["feasible_stream_sha256"] != EXPECTED_FEASIBLE_STREAM:
        raise ValueError("BC2-18 feasible stream regression")
    if (c19["result"]["unsat_count"], c19["result"]["unknown_count"], c19["result"]["sat_count"]) != (7100, 236, 0):
        raise ValueError("BC2-19 partition regression")

    targets = [int(v) for v in c21["result"]["residual_unknown_parent_indices"]]
    if len(targets) != 44 or len(set(targets)) != 44 or targets != sorted(targets):
        raise ValueError("BC2-21 residual target list regression")
    if c21["result"]["unsat_count"] != 20 or c21["result"]["unknown_count"] != 44 or c21["result"]["sat_count"] != 0:
        raise ValueError("BC2-21 partition regression")
    if c21["interpretation"]["bc2_19_known_unsat_count_after_this_slice"] != 7120:
        raise ValueError("BC2-21 known UNSAT lower bound regression")

    fixed = {int(k): int(v) for k, v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("fixed exceptional pairing regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc222_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc222_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("pairing matrix shape regression")

    selected_labels = [int(v) for v in d18.INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(PICARD_RANK)))
    if Psel.det() == 0:
        raise ValueError("selected64 pairing matrix singular")
    Pinv = Psel.inv()
    den = d18.lcm_denominator(Pinv)
    if den != 8:
        raise ValueError("selected64 denominator regression")
    Bq = Pinv * den
    if any(q.q != 1 for q in Bq):
        raise ValueError("selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])

    selected_normal_positions = [j for j, label in enumerate(selected_labels) if label <= NORMAL_COUNT]
    selected_exceptional_positions = [j for j, label in enumerate(selected_labels) if label > NORMAL_COUNT]
    selected_exceptional_labels = [selected_labels[j] for j in selected_exceptional_positions]
    free_selected_exceptional_labels = [label for label in selected_exceptional_labels if label not in fixed]
    if len(free_selected_exceptional_labels) != 19:
        raise ValueError("free selected exceptional count regression")

    full_check = d18.build_hnf_extension_check(B, den, selected_exceptional_positions, selected_normal_positions)
    x4_pos = selected_labels.index(X4_LABEL)
    x4_check = d18.build_hnf_extension_check(B, den, selected_exceptional_positions + [x4_pos], [j for j in selected_normal_positions if j != x4_pos])

    parents = []
    stream = hashlib.sha256()
    enumerated = 0
    for comp in d18.weak_compositions_at_most(6, len(free_selected_exceptional_labels)):
        enumerated += 1
        by_label = dict(fixed)
        by_label.update({label: int(value) for label, value in zip(free_selected_exceptional_labels, comp)})
        yE = [int(by_label[label]) for label in selected_exceptional_labels]
        allowed = [residue for residue in range(den) if d18.feasible(x4_check, yE + [residue])]
        full_ok = d18.feasible(full_check, yE)
        if full_ok != bool(allowed):
            raise ValueError("HNF parent/x4 extension regression")
        if not full_ok:
            continue
        record = {"selected_exceptional_pairings": yE, "selected_residual_mass": sum(comp), "x4_allowed_residues_mod8": allowed}
        stream.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parents.append((tuple(int(v) for v in comp), yE, allowed))

    if enumerated != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("parent enumeration coverage regression")
    if len(parents) != EXPECTED_PARENT_COUNT:
        raise ValueError("mod8-surviving parent count regression")
    if stream.hexdigest() != EXPECTED_FEASIBLE_STREAM:
        raise ValueError("parent ordering/feasible-stream regression")
    if max(targets) >= len(parents):
        raise ValueError("target index range regression")

    x = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    p = [sum(int(P[i, j]) * x[j] for j in range(PICARD_RANK)) for i in range(ALL140_COUNT)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.per_parent_timeout_ms)
    for i in range(NORMAL_COUNT):
        solver.add(p[i] >= 0, p[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, ALL140_COUNT):
        solver.add(p[i] >= 0, p[i] <= TARGET_E)
    solver.add(sum(p[:NORMAL_COUNT]) == NORMAL_MASS)
    solver.add(sum(p[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        solver.add(p[label - 1] == value)

    records = []
    first_sat_witness = None
    newly_unsat = []
    residual_unknown = []

    for idx in targets:
        comp, yE, allowed = parents[idx]
        solver.push()
        for label, value in zip(selected_exceptional_labels, yE):
            solver.add(p[label - 1] == int(value))
        result = solver.check()
        rec = {"parent_index": idx, "result": str(result)}
        if result == unsat:
            newly_unsat.append(idx)
        elif result == unknown:
            rec["reason_unknown"] = solver.reason_unknown()
            residual_unknown.append(idx)
        elif result == sat:
            model = solver.model()
            xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
            pv = [sum(int(P[i, j]) * xv[j] for j in range(PICARD_RANK)) for i in range(ALL140_COUNT)]
            if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != NORMAL_MASS or sum(pv[NORMAL_COUNT:]) != TARGET_E:
                raise ValueError("SAT witness mass/nonnegativity regression")
            if any(pv[label - 1] != value for label, value in zip(selected_exceptional_labels, yE)):
                raise ValueError("SAT witness parent regression")
            x4 = pv[X4_LABEL - 1]
            if x4 % den not in allowed:
                raise ValueError("SAT witness x4 residue regression")
            rec["x4"] = x4
            rec["all140_pairings_sha256"] = csha(pv)
            if first_sat_witness is None:
                first_sat_witness = {"parent_index": idx, "picard64_coordinates": xv, "all140_pairings": pv, "all140_pairings_sha256": csha(pv)}
        else:
            raise ValueError(f"unexpected solver result: {result}")
        records.append(rec)
        solver.pop()

    u = len(newly_unsat)
    q = len(residual_unknown)
    t = sum(rec["result"] == "sat" for rec in records)

    if t:
        status = "PASS_RETAINED_RESIDUAL_SLICE_PICARD64_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"
        next_id = "BC2_23_ANALYZE_RETAINED_RESIDUAL_SLICE_SAT_WITNESS"
    elif q == 0:
        status = "PASS_44_RETAINED_RESIDUAL_UNKNOWN_PARENTS_EXACT_UNSAT_10S"
        next_id = "BC2_23_RECOVER_OR_REPLAY_REMAINING_172_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_RETAINED_RESIDUAL_SLICE_STILL_HAS_UNKNOWN"
        next_id = "BC2_23_STRUCTURAL_OR_LONGER_RECHECK_OF_RETAINED_RESIDUAL_UNKNOWN"

    body = {
        "schema": "STAGE32EX5_BC2_22_RECHECK_44_RETAINED_RESIDUAL_UNKNOWN_PARENTS_10S_V1",
        "stage": "32EX5",
        "unit": "BC2_22_RECHECK_44_RETAINED_RESIDUAL_UNKNOWN_PARENTS_10S",
        "status": status,
        "source_locks": {"bc2_17": EXPECTED_BC2_17, "bc2_18": EXPECTED_BC2_18, "bc2_19": EXPECTED_BC2_19, "bc2_21": EXPECTED_BC2_21, "bc2_18_enumerator_git_blob_sha": EXPECTED_D18_BLOB, "bc2_18_feasible_stream_sha256": EXPECTED_FEASIBLE_STREAM, "retained_bundle": d18.EXPECTED_BUNDLE_CANONICAL, "retained_marking": d18.EXPECTED_MARKING_CANONICAL},
        "target": {"source_bc2_19_unknown_count": 236, "source_bc2_21_residual_unknown_count": 44, "checked_parent_indices": targets, "other_unretained_unknown_identity_count": 172, "other_unretained_unknown_identities_inferred": False},
        "result": {"checked_count": len(records), "unsat_count": u, "unknown_count": q, "sat_count": t, "newly_unsat_parent_indices": newly_unsat, "residual_unknown_parent_indices": residual_unknown, "records": records, "per_parent_timeout_ms": args.per_parent_timeout_ms, "solver": "Z3_QF_LIA", "z3_version": get_version_string()},
        "sat_witness": first_sat_witness,
        "interpretation": {"known_parent_unsat_count_lower_bound": 7120 + u, "known_retained_unknown_identity_count_after_this_run": q, "unretained_unknown_identity_count": 172, "whole_first_block_unsat_proved": False},
        "credit": {"this_44_parent_slice_exact_unsat": (t == 0 and q == 0), "whole_first_block_unsat": False, "whole_stratum_closed": False, "full178_complete": False, "stage32_main_credit": False, "effectivity_or_actual_curve_existence_proved": False, "theorem_credit": False, "endpoint_credit": False},
        "firewalls": {"unretained_172_parent_identities_inferred": False, "unknown_relabelled_unsat": False, "sat_relabelled_actual_curve": False, "main_promotion": False, "merge_authorized": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False},
        "next_exact_unit": {"id": next_id, "main_promotion_authorized": False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"canonical": body["canonical_sha256_without_this_field"], "status": status, "unsat": u, "unknown": q, "sat": t, "known_unsat_lower_bound": 7120 + u, "next": next_id}, sort_keys=True))

if __name__ == "__main__":
    main()
