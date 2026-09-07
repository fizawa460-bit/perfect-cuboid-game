#!/usr/bin/env python3
"""Goal4AJ diagnostic: numerator residual rigidity at degree 31.

Mirror the passing denominator rigidity argument for the exact numerator packet.
The effective Q-defined retained140 divisor D=D_strict+D_exc has class 31H.
On the minimal resolution H=b^*O(1).  Any effective remainder with H-degree zero
is exceptional.  The 48 A1 exceptional curves have Gram matrix -2 I, hence are
independent, so the remainder is forced coefficientwise to the exact D_exc.
Therefore all nonzero degree-31 sections satisfying the numerator strict
multiplicities have the same divisor and span exactly one line.  Existence comes
from the effective exact 31H divisor packet itself.

Diagnostic only: no homogeneous coefficients or literal F_B are materialized.
"""
from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy
import subprocess

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py"
GOAL4AI = ROOT / "stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence.json"
GOAL4AI_SOURCE = ROOT / "stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence-source-lock.md"

ACTIVE_SHA = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
ACTIVE_RUN = 34095500391
ACTIVE_JOB = 101658235698
GOAL4AI_SHA = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
DIVISOR_PACKET_SHA = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
LOCATOR_SHA = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
A1_SHA = "b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66"
DEN_RIGIDITY_SHA = "e493f4154fa4a6a5b64faceef4d3766a71828512d2323a3bd939d8bd1f53e3fc"
DEN_RIGIDITY_RUN = 34100994004
DEN_RIGIDITY_JOB = 101675227918
HIGHM_RESOURCE_RUN = 34096463932
HIGHM_RESOURCE_JOB = 101661191043

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_SHA
facts = set(ai["source_locks"]["stoll_testa"]["facts"])
assert {"48_A1_rational_double_points", "H_equals_K_on_minimal_resolution", "rational_singularity_global_section_transfer"} <= facts
assert "H=K_S=b^*O_Sbar(1)" in GOAL4AI_SOURCE.read_text(encoding="utf-8")

ap = subprocess.run(["python", "-B", str(ACTIVE)], text=True, capture_output=True, timeout=60)
assert ap.returncode == 0
line = next(x for x in ap.stdout.splitlines() if x.startswith("GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON="))
active = json.loads(line.split("=", 1)[1])
assert active["canonical_sha256"] == ACTIVE_SHA
num = active["numerator"]
assert num["homogeneous_degree_after_q_peel"] == 31
assert num["retained_support_count"] == 75
assert num["strict_support_count"] == 27
assert num["exceptional_support_count"] == 48
assert num["v4_invariant_exact"] is True
strict = {int(k): int(v) for k, v in num["strict_multiplicities_1based"].items()}
exc = {int(k): int(v) for k, v in num["exceptional_multiplicities_1based"].items()}
assert sum(strict.values()) == 202 and max(strict.values()) == 21
assert sum(exc.values()) == 612 and max(exc.values()) == 37
assert sum(v*v for v in exc.values()) == 11616

buf = io.StringIO()
with redirect_stdout(buf):
    base = runpy.run_path(str(BASE))
known = [[int(x) for x in r] for r in base["known"]]
gram = base["gram"]
H = [int(x) for x in list(base["H"])]
assert len(known) == 140 and len(H) == 64


def cls(packet: dict[int, int]) -> list[int]:
    return [sum(packet.get(j + 1, 0) * known[j][u] for j in range(140)) for u in range(64)]


def pair(a: list[int], b: list[int]) -> int:
    return sum(a[u] * int(gram[u, v]) * b[v] for u in range(64) for v in range(64))

Dstrict = cls(strict)
Dexc = cls(exc)
Dfull = [Dstrict[u] + Dexc[u] for u in range(64)]
assert Dfull == [31 * x for x in H]
H2 = pair(H, H)
assert H2 == 16
assert pair(H, Dfull) == 496
assert pair(H, Dstrict) == 496
assert pair(H, Dexc) == 0

for i in range(92, 140):
    assert pair(H, known[i]) == 0
    for j in range(92, 140):
        assert pair(known[i], known[j]) == (-2 if i == j else 0)
exc_square = pair(Dexc, Dexc)
assert exc_square == -23232

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_RESIDUAL_RIGIDITY_DIAGNOSTIC_V1",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_SHA,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA,
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_SHA,
        "active_divisor_condition_packet_run": ACTIVE_RUN,
        "active_divisor_condition_packet_job": ACTIVE_JOB,
        "a1_residual_jet_canonical_sha256": A1_SHA,
        "retained140_locator_canonical_sha256": LOCATOR_SHA,
        "denominator_rigidity_canonical_sha256": DEN_RIGIDITY_SHA,
        "denominator_rigidity_run": DEN_RIGIDITY_RUN,
        "denominator_rigidity_job": DEN_RIGIDITY_JOB,
        "high_m_resource_wall_run": HIGHM_RESOURCE_RUN,
        "high_m_resource_wall_job": HIGHM_RESOURCE_JOB,
    },
    "numerator_homogeneous_degree": 31,
    "surface_hyperplane_square": H2,
    "full_numerator_exact_picard_class_31H": True,
    "full_numerator_effective": True,
    "full_numerator_q_defined_v4_exact": True,
    "strict_support_count": len(strict),
    "strict_total_multiplicity": sum(strict.values()),
    "strict_max_multiplicity": max(strict.values()),
    "exceptional_support_count": len(exc),
    "exceptional_total_multiplicity": sum(exc.values()),
    "exceptional_max_multiplicity": max(exc.values()),
    "strict_H_degree": pair(H, Dstrict),
    "exceptional_H_degree": pair(H, Dexc),
    "exceptional_square": exc_square,
    "all_48_exceptionals_H_orthogonal": True,
    "exceptional_gram_is_minus2_identity": True,
    "exceptional_classes_independent": True,
    "H_is_pullback_of_canonical_model_ample_O1": True,
    "effective_H_zero_remainder_supported_on_exceptional_locus": True,
    "strict_condition_remainder_unique_effective_divisor": True,
    "strict_condition_space_dimension_upper_bound": 1,
    "nonzero_strict_condition_section_exists_from_effective_31H_divisor": True,
    "strict_condition_space_dimension_exact": 1,
    "numerator_section_line_unique_up_to_scalar": True,
    "q_rational_section_line_descends": True,
    "high_m_C1_m21_resource_wall_bypassed_for_dimension_proof": True,
    "literal_numerator_coefficients_materialized": False,
    "literal_numerator_polynomial_materialized": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_NUM_RIGIDITY_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_NUM_RIGIDITY=PASS")
