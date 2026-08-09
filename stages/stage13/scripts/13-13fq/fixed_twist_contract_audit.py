#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
proof = (root / "stages/stage13/13-13fq/fixed-twist-hecke-contract.md").read_text(encoding="utf-8")
result = (root / "stages/stage13/13-13fq/result.md").read_text(encoding="utf-8")

# Exact notation translation used by the two primary-source conventions.
for ell in range(1, 65):
    m = 8 * ell
    k_hlr = m // 4
    j_merikoski = m
    gamma_shift = 2 * k_hlr
    assert k_hlr == 2 * ell
    assert j_merikoski == 8 * ell
    assert gamma_shift == 4 * ell
    assert j_merikoski != 0

required_proof = [
    "R07_FIXED_TWIST_FAMILY_EXPLICIT=true",
    "R07_HLR_TO_MERIKOSKI_TRANSLATION=Xi_{2ell}=xi_{8ell}",
    "R07_FIXED_TWIST_PRIMARY_CONTRACT_VERIFIED=true",
    "R07_TWIST_CONDUCTOR_INDEPENDENT_OF_B=true",
    "R07_TWIST_INFINITY_TYPE_NONZERO_FOR_ELL_GE_1=true",
    "R07_TWIST_HOLOMORPHIC_AT_S1=true",
    "R07_TWIST_GAMMA_SHIFT=4*ell",
    "R07_COMMON_STRIP_GROWTH_EXPONENTS_EXIST=true",
    "R07_COMMON_STRIP_GROWTH_UNIFORM_IN_ELL=true",
    "R07_GROWING_MODULUS_THEOREM_USED=false",
    "R07_ZERO_FREE_REGION_REQUIRED=false",
    "NEXT=13-13fr",
]
for token in required_proof:
    assert token in proof, token

required_result = [
    "STAGE13_13FQ=COMPLETE_R07_FIXED_TWIST_HECKE_CONTRACT",
    "R07_GATE_A=COMPLETE",
    "R07_REPAIR_BLOCKERS_OPEN=2",
    "R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true",
    "R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true",
    "R06_IMMUTABLE=true",
    "THEOREM_CHANGED=false",
    "PROMOTE_TO_13_13G=false",
    "NEXT=13-13fr",
]
for token in required_result:
    assert token in result, token

# Guard against the old ambiguous angular-index language.
assert "k=8 ell" not in proof
assert "Xi_{8 ell}" not in proof

print("STAGE13_13FQ_AUDIT=PASS")
print("HLR_INDEX=2*ell")
print("MERIKOSKI_INDEX=8*ell")
print("GAMMA_SHIFT=4*ell")
print("DETERMINISTIC_AUDIT_SCOPE=CONTRACT_AND_NOTATION_CONSISTENCY_ONLY")
