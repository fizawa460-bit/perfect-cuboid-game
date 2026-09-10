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
BC2_22 = HERE / "bc2-22-recheck-44-residual-unknown-checkpoint.json"
PREFLIGHT = HERE / "bc2-23-n355-redundant-cut-acceleration-preflight.json"

EXPECTED_BC2_17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
EXPECTED_BC2_18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
EXPECTED_BC2_19 = "62e97cdb8bd6a8d14c0ac176576bd2cf2ec51020295f8703cbefc3bc85f001eb"
EXPECTED_BC2_22 = "e8151702d8386eeab44d9e9705abe7b4fa0e19dde96933ffdabdc56329f2fdc2"
EXPECTED_PREFLIGHT = "680ea3df4f90402d6535066a67b40bc8b635f68aa2fe2ab76bd06d9aaff96495"
EXPECTED_D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXPECTED_FEASIBLE_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
EXPECTED_PARENT_COUNT = 7336
EXPECTED_ENUMERATED_PARENT_COUNT = 177100
NORMAL_COUNT = 92
ALL140_COUNT = 140
PICARD_RANK = 64
NORMAL_MASS = 112
TARGET_D = 8
TARGET_E = 8
X4_LABEL = 49
BOUNDARY_PACKS = [[33,36,37,40,41,44], [34,35,38,39,42,43]]

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

