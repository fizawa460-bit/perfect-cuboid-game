#!/usr/bin/env python3
"""Goal4AJ diagnostic: exact denominator-residual strict symbolic intersection.

Build the 22 active post-Q-peel strict-curve symbolic-power conditions for the
degree-19 denominator residual over Q(i,sqrt(2)), intersect them exactly in the
four-quadric canonical ring, and measure the surviving degree-19 graded space.

This leaf intentionally stops before the 44 A1 exceptional jet conditions.
Even if the strict space is one-dimensional and a candidate polynomial is
visible, it does NOT grant literal denominator, literal F_B, local evaluation,
Brauer-Manin, E1, or theorem credit.
"""
from __future__ import annotations

from math import comb
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"

ACTIVE_PACKET_CANONICAL_SHA256 = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
ACTIVE_PACKET_RUN = 34095500391
ACTIVE_PACKET_JOB = 101658235698
A1_RESIDUAL_CANONICAL_SHA256 = "b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66"
A1_RESIDUAL_RUN = 34097042822
A1_RESIDUAL_JOB = 101663106764
GOAL4AI_CANONICAL_SHA256 = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
DIVISOR_PACKET_SHA256 = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
QPEEL_CANONICAL_SHA256 = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
STRICT_PREFLIGHT_CANONICAL_SHA256 = "43aa7374e83c5f245997e0b7cbdb67b27d1bc045d7606b9544b6cbc7b2e31f69"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
MODULE_HOM_PASS_RUN = 34088545584
MODULE_HOM_PASS_JOB = 101637261382
STOLL_CUBOIDS_BLOB_SHA1 = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

DEN_STRICT = {1: 3, 8: 3, 9: 3, 11: 2, 16: 1, 17: 3, 21: 2, 24: 1, 25: 7, 26: 9, 28: 1, 29: 1, 31: 9, 32: 7, 33: 2, 35: 2, 37: 13, 39: 13, 58: 9, 60: 9, 65: 1, 67: 1}
PROCESS_ORDER = [37, 39, 26, 31, 58, 60, 25, 32, 1, 8, 9, 17, 11, 21, 33, 35, 16, 24, 28, 29, 65, 67]
assert len(DEN_STRICT) == 22
assert sum(DEN_STRICT.values()) == 102
assert max(DEN_STRICT.values()) == 13
assert set(DEN_STRICT) == set(PROCESS_ORDER)

# Re-execute the compact packet cheaply and require the exact canonical lock.
ap = subprocess.run(
    ["python", "-B", str(ACTIVE)], text=True, capture_output=True, timeout=60
)
if ap.returncode != 0:
    raise SystemExit("active-condition source replay failed")
line = next(
    (x for x in ap.stdout.splitlines() if x.startswith("GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON=")),
    None,
)
if line is None:
    raise SystemExit("active-condition JSON marker missing")
active = json.loads(line.split("=", 1)[1])
if active.get("canonical_sha256") != ACTIVE_PACKET_CANONICAL_SHA256:
    raise SystemExit("active-condition canonical SHA moved")
got = {int(k): int(v) for k, v in active["denominator_residual"]["strict_multiplicities_1based"].items()}
if got != DEN_STRICT:
    raise SystemExit("denominator strict multiplicity packet moved")
if active["denominator_residual"]["homogeneous_degree_after_q_peel"] != 19:
    raise SystemExit("denominator residual degree moved")

