#!/usr/bin/env python3
"""Goal4AJ gen17: degree-31 numerator strict kernel over F_32009.

The denominator route is now literal over Q. Goal4AJ still requires a literal
numerator. This diagnostic reuses the exact retained92 strict-curve locator and
the active numerator divisor packet, imposes the 27 numerator strict symbolic
power conditions, and keeps only homogeneous standard-basis generators of
degree <=31 after each exact symbolic power and exact ideal intersection.

For a homogeneous ideal, generators of degree >31 cannot affect its degree-31
piece. Hence the truncation preserves the requested graded section space while
avoiding irrelevant high-degree Groebner growth. This is modular diagnostic
work only: exceptional A1 coefficients, Q lift, literal numerator, F_B, local
Brauer evaluation, E1, Stage35, theorem, receiver, and endpoint credit remain
false.
"""
from __future__ import annotations

from contextlib import redirect_stdout
from math import comb
import hashlib
import io
import json
import math
import runpy
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"
DEN31_NOTE = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-denominator-source-lock.md"

LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
STRICT_PACKET_SHA256 = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
ACTIVE_BLOB = "20da16902171b267294acee0f3b80997d8fd5246"
ACTIVE_CANONICAL = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"
DEN31_CANONICAL = "09683e1623b6c57ba1f96864fbcc47e51a878f032273a1da74327fa1b6b9122f"
DEN31_RUN = 34182361333
DEN31_JOB = 101923866397
FIELD_PRIME = 32009
I_ROOT = 10754
SQRT2_ROOT = 8047
DEGREE = 31
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")

NUM_STRICT = {
    2:21,3:1,4:1,5:1,6:1,7:21,9:3,10:10,12:10,13:18,14:4,15:12,
    16:1,17:3,18:12,19:12,22:12,23:10,24:1,27:1,30:1,38:13,40:13,
    58:9,60:9,65:1,67:1,
}
PROCESS_ORDER = sorted(NUM_STRICT, key=lambda i: (-NUM_STRICT[i], i))
assert PROCESS_ORDER == [2,7,13,38,40,15,18,19,22,10,12,23,58,60,14,9,17,3,4,5,6,16,24,27,30,65,67]
assert len(NUM_STRICT) == 27 and sum(NUM_STRICT.values()) == 202 and max(NUM_STRICT.values()) == 21


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(LOCATOR) == LOCATOR_BLOB
assert git_blob(ACTIVE) == ACTIVE_BLOB
assert git_blob(DEN31_NOTE) == DEN31_NOTE_BLOB
assert pow(I_ROOT, 2, FIELD_PRIME) == FIELD_PRIME - 1
assert pow(SQRT2_ROOT, 2, FIELD_PRIME) == 2

# Replay compact source locks. Locator also exposes exact retained92 equations.
buf = io.StringIO()
with redirect_stdout(buf):
    lns = runpy.run_path(str(LOCATOR))
locator_out = lns["out"]
curves = lns["curves"]
assert locator_out["canonical_sha256"] == LOCATOR_CANONICAL
assert locator_out["strict_curve_packet_sha256"] == STRICT_PACKET_SHA256
assert len(curves) == 92

buf = io.StringIO()
with redirect_stdout(buf):
    ans = runpy.run_path(str(ACTIVE))
active = ans["out"]
assert active["canonical_sha256"] == ACTIVE_CANONICAL
got = {int(k): int(v) for k, v in active["numerator"]["strict_multiplicities_1based"].items()}
assert got == NUM_STRICT
assert active["numerator"]["homogeneous_degree_after_q_peel"] == 31


def frac_mod(x) -> int:
    return (int(x.numerator) % FIELD_PRIME) * pow(int(x.denominator) % FIELD_PRIME, -1, FIELD_PRIME) % FIELD_PRIME


def k_mod(x) -> int:
    a, b, c, d = (frac_mod(q) for q in x.coeffs())
    return (a + b * I_ROOT + c * SQRT2_ROOT + d * I_ROOT * SQRT2_ROOT) % FIELD_PRIME


def centered(v: int) -> int:
    v %= FIELD_PRIME
    return v - FIELD_PRIME if v > FIELD_PRIME // 2 else v


