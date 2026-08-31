#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from z3 import sat

from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bl_joint_integer_closure import EXPECTED_TRIPLES, bands_for, build_joint
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_EVIDENCE_CANONICAL = "ac88fb355252750e6afdc10cbb54abec24babbad57c25090c017f9a55ac93a44"
EXPECTED_WITNESS_SHA = "1a131595c87cf9c5d54ef97dba62261eeb3dda7bb92a5a9fa62c280f46bc4137"
EXPECTED_ORDINAL = 1617
EXPECTED_TARGET = {"row_id": "g1-d186", "e": 266, "a": 592, "u": -44, "v": 32, "z": [-15, 62, -44, 26, 32]}
PRODUCING_RUN_ID = 33380510213
PRODUCING_ARTIFACT_ID = 9753613683
PRODUCING_HEAD = "b819b128beecdbbd6bb4e773ab98ad7c12e1b2ef"
PRODUCING_ARTIFACT_ZIP_SHA256 = "72a968f83cd0af4723b225b51b9bee7928bb56b4d393bc6442e27a9d98ad9072"


def canonical_without_field(x: dict, field: str) -> str:
    y = dict(x)
    y.pop(field, None)
    return csha(y)


def main() -> None:
    ap = argparse.ArgumentParser()
    for name in ("source_lock", "formula_lock", "pair_lock", "audit_lock", "seventh_lock", "eighth_lock", "ninth_lock", "tenth_lock", "retained", "marking", "evidence"):
        ap.add_argument("--" + name.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    evidence = json.loads(args.evidence.read_text())
    assert evidence["schema"] == "STAGE32_21BL_ISL_CURRENT_MODEL_PREFLIGHT_V1"
    assert evidence["leaf"] == "32-21bl"
    assert evidence["ordinal"] == EXPECTED_ORDINAL
    assert evidence["target"] == EXPECTED_TARGET
    assert evidence["result"]["status"] == "SAT"
    assert evidence["result"]["original_z3_replay_status"] == "sat"
    assert evidence["exact_problem"]["integer_rank"] == 59
    assert evidence["exact_problem"]["assertion_count"] == 514
    assert evidence["exact_problem"]["same_integerized_21bl_assertions_as_z3_solver"] is True
    assert evidence["exact_problem"]["fixed_triple_constraints_included"] is True
    assert evidence["exact_problem"]["numerical_backend_never_authorizes_unsat"] is True
    assert evidence["safety"]["full_3234_scaleout_authorized_by_this_result"] is False
    for flag in ("theorem_credit", "receiver_credit", "route_credit", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"):
        assert evidence["safety"][flag] is False

    recomputed_evidence_canonical = canonical_without_field(evidence, "canonical_sha256_without_this_field")
    assert evidence["canonical_sha256_without_this_field"] == EXPECTED_EVIDENCE_CANONICAL
    assert recomputed_evidence_canonical == EXPECTED_EVIDENCE_CANONICAL

    witness = [int(v) for v in evidence["result"]["witness_r_reduced"]]
    assert len(witness) == 59
    assert csha(witness) == EXPECTED_WITNESS_SHA
    assert evidence["result"]["witness_sha256"] == EXPECTED_WITNESS_SHA

    triples = list(prism_triples())
    assert len(triples) == EXPECTED_TRIPLES
    triple = triples[EXPECTED_ORDINAL]
    assert list(triple) == evidence["triple"] == [76, -55, -96]

    cfg = argparse.Namespace(
        source_lock=args.source_lock, formula_lock=args.formula_lock, pair_lock=args.pair_lock,
        audit_lock=args.audit_lock, seventh_lock=args.seventh_lock, eighth_lock=args.eighth_lock,
        ninth_lock=args.ninth_lock, tenth_lock=args.tenth_lock, retained=args.retained, marking=args.marking,
        per_check_timeout_ms=5000,
    )
    solver, r, ri, target, table = build_joint(cfg)
    assert target == EXPECTED_TARGET
    bands = bands_for(triple, table)
    expected_bands = {int(j): tuple(v) for j, v in evidence["current_exact_bands"].items()}
    assert bands == expected_bands

    solver.add(r[50] == triple[0], r[55] == triple[1], r[27] == triple[2])
    for j, (lo, hi) in bands.items():
        solver.add(r[j] >= lo, r[j] <= hi)
    for j, value in enumerate(witness):
        solver.add(ri[j] == value)
    replay = solver.check()
    assert replay == sat, replay
    replayed = [int(solver.model().eval(ri[j]).as_long()) for j in range(59)]
    assert replayed == witness

    payload = {
        "schema": "STAGE32_21BL_JOINT_INTEGER_WITNESS_FRESH_AUDIT_V1",
        "stage": 32,
        "leaf": "32-21bl",
        "verdict": "PASS_STAGE32_21BL_FRESH_EXACT_WITNESS_REPLAY_AUDIT",
        "producing_evidence": {
            "run_id": PRODUCING_RUN_ID,
            "artifact_id": PRODUCING_ARTIFACT_ID,
            "source_head": PRODUCING_HEAD,
            "artifact_zip_sha256": PRODUCING_ARTIFACT_ZIP_SHA256,
            "evidence_canonical_sha256": recomputed_evidence_canonical,
        },
        "witness_sha256": EXPECTED_WITNESS_SHA,
        "ordinal": EXPECTED_ORDINAL,
        "triple": list(triple),
        "target": target,
        "integer_rank": 59,
        "original_joint_z3_model_fixed_witness_replay": "sat",
        "witness_exactly_reproduced_from_model": True,
        "all_source_locks_reloaded": True,
        "current_exact_bands_recomputed_and_matched": True,
        "integer_sat_resolution_of_lone_representative_unknown": True,
        "representative_chain_after_audit": {"sat": 1, "unsat": 55, "unknown": 0},
        "scope": "deterministic 56 fixed-projection representative sample only; not FULL178 numerical credit",
        "safety": {
            "full_3234_scaleout_required_for_sat_resolution": False,
            "full_3234_scaleout_authorized": False,
            "fixed_projection_integer_sat_is_not_perfect_cuboid_existence": True,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": payload["verdict"], "canonical": payload["canonical_sha256_without_this_field"], "witness_sha256": EXPECTED_WITNESS_SHA}))


if __name__ == "__main__":
    main()
