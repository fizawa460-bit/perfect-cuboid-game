#!/usr/bin/env python3
"""Goal4AJ diagnostic: denominator residual rigidity after Q-hyperplane peel.

Prove, without a global Groebner intersection, that the post-Q-peel degree-19
denominator strict-condition space is one-dimensional.  The exact active packet
is an effective divisor D = D_strict + D_exc with class 19H.  On the minimal
resolution H=b^*O(1), so every effective divisor of H-degree zero is supported
on the exceptional locus.  The 48 retained A1 exceptional curves have Gram
matrix -2 I, hence their classes are independent.  Therefore any nonzero
section satisfying the required strict multiplicities has exactly the fixed
exceptional remainder D_exc and hence exactly divisor D.  Two such sections
have the same divisor, so their ratio is constant.  Since D itself is effective
and linearly equivalent to 19H, a nonzero section exists: the space has exact
dimension one.

Diagnostic only.  This characterizes the section line but does not materialize
its homogeneous coefficients and grants no literal F_B, local, BM, E1, or
endpoint credit.
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
QPEEL_SHA = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
A1_SHA = "b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66"
LOCATOR_SHA = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
GOAL4AI_SHA = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
DIVISOR_PACKET_SHA = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
FAILED_STRICT_RUN = 34099109748
FAILED_STRICT_JOB = 101669263303

# Exact geometry/source semantic lock.
ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_SHA
facts = set(ai["source_locks"]["stoll_testa"]["facts"])
assert {
    "normal_complete_intersection_four_quadrics_in_P6",
    "48_A1_rational_double_points",
    "projectively_normal",
    "H_equals_K_on_minimal_resolution",
    "rational_singularity_global_section_transfer",
} <= facts
source_text = GOAL4AI_SOURCE.read_text(encoding="utf-8")
assert "H=K_S=b^*O_Sbar(1)" in source_text

# Replay compact active packet and exact post-peel denominator vector.
ap = subprocess.run(["python", "-B", str(ACTIVE)], text=True, capture_output=True, timeout=60)
assert ap.returncode == 0
line = next(x for x in ap.stdout.splitlines() if x.startswith("GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON="))
active = json.loads(line.split("=", 1)[1])
assert active["canonical_sha256"] == ACTIVE_SHA
den = active["denominator_residual"]
assert den["homogeneous_degree_after_q_peel"] == 19
assert den["retained_support_count"] == 66
assert den["strict_support_count"] == 22
assert den["exceptional_support_count"] == 44
assert den["v4_invariant_exact"] is True
strict = {int(k): int(v) for k, v in den["strict_multiplicities_1based"].items()}
exc = {int(k): int(v) for k, v in den["exceptional_multiplicities_1based"].items()}
assert all(1 <= k <= 92 and v > 0 for k, v in strict.items())
assert all(93 <= k <= 140 and v > 0 for k, v in exc.items())
assert sum(strict.values()) == 102 and max(strict.values()) == 13
assert sum(exc.values()) == 316 and max(exc.values()) == 18

# Reuse compact retained Picard recovery.  Suppress its bounded JSON report.
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
assert Dfull == [19 * x for x in H]
H2 = pair(H, H)
assert H2 == 16
assert pair(H, Dfull) == 19 * H2 == 304
assert pair(H, Dexc) == 0
assert pair(H, Dstrict) == 304

# Exact exceptional lattice: 48 disjoint A1 (-2)-curves and H-orthogonal.
exceptional_gram_minus2_identity = True
for i in range(92, 140):
    assert pair(H, known[i]) == 0
    for j in range(92, 140):
        val = pair(known[i], known[j])
        expected = -2 if i == j else 0
        if val != expected:
            exceptional_gram_minus2_identity = False
            raise SystemExit(f"exceptional Gram regression at {i+1},{j+1}: {val} != {expected}")

# D_exc coordinates are therefore unique among exceptional divisors/classes.
exc_square = pair(Dexc, Dexc)
assert exc_square == -2 * sum(v * v for v in exc.values())
assert exc_square == -6360

# Mathematical rigidity argument encoded from the exact geometry and lattice:
# H=b^*O(1) with O(1) ample.  Hence an effective remainder R with H.R=0 is
# supported on the exceptional locus.  Its class must equal [D_exc].  Since the
# exceptional classes are independent (-2 I), R=D_exc coefficientwise.  Thus
# every nonzero strict-condition section has the same full divisor D.  The ratio
# of two such sections has divisor zero and is constant.  Conversely D is an
# effective divisor with [D]=19H, so it gives a nonzero section of O(19H).
strict_space_dimension = 1

out = {
    "schema": "STAGE35_EX_GOAL4AJ_DENOMINATOR_RESIDUAL_RIGIDITY_DIAGNOSTIC_V1",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_SHA,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA,
        "q_hyperplane_factor_peel_canonical_sha256": QPEEL_SHA,
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_SHA,
        "active_divisor_condition_packet_run": ACTIVE_RUN,
        "active_divisor_condition_packet_job": ACTIVE_JOB,
        "a1_residual_jet_canonical_sha256": A1_SHA,
        "retained140_locator_canonical_sha256": LOCATOR_SHA,
        "failed_direct_strict_intersection_run": FAILED_STRICT_RUN,
        "failed_direct_strict_intersection_job": FAILED_STRICT_JOB,
    },
    "denominator_residual_homogeneous_degree": 19,
    "surface_hyperplane_square": H2,
    "full_residual_exact_picard_class_19H": True,
    "full_residual_effective": True,
    "full_residual_q_defined_v4_exact": True,
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
    "exceptional_gram_is_minus2_identity": exceptional_gram_minus2_identity,
    "exceptional_classes_independent": True,
    "H_is_pullback_of_canonical_model_ample_O1": True,
    "effective_H_zero_remainder_supported_on_exceptional_locus": True,
    "strict_condition_remainder_class_equals_exact_exceptional_packet": True,
    "strict_condition_remainder_unique_effective_divisor": True,
    "any_two_nonzero_strict_condition_sections_have_same_divisor": True,
    "strict_condition_space_dimension_upper_bound": 1,
    "nonzero_strict_condition_section_exists_from_effective_19H_divisor": True,
    "strict_condition_space_dimension_exact": strict_space_dimension,
    "denominator_residual_section_line_unique_up_to_scalar": True,
    "q_rational_section_line_descends": True,
    "a1_exceptional_orders_for_unique_divisor_forced": True,
    "direct_singular_intersection_required_for_dimension_proof": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_denominator_polynomial_materialized": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_DEN_RIGIDITY_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_DEN_RIGIDITY=PASS")
