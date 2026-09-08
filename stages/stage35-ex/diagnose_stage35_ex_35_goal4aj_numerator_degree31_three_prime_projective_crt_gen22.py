#!/usr/bin/env python3
"""Goal4AJ gen22: three-prime projective CRT reconstruction of the degree-31 numerator line.

Gen21 matched the complete 5924-monomial support at p=32009 and p=32057, but
balanced rational reconstruction recovered only 4016/5924 coefficients.  This
diagnostic adds the independent split prime p=32089, preserves the exact gen21
projective normalization monomial, combines all coefficient ratios modulo the
three-prime product, and applies uniqueness-safe balanced rational reconstruction.
Only if all 5924 coefficients reconstruct is the first load-bearing strict
condition (#2, multiplicity 21) checked exactly over Q(i,sqrt(2)).

This is diagnostic-only.  Even a first-strict PASS does not materialize the Q
numerator until all 27 strict conditions and divisor data are replayed.  No
F_B/local/Brauer-Manin/E1/Stage35/theorem/receiver/endpoint credit is granted.
"""
from __future__ import annotations

from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
import math
import re
import runpy
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN21 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_two_prime_projective_crt_gen21.py"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN21_BLOB = "c98aac1a3f33051842681764921d6febed125d75"
GEN21_RUN = 34189796107
GEN21_JOB = 101945366434
GEN21_CANONICAL = "9a4c8acd3b6c311d521b18787da6943a410836cb4fbfde66e39ec591c930f4dc"
GEN21_ROUTE = "TWO_PRIME_SUPPORT_MATCHED_BALANCED_RATIONAL_RECONSTRUCTION_INCOMPLETE_THIRD_PRIME_REQUIRED"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
P1 = 32009
P2 = 32057
P3 = 32089
P3_I_ROOT = 9893
P3_SQRT2_ROOT = 9854
MOD12 = P1 * P2
MODULUS = MOD12 * P3
DEGREE = 31
FIRST_STRICT_INDEX = 2
FIRST_STRICT_MULTIPLICITY = 21
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
BALANCED_BOUND = 4_000_000
assert P3 % 8 == 1
assert pow(P3_I_ROOT, 2, P3) == P3 - 1
assert pow(P3_SQRT2_ROOT, 2, P3) == 2
assert 2 * BALANCED_BOUND * BALANCED_BOUND < MODULUS


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN21) == GEN21_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB

# Replay gen21 exactly.  Its globals retain the two-prime normalized support and
# CRT residues, while its result locks the observed 4016/5924 incomplete route.
buf = io.StringIO()
with redirect_stdout(buf):
    n21 = runpy.run_path(str(GEN21))
g21 = n21["out"]
assert g21["canonical_sha256"] == GEN21_CANONICAL
assert g21["route_result"] == GEN21_ROUTE
assert g21["monomial_support_equal"] is True
assert g21["support_count"] == 5924
assert g21["reconstructed_count"] == 4016
support12 = n21["support1"]
norm_mon = n21["norm_mon"]
crt12 = n21["crt_map"]
parse_candidate = n21["parse_candidate"]
crt_pair = n21["crt_pair"]
ratrec = n21["ratrec"]
assert len(support12) == 5924
assert norm_mon == g21["projective_normalization_monomial"]

