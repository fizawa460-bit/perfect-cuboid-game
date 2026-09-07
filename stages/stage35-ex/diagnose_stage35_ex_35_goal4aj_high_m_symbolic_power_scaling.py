#!/usr/bin/env python3
"""Goal4AJ diagnostic: bounded high-multiplicity symbolic-power scaling.

Exercise the exact symbolic-power constructor at multiplicities actually
present in the known degree-31 divisor packet / Q-hyperplane residual:
  * numerator C1[2] with multiplicity 21;
  * denominator residual C2[37] with multiplicity 13.

The purpose is operational feasibility only: measure whether the quotient-ring
saturation lane survives the real multiplicities before attempting the global
section intersection. No section coefficients or F_B are produced here.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GOAL4AI = ROOT / "stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence.json"

GOAL4AI_CANONICAL_SHA256 = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
DIVISOR_PACKET_SHA256 = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
QPEEL_CANONICAL_SHA256 = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
STRICT_PREFLIGHT_CANONICAL_SHA256 = "43aa7374e83c5f245997e0b7cbdb67b27d1bc045d7606b9544b6cbc7b2e31f69"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
STOLL_CUBOIDS_BLOB_SHA1 = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_CANONICAL_SHA256
assert ai["homogeneous_realization"]["achieved_homogeneous_degree"] == 31
assert ai["homogeneous_realization"]["explicit_F_B_materialized"] is False

# Exact selected strict components from the retained Stoll ordering.
# C1[2] is index 2: [a1,a2+b3,a3+b2,b1-c].
# C2[37] is index 37: [b2, i*a3+a1, a2+c].
CASES = [
    {
        "name": "NUMERATOR_C1_INDEX2_M21",
        "strict_index_1based": 2,
        "multiplicity": 21,
        "ideal": "ideal L=a1,a2+b3,a3+b2,b1-c;",
        "coefficient_field": "Q",
    },
    {
        "name": "DENOMINATOR_RESIDUAL_C2_INDEX37_M13",
        "strict_index_1based": 37,
        "multiplicity": 13,
        "ideal": "ideal L=b2,ii*a3+a1,a2+c;",
        "coefficient_field": "Q(i)",
    },
]

COMMON = r'''
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
ideal surf=
  a1^2+a2^2-b3^2,
  a2^2+a3^2-b1^2,
  a1^2+a3^2-b2^2,
  a1^2+a2^2+a3^2-c^2;
matrix J=jacob(surf);
ideal Sing=minor(J,4);
proc contained(ideal A,ideal B)
{
  ideal G=std(B);
  int j;
  for (j=1;j<=size(A);j++) { if (reduce(A[j],G)!=0) { return(0); } }
  return(1);
}
'''


def run_case(case: dict) -> dict:
    m = int(case["multiplicity"])
    body = COMMON + "\n" + case["ideal"] + f'''
if (dim(std(surf+L))!=2) {{ ERROR("selected strict curve height mismatch"); }}
ideal Om=surf+L^{m};
print("GOAL4AJ_HIGHM_ORDINARY_GENERATORS="+string(size(Om)));
list SmL=sat(Om,Sing);
ideal Sm=SmL[1];
print("GOAL4AJ_HIGHM_SYMBOLIC_GENERATORS="+string(size(Sm)));
if (contained(Om,Sm)!=1) {{ ERROR("ordinary power not contained in symbolic power"); }}
list StableL=sat(Sm,Sing);
ideal Stable=StableL[1];
if (contained(Sm,Stable)!=1 || contained(Stable,Sm)!=1) {{ ERROR("high-m symbolic power not saturation-stable"); }}
print("GOAL4AJ_HIGHM_CASE=PASS");
quit;
'''
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "highm.sing"
        p.write_text(body, encoding="utf-8")
        t0 = time.perf_counter()
        try:
            cp = subprocess.run(["Singular", "-q", str(p)], text=True, capture_output=True, timeout=600)
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            elapsed = time.perf_counter() - t0
            return {
                "name": case["name"],
                "strict_index_1based": case["strict_index_1based"],
                "multiplicity": m,
                "coefficient_field": case["coefficient_field"],
                "timed_out": True,
                "elapsed_seconds": round(elapsed, 3),
                "returncode": None,
                "error_text_present": False,
                "completion_marker_present": False,
                "ordinary_generator_count": None,
                "symbolic_generator_count": None,
            }
    elapsed = time.perf_counter() - t0
    stdout = cp.stdout
    stderr = cp.stderr
    print(f"GOAL4AJ_HIGHM_{case['name']}_STDOUT=" + json.dumps(stdout[:12000]))
    if stderr:
        print(f"GOAL4AJ_HIGHM_{case['name']}_STDERR=" + json.dumps(stderr[:12000]))
    error_text = any(s in stdout.lower() for s in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    def value(prefix: str):
        for line in stdout.splitlines():
            if line.startswith(prefix):
                return int(line.split("=", 1)[1])
        return None
    return {
        "name": case["name"],
        "strict_index_1based": case["strict_index_1based"],
        "multiplicity": m,
        "coefficient_field": case["coefficient_field"],
        "timed_out": timed_out,
        "elapsed_seconds": round(elapsed, 3),
        "returncode": cp.returncode,
        "error_text_present": error_text,
        "completion_marker_present": "GOAL4AJ_HIGHM_CASE=PASS" in stdout,
        "ordinary_generator_count": value("GOAL4AJ_HIGHM_ORDINARY_GENERATORS="),
        "symbolic_generator_count": value("GOAL4AJ_HIGHM_SYMBOLIC_GENERATORS="),
    }

rows = [run_case(c) for c in CASES]
all_pass = all(
    not r["timed_out"] and r["returncode"] == 0 and not r["error_text_present"]
    and r["completion_marker_present"] and r["ordinary_generator_count"] is not None
    and r["symbolic_generator_count"] is not None
    for r in rows
)
out = {
    "schema": "STAGE35_EX_GOAL4AJ_HIGH_M_SYMBOLIC_POWER_SCALING_DIAGNOSTIC_V1",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_CANONICAL_SHA256,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA256,
        "q_hyperplane_factor_peel_canonical_sha256": QPEEL_CANONICAL_SHA256,
        "strict_symbolic_power_preflight_canonical_sha256": STRICT_PREFLIGHT_CANONICAL_SHA256,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "stoll_cuboids_magma_blob_sha1": STOLL_CUBOIDS_BLOB_SHA1,
    },
    "cases": rows,
    "actual_packet_multiplicities_represented": True,
    "high_m_symbolic_power_lane_operational": all_pass,
    "full_all_strict_packet_built": False,
    "global_section_intersection_solved": False,
    "degree31_numerator_section_solved": False,
    "degree19_denominator_residual_section_solved": False,
    "literal_numerator_coefficients_materialized": False,
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
print("GOAL4AJ_HIGH_M_SYMBOLIC_POWER_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_HIGH_M_SYMBOLIC_POWER=" + ("PASS" if all_pass else "RESOURCE_OR_API_WALL"))
if not all_pass:
    raise SystemExit("Goal4AJ high-m symbolic-power scaling did not complete; no mathematical obstruction credit")
