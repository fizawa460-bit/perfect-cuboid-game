#!/usr/bin/env python3
"""Goal4AJ diagnostic: iterative high-m strict symbolic-power scaling, generation 2.

Generation 1 established that direct expansion followed by singular-locus
saturation is mathematically correct on the representative strict primes, but
hit a representation/resource wall for C1[2] at multiplicity 21:
C2[37], m=13 completed, whereas the direct L^21 construction timed out.

This generation computes the same symbolic powers incrementally on the normal
cuboid canonical surface:

    S_1 = I_S + P,
    S_k = sat(I_S + S_{k-1} P, Sing(S)).

Away from the isolated A1 singular locus the height-one strict prime P is
Cartier on the regular surface, so multiplication gives the next ordinary
power locally; saturation removes only singular-locus-supported discrepancy.
The final ideal is re-saturated and compared exactly for stability.

Cases are actual maxima needed by the active post-Q-peel packet:
  * numerator C1[2], multiplicity 21;
  * denominator/numerator C2 representative C2[37], multiplicity 13;
  * C3 representative C3[58], multiplicity 9.

Diagnostic only: no global section is solved and no literal F_B is produced.
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
ACTIVE_PACKET_CANONICAL_SHA256 = "59d22df424c22c1a62fe38feff64ed17cc858626b822887515c04edfac4e34e6"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
STOLL_CUBOIDS_BLOB_SHA1 = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
GEN1_RUN = 34094423360
GEN1_JOB = 101655068731

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_CANONICAL_SHA256
assert ai["homogeneous_realization"]["achieved_homogeneous_degree"] == 31
assert ai["homogeneous_realization"]["explicit_F_B_materialized"] is False

CASES = [
    {
        "name": "NUMERATOR_C1_INDEX2_M21",
        "family": "C1",
        "strict_index_1based": 2,
        "multiplicity": 21,
        "coefficient_field_needed": "Q",
        "ideal": "ideal P=a1,a2+b3,a3+b2,b1-c;",
        "timeout_seconds": 540,
    },
    {
        "name": "C2_INDEX37_M13",
        "family": "C2",
        "strict_index_1based": 37,
        "multiplicity": 13,
        "coefficient_field_needed": "Q(i)",
        "ideal": "ideal P=b2,ii*a3+a1,a2+c;",
        "timeout_seconds": 360,
    },
    {
        "name": "C3_INDEX58_M9",
        "family": "C3",
        "strict_index_1based": 58,
        "multiplicity": 9,
        "coefficient_field_needed": "Q(sqrt(2))",
        "ideal": "ideal P=a2-a3,ss*a2+b1,b2-b3;",
        "timeout_seconds": 300,
    },
]

COMMON = r'''
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
ideal surf=
  a1^2+a2^2-b3^2,
  a2^2+a3^2-b1^2,
  a1^2+a3^2-b2^2,
  a1^2+a2^2+a3^2-c^2;
matrix J=jacob(surf);
ideal Sing=minor(J,4);
proc contained(ideal A, ideal B)
{
  ideal G=std(B);
  int j;
  for (j=1; j<=size(A); j++)
  {
    if (reduce(A[j],G)!=0) { return(0); }
  }
  return(1);
}
proc equalideal(ideal A, ideal B)
{
  return(contained(A,B)==1 && contained(B,A)==1);
}
'''


def run_case(case: dict) -> dict:
    m = int(case["multiplicity"])
    body = COMMON + "\n" + case["ideal"] + f'''
if (dim(std(surf+P))!=2) {{ ERROR("selected strict curve height mismatch"); }}
ideal Sk=std(surf+P);
ideal Candidate;
list SatL;
ideal Sn;
int kk;
print("GOAL4AJ_ITERATIVE_STEP=1:"+string(size(Sk)));
for (kk=2; kk<={m}; kk++)
{{
  Candidate=surf+Sk*P;
  SatL=sat(Candidate,Sing);
  Sn=std(SatL[1]);
  if (contained(Candidate,Sn)!=1) {{ ERROR("iterative candidate not contained in saturation"); }}
  Sk=Sn;
  print("GOAL4AJ_ITERATIVE_STEP="+string(kk)+":"+string(size(Sk)));
}}
list StableL=sat(Sk,Sing);
ideal Stable=std(StableL[1]);
if (equalideal(Sk,Stable)!=1) {{ ERROR("final iterative symbolic power not saturation-stable"); }}
print("GOAL4AJ_ITERATIVE_FINAL_GENERATORS="+string(size(Sk)));
print("GOAL4AJ_ITERATIVE_HIGHM_CASE=PASS");
quit;
'''
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "iterative-highm.sing"
        p.write_text(body, encoding="utf-8")
        t0 = time.perf_counter()
        try:
            cp = subprocess.run(
                ["Singular", "-q", str(p)],
                text=True,
                capture_output=True,
                timeout=int(case["timeout_seconds"]),
            )
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            elapsed = time.perf_counter() - t0
            stdout = exc.stdout or ""
            if isinstance(stdout, bytes):
                stdout = stdout.decode("utf-8", errors="replace")
            completed = []
            for line in stdout.splitlines():
                if line.startswith("GOAL4AJ_ITERATIVE_STEP="):
                    k, g = line.split("=", 1)[1].split(":", 1)
                    completed.append([int(k), int(g)])
            print(f"GOAL4AJ_ITERATIVE_{case['name']}_TIMEOUT_STDOUT=" + json.dumps(stdout[-12000:]))
            return {
                "name": case["name"],
                "family": case["family"],
                "strict_index_1based": case["strict_index_1based"],
                "target_multiplicity": m,
                "coefficient_field_needed": case["coefficient_field_needed"],
                "timed_out": True,
                "elapsed_seconds": round(elapsed, 3),
                "returncode": None,
                "error_text_present": False,
                "completion_marker_present": False,
                "completed_multiplicity": completed[-1][0] if completed else 0,
                "per_step_generator_counts": completed,
                "final_generator_count": completed[-1][1] if completed else None,
            }
    elapsed = time.perf_counter() - t0
    stdout = cp.stdout
    stderr = cp.stderr
    print(f"GOAL4AJ_ITERATIVE_{case['name']}_STDOUT=" + json.dumps(stdout[-16000:]))
    if stderr:
        print(f"GOAL4AJ_ITERATIVE_{case['name']}_STDERR=" + json.dumps(stderr[-12000:]))
    error_text = any(s in stdout.lower() for s in (
        "error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"
    ))
    steps = []
    final_gens = None
    for line in stdout.splitlines():
        if line.startswith("GOAL4AJ_ITERATIVE_STEP="):
            k, g = line.split("=", 1)[1].split(":", 1)
            steps.append([int(k), int(g)])
        elif line.startswith("GOAL4AJ_ITERATIVE_FINAL_GENERATORS="):
            final_gens = int(line.split("=", 1)[1])
    return {
        "name": case["name"],
        "family": case["family"],
        "strict_index_1based": case["strict_index_1based"],
        "target_multiplicity": m,
        "coefficient_field_needed": case["coefficient_field_needed"],
        "timed_out": timed_out,
        "elapsed_seconds": round(elapsed, 3),
        "returncode": cp.returncode,
        "error_text_present": error_text,
        "completion_marker_present": "GOAL4AJ_ITERATIVE_HIGHM_CASE=PASS" in stdout,
        "completed_multiplicity": steps[-1][0] if steps else 0,
        "per_step_generator_counts": steps,
        "final_generator_count": final_gens,
    }

rows = [run_case(c) for c in CASES]
all_pass = all(
    not r["timed_out"]
    and r["returncode"] == 0
    and not r["error_text_present"]
    and r["completion_marker_present"]
    and r["completed_multiplicity"] == r["target_multiplicity"]
    and r["final_generator_count"] is not None
    for r in rows
)

out = {
    "schema": "STAGE35_EX_GOAL4AJ_HIGH_M_SYMBOLIC_POWER_SCALING_DIAGNOSTIC_V2",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_CANONICAL_SHA256,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA256,
        "q_hyperplane_factor_peel_canonical_sha256": QPEEL_CANONICAL_SHA256,
        "strict_symbolic_power_preflight_canonical_sha256": STRICT_PREFLIGHT_CANONICAL_SHA256,
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_PACKET_CANONICAL_SHA256,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "stoll_cuboids_magma_blob_sha1": STOLL_CUBOIDS_BLOB_SHA1,
        "generation1_resource_wall_run": GEN1_RUN,
        "generation1_resource_wall_job": GEN1_JOB,
    },
    "generation1_boundary": {
        "C1_index2_m21_direct_power_timed_out_at_seconds": 600,
        "C2_index37_m13_direct_power_passed": True,
        "C2_index37_m13_direct_elapsed_seconds": 122.5,
        "C2_index37_m13_direct_ordinary_generator_count": 109,
        "C2_index37_m13_direct_symbolic_generator_count": 22,
        "mathematical_obstruction_from_generation1": False,
        "classification": "REPRESENTATION_OR_RESOURCE_WALL_ONLY",
    },
    "constructor": "S1=I_S+P; Sk=saturation(I_S+S_(k-1)*P,JacobianSingularLocus)",
    "cases": rows,
    "actual_packet_family_maxima_represented": True,
    "iterative_high_m_symbolic_power_lane_operational": all_pass,
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
out["canonical_sha256"] = hashlib.sha256(
    json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
print("GOAL4AJ_ITERATIVE_HIGH_M_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_ITERATIVE_HIGH_M=" + ("PASS" if all_pass else "RESOURCE_OR_API_WALL"))
if not all_pass:
    raise SystemExit("Goal4AJ iterative high-m symbolic-power scaling did not complete; no mathematical obstruction credit")
