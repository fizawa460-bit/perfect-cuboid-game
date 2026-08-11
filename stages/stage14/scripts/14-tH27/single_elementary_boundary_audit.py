#!/usr/bin/env python3
"""Deterministic Stage14-tH27 frozen single-boundary audit."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T98 = ROOT / "stages/stage14/14-t98/result.md"
T99 = ROOT / "stages/stage14/14-t99/result.md"
TARGET = ROOT / "stages/stage14/14-t99/th27-target.md"
RESULT = ROOT / "stages/stage14/14-tH27/result.md"
BOUNDARY = ROOT / "stages/stage14/data/tH27/single_elementary_boundary_frozen.json"


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def predecessor_audit() -> None:
    t98 = T98.read_text()
    t99 = T99.read_text()
    target = TARGET.read_text()
    for token in [
        "SIGN_BOUNDARY_REDUCED_TO_O1_LINEAR_HALFSPACE_XOR=true",
        "FOUR_CELL_BOUNDARY_REDUCED_TO_BO1_FIXED_DIVISOR_CONGRUENCE_XORS=true",
        "ENDPOINT_BOUNDARY_REDUCED_TO_BO1_SMALL_MODULUS_RESIDUE_XORS=true",
        "FIXED_DIVISOR_MODULI_FORCED_SMALL=false",
    ]:
        need(t98, token, "t98")
    for token in [
        "STAGE14_T99=COMPLETE_BOUNDARY_CLASS_PIGEONHOLE_LOCALIZATION",
        "SINGLE_ELEMENTARY_BOUNDARY_PIGEONHOLE_PROVED=true",
        "SIGN_BOUNDARY_BRANCH_RETAINED=true",
        "FIXED_DIVISOR_BOUNDARY_BRANCH_RETAINED=true",
        "ENDPOINT_PROJECTIVE_BOUNDARY_BRANCH_RETAINED=true",
        "FIXED_POWER_BOUNDARY_SPARSITY_PROVED=false",
        "TH27_NEEDED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ]:
        need(t99, token, "t99")
    for token in [
        "SharedUCanonicalLPFSingleGenericPrimeSingleElementaryBoundaryClassEnergy",
        "SIGN_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=...",
        "FIXED_DIVISOR_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=...",
        "ENDPOINT_PROJECTIVE_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=...",
        "Do not treat a fixed divisor of `A0B0` as small",
        "Do not infer sparsity of a sign half-space boundary",
        "Do not reopen tH26",
    ]:
        need(target, token, "t99 target")


def sign_density_guard(N: int = 800) -> dict[str, float | int]:
    total = 0
    hit = 0
    for u in range(-N, N + 1):
        for v in range(-N, N + 1):
            if u == 0 and v == 0:
                continue
            total += 1
            plus = (u + v) > 0
            minus = (u - v) > 0
            hit += int(plus ^ minus)
    density = hit / total
    assert density > 0.45
    return {"sign_box_total": total, "sign_box_hits": hit, "sign_box_density": density}


def residue_xor_density(modulus: int) -> tuple[int, int, float]:
    total = modulus * modulus
    hit = 0
    for u in range(modulus):
        for v in range(modulus):
            plus = (u + v) % modulus == 0
            minus = (u - v) % modulus == 0
            hit += int(plus ^ minus)
    return total, hit, hit / total


def divisor_guard() -> dict[str, float | int]:
    total, hit, density = residue_xor_density(3)
    assert hit == 4
    assert density == 4 / 9
    return {"div_modulus": 3, "div_residue_total": total, "div_residue_hits": hit, "div_density": density}


def projective_guard() -> dict[str, float | int]:
    total, hit, density = residue_xor_density(5)
    assert hit == 8
    assert density == 8 / 25
    return {"proj_modulus": 5, "proj_residue_total": total, "proj_residue_hits": hit, "proj_density": density}


def boundary_audit() -> None:
    text = RESULT.read_text()
    tokens = [
        "STAGE14_TH27=COMPLETE_T99_SNAPSHOT_SINGLE_ELEMENTARY_INFLUENTIAL_BOUNDARY_APPLICABILITY_AUDIT",
        "AUDITED_THROUGH=Stage14-t99",
        "SOURCE_SNAPSHOT_SHA=41c850ab94f049f6a7523f9719bdc2f2ac9ecbaf",
        "TARGET_FROZEN=true",
        "T99_SNAPSHOT_RETAINED=true",
        "SIGN_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=false",
        "FIXED_DIVISOR_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=false",
        "ENDPOINT_PROJECTIVE_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED=false",
        "FULL_PHYSICAL_MASKS_RETAINED=true",
        "CERTIFIED_BOUNDARY_SAVING_EXPONENT=0",
        "FIXED_U_PACKET_POWER_SAVING_PROVED=false",
        "FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=false",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=SingleElementaryBoundaryPrincipalMassLacksUniformFixedPowerCodimensionUnderCanonicalLPFPhysicalMasks",
        "NEXT_H_NEEDED=false",
    ]
    for token in tokens:
        need(text, token, "tH27")

    data = json.loads(BOUNDARY.read_text())
    assert data["source_snapshot_sha"] == "41c850ab94f049f6a7523f9719bdc2f2ac9ecbaf"
    assert data["target_frozen"] is True
    assert data["branches"]["SIGN_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED"] is False
    assert data["branches"]["FIXED_DIVISOR_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED"] is False
    assert data["branches"]["ENDPOINT_PROJECTIVE_BOUNDARY_UNIFORM_FIXED_POWER_SAVING_PROVED"] is False
    assert data["certified_boundary_saving_exponent"] == "0"
    assert data["next_h_needed"] is False


def main() -> None:
    predecessor_audit()
    sign = sign_density_guard()
    div = divisor_guard()
    proj = projective_guard()
    boundary_audit()
    out = {
        "stage": "14-tH27",
        "status": "COMPLETE_T99_SNAPSHOT_SINGLE_ELEMENTARY_INFLUENTIAL_BOUNDARY_APPLICABILITY_AUDIT",
        "source_snapshot_sha": "41c850ab94f049f6a7523f9719bdc2f2ac9ecbaf",
        "target_frozen": True,
        "certified_boundary_saving_exponent": "0",
        "minimal_remaining_obstruction": "SingleElementaryBoundaryPrincipalMassLacksUniformFixedPowerCodimensionUnderCanonicalLPFPhysicalMasks",
        **sign,
        **div,
        **proj,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