SINGULAR = r"""
option(redSB);
LIB "elim.lib";
ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;
minpoly=u^4+1;
number ii=u^2;
number ss=u-u^3;
number isv=ii*ss;
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

proc sympow(ideal P, int m)
{
  ideal Sk=std(surf+P);
  ideal Candidate;
  ideal Sn;
  list SatL;
  int kk;
  for (kk=2; kk<=m; kk++)
  {
    Candidate=surf+Sk*P;
    SatL=sat(Candidate,Sing);
    Sn=std(SatL[1]);
    Sk=Sn;
  }
  list StableL=sat(Sk,Sing);
  ideal Stable=std(StableL[1]);
  if (equalideal(Sk,Stable)!=1) { ERROR("symbolic power not saturation-stable"); }
  return(Sk);
}

ideal Current=surf;
ideal P;
ideal T;

// retained strict curve 37, target multiplicity 13
P=b2,ii*a3+1*a1,a2+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 37 height mismatch"); }
T=sympow(P,13);
Current=intersect(Current,T);
Current=std(Current);
intvec h1=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=1:37:13:"+string(size(Current))+":"+string(h1));

// retained strict curve 39, target multiplicity 13
P=b2,ii*a3-1*a1,a2+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 39 height mismatch"); }
T=sympow(P,13);
Current=intersect(Current,T);
Current=std(Current);
intvec h2=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=2:39:13:"+string(size(Current))+":"+string(h2));

// retained strict curve 26, target multiplicity 9
P=c,ii*a1-1*b1,ii*a2+1*b2,ii*a3+1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 26 height mismatch"); }
T=sympow(P,9);
Current=intersect(Current,T);
Current=std(Current);
intvec h3=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=3:26:9:"+string(size(Current))+":"+string(h3));

// retained strict curve 31, target multiplicity 9
P=c,ii*a1+1*b1,ii*a2-1*b2,ii*a3-1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 31 height mismatch"); }
T=sympow(P,9);
Current=intersect(Current,T);
Current=std(Current);
intvec h4=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=4:31:9:"+string(size(Current))+":"+string(h4));

// retained strict curve 58, target multiplicity 9
P=a2-1*a3,ss*a2+1*b1,b2-1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 58 height mismatch"); }
T=sympow(P,9);
Current=intersect(Current,T);
Current=std(Current);
intvec h5=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=5:58:9:"+string(size(Current))+":"+string(h5));

// retained strict curve 60, target multiplicity 9
P=a2-1*a3,ss*a2-1*b1,b2-1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 60 height mismatch"); }
T=sympow(P,9);
Current=intersect(Current,T);
Current=std(Current);
intvec h6=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=6:60:9:"+string(size(Current))+":"+string(h6));

// retained strict curve 25, target multiplicity 7
P=c,ii*a1+1*b1,ii*a2+1*b2,ii*a3+1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 25 height mismatch"); }
T=sympow(P,7);
Current=intersect(Current,T);
Current=std(Current);
intvec h7=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=7:25:7:"+string(size(Current))+":"+string(h7));

// retained strict curve 32, target multiplicity 7
P=c,ii*a1-1*b1,ii*a2-1*b2,ii*a3-1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 32 height mismatch"); }
T=sympow(P,7);
Current=intersect(Current,T);
Current=std(Current);
intvec h8=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=8:32:7:"+string(size(Current))+":"+string(h8));

// retained strict curve 1, target multiplicity 3
P=a1,a2+1*b3,a3+1*b2,b1+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 1 height mismatch"); }
T=sympow(P,3);
Current=intersect(Current,T);
Current=std(Current);
intvec h9=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=9:1:3:"+string(size(Current))+":"+string(h9));

// retained strict curve 8, target multiplicity 3
P=a1,a2-1*b3,a3-1*b2,b1-1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 8 height mismatch"); }
T=sympow(P,3);
Current=intersect(Current,T);
Current=std(Current);
intvec h10=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=10:8:3:"+string(size(Current))+":"+string(h10));

// retained strict curve 9, target multiplicity 3
P=a2,a3+1*b1,a1+1*b3,b2+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 9 height mismatch"); }
T=sympow(P,3);
Current=intersect(Current,T);
Current=std(Current);
intvec h11=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=11:9:3:"+string(size(Current))+":"+string(h11));

// retained strict curve 17, target multiplicity 3
P=a3,a1+1*b2,a2+1*b1,b3+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 17 height mismatch"); }
T=sympow(P,3);
Current=intersect(Current,T);
Current=std(Current);
intvec h12=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=12:17:3:"+string(size(Current))+":"+string(h12));

// retained strict curve 11, target multiplicity 2
P=a2,a3+1*b1,a1-1*b3,b2+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 11 height mismatch"); }
T=sympow(P,2);
Current=intersect(Current,T);
Current=std(Current);
intvec h13=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=13:11:2:"+string(size(Current))+":"+string(h13));

// retained strict curve 21, target multiplicity 2
P=a3,a1-1*b2,a2+1*b1,b3+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 21 height mismatch"); }
T=sympow(P,2);
Current=intersect(Current,T);
Current=std(Current);
intvec h14=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=14:21:2:"+string(size(Current))+":"+string(h14));

// retained strict curve 33, target multiplicity 2
P=b1,ii*a2+1*a3,a1+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 33 height mismatch"); }
T=sympow(P,2);
Current=intersect(Current,T);
Current=std(Current);
intvec h15=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=15:33:2:"+string(size(Current))+":"+string(h15));

// retained strict curve 35, target multiplicity 2
P=b1,ii*a2-1*a3,a1+1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 35 height mismatch"); }
T=sympow(P,2);
Current=intersect(Current,T);
Current=std(Current);
intvec h16=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=16:35:2:"+string(size(Current))+":"+string(h16));

// retained strict curve 16, target multiplicity 1
P=a2,a3-1*b1,a1-1*b3,b2-1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 16 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h17=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=17:16:1:"+string(size(Current))+":"+string(h17));

// retained strict curve 24, target multiplicity 1
P=a3,a1-1*b2,a2-1*b1,b3-1*c;
if (dim(std(surf+P))!=2) { ERROR("strict curve 24 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h18=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=18:24:1:"+string(size(Current))+":"+string(h18));

// retained strict curve 28, target multiplicity 1
P=c,ii*a1-1*b1,ii*a2-1*b2,ii*a3+1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 28 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h19=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=19:28:1:"+string(size(Current))+":"+string(h19));

// retained strict curve 29, target multiplicity 1
P=c,ii*a1+1*b1,ii*a2+1*b2,ii*a3-1*b3;
if (dim(std(surf+P))!=2) { ERROR("strict curve 29 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h20=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=20:29:1:"+string(size(Current))+":"+string(h20));

// retained strict curve 65, target multiplicity 1
P=a3-1*a1,ss*a3+1*b2,b3+1*b1;
if (dim(std(surf+P))!=2) { ERROR("strict curve 65 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h21=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=21:65:1:"+string(size(Current))+":"+string(h21));

// retained strict curve 67, target multiplicity 1
P=a3-1*a1,ss*a3-1*b2,b3+1*b1;
if (dim(std(surf+P))!=2) { ERROR("strict curve 67 height mismatch"); }
T=sympow(P,1);
Current=intersect(Current,T);
Current=std(Current);
intvec h22=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_STEP=22:67:1:"+string(size(Current))+":"+string(h22));

list FinalSatL=sat(Current,Sing);
ideal FinalSat=std(FinalSatL[1]);
if (equalideal(Current,FinalSat)!=1) { ERROR("full strict intersection not saturation-stable"); }
ideal SurfStd=std(surf);
intvec HS=hilb(SurfStd,1);
intvec HF=hilb(Current,1);
print("GOAL4AJ_DEN_STRICT_SURFACE_HILB1="+string(HS));
print("GOAL4AJ_DEN_STRICT_FINAL_HILB1="+string(HF));
print("GOAL4AJ_DEN_STRICT_FINAL_GENERATORS="+string(size(Current)));

int jj;
int cc=0;
poly q;
for (jj=1; jj<=size(Current); jj++)
{
  q=reduce(Current[jj],SurfStd);
  if (q!=0 && deg(q)==19 && cc<3)
  {
    cc++;
    print("GOAL4AJ_DEN_STRICT_CANDIDATE_"+string(cc)+"="+string(q));
  }
}
print("GOAL4AJ_DEN_STRICT_CANDIDATE_COUNT="+string(cc));
print("GOAL4AJ_DEN_STRICT_INTERSECTION=PASS");
quit;
"""

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-den-strict.sing"
    src.write_text(SINGULAR, encoding="utf-8")
    try:
        cp = subprocess.run(
            ["Singular", "-q", str(src)],
            text=True,
            capture_output=True,
            timeout=1260,
        )
        timed_out = False
        stdout = cp.stdout
        stderr = cp.stderr
        rc = cp.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        rc = None

