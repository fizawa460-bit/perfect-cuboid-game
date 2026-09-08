#!/usr/bin/env python3
"""Goal4AJ gen21: two-prime projective CRT reconstruction of the degree-31 numerator line.

Gen20 found an independent unique degree-31 strict line at p=32057 with the same
5924-term count as the p=32009 line.  This diagnostic strengthens that preflight:
it replays both modular lines, requires identical monomial support, fixes one
deterministic common monomial coefficient to 1 projectively, combines every
coefficient ratio by CRT modulo 32009*32057, applies uniqueness-safe balanced
rational reconstruction, and only when all coefficients reconstruct checks the
first load-bearing strict condition (#2, multiplicity 21) exactly over
Q(i,sqrt(2)).

This remains diagnostic-only.  Even an exact first-strict PASS is not a literal
Q numerator until all 27 strict conditions and divisor data are replayed.  No
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
GEN20 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_second_prime_gen20.py"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN20_BLOB = "9277f2345d74a02016967f5a241385e7f540fad2"
GEN20_RUN = 34188843823
GEN20_JOB = 101942579200
GEN20_CANONICAL = "eb4a62463b30276e0d8783adeb704c3819c96a723434ccab0140782f9be83c65"
GEN20_ROUTE = "SECOND_PRIME_UNIQUE_DEGREE31_LINE_MATCHING_TERM_COUNT_MULTI_PRIME_RECONSTRUCTION_READY"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
P1 = 32009
P2 = 32057
MODULUS = P1 * P2
DEGREE = 31
FIRST_STRICT_INDEX = 2
FIRST_STRICT_MULTIPLICITY = 21
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
BALANCED_BOUND = 22650
assert 2 * BALANCED_BOUND * BALANCED_BOUND < MODULUS


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN20) == GEN20_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB


def parse_candidate(candidate: str, p: int) -> dict[str, int]:
    out: dict[str, int] = {}
    for m in re.finditer(r"([+-]?)([^+-]+)", candidate):
        sign_s, body = m.groups()
        sign = -1 if sign_s == "-" else 1
        factors = body.split("*")
        if factors[0].isdigit():
            coeff = sign * int(factors[0])
            mon = "*".join(factors[1:])
        else:
            coeff = sign
            mon = body
        if not mon or mon in out:
            raise SystemExit("unexpected modular candidate term encoding")
        out[mon] = coeff % p
    return out


# Replay p2 through the exact gen20 source; retain its candidate text from globals.
buf = io.StringIO()
with redirect_stdout(buf):
    n20 = runpy.run_path(str(GEN20))
g20 = n20["out"]
cand2 = n20["candidate"]
assert g20["canonical_sha256"] == GEN20_CANONICAL
assert g20["route_result"] == GEN20_ROUTE
assert g20["second_prime"] == P2
assert g20["second_prime_unique_line"] is True
assert cand2 is not None

# Replay the source-locked p1 line directly from gen17.
src = GEN17.read_text(encoding="utf-8")
old_note = 'DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"'
old_packet = f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"'
assert src.count(old_note) == 1 and src.count(old_packet) == 1
src = src.replace(old_note, f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"', 1)
src = src.replace(old_packet, f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"', 1)
n1 = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen21-p1-replay]", "exec"), n1)
g17 = n1["out"]
cands1 = n1["candidates"]
assert g17["field_prime"] == P1
assert g17["strict_condition_section_space_degree31_dimension"] == 1
assert len(cands1) == 1
cand1 = cands1[0]

m1 = parse_candidate(cand1, P1)
m2 = parse_candidate(cand2, P2)
support1 = sorted(m1)
support2 = sorted(m2)
support_equal = support1 == support2
support_sha1 = hashlib.sha256("\n".join(support1).encode()).hexdigest()
support_sha2 = hashlib.sha256("\n".join(support2).encode()).hexdigest()
if not support_equal:
    out = {
        "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_TWO_PRIME_PROJECTIVE_CRT_GEN21_DIAGNOSTIC_V1",
        "source_locks": {"gen17_script_blob_sha1": GEN17_BLOB, "gen20_script_blob_sha1": GEN20_BLOB,
                         "gen20_run": GEN20_RUN, "gen20_job": GEN20_JOB,
                         "gen20_canonical_sha256": GEN20_CANONICAL, "gen20_route": GEN20_ROUTE},
        "first_prime": P1, "second_prime": P2, "crt_modulus": MODULUS,
        "first_support_count": len(support1), "second_support_count": len(support2),
        "first_support_sha256": support_sha1, "second_support_sha256": support_sha2,
        "monomial_support_equal": False,
        "route_result": "TWO_PRIME_MONOMIAL_SUPPORT_MISMATCH_NO_CRT_RECONSTRUCTION",
        "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
        "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
        "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
    }
    out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    print("GOAL4AJ_NUM31_TWO_PRIME_CRT_GEN21_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
    print("GOAL4AJ_NUM31_TWO_PRIME_CRT_GEN21=DONE", flush=True)
    raise SystemExit(0)

# Deterministic common projective normalization: lexicographically first support monomial.
norm_mon = support1[0]
lead1, lead2 = m1[norm_mon], m2[norm_mon]
assert lead1 != 0 and lead2 != 0
nrm1 = {mon: (v * pow(lead1, -1, P1)) % P1 for mon, v in m1.items()}
nrm2 = {mon: (v * pow(lead2, -1, P2)) % P2 for mon, v in m2.items()}
assert nrm1[norm_mon] == 1 and nrm2[norm_mon] == 1


def crt_pair(a: int, p: int, b: int, q: int) -> int:
    t = ((b - a) * pow(p, -1, q)) % q
    return (a + p * t) % (p * q)


def ratrec(v: int, modulus: int, A: int, B: int) -> Fraction | None:
    """Unique a/b in |a|<=A, 1<=b<=B, with a == v*b mod modulus."""
    assert 2 * A * B < modulus
    v %= modulus
    if v == 0:
        return Fraction(0, 1)
    r0, r1 = modulus, v
    s0, s1 = 0, 1
    while r1 and abs(r1) > A:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if r1 == 0 or s1 == 0:
        return None
    a, b = r1, s1
    if b < 0:
        a, b = -a, -b
    g = math.gcd(abs(a), b)
    if g != 1:
        a //= g; b //= g
    if abs(a) > A or not (1 <= b <= B) or (a - v * b) % modulus != 0:
        return None
    return Fraction(a, b)


crt_map = {mon: crt_pair(nrm1[mon], P1, nrm2[mon], P2) for mon in support1}
recon = {mon: ratrec(v, MODULUS, BALANCED_BOUND, BALANCED_BOUND) for mon, v in crt_map.items()}
reconstructed_count = sum(q is not None for q in recon.values())
all_reconstructed = reconstructed_count == len(support1)
qrat_sha256 = None
qrat_bytes = None
qrat_max_num = None
qrat_max_den = None
first_strict_pass = False
singular_completed = False

if all_reconstructed:
    exact_terms = [(mon, recon[mon]) for mon in support1]
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
    sing += 'poly rr=reduce(qNum,T);\nif (rr==0) { print("GOAL4AJ_GEN21_FIRST_STRICT=PASS"); } else { print("GOAL4AJ_GEN21_FIRST_STRICT=FAIL"); }\nquit;\n'
    with tempfile.TemporaryDirectory() as td:
        sf = Path(td) / "goal4aj-num31-two-prime-crt-gen21.sing"
        sf.write_text(sing, encoding="utf-8")
        try:
            cp = subprocess.run(["Singular", "-q", str(sf)], text=True, capture_output=True, timeout=1800)
            sout, serr, rc, timed_out = cp.stdout, cp.stderr, cp.returncode, False
        except subprocess.TimeoutExpired as exc:
            sout = exc.stdout or ""; serr = exc.stderr or ""; rc = None; timed_out = True
            if isinstance(sout, bytes): sout = sout.decode("utf-8", errors="replace")
            if isinstance(serr, bytes): serr = serr.decode("utf-8", errors="replace")
    err = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    singular_completed = (not timed_out and rc == 0 and not err and "GOAL4AJ_GEN21_FIRST_STRICT=" in sout)
    if not singular_completed:
        print("GOAL4AJ_GEN21_SINGULAR_STDOUT_TAIL=" + json.dumps(sout[-8000:]))
        print("GOAL4AJ_GEN21_SINGULAR_STDERR_TAIL=" + json.dumps(serr[-4000:]))
        raise SystemExit("gen21 first-strict exact check did not complete")
    first_strict_pass = "GOAL4AJ_GEN21_FIRST_STRICT=PASS" in sout

if not all_reconstructed:
    route = "TWO_PRIME_SUPPORT_MATCHED_BALANCED_RATIONAL_RECONSTRUCTION_INCOMPLETE_THIRD_PRIME_REQUIRED"
elif first_strict_pass:
    route = "TWO_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_FIRST_STRICT_EXACT_PASS"
else:
    route = "TWO_PRIME_SUPPORT_MATCHED_BALANCED_RECONSTRUCTION_COMPLETE_BUT_FIRST_STRICT_EXACT_FAIL_THIRD_PRIME_REQUIRED"

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_TWO_PRIME_PROJECTIVE_CRT_GEN21_DIAGNOSTIC_V1",
    "source_locks": {"gen17_script_blob_sha1": GEN17_BLOB, "gen20_script_blob_sha1": GEN20_BLOB,
                     "gen20_run": GEN20_RUN, "gen20_job": GEN20_JOB,
                     "gen20_canonical_sha256": GEN20_CANONICAL, "gen20_route": GEN20_ROUTE,
                     "retained140_locator_blob_sha1": LOCATOR_BLOB,
                     "retained140_locator_canonical_sha256": LOCATOR_CANONICAL,
                     "strict_curve_packet_sha256": STRICT_PACKET},
    "degree": DEGREE, "first_prime": P1, "second_prime": P2, "crt_modulus": MODULUS,
    "monomial_support_equal": support_equal, "support_count": len(support1),
    "support_sha256": support_sha1, "projective_normalization_monomial": norm_mon,
    "balanced_numerator_bound": BALANCED_BOUND, "balanced_denominator_bound": BALANCED_BOUND,
    "uniqueness_product_twice": 2 * BALANCED_BOUND * BALANCED_BOUND,
    "reconstructed_count": reconstructed_count, "total_count": len(support1),
    "all_coefficients_balanced_reconstructed": all_reconstructed,
    "reconstructed_q_candidate_sha256": qrat_sha256,
    "reconstructed_q_candidate_text_bytes": qrat_bytes,
    "reconstructed_q_candidate_max_abs_numerator": qrat_max_num,
    "reconstructed_q_candidate_max_denominator": qrat_max_den,
    "first_exact_strict_index_1based": FIRST_STRICT_INDEX,
    "first_exact_strict_multiplicity": FIRST_STRICT_MULTIPLICITY,
    "first_exact_strict_check_executed": all_reconstructed,
    "first_exact_strict_check_completed": singular_completed,
    "first_exact_strict_pass": first_strict_pass, "route_result": route,
    "literal_q_numerator_materialized": False, "literal_F_B_materialized": False,
    "local_evaluations_computed": False, "brauer_manin_obstruction_obtained": False,
    "E1_proved": False, "stage35_closed": False, "theorem_credit": False, "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_NUM31_TWO_PRIME_CRT_GEN21_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_TWO_PRIME_CRT_GEN21=DONE", flush=True)
