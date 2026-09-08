#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage32-ex2/EX2-03/adjoint-nef-blocker-preflight.json"
PARENT = ROOT / "stages/stage32-ex2/EX2-03/remaining-five-conic-restriction-preflight.json"
EXPECTED_ART_BLOB = "3c93705c2515346853b58e337add31fa0ad83e93"
EXPECTED_PARENT_BLOB = "32e19797812f35ad15fc5cad7559be76140480ef"
EXPECTED_CANON = "f461e61b08036b35fbee5f115423b1795f9e3478fd457a670f1439c9e1284ca6"
LABELS = [21, 24, 25, 30, 31]


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


a = json.loads(ART.read_text())
p = json.loads(PARENT.read_text())
assert blob(ART) == EXPECTED_ART_BLOB
assert blob(PARENT) == EXPECTED_PARENT_BLOB
assert a["canonical_sha256_without_this_field"] == canonical(a) == EXPECTED_CANON
assert a["schema"] == "STAGE32EX2_EX2_03E_ADJOINT_NEF_BLOCKER_PREFLIGHT_V1"
assert a["status"] == "PASS_DIRECT_ADJOINT_NEF_VANISHING_ROUTE_BLOCKED_ON_ALL_FIVE_CONICS"
assert p["remaining_labels_1based"] == LABELS
geom = p["exact_geometry"]
assert geom["V6_dot_each_curve"] == 0
assert geom["all_five_canonical_degree"] == 2
assert geom["all_five_self_intersection"] == -4
assert geom["pairwise_disjoint"] is True
assert geom["intersection_matrix"] == [[-4 if i == j else 0 for j in range(5)] for i in range(5)]
rows = a["adjoint_test"]["rows"]
assert [r["target_label_1based"] for r in rows] == LABELS
for r in rows:
    i = r["target_label_1based"]
    others = [j for j in LABELS if j != i]
    # A_i.C_i = 0 - (-4) - 2 = 2.
    assert r["A_dot_target_C"] == 2
    # A_i.C_j = 0 - 0 - 2 = -2 for every j != i.
    assert r["other_four_labels_1based"] == others
    assert r["A_dot_each_other_conic"] == -2
    assert r["nef_failure_witness_labels_1based"] == others
    assert r["nef"] is False
fw = a["credit_firewall"]
for key in [
    "H1_vanishing_proved", "H1_jump_computed", "restriction_evaluation_computed",
    "remaining_five_fixedness_classified", "remaining_five_nonfixedness_classified",
    "complete_H0_reconstructed", "fixed_part_fully_classified",
    "integral_irreducible_V6_genus1_member_obtained", "population_wide_no_genus1_member_proved",
    "stage32_main_credit", "Q602_excluded", "O210_excluded", "receiver_credit",
    "theorem_credit", "endpoint_credit", "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False, key
print("PASS EX2-03E: every A_i=V6-C_i-K has four exact -2 conic intersections, so the direct nef-based vanishing route is blocked; no H1/fixedness/member/MAIN credit.")