def row_expr(row) -> str:
    terms = []
    for name, x in zip(NAMES, row):
        z = centered(k_mod(x))
        if z:
            terms.append(f"{z}*{name}")
    if not terms:
        raise SystemExit("zero retained strict linear equation")
    return "+".join(terms).replace("+-", "-")


sparts = [r'''
option(redSB);
LIB "elim.lib";
ring r=32009,(a1,a2,a3,b1,b2,b3,c),dp;
number ii=10754;
number ss=8047;
if (ii^2+1!=0) { ERROR("finite-field i root mismatch"); }
if (ss^2-2!=0) { ERROR("finite-field sqrt2 root mismatch"); }
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
proc trunc31(ideal A)
{
  ideal G=std(A);
  ideal T=0;
  int j;
  int k=0;
  for (j=1; j<=size(G); j++)
  {
    if (G[j]!=0 && deg(G[j])<=31)
    {
      k++;
      T[k]=G[j];
    }
  }
  return(std(T));
}
ideal NumAcc=1;
ideal P;
ideal T;
''']

for step, idx in enumerate(PROCESS_ORDER, 1):
    e = NUM_STRICT[idx]
    eqs = ",".join(row_expr(r) for r in curves[idx - 1])
    sparts.append(f'''// numerator retained strict curve {idx}, multiplicity {e}
P={eqs};
if (dim(std(surf+P))!=2) {{ ERROR("numerator strict curve {idx} height mismatch"); }}
T=trunc31(sympow(P,{e}));
NumAcc=trunc31(intersect(NumAcc,T));
print("GOAL4AJ_NUM31_TRUNC_STEP={step}:{idx}:{e}:"+string(size(NumAcc)));
''')

sparts.append(r'''
ideal SurfStd=std(surf);
intvec HS=hilb(SurfStd,1);
intvec HF=hilb(NumAcc,1);
print("GOAL4AJ_NUM31_TRUNC_SURFACE_HILB1="+string(HS));
print("GOAL4AJ_NUM31_TRUNC_FINAL_HILB1="+string(HF));
print("GOAL4AJ_NUM31_TRUNC_FINAL_GENERATORS="+string(size(NumAcc)));
int jj;
int numCC=0;
int numMinDeg=999;
poly q;
for (jj=1; jj<=size(NumAcc); jj++)
{
  q=reduce(NumAcc[jj],SurfStd);
  if (q!=0)
  {
    if (deg(q)<numMinDeg) { numMinDeg=deg(q); }
    if (deg(q)==31 && numCC<3)
    {
      numCC++;
      print("GOAL4AJ_NUM31_TRUNC_CANDIDATE_"+string(numCC)+"="+string(q));
    }
  }
}
print("GOAL4AJ_NUM31_TRUNC_MIN_NONSURFACE_GENERATOR_DEGREE="+string(numMinDeg));
print("GOAL4AJ_NUM31_TRUNC_CANDIDATE_COUNT="+string(numCC));
print("GOAL4AJ_NUM31_TRUNC_STRICT_KERNEL=PASS");
quit;
''')
singular_program = "\n".join(sparts)

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-num31-trunc-gen17.sing"
    src.write_text(singular_program, encoding="utf-8")
    try:
        cp = subprocess.run(["Singular", "-q", str(src)], text=True, capture_output=True, timeout=2100)
        timed_out = False
        stdout, stderr, rc = cp.stdout, cp.stderr, cp.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        rc = None


def marker(prefix: str):
    return next((x.split("=", 1)[1] for x in stdout.splitlines() if x.startswith(prefix + "=")), None)


def parse_iv(text: str | None) -> list[int]:
    if text is None:
        return []
    return [int(x.strip()) for x in text.split(",") if x.strip()]


def hf_from_first_hilb(v: list[int], d: int, nvars: int = 7) -> int:
    if not v:
        raise ValueError("empty Hilbert numerator")
    return sum(
        a * comb(d - j + nvars - 1, nvars - 1)
        for j, a in enumerate(v[:-1])
        if a and d >= j
    )

step_rows = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_NUM31_TRUNC_STEP="):
        p = x.split("=", 1)[1].split(":")
        if len(p) == 4:
            step_rows.append({
                "step": int(p[0]),
                "strict_index_1based": int(p[1]),
                "multiplicity": int(p[2]),
                "standard_basis_generator_count_after_truncation": int(p[3]),
            })

