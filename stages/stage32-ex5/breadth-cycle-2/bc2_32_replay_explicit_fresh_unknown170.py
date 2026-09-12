#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18
import bc2_19_n354_survivor_normal_positivity_mass_replay as b19

HERE = Path(__file__).resolve().parent
BC2_31 = HERE / "bc2-31-fresh-all7336-replay-checkpoint.json"

BC2_31_CANONICAL = "f2aec1d923ff43393d24364864be36e223d43674149e6655a920d3b3d5de3ae4"
BC2_31_BLOB = "188601efcb99d33fe00fc60dc3c2f40f51e65b20"
BC2_31_AUDIT_HEAD = "72118efafdd25ca3b08d408463db46e2800e22df"
BC2_31_AUDIT_REVIEW = 5184996992
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
UNKNOWN_SHA = "df7db2159df41d93ce64b7d2ccf230b9363711bbdf769280e1df0560cfbae1ae"
PRIOR_UNSAT = 7166
TARGET_COUNT = 170
TIMEOUT_MS = 20000


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_checkpoint() -> dict:
    raw = BC2_31.read_bytes()
    if hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest() != BC2_31_BLOB:
        raise ValueError("BC2-31 checkpoint blob drift")
    cp = json.loads(raw)
    q = dict(cp)
    got = q.pop("canonical_sha256_without_this_field", None)
    if got != BC2_31_CANONICAL or csha(q) != BC2_31_CANONICAL:
        raise ValueError("BC2-31 checkpoint canonical drift")
    fr = cp["fresh_replay"]
    ids = [int(v) for v in fr["unknown_parent_indices_all"]]
    if (
        fr["parents_checked"] != 7336
        or fr["unsat_count"] != PRIOR_UNSAT
        or fr["unknown_count"] != TARGET_COUNT
        or fr["sat_found"] is not False
        or len(ids) != TARGET_COUNT
        or ids != sorted(set(ids))
        or csha(ids) != UNKNOWN_SHA
        or fr["unknown_parent_indices_all_sha256"] != UNKNOWN_SHA
    ):
        raise ValueError("BC2-31 audited fresh target drift")
    return cp


