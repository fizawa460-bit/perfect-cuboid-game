#!/usr/bin/env python3
"""Enumerate every exact F2 adapter between named [J2,q1] and Kc coordinates.

This is deliberately an ambiguity witness, not an orientation guess.  The
hostile-audited Stage33-05 interface fixes d2(J2)=0 and d2(q1)!=0.  Those facts
fix a nonzero linear functional in the *named* basis.  They do not fix that
functional in the retained Kc discriminant coordinate basis.  Moreover, even
if the Kc kernel line <J2> were known, q1 and q1+J2 have the same d2 value, so
one additional named orientation invariant is mathematically necessary.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
AUDIT = S33 / "33-05" / "audit-state.json"
J2_ZERO = HERE / "j2-full-surface-mu2-zero-defect-contract.json"
PRIOR = HERE / "j2-kc-coordinate-ambiguity-reduction.json"
MARKED = S33 / "33-09" / "marked-picard-basis-source.json"
KC_DERIVE = S33 / "33-07" / "derive_kc_discriminant_from_split.py"
OUT = HERE / "j2-q1-kc-adapter-ambiguity-witness.json"

EXPECTED_Q1_D2 = "54e1b59b5080547034f0061eaf2c76e44e4ba16cdaec65ad7ac6269ddb5f17cf"
EXPECTED_J2_ZERO = "ac2999b2e684c534b90c9f6c8a68261b33b3d549b4d4162d107c0509a6082b6a"
EXPECTED_PRIOR = "b5333da1193ec65779e62e893b52c9ef0cd47093e0b41b73b4c6349a764fd7cb"
EXPECTED_MARKED = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
EXPECTED_KC_DERIVE_BLOB = "62724b75eba42bf980574b4b57b936775a1a893c"
STOLL_REPO = "MichaelStollBayreuth/Verification"
STOLL_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
STOLL_PATH = "Cuboids/cuboids.magma"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def dot(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (a[0] * b[0] + a[1] * b[1]) & 1


audit = json.loads(AUDIT.read_text(encoding="utf-8"))
j2 = json.loads(J2_ZERO.read_text(encoding="utf-8"))
prior = json.loads(PRIOR.read_text(encoding="utf-8"))
marked = json.loads(MARKED.read_text(encoding="utf-8"))

assert audit["unit_status"] == "CLOSED"
assert audit["audited_functional_head"] == "1e6452d2a3df9c9e054d454173b4f923d6f1d343"
assert audit["geometric_invariant_basis"] == ["J2", "q1"]
assert audit["q_surviving_geometric_br2_basis"] == ["J2"]
assert audit["q1_hs_d2_nonzero"] is True
assert audit["certificate_hashes"]["q1_hs_d2"] == EXPECTED_Q1_D2
assert j2["canonical_sha256"] == EXPECTED_J2_ZERO
assert j2["finite_v4_consequence"]["delta_Kum_V4_of_J2"] == "EXACT_ZERO"
assert prior["canonical_sha256"] == EXPECTED_PRIOR
assert prior["coordinate_ambiguity"]["j2_coordinate_candidate_count"] == 3
assert marked["canonical_sha256"] == EXPECTED_MARKED
assert marked["source"]["repository"] == STOLL_REPO
assert marked["source"]["commit"] == STOLL_COMMIT
assert marked["source"]["path"] == STOLL_PATH
assert len(marked["indlist_1based"]) == 64
assert len(marked["indlist_to_magma_picard_matrix_64x64"]) == 64
assert all(len(row) == 64 for row in marked["indlist_to_magma_picard_matrix_64x64"])
assert git_blob_sha1(KC_DERIVE) == EXPECTED_KC_DERIVE_BLOB
text = KC_DERIVE.read_text(encoding="utf-8")
assert "mods=[4,8]" in text
assert "audited_Kc_HS_d2_kernel_basis':['J2']" in text

nonzero = [(1, 0), (0, 1), (1, 1)]
adapters = []
for j2v in nonzero:
    for q1v in nonzero:
        if q1v == j2v:
            continue
        # In F2^2, two distinct nonzero vectors are automatically a basis.
        functionals = [ell for ell in nonzero if dot(ell, j2v) == 0 and dot(ell, q1v) == 1]
        assert len(functionals) == 1
        ell = functionals[0]
        adapters.append({
            "named_to_kc_matrix_columns_J2_q1": [[j2v[0], q1v[0]], [j2v[1], q1v[1]]],
            "J2_kc_coordinate": list(j2v),
            "q1_kc_coordinate": list(q1v),
            "q1_plus_J2_kc_coordinate": [j2v[0] ^ q1v[0], j2v[1] ^ q1v[1]],
            "transported_d2_functional_row_on_kc_coordinates": list(ell),
        })
assert len(adapters) == 6
assert len({tuple(tuple(row) for row in a["named_to_kc_matrix_columns_J2_q1"]) for a in adapters}) == 6

# Retained named d2 information is compatible with every adapter: each adapter
# simply transports the same named functional [0,1] to a different Kc row.
survivors = list(range(1, 7))
assert len(survivors) == 6

# For any fixed J2 line, exactly two q1 choices remain; they differ by J2 and
# hence have identical d2 because d2 is linear and d2(J2)=0.
for j2v in nonzero:
    same_line = [a for a in adapters if a["J2_kc_coordinate"] == list(j2v)]
    assert len(same_line) == 2
    q0 = tuple(same_line[0]["q1_kc_coordinate"])
    q1 = tuple(same_line[1]["q1_kc_coordinate"])
    assert q1 == (q0[0] ^ j2v[0], q0[1] ^ j2v[1])
    assert same_line[0]["transported_d2_functional_row_on_kc_coordinates"] == same_line[1]["transported_d2_functional_row_on_kc_coordinates"]

cert = {
    "schema": "STAGE33_12_J2_Q1_KC_ADAPTER_AMBIGUITY_WITNESS_V1",
    "source_locks": {
        "stage33_05_audit_functional_head": audit["audited_functional_head"],
        "stage33_05_q1_hs_d2_canonical_sha256": EXPECTED_Q1_D2,
        "j2_full_surface_mu2_zero_defect_contract_sha256": EXPECTED_J2_ZERO,
        "prior_j2_kc_ambiguity_sha256": EXPECTED_PRIOR,
        "marked_picard_basis_source_sha256": EXPECTED_MARKED,
        "pinned_stoll_repository": STOLL_REPO,
        "pinned_stoll_commit": STOLL_COMMIT,
        "pinned_stoll_path": STOLL_PATH,
        "kc_discriminant_derivation_script_blob_sha1": EXPECTED_KC_DERIVE_BLOB,
    },
    "enumeration": {
        "field": "F2",
        "named_basis": ["J2", "q1"],
        "kc_coordinate_basis": ["d1", "d2"],
        "GL2_F2_order": 6,
        "admissible_adapter_count_before_filter": 6,
        "adapters": adapters,
    },
    "filter_by_retained_named_d2_invariants": {
        "J2_d2": "ZERO",
        "q1_d2": "NONZERO",
        "q1_plus_J2_d2": "NONZERO",
        "kc_coordinate_d2_functional_materialized": False,
        "survivor_count": 6,
        "survivor_indices_1based": survivors,
        "reason": "The retained data fixes the d2 functional in the named basis but does not fix that functional in the Kc discriminant coordinate basis. Transporting the named functional through each GL(2,2) adapter gives a consistent Kc-coordinate functional, so all six adapters survive.",
    },
    "structural_nonuniqueness": {
        "even_if_kc_d2_kernel_line_is_materialized_survivor_count": 2,
        "reason": "For a fixed nonzero J2 kernel line there are exactly two q1 representatives outside that line, differing by J2. Since d2(J2)=0, q1 and q1+J2 have identical nonzero d2.",
        "therefore_J2_zero_and_q1_nonzero_can_never_alone_prove_unique_2x2_adapter": True,
    },
    "missing_distinguishing_invariant": {
        "first_missing_bit": "Kc discriminant coordinate of the named d2 kernel line <J2>, equivalently the Kc-coordinate d2 functional or one named class coordinate.",
        "second_missing_bit": "A named orientation invariant distinguishing q1 from q1+J2 after <J2> is fixed.",
        "acceptable_exact_sources": [
            "an exact CV named mu2/Kummer lift transported into the pinned Stoll Picard/discriminant quotient",
            "an exact coordinate of J2 or q1 in the Kc discriminant basis",
            "a retained pairing/evaluation functional on Kc discriminant coordinates whose values on q1 and q1+J2 are audited and distinct",
        ],
        "pinned_stoll_source_alone_sufficient": False,
        "reason": "The pinned Stoll source fixes the geometric Picard and quotient coordinates but does not label the CV Brauer classes J2 and q1.",
    },
    "full_surface_consequence": {
        "J2_proper14_coordinate_vector_materialized": False,
        "J2_P10_coordinate_vector_materialized": False,
        "J2_named_kernel_relation_in_75x10_materialized": False,
        "kummer_defect_columns_materialized": 0,
        "matrix_shape": [75, 10],
        "rank_upper_bound_from_named_J2_zero": 9,
    },
    "next_exact_leaf": "MATERIALIZE_ONE_NAMED_CV_TO_STOLL_DISCRIMINANT_ORIENTATION_INVARIANT_THEN_REPLAY_ALL_SIX_ADAPTERS",
    "promotion_firewall": {
        "adapter_unique": False,
        "arithmetic_hs_d2_computed": False,
        "proper_d2_map_computed": False,
        "global_q_residue_lifts_complete": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "receiver_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "GL2_F2_adapters": len(adapters),
    "survivors_after_retained_named_d2": len(survivors),
    "survivors_if_kernel_line_later_fixed": 2,
    "adapter_unique": False,
    "certificate_sha256": cert["canonical_sha256"],
    "next": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
