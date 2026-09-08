#!/usr/bin/env python3
"""Goal4AJ gen18: Q-lift the unique modular degree-31 numerator candidate.

Gen17-g3 proved that the 27 numerator strict symbolic-power conditions cut the
F_32009 degree-31 section space to one dimension.  This diagnostic replays that
source-locked computation runner-locally, takes its unique candidate, forms the
deterministic centered lift of 8*q_mod, and tests that literal integer polynomial
against every one of the same 27 strict symbolic-power ideals in characteristic
zero over Q(i,sqrt(2)).  The test is fail-fast if the dyadic lift hypothesis is
wrong.

The retained A1 incidence relation is also recomputed cheaply.  Passing this
leaf materializes a literal Q-coefficient numerator candidate and supplies the
inputs for the same exceptional-coefficient intersection bridge used on the
denominator side.  It does not itself grant F_B/local/Brauer-Manin/E1/Stage35/
theorem/endpoint credit.
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
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN17_G2_BLOB = "7a6dad9321d3029a0d8e8ec245dbd571133baef6"
GEN17_G3_BLOB = "6e65f80324d9bd767fa6ab9860a61995aa276c93"
GEN17_CANONICAL = "80cf6f47003c9791501c7f87248f803b9c495f2f42de46c6a3e500ced9c8a9c0"
GEN17_RUN = 34183119045
GEN17_JOB = 101926079352
MODULAR_CANDIDATE_SHA256 = "7d0020181c37b6ee7e203061bda0088ea5f072ac358b275e4b7446b2c40282a5"
MODULAR_CANDIDATE_BYTES = 149855
DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
LOCATOR_CANONICAL = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
ACTIVE_BLOB = "20da16902171b267294acee0f3b80997d8fd5246"
ACTIVE_CANONICAL = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
FIELD_PRIME = 32009
LIFT_MULTIPLIER = 8
DEGREE = 31
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
NUM_STRICT = {
    2:21,3:1,4:1,5:1,6:1,7:21,9:3,10:10,12:10,13:18,14:4,15:12,
    16:1,17:3,18:12,19:12,22:12,23:10,24:1,27:1,30:1,38:13,40:13,
    58:9,60:9,65:1,67:1,
}
PROCESS_ORDER = [2,7,13,38,40,15,18,19,22,10,12,23,58,60,14,9,17,3,4,5,6,16,24,27,30,65,67]
assert len(NUM_STRICT) == 27 and sum(NUM_STRICT.values()) == 202


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN17_G2) == GEN17_G2_BLOB
assert git_blob(GEN17_G3) == GEN17_G3_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB
assert git_blob(ACTIVE) == ACTIVE_BLOB

# Reproduce gen17-g3 exactly, but keep its large candidate in this process.
src = GEN17.read_text(encoding="utf-8")
old_note = 'DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"'
old_packet = f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"'
assert src.count(old_note) == 1 and src.count(old_packet) == 1
src = src.replace(old_note, f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"', 1)
src = src.replace(old_packet, f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"', 1)
ns = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen18-source-locked-replay]", "exec"), ns)
g17 = ns["out"]
candidates = ns["candidates"]
assert g17["canonical_sha256"] == GEN17_CANONICAL
assert g17["strict_condition_section_space_degree31_dimension"] == 1
assert len(candidates) == 1
candidate = candidates[0]
assert len(candidate.encode()) == MODULAR_CANDIDATE_BYTES
assert hashlib.sha256(candidate.encode()).hexdigest() == MODULAR_CANDIDATE_SHA256

# Rebuild compact exact locator/active packets.
buf = io.StringIO()
with redirect_stdout(buf):
    lns = runpy.run_path(str(LOCATOR))
locator_out = lns["out"]
curves = lns["curves"]
node_map = lns["node_map"]
assert locator_out["canonical_sha256"] == LOCATOR_CANONICAL
assert locator_out["strict_curve_packet_sha256"] == STRICT_PACKET
assert len(curves) == 92 and len(node_map) == 48

buf = io.StringIO()
with redirect_stdout(buf):
    ans = runpy.run_path(str(ACTIVE))
active = ans["out"]
assert active["canonical_sha256"] == ACTIVE_CANONICAL
assert {int(k): int(v) for k, v in active["numerator"]["strict_multiplicities_1based"].items()} == NUM_STRICT
num_exc = {int(k): int(v) for k, v in active["numerator"]["exceptional_multiplicities_1based"].items()}

# Exact retained incidence relation needed by the exceptional-coefficient bridge.
incidence_rows = {}
for j in range(93, 141):
    incident = [int(i) for i in node_map[str(j)]["incident_strict_curve_indices_1based"]]
    inc_sum = sum(NUM_STRICT.get(i, 0) for i in incident)
    e = num_exc.get(j, 0)
    incidence_rows[str(j)] = {
        "target_order": e,
        "active_strict_incidence_multiplicity_sum": inc_sum,
        "twice_target_order": 2 * e,
        "relation_holds": inc_sum == 2 * e,
    }
incidence_ok = all(r["relation_holds"] for r in incidence_rows.values())

# Parse the finite-field polynomial and form the deterministic centered 8x lift.
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
assert term_map


def centered(v: int) -> int:
    v %= FIELD_PRIME
    return v - FIELD_PRIME if v > FIELD_PRIME // 2 else v


def format_term(z: int, mon: str, first: bool) -> str:
    sign = "-" if z < 0 else "+"
    a = abs(z)
    body = mon if a == 1 else f"{a}*{mon}"
    if first:
        return ("-" if z < 0 else "") + body
    return sign + body


lifted = [(mon, centered(LIFT_MULTIPLIER * coeff)) for mon, coeff in term_map.items()]
assert all(z != 0 for _, z in lifted)
qz = "".join(format_term(z, mon, k == 0) for k, (mon, z) in enumerate(lifted))
coeff_gcd = 0
for _, z in lifted:
    coeff_gcd = math.gcd(coeff_gcd, abs(z))
if coeff_gcd > 1:
    primitive = [(mon, z // coeff_gcd) for mon, z in lifted]
else:
    primitive = lifted
qprim = "".join(format_term(z, mon, k == 0) for k, (mon, z) in enumerate(primitive))
qprim_sha256 = hashlib.sha256(qprim.encode()).hexdigest()
max_abs = max(abs(z) for _, z in primitive)


def fstr(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"({x.numerator}/{x.denominator})"


def kexpr(x) -> str:
    a, b, c, d = x.coeffs()
    terms = []
    for q, u in ((a, ""), (b, "ii"), (c, "ss"), (d, "isv")):
        if q == 0:
            continue
        qs = fstr(q)
        terms.append(qs if not u else f"({qs})*{u}")
    if not terms:
        return "0"
    return "+".join(terms).replace("+-", "-")


def row_expr_exact(row) -> str:
    terms = []
    for name, x in zip(NAMES, row):
        ex = kexpr(x)
        if ex != "0":
            terms.append(f"({ex})*{name}")
    if not terms:
        raise SystemExit("zero exact strict equation")
    return "+".join(terms).replace("+-", "-")


sparts = [r'''
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
  for (j=1; j<=size(A); j++) { if (reduce(A[j],G)!=0) { return(0); } }
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
ideal SurfStd=std(surf);
ideal P;
ideal T;
poly rr;
''']
sparts.append("poly qNum=" + qprim + ";")
sparts.append("qNum=reduce(qNum,SurfStd);")
sparts.append('if (qNum==0) { ERROR("gen18 lift collapsed modulo surface"); }')
for step, idx in enumerate(PROCESS_ORDER, 1):
    e = NUM_STRICT[idx]
    eqs = ",".join(row_expr_exact(r) for r in curves[idx - 1])
    sparts.append(f'''P={eqs};
if (dim(std(surf+P))!=2) {{ ERROR("gen18 strict curve {idx} height mismatch"); }}
T=sympow(P,{e});
T=std(T);
rr=reduce(qNum,T);
if (rr==0) {{ print("GOAL4AJ_NUM31_EXACT_STRICT_NODE={step}:{idx}:{e}:PASS"); }}
else {{ print("GOAL4AJ_NUM31_EXACT_STRICT_NODE={step}:{idx}:{e}:FAIL"); print("GOAL4AJ_NUM31_EXACT_STRICT_SINGULAR_DONE=FAIL"); quit; }}
''')
sparts += ['print("GOAL4AJ_NUM31_EXACT_STRICT_SINGULAR_DONE=PASS");', "quit;"]
singular_program = "\n".join(sparts) + "\n"

with tempfile.TemporaryDirectory() as td:
    srcfile = Path(td) / "goal4aj-num31-exact-strict-gen18.sing"
    srcfile.write_text(singular_program, encoding="utf-8")
    try:
        cp = subprocess.run(["Singular", "-q", str(srcfile)], text=True, capture_output=True, timeout=2400)
        timed_out = False
        sout, serr, rc = cp.stdout, cp.stderr, cp.returncode
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        sout = exc.stdout or ""
        serr = exc.stderr or ""
        if isinstance(sout, bytes):
            sout = sout.decode("utf-8", errors="replace")
        if isinstance(serr, bytes):
            serr = serr.decode("utf-8", errors="replace")
        rc = None

rows = []
for line in sout.splitlines():
    if line.startswith("GOAL4AJ_NUM31_EXACT_STRICT_NODE="):
        step, idx, e, status = line.split("=", 1)[1].split(":")
        rows.append({"step": int(step), "strict_index_1based": int(idx), "multiplicity": int(e), "status": status})
error_text = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign"))
done_pass = "GOAL4AJ_NUM31_EXACT_STRICT_SINGULAR_DONE=PASS" in sout
done_fail = "GOAL4AJ_NUM31_EXACT_STRICT_SINGULAR_DONE=FAIL" in sout
completed = (not timed_out and rc == 0 and not error_text and (done_pass or done_fail))
if not completed:
    if serr:
        print("GOAL4AJ_NUM31_EXACT_STRICT_GEN18_STDERR=" + json.dumps(serr[-8000:]))
    print("GOAL4AJ_NUM31_EXACT_STRICT_GEN18_STDOUT_TAIL=" + json.dumps(sout[-12000:]))
    raise SystemExit("Goal4AJ gen18 exact numerator replay did not complete")

all_pass = done_pass and len(rows) == len(PROCESS_ORDER) and all(r["status"] == "PASS" for r in rows)
route = "NUMERATOR_DYADIC_LIFT_EXACT_27_OF_27_PASS" if all_pass else "NUMERATOR_DYADIC_LIFT_REJECTED_BY_EXACT_STRICT_CONDITION"
out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_DYADIC_EXACT_STRICT_GEN18_DIAGNOSTIC_V1",
    "source_locks": {
        "gen17_script_blob_sha1": GEN17_BLOB,
        "gen17_g2_blob_sha1": GEN17_G2_BLOB,
        "gen17_g3_blob_sha1": GEN17_G3_BLOB,
        "gen17_success_run": GEN17_RUN,
        "gen17_success_job": GEN17_JOB,
        "gen17_canonical_sha256": GEN17_CANONICAL,
        "locator_blob_sha1": LOCATOR_BLOB,
        "locator_canonical_sha256": LOCATOR_CANONICAL,
        "active_condition_blob_sha1": ACTIVE_BLOB,
        "active_condition_canonical_sha256": ACTIVE_CANONICAL,
    },
    "modular_field": f"F_{FIELD_PRIME}",
    "degree": DEGREE,
    "modular_candidate_sha256": MODULAR_CANDIDATE_SHA256,
    "modular_candidate_text_bytes": MODULAR_CANDIDATE_BYTES,
    "lift_multiplier": LIFT_MULTIPLIER,
    "lift_rule": "coefficientwise centered representative of 8*q_mod modulo 32009, then primitive gcd normalization",
    "literal_q_numerator_sha256": qprim_sha256,
    "literal_q_numerator_text_bytes": len(qprim.encode()),
    "literal_q_numerator_term_count": len(primitive),
    "preprimitive_coefficient_gcd": coeff_gcd,
    "literal_q_numerator_max_abs_coefficient": max_abs,
    "coefficient_field_exact_replay": "Q(u)/(u^4+1), i=u^2, sqrt2=u-u^3",
    "strict_condition_count": len(PROCESS_ORDER),
    "exact_strict_checked_count": len(rows),
    "exact_strict_passed_count": sum(r["status"] == "PASS" for r in rows),
    "all_27_exact_strict_conditions_pass": all_pass,
    "rows": rows,
    "exceptional_incidence_relation_checked": True,
    "exceptional_incidence_relation_all_48_hold": incidence_ok,
    "incidence_rows": incidence_rows,
    "exceptional_bridge_ready": all_pass and incidence_ok,
    "route_result": route,
    "q_literal_numerator_strict_candidate_materialized": all_pass,
    "q_literal_numerator_materialized": False,
    "literal_denominator_coefficients_materialized": True,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_NUM31_EXACT_STRICT_GEN18_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
if all_pass:
    print("GOAL4AJ_NUM31_LITERAL=" + qprim, flush=True)
print("GOAL4AJ_NUM31_EXACT_STRICT_GEN18=DONE", flush=True)
