#!/usr/bin/env python3
"""Goal4AJ gen23: four-prime projective CRT reconstruction of the degree-31 numerator line.

Gen22 matched the complete 5924-monomial support at p=32009,32057,32089 but
balanced rational reconstruction recovered only 5753/5924 coefficients.  This
diagnostic adds the independent split prime p=32233, preserves the exact gen22
projective normalization monomial, combines all coefficient ratios modulo the
four-prime product, and applies uniqueness-safe balanced rational reconstruction.
Only if all 5924 coefficients reconstruct is the first load-bearing strict
condition (#2, multiplicity 21) checked exactly over Q(i,sqrt(2)).

This is diagnostic-only. Even a first-strict PASS does not materialize the Q
numerator until all 27 strict conditions and divisor data are replayed. No
F_B/local/Brauer-Manin/E1/Stage35/theorem/receiver/endpoint credit is granted.
"""
from __future__ import annotations

from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
import math
import runpy
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN22 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_three_prime_projective_crt_gen22.py"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN22_BLOB = "c3a374a4d93b808c2dff93a912ccc1c79895a5bb"
GEN22_RUN = 34191625177
GEN22_JOB = 101950747001
GEN22_CANONICAL = "7199145e16a0f00052499c7bbfea66dfd14323092c15f426a893c2d656fb57c1"
GEN22_ROUTE = "THREE_PRIME_SUPPORT_MATCHED_BALANCED_RATIONAL_RECONSTRUCTION_INCOMPLETE_FOURTH_PRIME_REQUIRED"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
P1, P2, P3 = 32009, 32057, 32089
P4 = 32233
P4_I_ROOT = 3354
P4_SQRT2_ROOT = 12944
MOD123 = P1 * P2 * P3
MODULUS = MOD123 * P4
DEGREE = 31
FIRST_STRICT_INDEX = 2
FIRST_STRICT_MULTIPLICITY = 21
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
BALANCED_BOUND = 700_000_000
assert P4 % 8 == 1
assert pow(P4_I_ROOT, 2, P4) == P4 - 1
assert pow(P4_SQRT2_ROOT, 2, P4) == 2
assert 2 * BALANCED_BOUND * BALANCED_BOUND < MODULUS


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN22) == GEN22_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB

# Replay gen22 exactly. Its globals retain the three-prime support and CRT map.
buf = io.StringIO()
with redirect_stdout(buf):
    n22 = runpy.run_path(str(GEN22))
g22 = n22["out"]
assert g22["canonical_sha256"] == GEN22_CANONICAL
assert g22["route_result"] == GEN22_ROUTE
assert g22["monomial_support_equal_across_three_primes"] is True
assert g22["support_count"] == 5924
assert g22["reconstructed_count"] == 5753
support123 = n22["support12"]
norm_mon = n22["norm_mon"]
crt123 = n22["crt123"]
parse_candidate = n22["parse_candidate"]
crt_pair = n22["crt_pair"]
ratrec = n22["ratrec"]
assert len(support123) == 5924
assert norm_mon == g22["projective_normalization_monomial"]