raw_sha = hashlib.sha256(stdout.encode()).hexdigest()
error_text = any(s in stdout.lower() for s in (
    "error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"
))

def marker(prefix: str):
    return next((x.split("=", 1)[1] for x in stdout.splitlines() if x.startswith(prefix+"=")), None)

def parse_iv(text: str | None) -> list[int]:
    if text is None:
        return []
    return [int(x.strip()) for x in text.split(",") if x.strip()]

def hf_from_first_hilb(v: list[int], d: int, nvars: int = 7) -> int:
    if not v:
        raise ValueError("empty hilbert numerator")
    coeffs = v[:-1]  # Singular: final intvec entry is stdhilb metadata.
    return sum(
        a * comb(d-j+nvars-1, nvars-1)
        for j, a in enumerate(coeffs)
        if a and d >= j
    )

step_rows = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_DEN_STRICT_STEP="):
        payload = x.split("=", 1)[1]
        p = payload.split(":", 4)
        if len(p) == 5:
            step_rows.append({
                "step": int(p[0]),
                "strict_index_1based": int(p[1]),
                "multiplicity": int(p[2]),
                "standard_basis_generator_count": int(p[3]),
                "hilb1": parse_iv(p[4]),
            })

hs = parse_iv(marker("GOAL4AJ_DEN_STRICT_SURFACE_HILB1"))
hf = parse_iv(marker("GOAL4AJ_DEN_STRICT_FINAL_HILB1"))
surface_hf19 = hf_from_first_hilb(hs, 19) if hs else None
quotient_hf19 = hf_from_first_hilb(hf, 19) if hf else None
strict_space_dim = (
    surface_hf19 - quotient_hf19
    if surface_hf19 is not None and quotient_hf19 is not None
    else None
)
candidates = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_DEN_STRICT_CANDIDATE_") and not x.startswith("GOAL4AJ_DEN_STRICT_CANDIDATE_COUNT"):
        candidates.append(x.split("=", 1)[1])
