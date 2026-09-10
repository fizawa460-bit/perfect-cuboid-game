#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_VERIFIER = HERE / "verify_n349b_factor_hurwitz_boundary_cap.py"
N349_AUDIT = HERE.parent / "N349/HOSTILE-AUDIT-PASS.json"

EXPECTED_BASE_CANONICAL = "f1595ea5b7ed99111ce32c5773bfb9c6e204154ca37bda2bf6e16e25d6b1782a"
EXPECTED_AUDIT_CANONICAL = "1752b861d0308cf4663d993c8d8c94b0ff491028ad88157580c64a39949907f3"
EXPECTED_REVIEW_ID = 5162530057
EXPECTED_AUDITED_HEAD = "77e1ea70a93149e1e0d7e3f5add3bfb15beec4c2"
EXPECTED_CEILING = "AUDITED_FSM_BOUNDARY_EQUALITY_LOCAL_PAIR_NECESSITY_ONLY_NO_PRUNING_NO_LOWGENUS_MEMBER_NO_FULL178_CREDIT"
EXPECTED_G0 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39]
EXPECTED_G1 = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    d = json.loads(path.read_text())
    claimed = d.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(d) != expected:
        raise ValueError(f"canonical regression: {path}")
    d["canonical_sha256_without_this_field"] = claimed
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    audit = load_canonical(N349_AUDIT, EXPECTED_AUDIT_CANONICAL)
    a = audit["audit"]
    if a["review_id"] != EXPECTED_REVIEW_ID:
        raise ValueError("N349 hostile-audit review regression")
    if a["verdict"] != "PASS":
        raise ValueError("N349 hostile-audit verdict regression")
    if a["audited_exact_head"] != EXPECTED_AUDITED_HEAD:
        raise ValueError("N349 hostile-audit head regression")
    if a["credit_ceiling"] != EXPECTED_CEILING:
        raise ValueError("N349 hostile-audit ceiling regression")
    if audit["consumption"]["local_pair_necessity_may_be_consumed"] is not True:
        raise ValueError("N349 local-pair consumption not authorized by receipt")
    if audit["consumption"]["numerical_pruning_credit_from_n349_alone"] is not False:
        raise ValueError("N349 receipt credit firewall regression")

    with tempfile.TemporaryDirectory() as td:
        base_path = Path(td) / "n349b-base.json"
        subprocess.run(
            [sys.executable, str(BASE_VERIFIER), "--output", str(base_path)],
            check=True,
        )
        base = load_canonical(base_path, EXPECTED_BASE_CANONICAL)

    agg = base["aggregate"]
    if agg["terminal_count"] != 21 or agg["sat_count"] != 0 or agg["unsat_count"] != 21 or agg["unknown_count"] != 0:
        raise ValueError(f"N349B aggregate regression: {agg}")
    if agg["unsat_partition"]["g0-d176"] != EXPECTED_G0:
        raise ValueError("N349B g0 partition regression")
    if agg["unsat_partition"]["g1-d192"] != EXPECTED_G1:
        raise ValueError("N349B g1 partition regression")
    if agg["sat_partition"]["g0-d176"] or agg["sat_partition"]["g1-d192"]:
        raise ValueError("N349B unexpected SAT partition")
    if agg["unknown_partition"]["g0-d176"] or agg["unknown_partition"]["g1-d192"]:
        raise ValueError("N349B unexpected UNKNOWN partition")

    body = {
        "schema": "STAGE32_32_01_178_N349B_FACTOR_HURWITZ_BOUNDARY_CAP_AUDIT_CONSUMED_V1",
        "node_id": "N349B",
        "status": "EXACT_ALL21_UNSAT_AUDIT_CANDIDATE",
        "source_locks": {
            "base_n349b_verifier_canonical": EXPECTED_BASE_CANONICAL,
            "n349_hostile_audit_receipt_canonical": EXPECTED_AUDIT_CANONICAL,
            "n349_hostile_audit_review_id": EXPECTED_REVIEW_ID,
            "n349_hostile_audit_exact_head": EXPECTED_AUDITED_HEAD,
            "n349_hostile_audit_credit_ceiling": EXPECTED_CEILING,
            "n349_checkpoint_canonical": base["source_locks"]["n349_checkpoint_canonical"],
            "n349a_checkpoint_canonical": base["source_locks"]["n349a_checkpoint_canonical"],
            "retained_bundle_canonical": base["source_locks"]["retained_bundle_canonical"],
            "retained_marking_canonical": base["source_locks"]["retained_marking_canonical"],
            "ao_source_note_blob_sha1": base["source_locks"]["ao_source_note_blob_sha1"],
        },
        "audit_consumption": {
            "n349_hostile_audit_consumed": True,
            "consumed_scope": "FSM boundary-equality / local cusp-pair necessity only",
            "consumption_does_not_expand_n349_credit_ceiling": True,
            "n349b_itself_hostile_audit_required_before_main_pruning_credit": True,
        },
        "exact_reduction": base["exact_reduction"],
        "aggregate": agg,
        "rows": base["rows"],
        "conclusion": {
            "all_current_21_picard_terminal_families_unsat_under_factor_hurwitz_boundary_cap": True,
            "self_square_was_omitted": True,
            "unsat_is_for_a_relaxed_integer_picard_problem": True,
            "n349_prerequisite_is_externally_hostile_audited": True,
            "candidate_pruning_if_n349b_hostile_audit_passes": 21,
        },
        "semantics": {
            "n349_hostile_audit_consumed": True,
            "n349b_hostile_audit_required": True,
            "n349b_main_pruning_credit_granted": False,
            "actual_integral_irreducible_member_not_constructed": True,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N349B_AUDIT_CONSUMED_RELOCK_ALL21_UNSAT_CANDIDATE",
        "sat": agg["sat_count"],
        "unsat": agg["unsat_count"],
        "unknown": agg["unknown_count"],
        "unsat_g0": agg["unsat_partition"]["g0-d176"],
        "unsat_g1": agg["unsat_partition"]["g1-d192"],
        "n349_review": EXPECTED_REVIEW_ID,
        "canonical": body["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