hs = parse_iv(marker("GOAL4AJ_NUM31_TRUNC_SURFACE_HILB1"))
hf = parse_iv(marker("GOAL4AJ_NUM31_TRUNC_FINAL_HILB1"))
surface_hf31 = hf_from_first_hilb(hs, DEGREE) if hs else None
quotient_hf31 = hf_from_first_hilb(hf, DEGREE) if hf else None
strict_space_dim = (
    surface_hf31 - quotient_hf31
    if surface_hf31 is not None and quotient_hf31 is not None
    else None
)

candidates = []
for x in stdout.splitlines():
    if x.startswith("GOAL4AJ_NUM31_TRUNC_CANDIDATE_") and not x.startswith("GOAL4AJ_NUM31_TRUNC_CANDIDATE_COUNT"):
        candidates.append(x.split("=", 1)[1])
candidate_hashes = [hashlib.sha256(x.encode()).hexdigest() for x in candidates]
candidate_bytes = [len(x.encode()) for x in candidates]
error_text = any(
    t in stdout.lower()
    for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign")
)
completed = (
    not timed_out and rc == 0 and not error_text
    and len(step_rows) == len(PROCESS_ORDER)
    and "GOAL4AJ_NUM31_TRUNC_STRICT_KERNEL=PASS" in stdout
    and strict_space_dim is not None and strict_space_dim >= 0
)
if not completed:
    if stderr:
        print("GOAL4AJ_NUM31_TRUNC_GEN17_STDERR=" + json.dumps(stderr[-8000:]))
    print("GOAL4AJ_NUM31_TRUNC_GEN17_STDOUT_TAIL=" + json.dumps(stdout[-12000:]))
    raise SystemExit("Goal4AJ numerator degree31 truncated strict kernel did not complete")

route = (
    "NUMERATOR_DEGREE31_STRICT_SPACE_UNIQUE_MODULAR_CANDIDATE"
    if strict_space_dim == 1
    else "NUMERATOR_DEGREE31_STRICT_SPACE_NOT_YET_UNIQUE"
)
out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_TRUNCATED_STRICT_KERNEL_GEN17_DIAGNOSTIC_V1",
    "source_locks": {
        "retained140_locator_blob_sha1": LOCATOR_BLOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL,
        "retained92_strict_curve_packet_sha256": STRICT_PACKET_SHA256,
        "active_condition_packet_blob_sha1": ACTIVE_BLOB,
        "active_condition_packet_canonical_sha256": ACTIVE_CANONICAL,
        "degree31_denominator_source_lock_blob_sha1": DEN31_NOTE_BLOB,
        "degree31_denominator_canonical_sha256": DEN31_CANONICAL,
        "degree31_denominator_run": DEN31_RUN,
        "degree31_denominator_job": DEN31_JOB,
    },
    "coefficient_field": f"F_{FIELD_PRIME}",
    "field_prime": FIELD_PRIME,
    "i_root": I_ROOT,
    "sqrt2_root": SQRT2_ROOT,
    "degree_cap": DEGREE,
    "numerator_strict_condition_count": len(NUM_STRICT),
    "numerator_strict_total_multiplicity": sum(NUM_STRICT.values()),
    "numerator_strict_max_multiplicity": max(NUM_STRICT.values()),
    "process_order": PROCESS_ORDER,
    "step_rows": step_rows,
    "surface_hf_degree31_from_hilb1": surface_hf31,
    "final_quotient_hf_degree31_from_hilb1": quotient_hf31,
    "strict_condition_section_space_degree31_dimension": strict_space_dim,
    "min_nonsurface_generator_degree": int(marker("GOAL4AJ_NUM31_TRUNC_MIN_NONSURFACE_GENERATOR_DEGREE") or -1),
    "degree31_candidate_count_capped3": int(marker("GOAL4AJ_NUM31_TRUNC_CANDIDATE_COUNT") or 0),
    "degree31_candidate_sha256_capped3": candidate_hashes,
    "degree31_candidate_text_bytes_capped3": candidate_bytes,
    "route_result": route,
    "numerator_strict_kernel_completed": True,
    "a1_exceptional_conditions_imposed": False,
    "q_literal_numerator_materialized": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_denominator_coefficients_materialized": True,
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
print("GOAL4AJ_NUM31_TRUNC_GEN17_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_TRUNC_GEN17=DONE", flush=True)
