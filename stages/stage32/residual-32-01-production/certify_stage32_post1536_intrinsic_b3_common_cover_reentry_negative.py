#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = "stages/stage32/residual-32-01-production/post1536-intrinsic-b3-common-cover-reentry-negative.json"
EXPECTED_CANONICAL = "503ae3c4165a93f744b8100e21509e0d00ba37a64489994edfa897ab0a55e500"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_lock(lock: dict):
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    if path.suffix == ".json":
        doc = json.loads(path.read_text())
        if "canonical_sha256" in lock:
            assert canonical_sha256(doc) == lock["canonical_sha256"], path
        return doc
    return path.read_text()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    assert Path(args.check).as_posix() == CERT_PATH

    cert = json.loads((ROOT / CERT_PATH).read_text())
    assert cert["schema"] == "STAGE32_POST1536_INTRINSIC_B3_COMMON_COVER_REENTRY_NEGATIVE_V1"
    assert cert["status"] == "EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    relative = load_lock(locks["relative_v4_coupling"])
    relative_note = load_lock(locks["relative_v4_source_note"])
    common = load_lock(locks["historical_common_cover_negative"])
    common_audit = load_lock(locks["historical_common_cover_audit"])
    b3 = load_lock(locks["single_b3_reduction"])
    b3_note = load_lock(locks["single_b3_source_note"])
    ambient_note = load_lock(locks["post1536_ambient_negative_note"])
    carrier_note = load_lock(locks["carrier_information_boundary"])
    s30 = load_lock(locks["arsenal_s30_w01"])
    s32 = load_lock(locks["arsenal_s32_pw05"])
    note = load_lock(locks["source_note"])

    ctl = json.loads((ROOT / "stages/stage32/controller.json").read_text())
    assert ctl["schema"] == "STAGE32_LOWGENUS_PICARD_CONTROLLER_V247_POST1520_Q602_RETAINED_GEOMETRY_18_TO_18_AUDITED"
    assert ctl["stage"] == 32 and ctl["stage32_closed"] is False
    ft = ctl["fixed_target"]
    assert (ft["row_id"], ft["O"], ft["qprime"], ft["Q"]) == ("g1-d186", 210, 4, 602)
    assert ctl["firewalls"]["O210_closed"] is False
    assert ctl["math_scope"]["fixed_z_O212_through_O266_qprime4"] == "BLOCKED_BEHIND_O210"

    rv4 = relative["relative_v4_coupling"]
    assert rv4["carrier_consequence"] == "f1^*Z ~= f2^*Z on Y"
    assert rv4["W_dimension"] == 2
    assert rv4["push_pull_consequence"] == ["T_12|W = identity mod 2", "T_21|W = identity mod 2"]
    assert relative["decision"]["generic_common_cover_inference_reopened"] is False
    assert relative["decision"]["Q602_excluded"] is False
    assert "f1^* Z ~= f2^* Z" in relative_note
    assert "Only the dimension condition is used below; no unidentified basis for W is assumed." in relative_note

    assert common["status"] == "AUDITED_NEGATIVE"
    assert common["result"]["new_geometric_exclusion_certified"] is False
    assert common["result"]["strict_rosati_loss_certified"] is False
    assert "shared cover + marked branch/ramification => strict Rosati loss" in common_audit
    assert "This is an evidence gap, not a proof that the implication is false." in common_audit

    exact = b3["finite_mod2_check"]
    residues = b3["audited_q602_residues"]
    assert residues == [73, 97, 235]
    assert exact["b3_commuting_residues"] == []
    assert exact["all_audited_q602_residues_fail_b3_commutation"] is True
    assert b3["decision"]["conditional_implication"] == "[T,b3]=0 => Q(T)!=602"
    assert b3["decision"]["b3_equivariance_proved_for_actual_correspondence"] is False
    assert "[T,b3]=0  =>  Q(T) != 602" in b3_note

    rv4_survivors = set(relative["q602_mod2_preflight"]["surviving_residue_classes_decimal"])
    assert set(residues) <= rv4_survivors
    assert exact["b3_commuting_residues"] == []

    assert "nonexistence of an intrinsic automorphism of a hypothetical carrier `Y`" in ambient_note
    assert "no actual carrier equation" in carrier_note
    assert "source/common-model anchor for semantic identification" in s30
    assert "semantic/geometric identification merely from reconstructed algebra" in s32

    assert "bounded authority/source-chain audit, not a repository-wide absence search" in note
    assert "REUSE_RETAINED_COMMON_DOUBLE_COVER_CARTESIAN_IDENTITY_AS_B3_COMMUTATION_PROOF" in note
    assert "It is not a counterexample to a stronger future geometric theorem" in note

    rc = cert["retained_common_cover_consequence"]
    assert rc["cartesian_identity"] == "f1^*Z ~= f2^*Z"
    assert rc["mod2_consequence"] == ["T|W = identity", "T^dagger|W = identity"]
    assert rc["already_consumed_by_stage32"] is True

    sep = cert["exact_separation"]
    assert sep["audited_q602_residues"] == residues
    assert sep["b3_commuting_residues"] == []
    assert sep["all_audited_q602_residues_fail_b3_commutation_mod2"] is True

    ars = cert["arsenal_precheck"]
    assert ars["direct_weapon_closes_missing_b3_semantic_bridge"] is False

    d = cert["decision"]
    assert d["closed_route"] == "REUSE_RETAINED_COMMON_DOUBLE_COVER_CARTESIAN_IDENTITY_AS_B3_COMMUTATION_PROOF"
    for key in [
        "actual_b3_commutation_proved",
        "actual_b3_noncommutation_proved",
        "intrinsic_carrier_automorphism_nonexistence_proved",
        "Q602_excluded_unconditionally",
        "O210_excluded_unconditionally",
        "O212_plus_authorized",
        "controller_change_authorized",
    ]:
        assert d[key] is False

    assert all(v is False for v in cert["firewalls"].values())

    print(
        "PASS: the retained Cartesian/relative-V4 identity is positive common-cover "
        "coupling already consumed by Stage32, but its exact extracted predicates do "
        "not imply b3 commutation. The three final Q602 residues survive the relative-V4 "
        "predicate and all fail b3 commutation mod 2. This closes only reuse of that "
        "retained identity as a b3-commutation proof; actual intrinsic carrier equivariance "
        "remains unresolved."
    )


if __name__ == "__main__":
    main()