# Replay the same strict kernel at p4, patching only source-locked split data.
src = GEN17.read_text(encoding="utf-8")
repls = [
    ('DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"', f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'),
    (f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"', f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"'),
    ("FIELD_PRIME = 32009", f"FIELD_PRIME = {P4}"),
    ("I_ROOT = 10754", f"I_ROOT = {P4_I_ROOT}"),
    ("SQRT2_ROOT = 8047", f"SQRT2_ROOT = {P4_SQRT2_ROOT}"),
    ("ring r=32009,(a1,a2,a3,b1,b2,b3,c),dp;", f"ring r={P4},(a1,a2,a3,b1,b2,b3,c),dp;"),
    ("number ii=10754;", f"number ii={P4_I_ROOT};"),
    ("number ss=8047;", f"number ss={P4_SQRT2_ROOT};"),
]
for old, new in repls:
    if src.count(old) != 1:
        raise SystemExit(f"gen23 source patch cardinality mismatch: {old!r}")
    src = src.replace(old, new, 1)

n4 = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen23-p32233]", "exec"), n4)
g4 = n4["out"]
cands4 = n4["candidates"]
assert g4["field_prime"] == P4
assert g4["strict_condition_section_space_degree31_dimension"] == 1
assert len(cands4) == 1
cand4 = cands4[0]
m4 = parse_candidate(cand4, P4)
support4 = sorted(m4)
support_equal = support4 == support123
support_sha123 = hashlib.sha256("\n".join(support123).encode()).hexdigest()
support_sha4 = hashlib.sha256("\n".join(support4).encode()).hexdigest()

if not support_equal or norm_mon not in m4 or m4.get(norm_mon, 0) == 0:
    out = {
        "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_FOUR_PRIME_PROJECTIVE_CRT_GEN23_DIAGNOSTIC_V1",
        "source_locks": {"gen17_script_blob_sha1": GEN17_BLOB, "gen22_script_blob_sha1": GEN22_BLOB,
                         "gen22_run": GEN22_RUN, "gen22_job": GEN22_JOB,
                         "gen22_canonical_sha256": GEN22_CANONICAL, "gen22_route": GEN22_ROUTE},
        "primes": [P1, P2, P3, P4], "four_prime_modulus": MODULUS,
        "first_three_support_count": len(support123), "fourth_support_count": len(support4),
        "first_three_support_sha256": support_sha123, "fourth_support_sha256": support_sha4,
        "monomial_support_equal_across_four_primes": False,
        "projective_normalization_monomial": norm_mon,
        "route_result": "FOURTH_PRIME_SUPPORT_OR_NORMALIZATION_MISMATCH_NO_FOUR_PRIME_RECONSTRUCTION",
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print("GOAL4AJ_NUM31_FOUR_PRIME_CRT_GEN23_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
    print("GOAL4AJ_NUM31_FOUR_PRIME_CRT_GEN23=DONE", flush=True)
    raise SystemExit(0)

lead4 = m4[norm_mon]
nrm4 = {mon: (v * pow(lead4, -1, P4)) % P4 for mon, v in m4.items()}
assert nrm4[norm_mon] == 1
crt1234 = {mon: crt_pair(crt123[mon], MOD123, nrm4[mon], P4) for mon in support123}
recon = {mon: ratrec(v, MODULUS, BALANCED_BOUND, BALANCED_BOUND) for mon, v in crt1234.items()}
reconstructed_count = sum(q is not None for q in recon.values())
all_reconstructed = reconstructed_count == len(support123)
qrat_sha256 = None
qrat_bytes = None
qrat_max_num = None
qrat_max_den = None
first_strict_pass = False
singular_completed = False

if all_reconstructed:
    exact_terms = [(mon, recon[mon]) for mon in support123]
    assert all(q is not None for _, q in exact_terms)

    def fstr(q: Fraction) -> str:
        return str(q.numerator) if q.denominator == 1 else f"({q.numerator}/{q.denominator})"

    def qterm(q: Fraction, mon: str, first: bool) -> str:
        sign = "-" if q < 0 else "+"
        a = abs(q)
        body = mon if a == 1 else f"({fstr(a)})*{mon}"
        return (("-" if q < 0 else "") if first else sign) + body

    qrat = "".join(qterm(q, mon, k == 0) for k, (mon, q) in enumerate(exact_terms))
    qrat_sha256 = hashlib.sha256(qrat.encode()).hexdigest()
    qrat_bytes = len(qrat.encode())
    qrat_max_num = max(abs(q.numerator) for _, q in exact_terms)
    qrat_max_den = max(q.denominator for _, q in exact_terms)

    buf = io.StringIO()
    with redirect_stdout(buf):
        lns = runpy.run_path(str(LOCATOR))
    locator_out = lns["out"]
    curves = lns["curves"]
    assert locator_out["canonical_sha256"] == LOCATOR_CANONICAL
    assert locator_out["strict_curve_packet_sha256"] == STRICT_PACKET

    def ffrac(x: Fraction) -> str:
        return str(x.numerator) if x.denominator == 1 else f"({x.numerator}/{x.denominator})"

    def kexpr(x) -> str:
        a, b, c, d = x.coeffs()
        parts = []
        for q, u in ((a, ""), (b, "ii"), (c, "ss"), (d, "isv")):
            if q == 0: continue
            qs = ffrac(q)
            parts.append(qs if not u else f"({qs})*{u}")
        return "+".join(parts).replace("+-", "-") if parts else "0"

    def row_expr_exact(row) -> str:
        parts = []
        for name, x in zip(NAMES, row):
            ex = kexpr(x)
            if ex != "0": parts.append(f"({ex})*{name}")
        return "+".join(parts).replace("+-", "-")

    eqs = ",".join(row_expr_exact(r) for r in curves[FIRST_STRICT_INDEX - 1])
    sing = r'''
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
  ideal G=std(B); int j;
  for (j=1; j<=size(A); j++) { if (reduce(A[j],G)!=0) { return(0); } }
  return(1);
}
proc equalideal(ideal A, ideal B) { return(contained(A,B)==1 && contained(B,A)==1); }
proc sympow(ideal P, int m)
{
  ideal Sk=std(surf+P); ideal Candidate; ideal Sn; list SatL; int kk;
  for (kk=2; kk<=m; kk++)
  {
    Candidate=surf+Sk*P; SatL=sat(Candidate,Sing); Sn=std(SatL[1]); Sk=Sn;
  }
  list StableL=sat(Sk,Sing); ideal Stable=std(StableL[1]);
  if (equalideal(Sk,Stable)!=1) { ERROR("symbolic power not saturation-stable"); }
  return(Sk);
}
ideal SurfStd=std(surf);
'''
    sing += "\npoly qNum=" + qrat + ";\nqNum=reduce(qNum,SurfStd);\n"
    sing += f"ideal P={eqs};\nideal T=std(sympow(P,{FIRST_STRICT_MULTIPLICITY}));\n"
    sing += 'poly rr=reduce(qNum,T);\nif (rr==0) { print("GOAL4AJ_GEN23_FIRST_STRICT=PASS"); } else { print("GOAL4AJ_GEN23_FIRST_STRICT=FAIL"); }\nquit;\n'
    with tempfile.TemporaryDirectory() as td:
        sf = Path(td) / "goal4aj-num31-four-prime-crt-gen23.sing"
        sf.write_text(sing, encoding="utf-8")
        try:
            cp = subprocess.run(["Singular", "-q", str(sf)], text=True, capture_output=True, timeout=1200)
            sout, serr, rc, timed_out = cp.stdout, cp.stderr, cp.returncode, False
        except subprocess.TimeoutExpired as exc:
            sout = exc.stdout or ""; serr = exc.stderr or ""; rc = None; timed_out = True
            if isinstance(sout, bytes): sout = sout.decode("utf-8", errors="replace")
            if isinstance(serr, bytes): serr = serr.decode("utf-8", errors="replace")
    err = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    singular_completed = (not timed_out and rc == 0 and not err and "GOAL4AJ_GEN23_FIRST_STRICT=" in sout)
    if not singular_completed:
        print("GOAL4AJ_GEN23_SINGULAR_STDOUT_TAIL=" + json.dumps(sout[-8000:]))
        print("GOAL4AJ_GEN23_SINGULAR_STDERR_TAIL=" + json.dumps(serr[-4000:]))
        raise SystemExit("gen23 first-strict exact check did not complete")
    first_strict_pass = "GOAL4AJ_GEN23_FIRST_STRICT=PASS" in sout

if not all_reconstructed:
    route = "FOUR_PRIME_SUPPORT_MATCHED_BALANCED_RATIONAL_RECONSTRUCTION_INCOMPLETE_FIFTH_PRIME_REQUIRED"
elif first_strict_pass:
    route = "FOUR_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_FIRST_STRICT_EXACT_PASS_ALL_STRICT_REPLAY_READY"
else:
    route = "FOUR_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_COMPLETE_BUT_FIRST_STRICT_EXACT_FAIL_FIFTH_PRIME_REQUIRED"

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_FOUR_PRIME_PROJECTIVE_CRT_GEN23_DIAGNOSTIC_V1",
    "source_locks": {
        "gen17_script_blob_sha1": GEN17_BLOB,
        "gen22_script_blob_sha1": GEN22_BLOB,
        "gen22_run": GEN22_RUN, "gen22_job": GEN22_JOB,
        "gen22_canonical_sha256": GEN22_CANONICAL, "gen22_route": GEN22_ROUTE,
        "retained140_locator_blob_sha1": LOCATOR_BLOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL,
        "strict_curve_packet_sha256": STRICT_PACKET,
    },
    "degree": DEGREE,
    "first_prime": P1, "second_prime": P2, "third_prime": P3, "fourth_prime": P4,
    "fourth_prime_i_root": P4_I_ROOT, "fourth_prime_sqrt2_root": P4_SQRT2_ROOT,
    "four_prime_modulus": MODULUS,
    "monomial_support_equal_across_four_primes": support_equal,
    "support_count": len(support123), "support_sha256": support_sha123,
    "fourth_support_sha256": support_sha4,
    "projective_normalization_monomial": norm_mon,
    "balanced_numerator_bound": BALANCED_BOUND, "balanced_denominator_bound": BALANCED_BOUND,
    "uniqueness_product_twice": 2 * BALANCED_BOUND * BALANCED_BOUND,
    "reconstructed_count": reconstructed_count, "total_count": len(support123),
    "all_coefficients_balanced_reconstructed": all_reconstructed,
    "reconstructed_q_candidate_sha256": qrat_sha256,
    "reconstructed_q_candidate_text_bytes": qrat_bytes,
    "reconstructed_q_candidate_max_abs_numerator": qrat_max_num,
    "reconstructed_q_candidate_max_denominator": qrat_max_den,
    "first_exact_strict_index_1based": FIRST_STRICT_INDEX,
    "first_exact_strict_multiplicity": FIRST_STRICT_MULTIPLICITY,
    "first_exact_strict_check_executed": all_reconstructed,
    "first_exact_strict_check_completed": singular_completed,
    "first_exact_strict_pass": first_strict_pass,
    "route_result": route,
    "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
    "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
    "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_NUM31_FOUR_PRIME_CRT_GEN23_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_FOUR_PRIME_CRT_GEN23=DONE", flush=True)
