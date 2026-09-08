#!/usr/bin/env python3
"""Goal4AJ gen19: rational-reconstruction diagnostic for the unique mod-32009 numerator line.

Gen18 rejected the denominator-style global 8x centered lift at the first exact
strict condition.  That does not reject the unique modular line: Singular's
standard-basis generator is projectively normalized, and an exact Q-line may
have non-dyadic rational coefficient ratios.  This leaf replays the source-
locked gen17-g3 line, rationally reconstructs its monic coefficient ratios under
several uniqueness-safe height profiles, and, only if one profile reconstructs
every coefficient, checks the first load-bearing strict condition (#2, order 21)
over Q(i,sqrt(2)).

No literal numerator/F_B/local/Brauer-Manin/E1/Stage35/theorem/endpoint credit
is granted by this diagnostic.
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
GEN17_G2 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17_g2.py"
GEN17_G3 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17_g3.py"
GEN18 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_dyadic_exact_strict_gen18.py"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN17_G2_BLOB = "7a6dad9321d3029a0d8e8ec245dbd571133baef6"
GEN17_G3_BLOB = "6e65f80324d9bd767fa6ab9860a61995aa276c93"
GEN18_BLOB = "0653516b77e7ae6fd8ddd07dda6901cc46994fdd"
GEN17_CANONICAL = "80cf6f47003c9791501c7f87248f803b9c495f2f42de46c6a3e500ced9c8a9c0"
GEN18_CANONICAL = "d306f79bde7a754edeb3657bd2c50b2614c7adcd194fb97ffdf72a9b93e5778d"
GEN18_RUN = 34184660698
GEN18_JOB = 101930509567
MODULAR_CANDIDATE_SHA256 = "7d0020181c37b6ee7e203061bda0088ea5f072ac358b275e4b7446b2c40282a5"
MODULAR_CANDIDATE_BYTES = 149855
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
FIELD_PRIME = 32009
DEGREE = 31
FIRST_STRICT_INDEX = 2
FIRST_STRICT_MULTIPLICITY = 21
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN17_G2) == GEN17_G2_BLOB
assert git_blob(GEN17_G3) == GEN17_G3_BLOB
assert git_blob(GEN18) == GEN18_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB

# Replay the exact gen17-g3 modular line while retaining its candidate text.
src = GEN17.read_text(encoding="utf-8")
old_note = 'DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"'
old_packet = f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"'
assert src.count(old_note) == 1 and src.count(old_packet) == 1
src = src.replace(old_note, f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"', 1)
src = src.replace(old_packet, f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"', 1)
ns = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen19-source-locked-replay]", "exec"), ns)
g17 = ns["out"]
candidates = ns["candidates"]
assert g17["canonical_sha256"] == GEN17_CANONICAL
assert g17["strict_condition_section_space_degree31_dimension"] == 1
assert len(candidates) == 1
candidate = candidates[0]
assert len(candidate.encode()) == MODULAR_CANDIDATE_BYTES
assert hashlib.sha256(candidate.encode()).hexdigest() == MODULAR_CANDIDATE_SHA256

# Parse the monic finite-field polynomial.
term_map: dict[str, int] = {}
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
    if not mon or mon in term_map:
        raise SystemExit("unexpected gen17 candidate term encoding")
    term_map[mon] = coeff % FIELD_PRIME
assert len(term_map) == 5924


def centered(v: int) -> int:
    v %= FIELD_PRIME
    return v - FIELD_PRIME if v > FIELD_PRIME // 2 else v


def ratrec(v: int, anum: int, bden: int) -> Fraction | None:
    """Unique a/b with |a|<=anum, 1<=b<=bden and a == v*b mod p."""
    assert 2 * anum * bden < FIELD_PRIME
    found = None
    for b in range(1, bden + 1):
        a = centered(v * b)
        if abs(a) <= anum and math.gcd(abs(a), b) == 1:
            q = Fraction(a, b)
            if found is not None and q != found:
                raise SystemExit("uniqueness-safe rational reconstruction produced two answers")
            found = q
    return found

# Profiles all satisfy 2*A*B < p.  They test both balanced and small-denominator/high-numerator regimes.
profiles = [(126,126),(250,64),(500,32),(1000,16),(2000,8),(4000,4),(8000,2),(16003,1)]
profile_rows = []
profile_reconstructions: dict[str, list[tuple[str, Fraction | None]]] = {}
for A, B in profiles:
    vals = [(mon, ratrec(v, A, B)) for mon, v in term_map.items()]
    ok = sum(q is not None for _, q in vals)
    key = f"A{A}_B{B}"
    profile_reconstructions[key] = vals
    profile_rows.append({
        "numerator_bound": A,
        "denominator_bound": B,
        "uniqueness_product_twice": 2*A*B,
        "reconstructed_count": ok,
        "total_count": len(vals),
        "coverage": ok / len(vals),
    })

best = max(profile_rows, key=lambda r: (r["reconstructed_count"], -r["denominator_bound"], -r["numerator_bound"]))
best_key = f"A{best['numerator_bound']}_B{best['denominator_bound']}"
all_reconstructed = best["reconstructed_count"] == len(term_map)

# Rebuild exact retained strict curve #2 only if a one-prime reconstruction is complete.
first_strict_pass = False
qrat_sha256 = None
qrat_bytes = None
qrat_max_num = None
qrat_max_den = None
singular_completed = False
if all_reconstructed:
    exact_terms = [(mon, q) for mon, q in profile_reconstructions[best_key] if q is not None]
    assert len(exact_terms) == len(term_map)

    def fstr(q: Fraction) -> str:
        if q.denominator == 1:
            return str(q.numerator)
        return f"({q.numerator}/{q.denominator})"

    def format_qterm(q: Fraction, mon: str, first: bool) -> str:
        sign = "-" if q < 0 else "+"
        a = abs(q)
        body = mon if a == 1 else f"({fstr(a)})*{mon}"
        if first:
            return ("-" if q < 0 else "") + body
        return sign + body

    qrat = "".join(format_qterm(q, mon, k == 0) for k, (mon, q) in enumerate(exact_terms))
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
    sing += "\npoly qNum=" + qrat + ";\n"
    sing += "qNum=reduce(qNum,SurfStd);\n"
    sing += f"ideal P={eqs};\n"
    sing += f"ideal T=std(sympow(P,{FIRST_STRICT_MULTIPLICITY}));\n"
    sing += 'poly rr=reduce(qNum,T);\n'
    sing += 'if (rr==0) { print("GOAL4AJ_GEN19_FIRST_STRICT=PASS"); } else { print("GOAL4AJ_GEN19_FIRST_STRICT=FAIL"); }\nquit;\n'
    with tempfile.TemporaryDirectory() as td:
        sf = Path(td) / "goal4aj-num31-ratrec-gen19.sing"
        sf.write_text(sing, encoding="utf-8")
        try:
            cp = subprocess.run(["Singular", "-q", str(sf)], text=True, capture_output=True, timeout=1800)
            sout, serr, rc, timed_out = cp.stdout, cp.stderr, cp.returncode, False
        except subprocess.TimeoutExpired as exc:
            sout = exc.stdout or ""; serr = exc.stderr or ""; rc = None; timed_out = True
            if isinstance(sout, bytes): sout = sout.decode("utf-8", errors="replace")
            if isinstance(serr, bytes): serr = serr.decode("utf-8", errors="replace")
    err = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
    singular_completed = (not timed_out and rc == 0 and not err and "GOAL4AJ_GEN19_FIRST_STRICT=" in sout)
    if not singular_completed:
        print("GOAL4AJ_GEN19_SINGULAR_STDOUT_TAIL=" + json.dumps(sout[-8000:]))
        print("GOAL4AJ_GEN19_SINGULAR_STDERR_TAIL=" + json.dumps(serr[-4000:]))
        raise SystemExit("gen19 first-strict exact check did not complete")
    first_strict_pass = "GOAL4AJ_GEN19_FIRST_STRICT=PASS" in sout

if not all_reconstructed:
    route = "ONE_PRIME_RATIONAL_RECONSTRUCTION_INCOMPLETE_MULTI_PRIME_REQUIRED"
elif first_strict_pass:
    route = "ONE_PRIME_RATIONAL_RECONSTRUCTION_COMPLETE_FIRST_STRICT_EXACT_PASS"
else:
    route = "ONE_PRIME_RATIONAL_RECONSTRUCTION_COMPLETE_BUT_FIRST_STRICT_EXACT_FAIL"

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_RATIONAL_RECONSTRUCTION_GEN19_DIAGNOSTIC_V1",
    "source_locks": {
        "gen17_script_blob_sha1": GEN17_BLOB,
        "gen17_g2_blob_sha1": GEN17_G2_BLOB,
        "gen17_g3_blob_sha1": GEN17_G3_BLOB,
        "gen17_canonical_sha256": GEN17_CANONICAL,
        "gen18_script_blob_sha1": GEN18_BLOB,
        "gen18_run": GEN18_RUN,
        "gen18_job": GEN18_JOB,
        "gen18_canonical_sha256": GEN18_CANONICAL,
        "gen18_route": "NUMERATOR_DYADIC_LIFT_REJECTED_BY_EXACT_STRICT_CONDITION",
        "gen18_first_failed_strict_index_1based": 2,
        "gen18_first_failed_multiplicity": 21,
    },
    "field_prime": FIELD_PRIME,
    "degree": DEGREE,
    "modular_candidate_sha256": MODULAR_CANDIDATE_SHA256,
    "modular_candidate_text_bytes": MODULAR_CANDIDATE_BYTES,
    "modular_term_count": len(term_map),
    "normalization": "Singular standard-basis degree31 generator; coefficient ratios reconstructed projectively from the monic modular line",
    "profiles": profile_rows,
    "best_profile": best,
    "all_coefficients_uniquely_reconstructed_under_one_profile": all_reconstructed,
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
    "literal_q_numerator_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_NUM31_RATREC_GEN19_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_RATREC_GEN19=DONE", flush=True)
