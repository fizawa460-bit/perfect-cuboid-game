#!/usr/bin/env python3
"""Goal4AJ gen16: materialize the literal degree-31 denominator.

Source-locked inputs:
- the passing Q-hyperplane peel selects singleton complete-hyperplane orbit 0
  once and singleton orbit 3 eleven times on the denominator side;
- gen15-g2 materializes the exact primitive Q-coefficient degree-19 residual
  section, whose divisor is identified with the locked residual divisor by the
  provisional exact exceptional bridge.

This leaf reconstructs the two selected Q-linear forms, rebuilds the exact
primitive degree-19 lift, expands q19*L0*L3^11, primitive-normalizes the degree-31
integer coefficient vector, and emits the literal polynomial when it fits the
bounded log contract. Diagnostic only: numerator/F_B/local/BM/E1/Stage35/theorem/
endpoint credit remains false.
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
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QPEEL = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_q_hyperplane_factor_peel.py"
GEN11 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_truncated_strict_kernel_gen11.py"
BRIDGE = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree19-exceptional-forced-from-strict-source-lock.md"

QPEEL_BLOB = "e5b41410e570d5e442afe985dd5b7f3355d5d653"
GEN11_BLOB = "1722fdf949915443985ce1c512b4d5474b18cd1e"
BRIDGE_BLOB = "c125b09be3fcf572e5264f0c0b1db41ae9b74cf2"
QPEEL_CANONICAL = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
QPEEL_RUN = 34092066114
QPEEL_JOB = 101647794285
GEN11_CANONICAL = "8c457f6c9a89f89548c382e1d371298e8ca45022e526a4a09f2618e364b2ab1f"
GEN15_G2_CANONICAL = "2a6b8b80ed8bca3b1801ac0a5a7f0300ee9ea33a6019fc4866605dd74fcb3a97"
GEN15_G2_RUN = 34180606310
GEN15_G2_JOB = 101918803163
Q19_SHA256 = "4acafb5681e92aae5f63efa101de72e0795d30cf4d81d936e7ef02c73dc0c7ea"
MODULAR_CANDIDATE_SHA256 = "a9fb2003a380d1855250dc0a556940f31e2c20c1c86cb69d5f52c56b4538d6a5"
FIELD_PRIME = 32009
LIFT_MULTIPLIER = 8
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
MAX_LITERAL_LOG_BYTES = 100000


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(QPEEL) == QPEEL_BLOB
assert git_blob(GEN11) == GEN11_BLOB
assert git_blob(BRIDGE) == BRIDGE_BLOB

# Reconstruct the exact 31 complete hyperplanes and source-lock the old peel.
buf = io.StringIO()
with redirect_stdout(buf):
    qns = runpy.run_path(str(QPEEL))
qout = qns["out"]
assert qout["canonical_sha256"] == QPEEL_CANONICAL
assert qout["denominator"]["peeled_linear_degree"] == 12
selected = qout["denominator"]["orbit_multiplicities"]
assert selected == [
    {"orbit_hyperplane_indices_0based": [0], "orbit_size": 1, "multiplicity": 1},
    {"orbit_hyperplane_indices_0based": [3], "orbit_size": 1, "multiplicity": 11},
]
complete = qns["complete"]
assert len(complete) == 31


def kcoord_to_q(x) -> Fraction:
    # qpeel stores each K=Q(i,sqrt2) coefficient in basis 1,i,s,is.
    fs = [Fraction(int(a), int(b)) for a, b in x]
    if any(fs[j] != 0 for j in range(1, 4)):
        raise SystemExit("selected singleton hyperplane is not Q-normalized")
    return fs[0]


def primitive_linear(form) -> tuple[int, ...]:
    q = [kcoord_to_q(x) for x in form]
    den = 1
    for x in q:
        den = math.lcm(den, x.denominator)
    z = [int(x * den) for x in q]
    g = 0
    for x in z:
        g = math.gcd(g, abs(x))
    if g == 0:
        raise SystemExit("zero hyperplane form")
    z = [x // g for x in z]
    first = next(x for x in z if x)
    if first < 0:
        z = [-x for x in z]
    return tuple(z)


L0 = primitive_linear(complete[0][0])
L3 = primitive_linear(complete[3][0])

# Rebuild exactly the same modular candidate and centered 8*q lift as gen15.
cp = subprocess.run([sys.executable, "-B", str(GEN11)], text=True, capture_output=True, timeout=300)
if cp.returncode != 0:
    raise SystemExit("source-locked gen11 rerun failed")
lines = cp.stdout.splitlines()
jline = next((x for x in lines if x.startswith("GOAL4AJ_DEN_TRUNC_GEN11_JSON=")), None)
cline = next((x for x in lines if x.startswith("GOAL4AJ_DEN_TRUNC_CANDIDATE_1=")), None)
if jline is None or cline is None or "GOAL4AJ_DEN_TRUNC_GEN11=PASS" not in lines:
    raise SystemExit("gen11 markers moved")
g11 = json.loads(jline.split("=", 1)[1])
assert g11["canonical_sha256"] == GEN11_CANONICAL
candidate = cline.split("=", 1)[1]
assert hashlib.sha256(candidate.encode()).hexdigest() == MODULAR_CANDIDATE_SHA256


def centered(v: int) -> int:
    v %= FIELD_PRIME
    return v - FIELD_PRIME if v > FIELD_PRIME // 2 else v


def parse_mon(mon: str) -> tuple[int, ...]:
    ex = [0] * 7
    for f in mon.split("*"):
        if "^" in f:
            n, e = f.split("^", 1)
            e = int(e)
        else:
            n, e = f, 1
        ex[NAMES.index(n)] += e
    return tuple(ex)


q19_ordered: list[tuple[str, int]] = []
q19: dict[tuple[int, ...], int] = {}
for m in re.finditer(r"([+-]?)([^+-]+)", candidate):
    sign_s, body = m.groups()
    sign = -1 if sign_s == "-" else 1
    fac = body.split("*")
    if fac[0].isdigit():
        c = sign * int(fac[0])
        mon = "*".join(fac[1:])
    else:
        c = sign
        mon = body
    z = centered(LIFT_MULTIPLIER * (c % FIELD_PRIME))
    exp = parse_mon(mon)
    if exp in q19:
        raise SystemExit("duplicate q19 monomial")
    q19[exp] = z
    q19_ordered.append((mon, z))
assert len(q19) == 1542
assert all(sum(e) == 19 for e in q19)

# Reproduce gen15's literal q19 string commitment.
def old_term(z: int, mon: str, first: bool) -> str:
    a = abs(z)
    body = mon if a == 1 else f"{a}*{mon}"
    if first:
        return ("-" if z < 0 else "") + body
    return ("-" if z < 0 else "+") + body

q19_text = "".join(old_term(z, mon, k == 0) for k, (mon, z) in enumerate(q19_ordered))
assert hashlib.sha256(q19_text.encode()).hexdigest() == Q19_SHA256


def mul_poly(A: dict[tuple[int, ...], int], B: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    C: dict[tuple[int, ...], int] = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = tuple(ea[j] + eb[j] for j in range(7))
            C[e] = C.get(e, 0) + ca * cb
    return {e: c for e, c in C.items() if c}


def linear_poly(v: tuple[int, ...]) -> dict[tuple[int, ...], int]:
    out = {}
    for j, c in enumerate(v):
        if c:
            e = [0] * 7
            e[j] = 1
            out[tuple(e)] = c
    return out

factor = {(0, 0, 0, 0, 0, 0, 0): 1}
factor = mul_poly(factor, linear_poly(L0))
for _ in range(11):
    factor = mul_poly(factor, linear_poly(L3))
assert all(sum(e) == 12 for e in factor)

q31 = mul_poly(q19, factor)
assert q31 and all(sum(e) == 31 for e in q31)

# Primitive/sign normalization gives one deterministic Q-polynomial representative.
g = 0
for c in q31.values():
    g = math.gcd(g, abs(c))
assert g > 0
q31 = {e: c // g for e, c in q31.items()}
first_exp = sorted(q31)[0]
if q31[first_exp] < 0:
    q31 = {e: -c for e, c in q31.items()}


def mon_text(e: tuple[int, ...]) -> str:
    fs = []
    for n, k in zip(NAMES, e):
        if k == 1:
            fs.append(n)
        elif k > 1:
            fs.append(f"{n}^{k}")
    return "*".join(fs) if fs else "1"


def polynomial_text(P: dict[tuple[int, ...], int]) -> str:
    out = []
    for k, e in enumerate(sorted(P)):
        c = P[e]
        mon = mon_text(e)
        a = abs(c)
        body = mon if a == 1 else f"{a}*{mon}"
        if k == 0:
            out.append(("-" if c < 0 else "") + body)
        else:
            out.append(("-" if c < 0 else "+") + body)
    return "".join(out)

literal = polynomial_text(q31)
literal_bytes = len(literal.encode())
literal_sha = hashlib.sha256(literal.encode()).hexdigest()
stream = "".join(
    ",".join(map(str, e)) + ":" + str(q31[e]) + "\n" for e in sorted(q31)
)
stream_sha = hashlib.sha256(stream.encode()).hexdigest()
max_abs = max(abs(c) for c in q31.values())
persist_literal = literal_bytes <= MAX_LITERAL_LOG_BYTES

out = {
    "schema": "STAGE35_EX_GOAL4AJ_DEGREE31_DENOMINATOR_MATERIALIZE_GEN16_DIAGNOSTIC_V1",
    "source_locks": {
        "q_hyperplane_peel_blob_sha1": QPEEL_BLOB,
        "q_hyperplane_peel_canonical_sha256": QPEEL_CANONICAL,
        "q_hyperplane_peel_run": QPEEL_RUN,
        "q_hyperplane_peel_job": QPEEL_JOB,
        "gen11_blob_sha1": GEN11_BLOB,
        "gen11_canonical_sha256": GEN11_CANONICAL,
        "gen15_g2_canonical_sha256": GEN15_G2_CANONICAL,
        "gen15_g2_run": GEN15_G2_RUN,
        "gen15_g2_job": GEN15_G2_JOB,
        "degree19_exceptional_bridge_blob_sha1": BRIDGE_BLOB,
    },
    "degree19_residual_integer_sha256": Q19_SHA256,
    "degree19_term_count": len(q19),
    "selected_denominator_hyperplane_orbits": selected,
    "L0_primitive_Q_coefficients_a1_a2_a3_b1_b2_b3_c": list(L0),
    "L3_primitive_Q_coefficients_a1_a2_a3_b1_b2_b3_c": list(L3),
    "factorization": "q19 * L0 * L3^11",
    "peeled_factor_degree": 12,
    "factor_expanded_term_count": len(factor),
    "degree31": 31,
    "degree31_expanded_term_count": len(q31),
    "degree31_primitive_gcd": 1,
    "degree31_max_abs_coefficient": max_abs,
    "degree31_literal_text_bytes": literal_bytes,
    "degree31_literal_sha256": literal_sha,
    "degree31_coefficient_stream_sha256": stream_sha,
    "degree31_literal_persisted_in_actions_log": persist_literal,
    "literal_q_polynomial_factor_normalization_materialized": True,
    "q_literal_degree19_denominator_materialized": True,
    "q_literal_degree31_denominator_materialized": persist_literal,
    "literal_denominator_coefficients_materialized": persist_literal,
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
print("GOAL4AJ_DEN31_GEN16_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
if persist_literal:
    print("GOAL4AJ_DEN31_LITERAL=" + literal, flush=True)
else:
    print("GOAL4AJ_DEN31_LITERAL=OMITTED_LOG_BOUND", flush=True)
print("GOAL4AJ_DEN31_GEN16=DONE", flush=True)
