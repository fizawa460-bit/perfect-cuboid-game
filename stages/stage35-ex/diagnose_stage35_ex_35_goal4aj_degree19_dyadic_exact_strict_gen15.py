#!/usr/bin/env python3
"""Goal4AJ gen15: centered dyadic lift and exact characteristic-zero strict test.

Gen11 found a unique degree-19 strict section over F_32009. Its coefficients
visibly admit a natural dyadic interpretation. This leaf does not assume that
interpretation is correct: it constructs the deterministic centered lift of
8*q_mod and then verifies that literal integer polynomial directly against all
22 source-locked strict symbolic-power conditions over Q(i,sqrt(2)).

Passing this diagnostic materializes only an exact Q-valued degree-19 strict
candidate. A1 exceptional jets are not checked here, so no full degree-19
denominator, degree-31 denominator, F_B, local-evaluation, E1, Stage35, theorem,
or endpoint credit is granted.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN11 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_truncated_strict_kernel_gen11.py"
PARENT = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_denominator_strict_intersection.py"

GEN11_BLOB = "1722fdf949915443985ce1c512b4d5474b18cd1e"
PARENT_BLOB = "1b2d1079b39333aceb97fb52894a4fa4048d6d67"
GEN11_CANONICAL_SHA256 = "8c457f6c9a89f89548c382e1d371298e8ca45022e526a4a09f2618e364b2ab1f"
GEN11_RUN = 34151421440
GEN11_JOB = 101834380178
GEN14_RUN = 34173380623
GEN14_JOB = 101897943850
GEN14_CANONICAL_SHA256 = "967531fd620bc9e598fd1bae321c0a9eb92caf20960d7a7aae90c1a9b4195f48"
MODULAR_CANDIDATE_SHA256 = "a9fb2003a380d1855250dc0a556940f31e2c20c1c86cb69d5f52c56b4538d6a5"
FIELD_PRIME = 32009
DEGREE = 19
LIFT_MULTIPLIER = 8
EXPECTED_STEPS = [
    (37,13),(39,13),(26,9),(31,9),(58,9),(60,9),(25,7),(32,7),
    (1,3),(8,3),(9,3),(17,3),(11,2),(21,2),(33,2),(35,2),
    (16,1),(24,1),(28,1),(29,1),(65,1),(67,1),
]


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN11) == GEN11_BLOB
assert git_blob(PARENT) == PARENT_BLOB

# Rerun the source-locked modular computation, but keep its large polynomial
# runner-local. Only compact commitments and exact-lift diagnostics are emitted.
cp = subprocess.run(
    [sys.executable, "-B", str(GEN11)],
    text=True,
    capture_output=True,
    timeout=300,
)
if cp.returncode != 0:
    raise SystemExit("source-locked gen11 rerun failed")
lines = cp.stdout.splitlines()
json_line = next((x for x in lines if x.startswith("GOAL4AJ_DEN_TRUNC_GEN11_JSON=")), None)
cand_line = next((x for x in lines if x.startswith("GOAL4AJ_DEN_TRUNC_CANDIDATE_1=")), None)
if json_line is None or cand_line is None or "GOAL4AJ_DEN_TRUNC_GEN11=PASS" not in lines:
    raise SystemExit("gen11 output markers moved")
g11 = json.loads(json_line.split("=", 1)[1])
assert g11["canonical_sha256"] == GEN11_CANONICAL_SHA256
assert g11["strict_condition_section_space_degree19_dimension"] == 1
assert [(r["strict_index_1based"], r["multiplicity"]) for r in g11["step_rows"]] == EXPECTED_STEPS
candidate = cand_line.split("=", 1)[1]
assert hashlib.sha256(candidate.encode()).hexdigest() == MODULAR_CANDIDATE_SHA256
assert len(candidate.encode()) == 35004

# Parse Singular's flat polynomial text. The emitted candidate contains only
# signed integer coefficients and monomial factors; no parenthesized sums.
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
    if not mon:
        raise SystemExit("constant term unexpectedly present")
    if mon in term_map:
        raise SystemExit("duplicate monomial in gen11 candidate")
    term_map[mon] = coeff % FIELD_PRIME
if not term_map:
    raise SystemExit("candidate parse produced no terms")

def centered(v: int) -> int:
    v %= FIELD_PRIME
    return v - FIELD_PRIME if v > FIELD_PRIME // 2 else v

lifted = [(mon, centered(LIFT_MULTIPLIER * coeff)) for mon, coeff in term_map.items()]
if any(z == 0 for _, z in lifted):
    raise SystemExit("nonzero modular term vanished in lift")
for mon, z in lifted:
    if z % FIELD_PRIME != (LIFT_MULTIPLIER * term_map[mon]) % FIELD_PRIME:
        raise SystemExit("coefficientwise modular lift mismatch")

def format_term(z: int, mon: str, first: bool) -> str:
    sign = "-" if z < 0 else "+"
    a = abs(z)
    body = mon if a == 1 else f"{a}*{mon}"
    if first:
        return ("-" if z < 0 else "") + body
    return sign + body

pieces = []
for k, (mon, z) in enumerate(lifted):
    pieces.append(format_term(z, mon, k == 0))
qz = "".join(pieces)
qz_sha256 = hashlib.sha256(qz.encode()).hexdigest()
coeff_gcd = 0
for _, z in lifted:
    coeff_gcd = math.gcd(coeff_gcd, abs(z))
max_abs = max(abs(z) for _, z in lifted)

# Extract the exact characteristic-zero Singular program from the source-locked
# parent. It works in Q(u), u^4+1=0, with i=u^2 and sqrt(2)=u-u^3.
tree = ast.parse(PARENT.read_text(encoding="utf-8"))
parent_singular = None
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        t = node.targets[0]
        if isinstance(t, ast.Name) and t.id == "SINGULAR":
            parent_singular = ast.literal_eval(node.value)
            break
if not isinstance(parent_singular, str):
    raise SystemExit("source-locked parent SINGULAR program not found")
if "ring r=(0,u),(a1,a2,a3,b1,b2,b3,c),dp;" not in parent_singular:
    raise SystemExit("parent characteristic-zero coefficient field moved")
if "minpoly=u^4+1;" not in parent_singular:
    raise SystemExit("parent number-field minpoly moved")

# Insert the literal Q polynomial after the parent's surface/current setup.
s = parent_singular
anchor = "ideal Current=surf;"
if anchor not in s:
    raise SystemExit("parent Current initialization moved")
s = s.replace(
    anchor,
    anchor
    + "\npoly qDyadic="
    + qz
    + ";\nideal SurfDyadicStd=std(surf);\nqDyadic=reduce(qDyadic,SurfDyadicStd);"
    + '\nif (qDyadic==0) { ERROR("dyadic lift collapsed modulo surface"); }',
    1,
)

# Replace only the expensive cumulative intersections. Each exact symbolic power
# T is still constructed by the parent's source-locked sympow procedure, and the
# candidate is reduced directly against std(T). Thus every one of the 22 strict
# conditions is checked in characteristic zero without cumulative Groebner growth.
pat = re.compile(
    r"T=sympow\(P,(\d+)\);\n"
    r"Current=intersect\(Current,T\);\n"
    r"Current=std\(Current\);"
)
step_counter = 0

def repl(m: re.Match[str]) -> str:
    global step_counter
    step_counter += 1
    if step_counter > len(EXPECTED_STEPS):
        raise SystemExit("parent has too many strict blocks")
    idx, expected_e = EXPECTED_STEPS[step_counter - 1]
    got_e = int(m.group(1))
    if got_e != expected_e:
        raise SystemExit(
            f"parent strict multiplicity moved at step {step_counter}: {got_e}!={expected_e}"
        )
    return (
        f"T=sympow(P,{got_e});\n"
        f"ideal ExactTStd{step_counter}=std(T);\n"
        f"poly ExactRR{step_counter}=reduce(qDyadic,ExactTStd{step_counter});\n"
        f'if (ExactRR{step_counter}==0) '
        f'{{ print("GOAL4AJ_DYADIC_EXACT_STRICT_NODE={step_counter}:{idx}:{got_e}:PASS"); }} '
        f'else {{ print("GOAL4AJ_DYADIC_EXACT_STRICT_NODE={step_counter}:{idx}:{got_e}:FAIL"); }}'
    )

s, nblocks = pat.subn(repl, s)
if nblocks != 22 or step_counter != 22:
    raise SystemExit(f"parent strict block count moved: {nblocks}")

# The parent's final saturation concerns its cumulative ideal and is not part of
# this membership-only exact replay.
cut = "list FinalSatL=sat(Current,Sing);"
if cut not in s:
    raise SystemExit("parent final tail marker moved")
s = s.split(cut, 1)[0]
s += '\nprint("GOAL4AJ_DYADIC_EXACT_STRICT_SINGULAR_DONE=PASS");\nquit;\n'

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-dyadic-exact-strict-gen15.sing"
    src.write_text(s, encoding="utf-8")
    try:
        scp = subprocess.run(
            ["Singular", "-q", str(src)],
            text=True,
            capture_output=True,
            timeout=1500,
        )
        timed_out = False
        sout, serr, rc = scp.stdout, scp.stderr, scp.returncode
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
    if line.startswith("GOAL4AJ_DYADIC_EXACT_STRICT_NODE="):
        step, idx, e, status = line.split("=", 1)[1].split(":")
        rows.append(
            {
                "step": int(step),
                "strict_index_1based": int(idx),
                "multiplicity": int(e),
                "status": status,
            }
        )
error_text = any(
    t in sout.lower()
    for t in ("error occurred", "? error", "? cannot", "? wrong", "? member", "? assign")
)
completed = (
    not timed_out
    and rc == 0
    and not error_text
    and len(rows) == 22
    and [(r["strict_index_1based"], r["multiplicity"]) for r in rows] == EXPECTED_STEPS
    and "GOAL4AJ_DYADIC_EXACT_STRICT_SINGULAR_DONE=PASS" in sout
)
if not completed:
    if serr:
        print("GOAL4AJ_DYADIC_EXACT_STRICT_GEN15_STDERR=" + json.dumps(serr[-8000:]))
    print("GOAL4AJ_DYADIC_EXACT_STRICT_GEN15_STDOUT_TAIL=" + json.dumps(sout[-12000:]))
    raise SystemExit("Goal4AJ gen15 characteristic-zero strict replay did not complete")

passed = sum(r["status"] == "PASS" for r in rows)
all_pass = passed == 22
route = (
    "DYADIC_INTEGER_LIFT_EXACTLY_SATISFIES_ALL_22_STRICT_CONDITIONS"
    if all_pass
    else "CENTERED_DYADIC_LIFT_REJECTED_BY_EXACT_STRICT_CONDITION"
)
out = {
    "schema": "STAGE35_EX_GOAL4AJ_DEGREE19_DYADIC_EXACT_STRICT_GEN15_DIAGNOSTIC_V1",
    "source_locks": {
        "gen11_script_blob_sha1": GEN11_BLOB,
        "gen11_canonical_sha256": GEN11_CANONICAL_SHA256,
        "gen11_success_run": GEN11_RUN,
        "gen11_success_job": GEN11_JOB,
        "parent_strict_intersection_blob_sha1": PARENT_BLOB,
        "gen14_success_run": GEN14_RUN,
        "gen14_success_job": GEN14_JOB,
        "gen14_canonical_sha256": GEN14_CANONICAL_SHA256,
    },
    "modular_field": f"F_{FIELD_PRIME}",
    "degree": DEGREE,
    "modular_candidate_sha256": MODULAR_CANDIDATE_SHA256,
    "lift_multiplier": LIFT_MULTIPLIER,
    "lift_rule": "coefficientwise centered representative of 8*q_mod modulo 32009",
    "integer_lift_sha256": qz_sha256,
    "integer_lift_term_count": len(lifted),
    "integer_lift_coefficient_gcd": coeff_gcd,
    "integer_lift_max_abs_coefficient": max_abs,
    "coefficient_field_exact_replay": "Q(u)/(u^4+1), i=u^2, sqrt2=u-u^3",
    "strict_condition_count": 22,
    "exact_strict_checked_count": len(rows),
    "exact_strict_passed_count": passed,
    "all_22_exact_strict_conditions_pass": all_pass,
    "rows": rows,
    "route_result": route,
    "q_literal_degree19_strict_candidate_materialized": all_pass,
    "a1_exceptional_jets_exactly_verified": False,
    "q_literal_degree19_denominator_materialized": False,
    "q_literal_degree31_denominator_materialized": False,
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
print(
    "GOAL4AJ_DYADIC_EXACT_STRICT_GEN15_JSON="
    + json.dumps(out, sort_keys=True, separators=(",", ":")),
    flush=True,
)
print("GOAL4AJ_DYADIC_EXACT_STRICT_GEN15=DONE", flush=True)