candidate_bytes = sum(len(x.encode()) for x in candidates)

completed = (
    not timed_out
    and rc == 0
    and not error_text
    and len(step_rows) == 22
    and "GOAL4AJ_DEN_STRICT_INTERSECTION=PASS" in stdout
    and surface_hf19 == 2744
    and strict_space_dim is not None
    and strict_space_dim >= 0
)

out = {
    "schema": "STAGE35_EX_GOAL4AJ_DENOMINATOR_STRICT_INTERSECTION_DIAGNOSTIC_V1",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_CANONICAL_SHA256,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA256,
        "q_hyperplane_factor_peel_canonical_sha256": QPEEL_CANONICAL_SHA256,
        "strict_symbolic_power_preflight_canonical_sha256": STRICT_PREFLIGHT_CANONICAL_SHA256,
        "active_divisor_condition_packet_canonical_sha256": ACTIVE_PACKET_CANONICAL_SHA256,
        "active_divisor_condition_packet_run": ACTIVE_PACKET_RUN,
        "active_divisor_condition_packet_job": ACTIVE_PACKET_JOB,
        "a1_residual_jet_canonical_sha256": A1_RESIDUAL_CANONICAL_SHA256,
        "a1_residual_jet_run": A1_RESIDUAL_RUN,
        "a1_residual_jet_job": A1_RESIDUAL_JOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "module_hom_pass_run": MODULE_HOM_PASS_RUN,
        "module_hom_pass_job": MODULE_HOM_PASS_JOB,
        "stoll_cuboids_magma_blob_sha1": STOLL_CUBOIDS_BLOB_SHA1,
    },
    "coefficient_field_used_for_split_strict_conditions": "Q(i,sqrt(2))",
    "denominator_residual_homogeneous_degree": 19,
    "active_strict_curve_count": 22,
    "active_strict_total_multiplicity": 102,
    "active_strict_max_multiplicity": 13,
    "process_order_1based": PROCESS_ORDER,
    "singular_timed_out": timed_out,
    "singular_returncode": rc,
    "singular_error_text_present": error_text,
    "completed_strict_curve_intersections": len(step_rows),
    "surface_degree19_dimension": surface_hf19,
    "quotient_by_strict_intersection_degree19_dimension": quotient_hf19,
    "strict_condition_section_space_degree19_dimension": strict_space_dim,
    "final_standard_basis_generator_count": int(marker("GOAL4AJ_DEN_STRICT_FINAL_GENERATORS")) if marker("GOAL4AJ_DEN_STRICT_FINAL_GENERATORS") else None,
    "degree19_candidate_standard_basis_count_capped3": len(candidates),
    "degree19_candidate_text_total_bytes": candidate_bytes,
    "degree19_candidates_capped3": candidates if candidate_bytes <= 200000 else [],
    "raw_singular_stdout_sha256": raw_sha,
    "strict_symbolic_power_intersection_completed": completed,
    "a1_exceptional_jet_conditions_imposed": False,
    "global_section_intersection_solved": False,
    "degree19_denominator_residual_section_solved": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_numerator_coefficients_materialized": False,
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
print("GOAL4AJ_DEN_STRICT_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_DEN_STRICT=" + ("PASS" if completed else "RESOURCE_OR_IMPLEMENTATION_WALL"))
if not completed:
    if stderr:
        print("GOAL4AJ_DEN_STRICT_STDERR=" + json.dumps(stderr[-12000:]))
    raise SystemExit("Goal4AJ denominator strict intersection did not complete; no mathematical obstruction credit")