# Independently replay the same strict kernel at p3 by patching only the split
# prime and the fixed source-lock substitutions used by gen20/gen21.
src = GEN17.read_text(encoding="utf-8")
repls = [
    ('DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"', f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'),
    (f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"', f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"'),
    ("FIELD_PRIME = 32009", f"FIELD_PRIME = {P3}"),
    ("I_ROOT = 10754", f"I_ROOT = {P3_I_ROOT}"),
    ("SQRT2_ROOT = 8047", f"SQRT2_ROOT = {P3_SQRT2_ROOT}"),
    ("ring r=32009,(a1,a2,a3,b1,b2,b3,c),dp;", f"ring r={P3},(a1,a2,a3,b1,b2,b3,c),dp;"),
    ("number ii=10754;", f"number ii={P3_I_ROOT};"),
    ("number ss=8047;", f"number ss={P3_SQRT2_ROOT};"),
]
for old, new in repls:
    if src.count(old) != 1:
        raise SystemExit(f"gen22 source patch cardinality mismatch: {old!r}")
    src = src.replace(old, new, 1)

n3 = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen22-p32089]", "exec"), n3)
g3 = n3["out"]
cands3 = n3["candidates"]
assert g3["field_prime"] == P3
assert g3["strict_condition_section_space_degree31_dimension"] == 1
assert len(cands3) == 1
cand3 = cands3[0]
m3 = parse_candidate(cand3, P3)
support3 = sorted(m3)
support_equal = support3 == support12
support_sha12 = hashlib.sha256("\n".join(support12).encode()).hexdigest()
support_sha3 = hashlib.sha256("\n".join(support3).encode()).hexdigest()

if not support_equal or norm_mon not in m3 or m3.get(norm_mon, 0) == 0:
    out = {
        "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_THREE_PRIME_PROJECTIVE_CRT_GEN22_DIAGNOSTIC_V1",
        "source_locks": {
            "gen17_script_blob_sha1": GEN17_BLOB,
            "gen21_script_blob_sha1": GEN21_BLOB,
            "gen21_run": GEN21_RUN,
            "gen21_job": GEN21_JOB,
            "gen21_canonical_sha256": GEN21_CANONICAL,
            "gen21_route": GEN21_ROUTE,
        },
        "first_prime": P1, "second_prime": P2, "third_prime": P3,
        "three_prime_modulus": MODULUS,
        "first_two_support_count": len(support12), "third_support_count": len(support3),
        "first_two_support_sha256": support_sha12, "third_support_sha256": support_sha3,
        "monomial_support_equal_across_three_primes": False,
        "projective_normalization_monomial": norm_mon,
        "route_result": "THIRD_PRIME_SUPPORT_OR_NORMALIZATION_MISMATCH_NO_THREE_PRIME_RECONSTRUCTION",
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print("GOAL4AJ_NUM31_THREE_PRIME_CRT_GEN22_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
    print("GOAL4AJ_NUM31_THREE_PRIME_CRT_GEN22=DONE", flush=True)
    raise SystemExit(0)

lead3 = m3[norm_mon]
nrm3 = {mon: (v * pow(lead3, -1, P3)) % P3 for mon, v in m3.items()}
assert nrm3[norm_mon] == 1
crt123 = {mon: crt_pair(crt12[mon], MOD12, nrm3[mon], P3) for mon in support12}
recon = {mon: ratrec(v, MODULUS, BALANCED_BOUND, BALANCED_BOUND) for mon, v in crt123.items()}
reconstructed_count = sum(q is not None for q in recon.values())
all_reconstructed = reconstructed_count == len(support12)
qrat_sha256 = None
qrat_bytes = None
qrat_max_num = None
qrat_max_den = None
first_strict_pass = False
singular_completed = False

if all_reconstructed:
    exact_terms = [(mon, recon[mon]) for mon in support12]
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
            if q == 0:
                continue
            qs = ffrac(q)
            parts.append(qs if not u else f"({qs})*{u}")
        return "+".join(parts).replace("+-", "-") if parts else "0"

    def row_expr_exact(row) -> str:
        parts = []
        for name, x in zip(NAMES, row):
            ex = kexpr(x)
            if ex != "0":
                parts.append(f"({ex})*{name}")
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
    sing += 'poly rr=reduce(qNum,T);\nif (rr==0) { print("GOAL4AJ_GEN22_FIRST_STRICT=PASS"); } else { print("GOAL4AJ_GEN22_FIRST_STRICT=FAIL"); }\nquit;\n'
    with tempfile.TemporaryDirectory() as td:
        sf = Path(td) / "goal4aj-num31-three-prime-crt-gen22.sing"
        sf.write_text(sing, encoding="utf-8")
        try:
            cp = subprocess.run(["Singular", "-q", str(sf)], text=True, capture_output=True, timeout=1200)
            sout, serr, rc, timed_out = cp.stdout, cp.stderr, cp.returncode, False
        except subprocess.TimeoutExpired as exc:
            sout = exc.stdout or ""; serr = exc.stderr or ""; rc = None; timed_out = True
            if isinstance(sout, bytes): sout = sout.decode("utf-8", errors="replace")
            if isinstance(serr, bytes): serr = serr.decode("utf-8", errors="replace")
    err = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    singular_completed = (not timed_out and rc == 0 and not err and "GOAL4AJ_GEN22_FIRST_STRICT=" in sout)
    if not singular_completed:
        print("GOAL4AJ_GEN22_SINGULAR_STDOUT_TAIL=" + json.dumps(sout[-8000:]))
        print("GOAL4AJ_GEN22_SINGULAR_STDERR_TAIL=" + json.dumps(serr[-4000:]))
        raise SystemExit("gen22 first-strict exact check did not complete")
    first_strict_pass = "GOAL4AJ_GEN22_FIRST_STRICT=PASS" in sout

if not all_reconstructed:
    route = "THREE_PRIME_SUPPORT_MATCHED_BALANCED_RATIONAL_RECONSTRUCTION_INCOMPLETE_FOURTH_PRIME_REQUIRED"
elif first_strict_pass:
    route = "THREE_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_FIRST_STRICT_EXACT_PASS_ALL_STRICT_REPLAY_READY"
else:
    route = "THREE_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_COMPLETE_BUT_FIRST_STRICT_EXACT_FAIL_FOURTH_PRIME_REQUIRED"

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_THREE_PRIME_PROJECTIVE_CRT_GEN22_DIAGNOSTIC_V1",
    "source_locks": {
        "gen17_script_blob_sha1": GEN17_BLOB,
        "gen21_script_blob_sha1": GEN21_BLOB,
        "gen21_run": GEN21_RUN,
        "gen21_job": GEN21_JOB,
        "gen21_canonical_sha256": GEN21_CANONICAL,
        "gen21_route": GEN21_ROUTE,
        "retained140_locator_blob_sha1": LOCATOR_BLOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL,
        "strict_curve_packet_sha256": STRICT_PACKET,
    },
    "degree": DEGREE,
    "first_prime": P1, "second_prime": P2, "third_prime": P3,
    "third_prime_i_root": P3_I_ROOT, "third_prime_sqrt2_root": P3_SQRT2_ROOT,
    "three_prime_modulus": MODULUS,
    "monomial_support_equal_across_three_primes": support_equal,
    "support_count": len(support12), "support_sha256": support_sha12,
    "third_support_sha256": support_sha3,
    "projective_normalization_monomial": norm_mon,
    "balanced_numerator_bound": BALANCED_BOUND, "balanced_denominator_bound": BALANCED_BOUND,
    "uniqueness_product_twice": 2 * BALANCED_BOUND * BALANCED_BOUND,
    "reconstructed_count": reconstructed_count, "total_count": len(support12),
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
print("GOAL4AJ_NUM31_THREE_PRIME_CRT_GEN22_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_THREE_PRIME_CRT_GEN22=DONE", flush=True)
