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
P17 = HERE / "bc2-17-n354-authority-picard64-retarget-v2-evidence.json"
P18 = HERE / "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"
P23 = HERE / "bc2-23-n355-redundant-cut-acceleration-checkpoint.json"
PF = HERE / "bc2-24-explicit-fibre-degree-partition-preflight.json"

E17 = "a8dd000481a39011bd1d9d108d55e38e0420dbc2bb7abf4851595dfdb5da5072"
E18 = "b789468cb515e9ebff55ca7bbfab98a32b3857137dd0ea534fcfdf20b914f6f8"
E23 = "6da1c158da8f8171d446c39b517270c0f7bf524ac62df0cd8f9d099155cdb3a0"
EPF = "6606fe259e5393be5b086384e546be35f0c8efb0d16f98e221cc72dac4046cb9"
ED18 = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
ESTREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
NORMAL_COUNT = 92
PICARD_RANK = 64
NORMAL_MASS = 112
TARGET_E = 8
TARGET_D = 8


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked(path: Path, expected: str, replay: bool = True) -> dict:
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != expected:
        raise ValueError(f"canonical field drift: {path.name}")
    if replay:
        q = dict(obj)
        q.pop("canonical_sha256_without_this_field", None)
        if csha(q) != expected:
            raise ValueError(f"canonical replay drift: {path.name}")
    return obj


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-branch-timeout-ms", type=int, default=2000)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_branch_timeout_ms <= 0:
        raise ValueError("timeout must be positive")
    if git_blob_sha(Path(d18.__file__).resolve()) != ED18:
        raise ValueError("BC2-18 enumerator source blob regression")

    c17 = checked(P17, E17)
    c18 = checked(P18, E18, replay=False)
    c23 = checked(P23, E23)
    pf = checked(PF, EPF)
    targets = [int(v) for v in c23["result"]["residual_unknown_parent_indices"]]
    if targets != [int(v) for v in pf["target"]["retained_unknown_parent_indices"]]:
        raise ValueError("BC2-23/preflight target mismatch")
    if len(targets) != 23 or len(set(targets)) != 23 or targets != sorted(targets):
        raise ValueError("target list regression")
    if c23["interpretation"]["known_parent_unsat_count_lower_bound"] != 7141:
        raise ValueError("BC2-23 known UNSAT lower bound regression")
    if c23["target"]["other_unretained_bc2_19_unknown_identity_count"] != 172:
        raise ValueError("unretained identity count regression")
    if c18["exact_decomposition"]["enumerated_parent_count"] != 177100:
        raise ValueError("enumerated parent count regression")
    if c18["exact_decomposition"]["mod8_extendable_parent_count"] != 7336:
        raise ValueError("extendable parent count regression")
    if c18["exact_decomposition"]["feasible_stream_sha256"] != ESTREAM:
        raise ValueError("feasible stream regression")

    fixed = {int(k): int(v) for k, v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("fixed exceptional pairing regression")

    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc224_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc224_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("bundle regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("marking regression")
    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, PICARD_RANK) or coords.shape != (140, PICARD_RANK) or gram.shape != (PICARD_RANK, PICARD_RANK):
        raise ValueError("retained matrix shape regression")
    full = coords * gram * coords.T

    blocks: list[list[list[int]]] = []
    fibre_coeffs: list[Matrix] = []
    for factor_index, pack in enumerate(PACKS, start=1):
        seen: list[int] = []
        factor_blocks: list[list[int]] = []
        funcs: list[Matrix] = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"incidence regression at boundary {boundary}")
            seen.extend(inc)
            factor_blocks.append(inc)
            funcs.append(2 * P.row(boundary - 1) + row_sum(P, inc))
        if sorted(seen) != list(range(93, 141)):
            raise ValueError(f"exceptional partition regression factor {factor_index}")
        if any(f != funcs[0] for f in funcs[1:]):
            raise ValueError(f"fibre functional regression factor {factor_index}")
        blocks.append(factor_blocks)
        fibre_coeffs.append(funcs[0])
    if 19 * (fibre_coeffs[0] + fibre_coeffs[1]) != row_sum(P, list(range(1, 93))) + 5 * row_sum(P, list(range(93, 141))):
        raise ValueError("degree-sum mass functional regression")
    if NORMAL_MASS + 5 * TARGET_E != 19 * TARGET_D:
        raise ValueError("target mass-degree substitution regression")

    labels = [int(v) for v in d18.INDLIST]
    Psel = P.extract([label - 1 for label in labels], list(range(PICARD_RANK)))
    Pinv = Psel.inv()
    den = d18.lcm_denominator(Pinv)
    if den != 8:
        raise ValueError("selected64 denominator regression")
    Bq = Pinv * den
    if any(q.q != 1 for q in Bq):
        raise ValueError("selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    normal_pos = [j for j, label in enumerate(labels) if label <= NORMAL_COUNT]
    exceptional_pos = [j for j, label in enumerate(labels) if label > NORMAL_COUNT]
    exceptional_labels = [labels[j] for j in exceptional_pos]
    free_labels = [label for label in exceptional_labels if label not in fixed]
    if len(free_labels) != 19:
        raise ValueError("free selected exceptional label count regression")
    hfull = d18.build_hnf_extension_check(B, den, exceptional_pos, normal_pos)
    x4pos = labels.index(49)
    hx4 = d18.build_hnf_extension_check(B, den, exceptional_pos + [x4pos], [j for j in normal_pos if j != x4pos])

    parents: list[tuple[list[int], list[int]]] = []
    stream = hashlib.sha256()
    enumerated = 0
    for comp in d18.weak_compositions_at_most(6, len(free_labels)):
        enumerated += 1
        by = dict(fixed)
        by.update({label: int(value) for label, value in zip(free_labels, comp)})
        yE = [int(by[label]) for label in exceptional_labels]
        allowed = [r for r in range(den) if d18.feasible(hx4, yE + [r])]
        ok = d18.feasible(hfull, yE)
        if ok != bool(allowed):
            raise ValueError("HNF/x4 extension regression")
        if not ok:
            continue
        rec = {"selected_exceptional_pairings": yE, "selected_residual_mass": sum(comp), "x4_allowed_residues_mod8": allowed}
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parents.append((yE, allowed))
    if enumerated != 177100 or len(parents) != 7336 or stream.hexdigest() != ESTREAM:
        raise ValueError("BC2-18 parent ordering regression")

    x = [Int(f"x_{j}") for j in range(PICARD_RANK)]
    p = [sum(int(P[i, j]) * x[j] for j in range(PICARD_RANK)) for i in range(140)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.per_branch_timeout_ms)
    for i in range(NORMAL_COUNT):
        solver.add(p[i] >= 0, p[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, 140):
        solver.add(p[i] >= 0, p[i] <= TARGET_E)
    solver.add(sum(p[:NORMAL_COUNT]) == NORMAL_MASS)
    solver.add(sum(p[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        solver.add(p[label - 1] == value)

    fibre_exprs = []
    for pack, factor_blocks in zip(PACKS, blocks):
        vals = [2 * p[b - 1] + sum(p[j - 1] for j in block) for b, block in zip(pack, factor_blocks)]
        for value in vals[1:]:
            solver.add(value == vals[0])
        fibre_exprs.append(vals[0])
    n1, n2 = fibre_exprs
    solver.add(n1 + n2 == TARGET_D, n1 >= 0, n1 <= TARGET_D, n2 >= 0, n2 <= TARGET_D)
    for label in range(93, 141):
        solver.add(p[label - 1] <= TARGET_D // 2)
    for block1 in blocks[0]:
        s1 = sum(p[j - 1] for j in block1)
        for block2 in blocks[1]:
            solver.add(s1 + sum(p[j - 1] for j in block2) <= TARGET_D)

    parent_records = []
    newly_unsat = []
    residual_unknown = []
    first_sat_witness = None
    branch_unsat = branch_unknown = branch_sat = 0

    for parent_index in targets:
        yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(exceptional_labels, yE):
            solver.add(p[label - 1] == value)
        branches = []
        parent_sat = False
        parent_unknown = False
        parent_witness = None
        for fibre_degree in range(TARGET_D + 1):
            solver.push()
            solver.add(n1 == fibre_degree)
            result = solver.check()
            rec = {"n1": fibre_degree, "n2": TARGET_D - fibre_degree, "result": str(result)}
            if result == unsat:
                branch_unsat += 1
            elif result == unknown:
                branch_unknown += 1
                parent_unknown = True
                rec["reason_unknown"] = solver.reason_unknown()
            elif result == sat:
                branch_sat += 1
                parent_sat = True
                model = solver.model()
                xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
                pv = [sum(int(P[i, j]) * xv[j] for j in range(PICARD_RANK)) for i in range(140)]
                if min(pv) < 0 or sum(pv[:NORMAL_COUNT]) != NORMAL_MASS or sum(pv[NORMAL_COUNT:]) != TARGET_E:
                    raise ValueError("SAT witness base regression")
                if any(pv[label - 1] != value for label, value in zip(exceptional_labels, yE)):
                    raise ValueError("SAT witness parent regression")
                n1v = 2 * pv[PACKS[0][0] - 1] + sum(pv[j - 1] for j in blocks[0][0])
                n2v = 2 * pv[PACKS[1][0] - 1] + sum(pv[j - 1] for j in blocks[1][0])
                if n1v != fibre_degree or n1v + n2v != TARGET_D:
                    raise ValueError("SAT witness fibre degree regression")
                if pv[48] % den not in allowed:
                    raise ValueError("SAT witness x4 residue regression")
                parent_witness = {"parent_index": parent_index, "n1": n1v, "n2": n2v, "picard64_coordinates": xv, "all140_pairings": pv, "all140_pairings_sha256": csha(pv)}
                rec["all140_pairings_sha256"] = parent_witness["all140_pairings_sha256"]
            else:
                raise ValueError("unexpected solver result")
            branches.append(rec)
            solver.pop()
            if parent_sat:
                break
        if parent_sat:
            parent_result = "sat"
            if first_sat_witness is None:
                first_sat_witness = parent_witness
        elif parent_unknown:
            parent_result = "unknown"
            residual_unknown.append(parent_index)
        else:
            if len(branches) != TARGET_D + 1 or any(b["result"] != "unsat" for b in branches):
                raise ValueError("UNSAT parent branch coverage regression")
            parent_result = "unsat"
            newly_unsat.append(parent_index)
        parent_records.append({"parent_index": parent_index, "result": parent_result, "branch_count_checked": len(branches), "branches": branches})
        solver.pop()

    parent_unsat = len(newly_unsat)
    parent_unknown = len(residual_unknown)
    parent_sat = sum(rec["result"] == "sat" for rec in parent_records)
    known_unsat_lower_bound = 7141 + parent_unsat
    if parent_sat:
        status = "PASS_EXPLICIT_FIBRE_DEGREE_PARTITION_FOUND_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
        next_id = "BC2_25_ANALYZE_FIBRE_DEGREE_PARTITION_SAT_WITNESS"
    elif parent_unknown == 0:
        status = "PASS_ALL_23_RETAINED_BC2_23_UNKNOWN_EXACT_UNSAT_BY_EXPLICIT_FIBRE_DEGREE_PARTITION"
        next_id = "BC2_25_RECOVER_OR_REPLAY_REMAINING_172_BC2_19_UNKNOWN_IDENTITIES"
    else:
        status = "BLOCKED_EXPLICIT_FIBRE_DEGREE_PARTITION_LEAVES_RETAINED_UNKNOWN"
        next_id = "BC2_25_PARTITION_RESIDUAL_BY_BOUNDARY_PAIRING_OR_X4"

    body = {
        "schema": "STAGE32EX5_BC2_24_EXPLICIT_FIBRE_DEGREE_PARTITION_V1",
        "stage": "32EX5",
        "unit": "BC2_24_PARTITION_REMAINING_RETAINED_UNKNOWN_BY_EXPLICIT_FIBRE_DEGREE",
        "status": status,
        "source_locks": {"bc2_17": E17, "bc2_18": E18, "bc2_23_checkpoint": E23, "preflight": EPF, "bc2_18_enumerator_git_blob_sha": ED18, "bc2_18_feasible_stream_sha256": ESTREAM, "retained_bundle": d18.EXPECTED_BUNDLE_CANONICAL, "retained_marking": d18.EXPECTED_MARKING_CANONICAL},
        "partition_certificate": {"fibre_degree_variable": "n1", "integer_values": list(range(TARGET_D + 1)), "n2_relation": "n2=8-n1", "coverage_exact": True, "disjoint": True, "parent_unsat_requires_all_nine_branches_unsat": True},
        "target": {"checked_parent_indices": targets, "checked_parent_count": len(targets), "unretained_bc2_19_unknown_identity_count": 172, "unretained_bc2_19_unknown_identities_inferred": False},
        "result": {"parent_unsat_count": parent_unsat, "parent_unknown_count": parent_unknown, "parent_sat_count": parent_sat, "newly_unsat_parent_indices": newly_unsat, "residual_unknown_parent_indices": residual_unknown, "parent_records": parent_records, "branch_unsat_count": branch_unsat, "branch_unknown_count": branch_unknown, "branch_sat_count": branch_sat, "per_branch_timeout_ms": args.per_branch_timeout_ms, "solver": "Z3_QF_LIA_N355_REDUNDANT_CUTS_PLUS_EXACT_N1_PARTITION", "z3_version": get_version_string()},
        "sat_witness": first_sat_witness,
        "interpretation": {"known_parent_unsat_count_lower_bound": known_unsat_lower_bound, "known_retained_unknown_identity_count_after_this_run": parent_unknown, "unretained_unknown_identity_count": 172, "whole_first_block_unsat_proved": False},
        "credit": {"this_23_parent_slice_exact_unsat": parent_sat == 0 and parent_unknown == 0, "whole_first_block_unsat": False, "whole_stratum_closed": False, "full178_complete": False, "stage32_main_credit": False, "effectivity_or_actual_curve_existence_proved": False, "theorem_credit": False, "endpoint_credit": False},
        "firewalls": {"unretained_172_parent_identities_inferred": False, "unknown_relabelled_unsat": False, "partition_branch_unknown_dropped": False, "sat_relabelled_actual_curve": False, "main_promotion": False, "merge_authorized": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False},
        "next_exact_unit": {"id": next_id, "main_promotion_authorized": False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"canonical": body["canonical_sha256_without_this_field"], "status": status, "parent_unsat": parent_unsat, "parent_unknown": parent_unknown, "parent_sat": parent_sat, "branch_unsat": branch_unsat, "branch_unknown": branch_unknown, "branch_sat": branch_sat, "known_unsat_lower_bound": known_unsat_lower_bound, "next": next_id}, sort_keys=True))


if __name__ == "__main__":
    main()
