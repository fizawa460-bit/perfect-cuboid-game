#!/usr/bin/env python3
"""Post-R5 hostile guard for corrected J2 Q-descent.

This verifier intentionally does NOT claim arithmetic descent.  It replays the
finite F2-presentation Galois fixedness of corrected geometric J2 and then
checks the repo's own source firewall: xalpha_pair_galois_repair.py explicitly
states that arithmetic Hochschild--Serre descent is not established.

The previous version incorrectly assigned Pic/2 defect, an integral Pic lift,
and the HS d2 cocycle to zero constants after proving only Galois fixedness.
That implication is invalid.  The exact next leaf is to materialize the actual
HS d2 obstruction and prove that class is zero (or construct an equivalent
explicit Q-defined Brauer representative).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
S33 = ROOT.parent

EXPECTED_BLOBS = {
    "xalpha_pair_galois_repair.py": "b7f37df50a123ef6c972aa210e7efb5f16535f76",
    "j2-corrected-full-l-representative.json": "466b193b0fda90480484dbc520dcb5938879196c",
    "j2-corrected-cv-e2-cocycle.json": "5165ee50011382f6cbe34340d51538a35f9fc942",
    "j2-r4-hostile-torsor-brauer-kernel-verification.json": "32be9c1f272a4b12d032bbba00d9bbea1edf2622",
}
EXPECTED_EXTERNAL_BLOB = {
    S33 / "33-12" / "j2-cv-lclass-zero-regression.json": "06eeb5356323db06bfb312061095be0320aa52d0",
}


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


for name, sha in EXPECTED_BLOBS.items():
    p = ROOT / name
    assert git_blob_sha1(p) == sha, (name, git_blob_sha1(p), sha)
for p, sha in EXPECTED_EXTERNAL_BLOB.items():
    assert git_blob_sha1(p) == sha, (str(p), git_blob_sha1(p), sha)

r2 = json.loads((ROOT / "j2-corrected-full-l-representative.json").read_text(encoding="utf-8"))
r3 = json.loads((ROOT / "j2-corrected-cv-e2-cocycle.json").read_text(encoding="utf-8"))
r4 = json.loads((ROOT / "j2-r4-hostile-torsor-brauer-kernel-verification.json").read_text(encoding="utf-8"))
old_zero = json.loads((S33 / "33-12" / "j2-cv-lclass-zero-regression.json").read_text(encoding="utf-8"))

assert r2["status"] == "PASS_EXACT_R2_CORRECTED_REPRESENTATIVE_NONZERO"
assert r2["corrected_representative"]["pair"] == "(f2,1)"
assert r2["full_quotient_zero_test"]["corrected_pair_zero"] is False
assert r3["status"] == "PASS_EXACT_R3_EXPLICIT_NONZERO_CV_E2_COCYCLE"
assert r3["cv_lemma_4_6"]["xi_rho"] == "Tr"
assert r4["status"] == "PASS_HOSTILE_R4_INTEGRAL_KERNEL_IDENTIFICATION"
assert r4["integral_lattice_check"]["marked_brauer_coordinate"] == [1, 0]
assert r4["integral_lattice_check"]["minimum_norm"] == 8
assert old_zero["status"] == "PASS_EXACT_UPSTREAM_REPRESENTATIVE_CONTRADICTION"
assert old_zero["stage33_05_named_representative_geometric_nontriviality_supported"] is False

# Replay only the finite-presentation fixedness that is actually computed.
BASIS = ["J1", "J2", "q1", "q2", "q3"]
I5 = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
ct = [row[:] for row in I5]
ct[0][2] ^= 1
ct[0][3] ^= 1
MATS = {"tau": I5, "cc": I5, "ct": ct}
J2 = [0, 1, 0, 0, 0]


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(5)) & 1 for i in range(5)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(5)) & 1 for j in range(5)] for i in range(5)]


for name, M in MATS.items():
    assert matvec(M, J2) == J2, name

group_image = []
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            M = I5
            for bit, name in ((a, "tau"), (b, "cc"), (c, "ct")):
                if bit:
                    M = matmul(MATS[name], M)
            if M not in group_image:
                group_image.append(M)
assert len(group_image) == 2
assert all(matvec(M, J2) == J2 for M in group_image)

# Repo self-check: the source of this action explicitly stops at geometry.
xalpha_text = (ROOT / "xalpha_pair_galois_repair.py").read_text(encoding="utf-8")
assert "This remains a geometric statement.  Arithmetic Hochschild--Serre descent is" in xalpha_text
assert '"descent_obstruction_accounted": False' in xalpha_text
assert '"Q_defined_arithmetic_representatives_materialized": False' in xalpha_text
assert '"Q_relevant_surviving_dimension_certified": False' in xalpha_text

cert = {
    "schema": "STAGE33_05_J2_POST_R5_HS_DESCENT_AUDIT_REOPENED_V2",
    "status": "FAIL_UNPROVEN_POST_R5_Q_DESCENT_HS_D2_NOT_MATERIALIZED",
    "scope": "CORRECTED_J2_Q_DESCENT_BLOCKER_ONLY_R0_TO_R4_RETAINED",
    "retained_exact_geometric_credit": {
        "corrected_J2_full_L_pair": "(f2,1)",
        "R2_nonzero": True,
        "R3_E2_cocycle": "xi(rho)=Tr",
        "R4_twisted_kernel_gram": [[8, 0], [0, 16]],
        "R4_minimum_norm": 8,
        "R4_marked_brauer_coordinate": [1, 0],
        "named_J2_torsor_geometric_credit_retained": True,
    },
    "finite_presentation_replay": {
        "basis": BASIS,
        "J2_lift_vector": J2,
        "galois_generators": ["tau", "cc", "ct"],
        "action_image_size": len(group_image),
        "J2_fixed_by_every_action_image_element": True,
        "exact_credit": "GALOIS_INVARIANCE_OF_GEOMETRIC_BRAUER_QUOTIENT_CLASS_ONLY",
    },
    "source_self_check": {
        "source": "stages/stage33/33-05/xalpha_pair_galois_repair.py",
        "source_states_geometric_only": True,
        "descent_obstruction_accounted": False,
        "Q_defined_arithmetic_representatives_materialized": False,
        "Q_relevant_surviving_dimension_certified": False,
    },
    "audit_failure": {
        "forbidden_inference": "Galois-fixed geometric Brauer class => HS d2=0",
        "presentation_defect_zero_does_not_compute_pic_mod2_defect": True,
        "pic_mod2_defect_1cocycle_materialized": False,
        "normalized_integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_corrected_J2_zero_proved": False,
        "corrected_J2_in_image_of_Br_Kc_Q_proved": False,
        "equivalent_arithmetic_descent_datum_materialized": False,
        "closed_form_Q_CSA_formula_materialized": False,
        "arithmetic_unramifiedness_for_corrected_Q_lift_proved": False,
        "reason": "The prior verifier computed only fixedness in a 5D F2 presentation, then assigned Pic/2 defect, integral Pic lift, and HS d2 cocycle to zero constants without deriving them. Hochschild-Serre exactness requires an actual proof that d2(J2)=0 before arithmetic Brauer image credit.",
    },
    "required_next_leaf": {
        "id": "POST_R5_MATERIALIZE_HS_D2_OBSTRUCTION_AND_PROVE_ZERO",
        "objective": "Construct the actual Hochschild-Serre d2 obstruction for corrected geometric J2 and prove it vanishes, or construct an equivalent explicit Q-defined arithmetic Brauer representative.",
        "mandatory_checks": [
            "materialize a genuine Pic/2 or integral-Pic lift datum from the full Galois action, not a zero constant",
            "compute the resulting HS d2 2-cocycle/class",
            "prove the computed d2 class is zero in the correct H2 target",
            "only then invoke HS kernel=image to obtain a Q-defined Brauer lift",
            "prove the geometric restriction is corrected nonzero J2=(f2,1), never the revoked old ell_Q",
            "verify arithmetic unramifiedness/residue conditions required by Stage33-05 closure contract",
        ],
    },
    "repair_exit": {
        "corrected_J2_Q_descent_exact_evidence_reestablished": False,
        "corrected_J2_equivalent_arithmetic_descent_datum_materialized": False,
        "all_surviving_K3_classes_have_explicit_arithmetic_representatives_evidence": False,
        "unresolved_unknown_in_R5_repair_scope": 1,
        "R5_geometric_hostile_replay_pass": True,
        "R5_full_repair_exit_reached": False,
        "Q_defined_descent_credit_authoritatively_restored": False,
        "super_hostile_closure_gate_released": False,
    },
    "firewalls": {
        "stage33_05_reclosed": False,
        "stage33_05_unit_status": "BLOCKED_NEW_KERNEL",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "stage33_progress": "5/11",
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()

OUT = ROOT / "j2-post-r5-hs-descent-datum.json"
if OUT.exists():
    recorded = json.loads(OUT.read_text(encoding="utf-8"))
    assert recorded == cert, "recorded post-R5 audit-reopened certificate does not match recomputation"
else:
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(json.dumps(cert, indent=2, sort_keys=True))
