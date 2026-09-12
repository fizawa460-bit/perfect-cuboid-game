#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from z3 import Int, SolverFor, get_version_string, sat, unknown, unsat

import bc2_32_replay_explicit_fresh_unknown170 as b32

HERE = Path(__file__).resolve().parent
BC2_34 = HERE / "bc2-34-fresh-unknown81-replay-checkpoint.json"
REPAIR = HERE / "bc2-34-dependency-identity-repair.json"

BC2_34_CANONICAL = "e535e86ddfcd19aaa3aa316f5f42e49be830e48c16e1cdd15c03a6a80e6a84ba"
BC2_34_BLOB = "e566aeda2931642d79c88dc5eeb84b142f655609"
BC2_34_AUDIT_HEAD = "cdb455860849cfd064e3ab8c83d6d4993fb5ff1b"
BC2_34_AUDIT_REVIEW = 5186516652
BC2_34_REPAIR_CANONICAL = "fb111cd123eb1ee0aa99848fc7c75bd976684517cd63a2bfd44f9e9abdaed01f"
BC2_34_REPAIR_BLOB = "5569d0d0c806db361ad6cafdafbe5e7911850e4c"
B32_BLOB = "7cfe8450cb9b9ab7f04da797d487655505598b93"
B19_BLOB = "b2899aa228e7a3ee97526e3787ffbefa483530b4"
D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
UNKNOWN_SHA = "00626c95f20bfcab7d9e78c86fdc2b5900684e9765bd483b813c8c047302497b"
PRIOR_UNSAT = 7272
TARGET_COUNT = 64
TIMEOUT_MS = 80000


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked(path: Path, canonical: str, blob: str) -> dict:
    if git_blob_sha(path) != blob:
        raise ValueError(f"Git blob drift: {path.name}")
    obj = json.loads(path.read_text())
    q = dict(obj)
    got = q.pop("canonical_sha256_without_this_field", None)
    if got != canonical or csha(q) != canonical:
        raise ValueError(f"canonical drift: {path.name}")
    return obj


