#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import runpy
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKPOINT = HERE / "RR-EFFECTIVITY-SUFFICIENT-CHECKPOINT.json"
CLASSIFIER = HERE / "rr_effectivity_sufficient.py"
SURFACE_LOCK = HERE / "SURFACE-INVARIANT-SOURCE-LOCK.json"
SURFACE_LOCK_VERIFIER = HERE / "verify_surface_invariant_source_lock.py"
DEGREE_GATE_VERIFIER = HERE / "verify_full178_rr_degree_gate.py"
HPERP_ADAPTER_VERIFIER = HERE / "verify_hperp_norm_rr_adapter.py"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def canonical_without_self(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def load_classifier():
    spec = importlib.util.spec_from_file_location("stage32_rr_effectivity", CLASSIFIER)
    req(spec is not None and spec.loader is not None, "cannot load classifier module")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_cli(*args: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(CLASSIFIER), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(proc.stdout)


def main() -> None:
    cp = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    req(cp["schema"] == "STAGE32_32_02_RR_EFFECTIVITY_SUFFICIENT_CHECKPOINT_V1", "checkpoint schema drift")
    req(canonical_without_self(cp) == cp["canonical_sha256_without_this_field"], "checkpoint canonical drift")

    authority = cp["authority"]
    req(authority["parent_exact_head"] == "d44ff4403559dce4ea296698630f57a56cd0d0fe", "parent audited coordination head drift")
    req(authority["parent_hostile_reaudit_status"] == "PASS", "parent hostile re-audit is not PASS")
    req(authority["parent_hostile_reaudit_review_id"] == 5179390797, "parent hostile re-audit review drift")
    req(authority["authoritative_remaining_strata"] == 17128, "MAIN strata authority drift")
    req(authority["authoritative_remaining_terminals"] == 65396964990500233636101, "MAIN terminal authority drift")
    req(authority["full178_complete"] is False, "FULL178 was silently promoted")

    # The production wrapper may affirm the RR surface hypotheses only after
    # replaying the retained Stage29/Stage32 source-lock chain. The standalone
    # classifier itself remains fail-closed by default.
    runpy.run_path(str(SURFACE_LOCK_VERIFIER), run_name="__main__")
    surface_lock = json.loads(SURFACE_LOCK.read_text(encoding="utf-8"))
    req(canonical_without_self(surface_lock) == surface_lock["canonical_sha256_without_this_field"], "surface source-lock canonical drift")

    assumptions = cp["conditional_surface_assumptions"]
    req(assumptions["K2"] == 16 and assumptions["chi_O"] == 8, "RR constants drift")
    req(assumptions["K_nef"] is True, "nefness assumption missing")
    req(assumptions["assumptions_are_not_newly_proved_by_this_checkpoint"] is True, "source provenance firewall missing")
    req(assumptions["external_source_lock_for_surface_invariants_present_in_this_checkpoint"] is True, "retained invariant source-lock not consumed")
    req(assumptions["source_lock_path"] == "stages/stage32/final-chain/32-02-effectivity/SURFACE-INVARIANT-SOURCE-LOCK.json", "surface source-lock path drift")
    req(assumptions["source_lock_canonical_sha256_without_this_field"] == surface_lock["canonical_sha256_without_this_field"], "surface source-lock canonical mismatch")
    req(assumptions["official_wrapper_affirmation_requires_source_lock_pass"] is True, "official wrapper can affirm assumptions without source-lock replay")

    firewall = cp["credit_firewall"]
    req(firewall["effectivity_preparation_credit"] is True, "preparation credit missing")
    req(firewall["surface_invariant_source_lock_complete"] is True, "surface source-lock completion missing")
    for key in (
        "effectivity_final_execution_released",
        "receiver_credit",
        "full178_pruning_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ):
        req(firewall[key] is False, f"credit firewall opened: {key}")

    runpy.run_path(str(DEGREE_GATE_VERIFIER), run_name="__main__")
    runpy.run_path(str(HPERP_ADAPTER_VERIFIER), run_name="__main__")
    pop = cp["population_firewall"]
    req(pop["full178_manifest_degree_partition_source_locked"] is True, "FULL178 RR degree partition is not source-locked")
    req(pop["degree_gt_16_row_count"] == 168, "degree>16 row count drift")
    req(pop["degree_le_16_row_count"] == 10, "degree<=16 row count drift")
    req(pop["degree_gate_certificate_path"] == "stages/stage32/final-chain/32-02-effectivity/FULL178-RR-DEGREE-GATE.json", "degree-gate certificate path drift")
    req(pop["full178_rows_effectivity_classified"] is False, "degree partition mislabeled as effectivity classification")
    req(pop["final_survivor_picard_ledger_available"] is False, "full Picard ledger availability silently assumed")
    req(pop["minimal_rr_scalar_interface_ready"] is True, "minimal Hperp-norm RR interface missing")
    req(pop["minimal_rr_scalar_fields"] == ["row_id", "d", "negative_hperp_square_N"], "minimal RR scalar fields drift")
    req(pop["hperp_norm_adapter_path"] == "stages/stage32/final-chain/32-02-effectivity/HPERP-NORM-RR-ADAPTER.json", "Hperp norm adapter path drift")
    req(pop["final_survivor_hperp_norm_scalar_available"] is False, "32-01 Hperp norm producer silently assumed complete")

    cut = cp["live_specialist_observation"]
    req(cut["cut193_pr"] == 1786, "CUT193 PR drift")
    req(cut["cut193_candidate_pruned_terminals"] == 25651, "CUT193 candidate count drift")
    req(cut["cut193_hostile_audit_passed"] is False, "CUT193 audit falsely promoted")
    req(cut["cut193_main_credit"] is False and cut["cut193_is_not_consumed_here"] is True, "CUT193 candidate leaked into MAIN credit")

    mod = load_classifier()
    for row in cp["regressions"]:
        result = mod.classify(row["d"], row["C2"], assumptions_affirmed=True)
        req(result.status == row["expected_status"], f"regression status mismatch: {row['id']}")
        req(result.chi_OC == row["expected_chi"], f"regression chi mismatch: {row['id']}")

    odd = mod.classify(186, 171, assumptions_affirmed=True)
    req(odd.status == "INVALID_INTEGRAL_CLASS_PARITY", "odd RR parity did not fail closed")
    low_degree = mod.classify(16, 100, assumptions_affirmed=True)
    req(low_degree.status == "RR_INCONCLUSIVE", "d=K2 boundary was overclaimed")

    default_call = mod.classify(186, 858)
    req(default_call.status == "RR_INCONCLUSIVE_ASSUMPTIONS_NOT_AFFIRMED", "standalone default API call did not fail closed")
    explicit_call = mod.classify(186, 858, assumptions_affirmed=True)
    req(explicit_call.status == "RR_EFFECTIVE_DIVISOR_CERTIFIED", "source-locked wrapper affirmation did not enable conditional certification")

    cli_default = run_cli("--d", "186", "--c2", "858")
    req(cli_default["status"] == "RR_INCONCLUSIVE_ASSUMPTIONS_NOT_AFFIRMED", "standalone default CLI invocation did not fail closed")
    cli_affirmed = run_cli("--d", "186", "--c2", "858", "--assumptions-affirmed")
    req(cli_affirmed["status"] == "RR_EFFECTIVE_DIVISOR_CERTIFIED", "explicit CLI affirmation did not enable conditional certification")

    print("PASS: Stage32 final-chain 32-02 source-locked RR effectivity sufficient classifier")
    print("surface lock: K^2=16; p_g=7; q=0; chi(O)=8; K big and nef; degree=K.C")
    print("FULL178 degree gate: source-locked 168 rows with d>16 / 10 rows with d<=16")
    print("minimal downstream RR interface: row_id, d, N=-y^2; full 59-entry Picard vector not required by this gate")
    print("criterion: d>16 and C2>=d-14 with even C2-d; conclusion=effective divisor only")
    print("standalone API/CLI remains fail-closed; official wrapper affirms only after retained source-lock replay")
    print("parent hostile re-audit: #1785 review 5179390797 at d44ff4403559dce4ea296698630f57a56cd0d0fe")
    print("credit: preparation only; CUT193/FULL178/receiver/theorem/endpoint remain zero")


if __name__ == "__main__":
    main()
