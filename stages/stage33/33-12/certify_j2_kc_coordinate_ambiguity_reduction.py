#!/usr/bin/env python3
"""Reduce the missing J2 coordinate adapter to exactly three F2^2 directions.

This is a MAIN progress certificate, not a closure certificate.  The hostile-
audited K_c interface fixes Br(K_cbar)[2]^G_Q as a two-dimensional space with
named basis [J2,q1], with kernel(d2)=<J2> and d2(q1) nonzero.  The retained
K_c discriminant derivation fixes the coordinate target as the two-dimensional
2-torsion of Z/4 direct_sum Z/8.  Until the named-basis/discriminant adapter is
materialized, J2 is therefore exactly one of the three nonzero F2^2 vectors.

No candidate is selected here, and no 75x10 full-surface Kummer column is
silently assigned.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
AUDIT = S33 / "33-05" / "audit-state.json"
J2_ZERO = HERE / "j2-full-surface-mu2-zero-defect-contract.json"
KC_DERIVE = S33 / "33-07" / "derive_kc_discriminant_from_split.py"
OUT = HERE / "j2-kc-coordinate-ambiguity-reduction.json"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


audit = json.loads(AUDIT.read_text(encoding="utf-8"))
j2 = json.loads(J2_ZERO.read_text(encoding="utf-8"))

assert audit["unit_status"] == "CLOSED"
assert audit["audited_functional_head"] == "1e6452d2a3df9c9e054d454173b4f923d6f1d343"
assert audit["geometric_br2_gq_invariant_dimension"] == 2
assert audit["geometric_invariant_basis"] == ["J2", "q1"]
assert audit["q_relevant_surviving_dim"] == 1
assert audit["q_surviving_geometric_br2_basis"] == ["J2"]
assert audit["j2_q_descent_certified"] is True
assert audit["q1_hs_d2_nonzero"] is True
assert j2["canonical_sha256"] == "ac2999b2e684c534b90c9f6c8a68261b33b3d549b4d4162d107c0509a6082b6a"
assert j2["finite_v4_consequence"]["delta_Kum_V4_of_J2"] == "EXACT_ZERO"
assert j2["coordinate_firewall"]["j2_vector_in_original_proper_br2_coordinates_materialized"] is False
assert KC_DERIVE.exists()
assert git_blob_sha1(KC_DERIVE) == "62724b75eba42bf980574b4b57b936775a1a893c"
text = KC_DERIVE.read_text(encoding="utf-8")
assert "mods=[4,8]" in text
assert "audited_Kc_Br2_invariant_dimension_f2':2" in text
assert "audited_Kc_HS_d2_kernel_basis':['J2']" in text

# Historical transient outputs are deliberately not treated as retained
# evidence.  If they reappear later, this certificate still refuses to infer
# a named-coordinate adapter from their mere presence.
missing_picard_maps = not (S33 / "33-07" / "kc-picard-maps.json").exists()
missing_disc_json = not (S33 / "33-07" / "kc-discriminant-compact.json").exists()

nonzero = [[1, 0], [0, 1], [1, 1]]
assert len({tuple(v) for v in nonzero}) == 3
assert all(any(v) for v in nonzero)

cert = {
    "schema": "STAGE33_12_J2_KC_COORDINATE_AMBIGUITY_REDUCTION_V1",
    "source_locks": {
        "stage33_05_audit_state_path": "stages/stage33/33-05/audit-state.json",
        "stage33_05_audit_functional_head": audit["audited_functional_head"],
        "j2_full_surface_mu2_zero_defect_contract_sha256": j2["canonical_sha256"],
        "kc_discriminant_derivation_script_blob_sha1": git_blob_sha1(KC_DERIVE),
    },
    "kc_side_exact": {
        "geometric_br2_gq_invariant_dimension_f2": 2,
        "named_invariant_basis": ["J2", "q1"],
        "q_surviving_dimension_f2": 1,
        "q_surviving_basis": ["J2"],
        "q1_hs_d2_nonzero": True,
        "j2_hs_d2_zero": True,
        "kc_picard_discriminant_group": "Z/4 direct_sum Z/8",
        "kc_br2_coordinate_dimension_f2": 2,
    },
    "coordinate_ambiguity": {
        "nonzero_vectors_in_any_f2_basis": nonzero,
        "j2_coordinate_candidate_count": 3,
        "j2_coordinate_candidate_set_exact": True,
        "j2_zero_vector_excluded": True,
        "reason": "J2 is a nonzero class spanning the one-dimensional HS-d2 kernel inside the two-dimensional invariant geometric Br[2]. Without the missing Kc named-basis-to-discriminant adapter, its coordinate is exactly one of the three nonzero F2^2 vectors.",
        "named_basis_to_kc_discriminant_basis_materialized": False,
        "candidate_selected": False,
    },
    "full_surface_consequence": {
        "j2_full_surface_q_defined_pullback_certified": True,
        "j2_full_surface_kummer_defect": "EXACT_ZERO",
        "proper14_coordinate_vector_materialized": False,
        "retained_P10_coordinate_vector_materialized": False,
        "existing_75x10_column_index_identified": False,
        "columns_materialized": 0,
    },
    "retention_gap": {
        "kc_picard_maps_json_present_on_current_branch": not missing_picard_maps,
        "kc_discriminant_compact_json_present_on_current_branch": not missing_disc_json,
        "derivation_scripts_present": True,
        "historical_intermediate_json_must_not_be_assumed": True,
    },
    "next_exact_leaf": "REGENERATE_MINIMAL_KC_DISCRIMINANT_NAMED_BASIS_ADAPTER_FROM_PINNED_STOLL_SOURCE_AND_RETAIN_ONLY_THE_2X2_F2_CHANGE_OF_BASIS",
    "promotion_firewall": {
        "arithmetic_hs_d2_computed": False,
        "proper_d2_map_computed": False,
        "global_q_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "stage33_progress": "6/11",
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "j2_coordinate_candidate_count": 3,
    "candidate_selected": False,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