def build_parent_space() -> tuple[list[int], list[tuple[tuple[int, ...], list[int], list[int]]], Matrix]:
    if git_blob_sha(Path(b19.__file__).resolve()) != B19_BLOB:
        raise ValueError("BC2-19 source blob drift")
    if git_blob_sha(Path(d18.__file__).resolve()) != D18_BLOB:
        raise ValueError("BC2-18 source blob drift")

    bc217 = json.loads(b19.BC2_17_EVIDENCE.read_text())
    bc218 = json.loads(b19.BC2_18_CHECKPOINT.read_text())
    if bc217.get("canonical_sha256_without_this_field") != b19.EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical regression")
    if bc218.get("canonical_sha256_without_this_field") != b19.EXPECTED_BC2_18_CANONICAL:
        raise ValueError("BC2-18 checkpoint canonical regression")
    if bc218["exact_decomposition"]["feasible_stream_sha256"] != b19.EXPECTED_FEASIBLE_STREAM_SHA256:
        raise ValueError("BC2-18 feasible stream regression")

    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}
    bundle = d18.load_retained(d18.RETAINED, "s32ex5_bc232_bundle")
    marking = d18.load_retained(d18.MARKING, "s32ex5_bc232_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical regression")

    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    if P.shape != (b19.ALL140_COUNT, b19.PICARD_RANK):
        raise ValueError("all140 pairing matrix shape regression")

    selected_labels = [int(v) for v in d18.INDLIST]
    selected_indices = [label - 1 for label in selected_labels]
    Psel = P.extract(selected_indices, list(range(b19.PICARD_RANK)))
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
    if Psel * B != den * Matrix.eye(b19.PICARD_RANK):
        raise ValueError("selected64 inverse reconstruction regression")

    selected_normal_positions = [j for j, label in enumerate(selected_labels) if label <= b19.NORMAL_COUNT]
    selected_exceptional_positions = [j for j, label in enumerate(selected_labels) if label > b19.NORMAL_COUNT]
    selected_exceptional_labels = [selected_labels[j] for j in selected_exceptional_positions]
    free_selected_exceptional_labels = [label for label in selected_exceptional_labels if label not in fixed]
    if len(free_selected_exceptional_labels) != 19:
        raise ValueError("free selected exceptional count regression")

    full_check = d18.build_hnf_extension_check(
        B, den, selected_exceptional_positions, selected_normal_positions
    )
    x4_pos = selected_labels.index(b19.X4_LABEL)
    x4_check = d18.build_hnf_extension_check(
        B,
        den,
        selected_exceptional_positions + [x4_pos],
        [j for j in selected_normal_positions if j != x4_pos],
    )

    def exceptional_values(comp: tuple[int, ...]) -> list[int]:
        by_label = dict(fixed)
        by_label.update({label: int(value) for label, value in zip(free_selected_exceptional_labels, comp)})
        return [int(by_label[label]) for label in selected_exceptional_labels]

    parents: list[tuple[tuple[int, ...], list[int], list[int]]] = []
    stream = hashlib.sha256()
    enumerated = 0
    for comp in d18.weak_compositions_at_most(
        b19.RESIDUAL_EXCEPTIONAL_MASS, len(free_selected_exceptional_labels)
    ):
        enumerated += 1
        yE = exceptional_values(comp)
        allowed = [residue for residue in range(den) if d18.feasible(x4_check, yE + [residue])]
        full_ok = d18.feasible(full_check, yE)
        if full_ok != bool(allowed):
            raise ValueError("HNF parent/x4 extension regression")
        if not full_ok:
            continue
        record = {
            "selected_exceptional_pairings": yE,
            "selected_residual_mass": sum(comp),
            "x4_allowed_residues_mod8": allowed,
        }
        stream.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parents.append((comp, yE, allowed))

    if enumerated != b19.EXPECTED_ENUMERATED_PARENT_COUNT:
        raise ValueError("parent enumeration coverage regression")
    if len(parents) != b19.EXPECTED_PARENT_COUNT:
        raise ValueError("mod8 surviving parent count regression")
    if stream.hexdigest() != b19.EXPECTED_FEASIBLE_STREAM_SHA256:
        raise ValueError("mod8 surviving parent stream regression")
    return selected_exceptional_labels, parents, P


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=TIMEOUT_MS)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms != TIMEOUT_MS:
        raise ValueError("BC2-32 is locked to 20000 ms per audited UNKNOWN parent")

    cp = load_checkpoint()
    target_indices = [int(v) for v in cp["fresh_replay"]["unknown_parent_indices_all"]]
    selected_exceptional_labels, parents, P = build_parent_space()

    bc217 = json.loads(b19.BC2_17_EVIDENCE.read_text())
    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}

    x = [Int(f"x_{j}") for j in range(b19.PICARD_RANK)]
    p = [
        sum(int(P[i, j]) * x[j] for j in range(b19.PICARD_RANK))
        for i in range(b19.ALL140_COUNT)
    ]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=args.per_parent_timeout_ms)
    for i in range(b19.NORMAL_COUNT):
        solver.add(p[i] >= 0, p[i] <= b19.NORMAL_MASS)
    for i in range(b19.NORMAL_COUNT, b19.ALL140_COUNT):
        solver.add(p[i] >= 0, p[i] <= b19.TARGET_E)
    solver.add(sum(p[:b19.NORMAL_COUNT]) == b19.NORMAL_MASS)
    solver.add(sum(p[b19.NORMAL_COUNT:]) == b19.TARGET_E)
    for label, value in fixed.items():
        solver.add(p[label - 1] == value)
    solver.add(p[b19.X4_LABEL - 1] >= 0, p[b19.X4_LABEL - 1] <= b19.NORMAL_MASS)

    checked = 0
    unsat_indices: list[int] = []
    unknown_indices: list[int] = []
    sat_witnesses: list[dict] = []
    status_stream = hashlib.sha256()

    for parent_index in target_indices:
        comp, yE, allowed = parents[parent_index]
        solver.push()
        for label, value in zip(selected_exceptional_labels, yE):
            solver.add(p[label - 1] == int(value))
        result = solver.check()
        checked += 1
        if result == unsat:
            unsat_indices.append(parent_index)
            status_stream.update(f"{parent_index}:UNSAT\n".encode())
        elif result == unknown:
            unknown_indices.append(parent_index)
            status_stream.update(f"{parent_index}:UNKNOWN:{solver.reason_unknown()}\n".encode())
        elif result == sat:
            model = solver.model()
            xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
            pv = [
                sum(int(P[i, j]) * xv[j] for j in range(b19.PICARD_RANK))
                for i in range(b19.ALL140_COUNT)
            ]
            if min(pv) < 0 or sum(pv[:b19.NORMAL_COUNT]) != b19.NORMAL_MASS or sum(pv[b19.NORMAL_COUNT:]) != b19.TARGET_E:
                raise ValueError("SAT witness violates retained Picard64 feasibility constraints")
            if any(pv[label - 1] != value for label, value in fixed.items()):
                raise ValueError("SAT witness terminal fixed-pairing regression")
            if any(pv[label - 1] != value for label, value in zip(selected_exceptional_labels, yE)):
                raise ValueError("SAT witness parent regression")
            x4 = pv[b19.X4_LABEL - 1]
            if not 0 <= x4 <= b19.NORMAL_MASS or x4 % 8 not in allowed:
                raise ValueError("SAT witness x4 residue regression")
            sat_witnesses.append({
                "parent_index": parent_index,
                "selected_residual_mass": sum(comp),
                "x4": x4,
                "x4_mod8": x4 % 8,
                "picard64_coordinates": xv,
                "all140_pairings": pv,
                "all140_pairings_sha256": csha(pv),
            })
            status_stream.update(f"{parent_index}:SAT\n".encode())
        else:
            raise ValueError(f"unexpected solver result: {result}")
        solver.pop()

    if checked != TARGET_COUNT:
        raise ValueError("targeted replay coverage regression")
    if len(unsat_indices) + len(unknown_indices) + len(sat_witnesses) != TARGET_COUNT:
        raise ValueError("targeted replay status partition regression")
    if any(i not in target_indices for i in unsat_indices + unknown_indices):
        raise ValueError("status escaped audited target set")

    known_unsat = PRIOR_UNSAT + len(unsat_indices)
    all170_unsat = len(unsat_indices) == TARGET_COUNT and not unknown_indices and not sat_witnesses
    if sat_witnesses:
        status = "PASS_TARGETED_REPLAY_HAS_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
    elif unknown_indices:
        status = "PASS_TARGETED_REPLAY_REDUCED_OR_RETAINED_UNKNOWN_SET"
    else:
        status = "PASS_TARGETED_REPLAY_ALL_170_EXACT_UNSAT_CANDIDATE_CLOSURE"

    body = {
        "schema": "STAGE32EX5_BC2_32_FRESH_UNKNOWN170_REPLAY_V1",
        "stage": "32EX5",
        "unit": "BC2_32_REPLAY_EXPLICIT_FRESH_UNKNOWN_SET",
        "status": status,
        "audit_consumption": {
            "bc2_31_hostile_audit_status": "PASS",
            "bc2_31_hostile_audit_exact_head": BC2_31_AUDIT_HEAD,
            "bc2_31_hostile_audit_review_id": BC2_31_AUDIT_REVIEW,
        },
        "source_locks": {
            "bc2_31_checkpoint_canonical": BC2_31_CANONICAL,
            "bc2_31_checkpoint_git_blob_sha": BC2_31_BLOB,
            "bc2_19_replay_source_git_blob_sha": B19_BLOB,
            "bc2_18_enumerator_source_git_blob_sha": D18_BLOB,
            "target_unknown_parent_indices_sha256": UNKNOWN_SHA,
            "python_version": "3.10.6",
            "sympy_version": "1.14.0",
            "z3_solver_version": get_version_string(),
        },
        "target": {
            "audited_bc2_31_unknown_count": TARGET_COUNT,
            "parent_indices_sha256": UNKNOWN_SHA,
            "parent_indices": target_indices,
            "prior_audited_unsat_count": PRIOR_UNSAT,
            "target_is_exact_audited_unknown_complement": True,
        },
        "replay": {
            "per_parent_timeout_ms": args.per_parent_timeout_ms,
            "parents_checked": checked,
            "unsat_count": len(unsat_indices),
            "unknown_count": len(unknown_indices),
            "sat_count": len(sat_witnesses),
            "unsat_parent_indices": unsat_indices,
            "unknown_parent_indices": unknown_indices,
            "unknown_parent_indices_sha256": csha(unknown_indices),
            "sat_parent_indices": [w["parent_index"] for w in sat_witnesses],
            "status_stream_sha256": status_stream.hexdigest(),
            "all_remaining_unknown_identities_explicitly_retained": len(set(unknown_indices)) == len(unknown_indices),
            "solver": "Z3_QF_LIA_INCREMENTAL",
        },
        "sat_witnesses": sat_witnesses,
        "credit": {
            "new_exact_parent_unsat_count": len(unsat_indices),
            "known_parent_unsat_count_lower_bound": known_unsat,
            "whole_first_block_picard64_unsat_candidate": all170_unsat,
            "whole_stratum_closed": False,
            "full178_complete": False,
            "stage32_main_credit": False,
            "effectivity_or_actual_curve_existence_proved": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
        "firewalls": {
            "timeout_unknown_relabelled_unsat": False,
            "unknown_dropped": False,
            "sat_relabelled_actual_curve": False,
            "main_promotion": False,
            "merge_authorized": False,
            "heavy_scaleout_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "next_exact_unit": {
            "id": "HOSTILE_AUDIT_BC2_32_TARGETED_REPLAY",
            "post_audit_if_unknown": "BC2_33_REFINE_REMAINING_FRESH_UNKNOWN_SET",
            "post_audit_if_sat": "BC2_33_ANALYZE_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT",
            "post_audit_if_all_unsat": "BC2_33_CONSUME_FIRST_BLOCK_PICARD64_CLOSURE_CANDIDATE",
            "main_promotion_authorized": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "canonical": body["canonical_sha256_without_this_field"],
        "target": TARGET_COUNT,
        "checked": checked,
        "unsat": len(unsat_indices),
        "unknown": len(unknown_indices),
        "sat": len(sat_witnesses),
        "known_unsat_lower_bound": known_unsat,
        "next": body["next_exact_unit"]["id"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
