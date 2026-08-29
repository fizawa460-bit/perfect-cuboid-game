#!/usr/bin/env python3
"""Network-free verifier: Picard-discriminant ct connecting cannot identify J2."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PIC = HERE / "j2-semantic-kc-picard-basis.json"
TARGET = HERE / "j2-semantic-kc-discriminant-2torsion-target.json"
OUT = HERE / "j2-picard-discriminant-galois-functional-rejection.json"

EXPECTED_PIC = "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"
EXPECTED_TARGET = "0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df"
EXPECTED_OUT = "ae980dae7e33ecf58e35d697dde1c1be20c98c170bde6b6b9591e9b1f8680e54"

def csha(d):
    d = dict(d)
    d.pop("canonical_sha256", None)
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def ct_curve_slot(j):
    # Stoll source: CsK[1..26] contains no sqrt(2), hence ct-fixed.
    if 1 <= j <= 26:
        return j
    # C3sK first three 8-curve families: ct flips e2; with Magma
    # comprehension order e3 varies fastest, this toggles zero-based bit 1.
    if 27 <= j <= 50:
        b = 27 + 8 * ((j - 27) // 8)
        return b + (((j - b) ^ 2))
    # Last three 4-curve families: ct flips e3, again toggling bit 1.
    if 51 <= j <= 62:
        b = 51 + 4 * ((j - 51) // 4)
        return b + (((j - b) ^ 2))
    raise ValueError(j)

def support(v):
    return [i + 1 for i, x in enumerate(v) if x & 1]

def main():
    pic = json.loads(PIC.read_text())
    target = json.loads(TARGET.read_text())
    out = json.loads(OUT.read_text())
    assert pic["canonical_sha256"] == EXPECTED_PIC == csha(pic)
    assert target["canonical_sha256"] == EXPECTED_TARGET == csha(target)
    assert out["canonical_sha256"] == EXPECTED_OUT == csha(out)

    slots = pic["curve_slots_1based"]
    assert slots == [2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54]
    assert ct_curve_slot(47) == 49 and ct_curve_slot(49) == 47
    assert ct_curve_slot(52) == 54 and ct_curve_slot(54) == 52

    basis = [r["numerator_mod2"] for r in target["semantic_half_lattice_basis"]]
    assert support(basis[0]) == [1,2,5,6,14,15]
    assert support(basis[1]) == [16,17]

    for rec, v in zip(out["semantic_half_lattice_ct_test"], basis):
        supp = support(v)
        assert rec["support_semantic_basis_positions_1based"] == supp
        curve_supp = [slots[i-1] for i in supp]
        assert rec["support_stoll_curve_slots_1based"] == curve_supp
        moved = sorted(ct_curve_slot(j) for j in curve_supp)
        assert moved == sorted(curve_supp)
        assert rec["numerator_fixed_exactly"]
        assert rec["dual_representative_fixed_exactly"]
        assert rec["picard_discriminant_connecting_cocycle"] == "0"

    assert out["all_three_nonzero_candidates_picard_discriminant_ct_connecting_zero"]
    assert out["cv_presentation_reference"] == {"J2_ct_connecting":"0","q1_ct_connecting":"J1_nonzero"}
    assert out["j2_coordinate_materialized"] is False
    assert out["stage33_12_closed_exact"] is False
    assert out["stage33_13_released"] is False
    print(json.dumps({
        "status":"PASS_EXACT",
        "ct_swaps":[[47,49],[52,54]],
        "candidate_connecting_values":["0","0","0"],
        "canonical_sha256":out["canonical_sha256"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