def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=5000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_D18_BLOB:
        raise ValueError("BC2-18 enumerator source blob regression")

    c17 = checked(BC2_17, EXPECTED_BC2_17)
    c18 = checked(BC2_18, EXPECTED_BC2_18, replay=False)
    c19 = checked(BC2_19, EXPECTED_BC2_19)
    c22 = checked(BC2_22, EXPECTED_BC2_22)
    pf = checked(PREFLIGHT, EXPECTED_PREFLIGHT)

    targets = [int(v) for v in c22["result"]["residual_unknown_parent_indices"]]
    if targets != [int(v) for v in pf["target"]["retained_unknown_parent_indices"]]:
        raise ValueError("BC2-22/preflight residual target mismatch")
    if len(targets) != 36 or len(set(targets)) != 36 or targets != sorted(targets):
        raise ValueError("BC2-23 target list regression")
    if c22["interpretation"]["known_parent_unsat_count_lower_bound"] != 7128:
        raise ValueError("BC2-22 known UNSAT lower bound regression")
    if c22["target"]["other_unretained_unknown_identity_count"] != 172:
        raise ValueError("unretained unknown count regression")
    if c18["exact_decomposition"]["enumerated_parent_count"] != EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("BC2-18 enumeration count regression")
    if c18["exact_decomposition"]["mod8_extendable_parent_count"] != EXPECTED_PARENT_COUNT:
        raise ValueError("BC2-18 parent count regression")
    if c18["exact_decomposition"]["feasible_stream_sha256"] != EXPECTED_FEASIBLE_STREAM:
        raise ValueError("BC2-18 feasible stream regression")
    if (c19["result"]["unsat_count"], c19["result"]["unknown_count"], c19["result"]["sat_count"]) != (7100, 236, 0):
        raise ValueError("BC2-19 partition regression")

    fixed = {int(k): int(v) for k, v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("fixed exceptional pairing regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc223_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc223_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (ALL140_COUNT, PICARD_RANK):
        raise ValueError("pairing matrix shape regression")

    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    if coords.shape != (ALL140_COUNT, PICARD_RANK) or gram.shape != (PICARD_RANK, PICARD_RANK):
        raise ValueError("retained coordinate/Gram shape regression")
    full = coords * gram * coords.T

    block_labels: list[list[list[int]]] = []
    fibre_functionals: list[list[Matrix]] = []
    geometry_summary = []
    for factor_index, pack in enumerate(BOUNDARY_PACKS, start=1):
        seen: list[int] = []
        blocks: list[list[int]] = []
        funcs: list[Matrix] = []
        summaries = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression label={boundary}")
            seen.extend(inc)
            blocks.append(inc)
            fcoef = 2 * P.row(boundary - 1) + row_sum(P, inc)
            funcs.append(fcoef)
            summaries.append({"boundary_label": boundary, "exceptional_labels": inc})
        if sorted(seen) != list(range(93, 141)):
            raise ValueError(f"factor {factor_index} exceptional partition regression")
        if any(f != funcs[0] for f in funcs[1:]):
            raise ValueError(f"factor {factor_index} fibre functional regression")
        block_labels.append(blocks)
        fibre_functionals.append(funcs)
        geometry_summary.append({"factor": factor_index, "boundary_pack": pack, "blocks": summaries})

    normal_mass_functional = row_sum(P, list(range(1, 93)))
    exceptional_mass_functional = row_sum(P, list(range(93, 141)))
    if 19 * (fibre_functionals[0][0] + fibre_functionals[1][0]) != normal_mass_functional + 5 * exceptional_mass_functional:
        raise ValueError("N352 degree-sum Picard functional regression")
    if (NORMAL_MASS + 5 * TARGET_E) != 19 * TARGET_D:
        raise ValueError("target mass/degree substitution regression")

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
        allowed = [r for r in range(den) if d18.feasible(x4_check, yE + [r])]
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

    fibre_exprs = []
    for pack, blocks in zip(BOUNDARY_PACKS, block_labels):
        vals = []
        for boundary, block in zip(pack, blocks):
            vals.append(2 * p[boundary - 1] + sum(p[j - 1] for j in block))
        for v in vals[1:]:
            solver.add(v == vals[0])
        fibre_exprs.append(vals[0])

    solver.add(fibre_exprs[0] + fibre_exprs[1] == TARGET_D)
    solver.add(fibre_exprs[0] >= 0, fibre_exprs[0] <= TARGET_D)
    solver.add(fibre_exprs[1] >= 0, fibre_exprs[1] <= TARGET_D)

    for label in range(93, 141):
        solver.add(p[label - 1] <= TARGET_D // 2)

    block_pair_cut_count = 0
    for block1 in block_labels[0]:
        s1 = sum(p[j - 1] for j in block1)
        for block2 in block_labels[1]:
            s2 = sum(p[j - 1] for j in block2)
            solver.add(s1 + s2 <= TARGET_D)
            block_pair_cut_count += 1
    if block_pair_cut_count != 36:
        raise ValueError("block-pair cut count regression")

    records = []
    newly_unsat = []
    residual_unknown = []
    first_sat_witness = None

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
                raise ValueError("SAT witness original base regression")
            if any(pv[label - 1] != value for label, value in zip(selected_exceptional_labels, yE)):
                raise ValueError("SAT witness parent regression")
            if max(pv[92:]) > TARGET_D // 2:
                raise ValueError("SAT witness redundant diagonal cut regression")
            for block1 in block_labels[0]:
                for block2 in block_labels[1]:
                    if sum(pv[j - 1] for j in block1) + sum(pv[j - 1] for j in block2) > TARGET_D:
                        raise ValueError("SAT witness redundant block cut regression")
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
    known_unsat_lower_bound = 7128 + u

    if t:
        status = "PASS_N355_REDUNDANT_CUT_PICARD64_FEASIBLE_WITNESS_FOUND_NO_CURVE_CREDIT"
        next_id = "BC2_24_ANALYZE_REDUNDANT_CUT_SAT_WITNESS"
    elif q == 0:
        status = "PASS_ALL_36_RETAINED_BC2_22_UNKNOWN_EXACT_UNSAT_WITH_N355_REDUNDANT_CUT_ACCELERATION"
        next_id = "BC2_24_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_N355_REDUNDANT_CUT_ACCELERATION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_24_PARTITION_REMAINING_RETAINED_UNKNOWN_BY_EXPLICIT_FIBRE_DEGREE"

    body = {
        "schema": "STAGE32EX5_BC2_23_N355_REDUNDANT_CUT_ACCELERATION_V1",
        "stage": "32EX5",
        "unit": "BC2_23_TEST_N355_STRUCTURAL_INEQUALITIES_ON_36_RETAINED_UNKNOWN_PARENTS",
        "status": status,
        "source_locks": {
            "bc2_17": EXPECTED_BC2_17,
            "bc2_18": EXPECTED_BC2_18,
            "bc2_19": EXPECTED_BC2_19,
            "bc2_22": EXPECTED_BC2_22,
            "preflight": EXPECTED_PREFLIGHT,
            "bc2_18_enumerator_git_blob_sha": EXPECTED_D18_BLOB,
            "bc2_18_feasible_stream_sha256": EXPECTED_FEASIBLE_STREAM,
            "retained_bundle": d18.EXPECTED_BUNDLE_CANONICAL,
            "retained_marking": d18.EXPECTED_MARKING_CANONICAL,
            "n355_full_prefix_hostile_audit_review_id": pf["source_locks"]["n355_full_prefix_hostile_audit_review_id"],
            "n355_full_prefix_hostile_audit_exact_head": pf["source_locks"]["n355_full_prefix_hostile_audit_exact_head"],
            "stage32_main_head_observed": pf["source_locks"]["stage32_main_head_observed"]
        },
        "geometry_replay": {
            "boundary_packs": BOUNDARY_PACKS,
            "pack_data": geometry_summary,
            "each_boundary_incident_exceptional_count": 8,
            "each_pack_partitions_all_48_exceptionals": true,
            "fibre_functionals_constant_within_each_pack": true,
            "degree_sum_mass_functional_identity_replayed": true,
            "target_mass_substitution": {"normal_mass": NORMAL_MASS, "exceptional_mass": TARGET_E, "project_degree": TARGET_D, "identity": "112+5*8=19*8"}
        },
        "redundant_cut_certificate": {
            "feasible_set_preserved": true,
            "reason": "All added constraints are consequences of the exact retained Picard64 fibre functionals, BC2-19 all140 nonnegativity, and BC2-19 mass equations.",
            "explicit_fibre_equalities": 10,
            "explicit_degree_sum_equality": 1,
            "explicit_fibre_degree_box_constraints": 4,
            "explicit_exceptional_diagonal_caps": 48,
            "explicit_full_block_pair_cuts": 36,
            "diagonal_cap": 4,
            "block_pair_cap": 8
        },
        "target": {
            "row_id": "g1-d008", "g": 1, "d": TARGET_D, "e": TARGET_E,
            "checked_parent_indices": targets, "checked_count": len(targets),
            "unretained_bc2_19_unknown_identity_count": 172,
            "unretained_bc2_19_unknown_identities_inferred": false
        },
        "result": {
            "unsat_count": u, "unknown_count": q, "sat_count": t,
            "newly_unsat_parent_indices": newly_unsat,
            "residual_unknown_parent_indices": residual_unknown,
            "records": records,
            "per_parent_timeout_ms": args.per_parent_timeout_ms,
            "solver": "Z3_QF_LIA_WITH_LOGICALLY_REDUNDANT_N355_PICARD_CUTS",
            "z3_version": get_version_string()
        },
        "sat_witness": first_sat_witness,
        "interpretation": {
            "known_parent_unsat_count_lower_bound": known_unsat_lower_bound,
            "known_retained_unknown_identity_count_after_this_run": q,
            "unretained_unknown_identity_count": 172,
            "whole_first_block_unsat_proved": false,
            "n355_added_new_mathematical_feasible_set_restriction": false,
            "n355_used_as_solver_acceleration": true
        },
        "credit": {
            "this_36_parent_slice_exact_unsat": (t == 0 and q == 0),
            "whole_first_block_unsat": false,
            "whole_stratum_closed": false,
            "full178_complete": false,
            "stage32_main_credit": false,
            "effectivity_or_actual_curve_existence_proved": false,
            "theorem_credit": false,
            "endpoint_credit": false
        },
        "firewalls": {
            "unretained_172_parent_identities_inferred": false,
            "unknown_relabelled_unsat": false,
            "redundant_cut_relabelled_new_main_theorem": false,
            "sat_relabelled_actual_curve": false,
            "main_promotion": false,
            "merge_authorized": false,
            "perfect_cuboid_existence_claim": false,
            "perfect_cuboid_nonexistence_claim": false
        },
        "next_exact_unit": {"id": next_id, "main_promotion_authorized": false}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"canonical": body["canonical_sha256_without_this_field"], "status": status, "unsat": u, "unknown": q, "sat": t, "known_unsat_lower_bound": known_unsat_lower_bound, "next": next_id}, sort_keys=True))

if __name__ == "__main__":
    main()
