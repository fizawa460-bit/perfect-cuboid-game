#!/usr/bin/env python3
"""Certify the exact diagnostic reopening of the J2 Picard-adjoint source binding.

This does not guess a replacement J2 source.  It records that the previously
materialized Picard-adjoint beta1 coordinate is incompatible with the locked
J2 Kummer target in every V4-module extension with the locked actions, while
the companion adjoint lines are not blanket-obstructed.  The missing durable
interface is a marked full-surface transcendental/discriminant anti-isometry
(or an equivalent explicit H^2(mu2) -> Br[2] pullback adapter).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
ORIENTATION = HERE / "j2-cv-d2-semantic-orientation.json"
ADJOINT = HERE / "j2-picard-adjoint-proper-br2.json"
ADJOINT_MATERIALIZER = HERE / "materialize_j2_picard_adjoint_proper_br2.py"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
PROPER_PRODUCER = S33 / "33-07" / "certify_proper_brauer2_from_discriminant.py"
PIC_DISC = S33 / "33-07" / "picard-discriminant-compact.json"
AUDIT = HERE / "j2-kummer-source-target-module-compatibility-audit.json"
TARGET = HERE / "j2-named-v4-h1-target-before-source-orientation.json"
OUT = HERE / "j2-picard-adjoint-reopen-diagnostic.json"

LOCKS = {
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    ADJOINT: "066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    PIC_DISC: "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0",
    AUDIT: "463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229",
    TARGET: "4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3",
}
ADJOINT_MATERIALIZER_BLOB = "aaf4cf64cb9bc65aaea1e9c06d3d9c885b4a5299"
PROPER_PRODUCER_BLOB = "23fe426ab0a43b7cacc6923c92cd93367906e2fd"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def locked(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


def mask(bits: list[int]) -> int:
    return sum((int(bit) & 1) << i for i, bit in enumerate(bits))


def recompute() -> dict:
    orientation = locked(ORIENTATION)
    adjoint = locked(ADJOINT)
    proper = locked(PROPER)
    pic_disc = locked(PIC_DISC)
    audit = locked(AUDIT)
    target = locked(TARGET)

    assert git_blob_sha1(ADJOINT_MATERIALIZER) == ADJOINT_MATERIALIZER_BLOB
    assert git_blob_sha1(PROPER_PRODUCER) == PROPER_PRODUCER_BLOB
    assert orientation["exact_conclusion"]["named_CV_J2_fixed_marked_Kc_coordinate_f2"] == [1, 0]
    assert orientation["explicit_marked_adapter"]["brauer_functional_f2"] == [1, 0]

    p = adjoint["proper_brauer2_pullback"]
    beta1 = [int(x) & 1 for x in p["retained_10D_coordinate_f2"]]
    beta2 = [int(x) & 1 for x in p["companion_beta2_retained_10D_coordinate_f2"]]
    beta12 = [a ^ b for a, b in zip(beta1, beta2)]
    assert beta1 == [0,1,1,0,0,0,0,0,0,0]
    assert beta2 == [0,1,1,0,0,1,1,1,0,1]
    assert beta12 == [0,0,0,0,0,1,1,1,0,1]
    m1, m2, m12 = mask(beta1), mask(beta2), mask(beta12)
    assert (m1, m2, m12) == (6, 742, 736)

    bad = set(int(x) for x in audit["diagnostic"]["incompatible_source_masks_decimal"])
    assert len(bad) == 23
    assert m1 in bad and m2 not in bad and m12 not in bad
    assert audit["locked_named_j2"]["retained_10D_mask_decimal"] == m1
    assert audit["locked_named_j2"]["locked_75D_target_reachable_from_locked_source"] is False
    assert audit["all_v4_module_extensions_audit"]["nullity_f2"] == 1011
    assert target["retained_H1_projection"]["coordinate_weight"] == 15

    # The current proper-Br2 producer materializes only the abstract dual module
    # from the Picard discriminant module.  It does not source-lock a marked
    # full-surface transcendental anti-isometry.
    assert pic_disc["transcendental_discriminant_form_is_negative_of_picard_form"] is True
    assert pic_disc["actual_index512_k3_glue_identified"] is False
    assert proper["source_locks"] == {
        "picard_discriminant_compact_sha256": LOCKS[PIC_DISC]
    }
    source_lock_keys = set(adjoint["source_locks"])
    assert not any(
        ("anti_isometry" in k or "transcendental_marking" in k)
        for k in source_lock_keys
    )
    materializer = ADJOINT_MATERIALIZER.read_text(encoding="utf-8")
    assert "Via the\nK3 discriminant anti-isometries" in materializer

    cert = {
        "schema": "STAGE33_12_J2_PICARD_ADJOINT_REOPEN_DIAGNOSTIC_V1",
        "stage": "33-12",
        "status": "PASS_EXACT_DIAGNOSTIC_PICARD_ADJOINT_NAMED_SOURCE_REOPENED",
        "source_locks": {
            "semantic_orientation_sha256": LOCKS[ORIENTATION],
            "picard_adjoint_certificate_sha256": LOCKS[ADJOINT],
            "picard_adjoint_materializer_git_blob_sha1": ADJOINT_MATERIALIZER_BLOB,
            "proper_brauer2_sha256": LOCKS[PROPER],
            "proper_brauer2_producer_git_blob_sha1": PROPER_PRODUCER_BLOB,
            "picard_discriminant_compact_sha256": LOCKS[PIC_DISC],
            "compatibility_audit_sha256": LOCKS[AUDIT],
            "named_j2_target_sha256": LOCKS[TARGET],
        },
        "exact_reopen_trigger": {
            "rule": "authoritative current certificate contradicts the recorded fact",
            "named_Kc_J2_Br2_coordinate_f2": [1, 0],
            "picard_adjoint_J2_retained10_f2": beta1,
            "picard_adjoint_J2_mask_decimal": m1,
            "locked_target_reachable_from_mask6": False,
            "all_compatible_V4_module_extensions_were_audited": True,
            "consequence": "the Picard-adjoint coordinate may remain a valid lattice-derived candidate, but it is no longer promotable as the actual named J2 pullback source without an additional marked correspondence/anti-isometry adapter or a revocation of another locked input",
        },
        "two_dimensional_adjoint_image_diagnostic": {
            "beta1_retained10_f2": beta1,
            "beta1_mask_decimal": m1,
            "beta1_target_compatible": False,
            "beta2_retained10_f2": beta2,
            "beta2_mask_decimal": m2,
            "beta2_target_compatible": True,
            "beta1_plus_beta2_retained10_f2": beta12,
            "beta1_plus_beta2_mask_decimal": m12,
            "beta1_plus_beta2_target_compatible": True,
            "meaning": "the failure is not a blanket failure of the two-dimensional adjoint image; it is concentrated in the named J2 line selected as beta1. The compatible alternatives are diagnostics only and are not promoted as J2.",
        },
        "dependency_gap": {
            "proper_Br2_module_is_derived_from": "Picard discriminant module and dual action",
            "picard_adjoint_claim_uses": "a discriminant anti-isometry to decode full-surface target A_T[2] basis vectors as actual T(S)/2T(S) vectors before applying the Kc functional",
            "full_surface_marked_transcendental_anti_isometry_or_equivalent_H2_mu2_to_Br2_correspondence_source_locked_by_picard_adjoint": False,
            "next_required_adapter": "MATERIALIZE_FULL_SURFACE_MARKED_DISCRIMINANT_ANTI_ISOMETRY_OR_EQUIVALENT_EXPLICIT_H2_MU2_TO_PROPER_BR2_PULLBACK_ADAPTER_FOR_LAMBDA_D",
        },
        "promotion_firewall": {
            "beta2_promoted_as_J2": False,
            "beta1_plus_beta2_promoted_as_J2": False,
            "picard_adjoint_certificate_deleted": False,
            "picard_adjoint_named_J2_binding_retained_as_authoritative": False,
            "named_J2_target_revoked": False,
            "proper_Br2_module_revoked": False,
            "first_75D_matrix_column_materialized": False,
            "finite_v4_kummer_columns_materialized": 0,
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    cert = recompute()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "status": cert["status"],
        "beta1_mask": cert["two_dimensional_adjoint_image_diagnostic"]["beta1_mask_decimal"],
        "beta2_mask": cert["two_dimensional_adjoint_image_diagnostic"]["beta2_mask_decimal"],
        "beta1_plus_beta2_mask": cert["two_dimensional_adjoint_image_diagnostic"]["beta1_plus_beta2_mask_decimal"],
        "canonical_sha256": cert["canonical_sha256"],
        "wrote": args.write,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