def load_target() -> dict:
    cp = checked(BC2_34, BC2_34_CANONICAL, BC2_34_BLOB)
    repair = checked(REPAIR, BC2_34_REPAIR_CANONICAL, BC2_34_REPAIR_BLOB)
    if repair["execution_identity"]["bc2_32_producer_git_blob_sha"] != B32_BLOB:
        raise ValueError("BC2-34 repair receipt BC2-32 identity drift")
    r = cp["replay"]
    ids = [int(v) for v in r["unknown_parent_indices"]]
    if (
        r["parents_checked"] != 81
        or r["unsat_count"] != 17
        or r["unknown_count"] != TARGET_COUNT
        or r["sat_count"] != 0
        or len(ids) != TARGET_COUNT
        or ids != sorted(set(ids))
        or csha(ids) != UNKNOWN_SHA
        or r["unknown_parent_indices_sha256"] != UNKNOWN_SHA
        or cp["credit"]["known_parent_unsat_count_lower_bound"] != PRIOR_UNSAT
    ):
        raise ValueError("BC2-34 audited target drift")
    return cp


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-parent-timeout-ms", type=int, default=TIMEOUT_MS)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    if args.per_parent_timeout_ms != TIMEOUT_MS:
        raise ValueError("BC2-35 is locked to 80000 ms per audited UNKNOWN parent")

    # Fail-close the directly executed module itself and its load-bearing
    # parent-space dependencies before calling build_parent_space().
    if git_blob_sha(Path(b32.__file__).resolve()) != B32_BLOB:
        raise ValueError("BC2-32 producer blob drift")
    if git_blob_sha(Path(b32.b19.__file__).resolve()) != B19_BLOB:
        raise ValueError("BC2-19 replay source blob drift")
    if git_blob_sha(Path(b32.d18.__file__).resolve()) != D18_BLOB:
        raise ValueError("BC2-18 enumerator source blob drift")

    cp = load_target()
    target_indices = [int(v) for v in cp["replay"]["unknown_parent_indices"]]
    selected_exceptional_labels, parents, P = b32.build_parent_space()
    b19 = b32.b19

    bc217 = json.loads(b19.BC2_17_EVIDENCE.read_text())
    fixed = {int(k): int(v) for k, v in bc217["retarget"]["fixed_exceptional_pairings"].items()}

    x = [Int(f"x_{j}") for j in range(b19.PICARD_RANK)]
    p = [sum(int(P[i, j]) * x[j] for j in range(b19.PICARD_RANK)) for i in range(b19.ALL140_COUNT)]
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
        if result == unsat:
            unsat_indices.append(parent_index)
            status_stream.update(f"{parent_index}:UNSAT\n".encode())
        elif result == unknown:
            unknown_indices.append(parent_index)
            status_stream.update(f"{parent_index}:UNKNOWN:{solver.reason_unknown()}\n".encode())
        elif result == sat:
            model = solver.model()
            xv = [int(model.eval(q, model_completion=True).as_long()) for q in x]
            pv = [sum(int(P[i, j]) * xv[j] for j in range(b19.PICARD_RANK)) for i in range(b19.ALL140_COUNT)]
            if min(pv) < 0 or sum(pv[:b19.NORMAL_COUNT]) != b19.NORMAL_MASS or sum(pv[b19.NORMAL_COUNT:]) != b19.TARGET_E:
                raise ValueError("SAT witness violates retained Picard64 feasibility constraints")
            if any(pv[label - 1] != value for label, value in fixed.items()):
                raise ValueError("SAT witness fixed-pairing regression")
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

    if len(unsat_indices) + len(unknown_indices) + len(sat_witnesses) != TARGET_COUNT:
        raise ValueError("targeted replay status partition regression")

    known_unsat = PRIOR_UNSAT + len(unsat_indices)
    all64_unsat = len(unsat_indices) == TARGET_COUNT and not unknown_indices and not sat_witnesses
    if sat_witnesses:
        status = "PASS_TARGETED_REPLAY_HAS_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT"
    elif unknown_indices:
        status = "PASS_TARGETED_REPLAY_REDUCED_OR_RETAINED_UNKNOWN_SET"
    else:
        status = "PASS_TARGETED_REPLAY_ALL_64_EXACT_UNSAT_CANDIDATE_CLOSURE"

    body = {
        "schema": "STAGE32EX5_BC2_35_FRESH_UNKNOWN64_REPLAY_V1",
        "stage": "32EX5",
        "unit": "BC2_35_REFINE_REMAINING_FRESH_UNKNOWN_SET",
        "status": status,
        "audit_consumption": {
            "bc2_34_hostile_audit_status": "PASS",
            "bc2_34_hostile_audit_exact_head": BC2_34_AUDIT_HEAD,
            "bc2_34_hostile_audit_review_id": BC2_34_AUDIT_REVIEW,
        },
        "source_locks": {
            "bc2_34_checkpoint_canonical": BC2_34_CANONICAL,
            "bc2_34_checkpoint_git_blob_sha": BC2_34_BLOB,
            "bc2_34_repair_receipt_canonical": BC2_34_REPAIR_CANONICAL,
            "bc2_34_repair_receipt_git_blob_sha": BC2_34_REPAIR_BLOB,
            "bc2_32_producer_git_blob_sha": B32_BLOB,
            "bc2_19_replay_source_git_blob_sha": B19_BLOB,
            "bc2_18_enumerator_source_git_blob_sha": D18_BLOB,
            "target_unknown_parent_indices_sha256": UNKNOWN_SHA,
            "python_version": "3.10.6",
            "sympy_version": "1.14.0",
            "z3_solver_version": get_version_string(),
        },
        "target": {
            "audited_bc2_34_unknown_count": TARGET_COUNT,
            "parent_indices_sha256": UNKNOWN_SHA,
            "parent_indices": target_indices,
            "prior_audited_unsat_count": PRIOR_UNSAT,
            "target_is_exact_audited_unknown_complement": True,
        },
        "replay": {
            "per_parent_timeout_ms": args.per_parent_timeout_ms,
            "parents_checked": TARGET_COUNT,
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
            "whole_first_block_picard64_unsat_candidate": all64_unsat,
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
            "id": "HOSTILE_AUDIT_BC2_35_TARGETED_REPLAY",
            "post_audit_if_unknown": "BC2_36_REFINE_REMAINING_FRESH_UNKNOWN_SET",
            "post_audit_if_sat": "BC2_36_ANALYZE_PICARD64_FEASIBLE_WITNESS_NO_CURVE_CREDIT",
            "post_audit_if_all_unsat": "BC2_36_CONSUME_FIRST_BLOCK_PICARD64_CLOSURE_CANDIDATE",
            "main_promotion_authorized": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "canonical": body["canonical_sha256_without_this_field"],
        "target": TARGET_COUNT,
        "checked": TARGET_COUNT,
        "unsat": len(unsat_indices),
        "unknown": len(unknown_indices),
        "sat": len(sat_witnesses),
        "known_unsat_lower_bound": known_unsat,
        "next": body["next_exact_unit"]["id"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
