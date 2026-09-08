#!/usr/bin/env python3
"""Goal4AJ gen13: first-order A1/incidence consistency audit after gen12 wall.

Gen12 found that the unique modular degree-19 strict-condition candidate failed
all 44 nonzero exceptional target orders.  This leaf does not reinterpret that
as nonexistence.  It checks the cheaper compatibility that must hold before any
higher A1 jet condition is meaningful:

1. for every retained A1 exceptional E, the post-peel divisor packet satisfies
      sum_{strict C incident to E} mult(C) = 2 * mult(E),
   using C.E=1, E^2=-2, and H.E=0;
2. the unique gen11 degree-19 candidate vanishes to at least first order at
   every node with positive residual exceptional target.

If (1) holds but (2) fails, the remaining wall is a section/locator/symbolic
adapter mismatch rather than a mathematical nonexistence statement.  If both
hold, gen12's failure is genuinely confined to higher-order jet translation or
higher-order section membership.

Diagnostic only: no Q-literal section, F_B, local Brauer evaluation, E1,
Stage35, theorem, receiver, or endpoint credit is granted.
"""
from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
GEN11 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_truncated_strict_kernel_gen11.py"
GEN12 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree19_a1_candidate_check_gen12.py"
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
A1 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_a1_exceptional_valuation.py"
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"

GEN11_BLOB = "1722fdf949915443985ce1c512b4d5474b18cd1e"
GEN12_BLOB = "56b72500b03cc6d1d50cf73b5ec71e87f8bf096e"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
A1_BLOB = "096a3699d32522c3fb7556f398e5f2d39a2866d9"
ACTIVE_BLOB = "20da16902171b267294acee0f3b80997d8fd5246"
GEN11_CANONICAL_SHA256 = "8c457f6c9a89f89548c382e1d371298e8ca45022e526a4a09f2618e364b2ab1f"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
LOCATOR_NODE_SHA256 = "5f562c9c06c31119dfbdccc746f3f980a0e6e6de84d4c4d3971ef8a7bf67a2f0"
A1_CANONICAL_SHA256 = "b98f761bf26edfc9af060934a9921722b85b9a867b0716360ab38950d53d4a66"
ACTIVE_CANONICAL_SHA256 = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
GEN12_FAILED_RUN = 34162971655
GEN12_FAILED_JOB = 101868422186
GEN12_FAILED_CANONICAL_SHA256 = "dc2bb44ade74d518dc1b54ba279219c174a2edc634ad67c40ed6db7eca6ec776"
FIELD_PRIME = 32009
I_ROOT = 10754
SQRT2_ROOT = 8047
DEGREE = 19
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN11) == GEN11_BLOB
assert git_blob(GEN12) == GEN12_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB
assert git_blob(A1) == A1_BLOB
assert git_blob(ACTIVE) == ACTIVE_BLOB
assert pow(I_ROOT, 2, FIELD_PRIME) == FIELD_PRIME - 1
assert pow(SQRT2_ROOT, 2, FIELD_PRIME) == 2

# Recompute the exact source-locked unique strict candidate without streaming it.
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
assert g11["strict_degree19_kernel_completed"] is True
assert g11["strict_condition_section_space_degree19_dimension"] == 1
assert g11["degree19_candidate_standard_basis_count_capped3"] == 1
candidate = cand_line.split("=", 1)[1]
candidate_sha256 = hashlib.sha256(candidate.encode()).hexdigest()
assert len(candidate.encode()) == 35004

# Rebuild compact source-locked packets.
buf = io.StringIO()
with redirect_stdout(buf):
    loc_ns = runpy.run_path(str(LOCATOR))
locator_out = loc_ns["out"]
node_map = loc_ns["node_map"]
assert locator_out["canonical_sha256"] == LOCATOR_CANONICAL_SHA256
assert locator_out["exceptional_node_locator_sha256"] == LOCATOR_NODE_SHA256
assert len(node_map) == 48

buf = io.StringIO()
with redirect_stdout(buf):
    a1_ns = runpy.run_path(str(A1))
a1_out = a1_ns["out"]
denr = {int(k): int(v) for k, v in a1_ns["DENR"].items()}
assert a1_out["canonical_sha256"] == A1_CANONICAL_SHA256
assert sorted(denr) == list(range(93, 141))

buf = io.StringIO()
with redirect_stdout(buf):
    active_ns = runpy.run_path(str(ACTIVE))
active_out = active_ns["out"]
assert active_out["canonical_sha256"] == ACTIVE_CANONICAL_SHA256
strict = {
    int(k): int(v)
    for k, v in active_out["denominator_residual"]["strict_multiplicities_1based"].items()
}
assert len(strict) == 22
assert sum(strict.values()) == 102

# Exact divisor-incidence compatibility on the resolution:
# H.E=0, E^2=-2, distinct exceptionals are disjoint, and C.E is the locator's
# retained 0/1 incidence pairing.  Thus a divisor of class 19H must satisfy
# sum_C m_C(C.E) - 2e_E = 0 at every exceptional.
incidence_rows = {}
for j in range(93, 141):
    sig = [int(i) for i in node_map[str(j)]["incident_strict_curve_indices_1based"]]
    inc_sum = sum(strict.get(i, 0) for i in sig)
    target = denr[j]
    incidence_rows[str(j)] = {
        "target_order": target,
        "active_strict_incidence_multiplicity_sum": inc_sum,
        "twice_target_order": 2 * target,
        "relation_holds": inc_sum == 2 * target,
    }
incidence_ok = all(r["relation_holds"] for r in incidence_rows.values())


def frac_mod(pair: list[int]) -> int:
    n, d = pair
    return (n % FIELD_PRIME) * pow(d % FIELD_PRIME, -1, FIELD_PRIME) % FIELD_PRIME


def k_mod(kjson) -> int:
    a, b, c, d = (frac_mod(x) for x in kjson)
    return (a + b * I_ROOT + c * SQRT2_ROOT + d * I_ROOT * SQRT2_ROOT) % FIELD_PRIME


def point_mod(entry) -> list[int]:
    vals = [k_mod(x) for x in entry["projective_coordinates_basis_1_i_s_is"]]
    if not any(vals):
        raise SystemExit("zero projective node")
    return vals


rows = []
for j in range(93, 141):
    vals = point_mod(node_map[str(j)])
    chart = next(k for k, v in enumerate(vals) if v)
    inv = pow(vals[chart], -1, FIELD_PRIME)
    vals = [(v * inv) % FIELD_PRIME for v in vals]
    assert vals[chart] == 1
    rows.append((j, denr[j], chart, vals))

# First-order check only.  The homogeneous point ideal is enough: q belongs to
# it iff q vanishes at that projective node.  Adding surf is a consistency-safe
# no-op because each recovered point lies on the surface.
surf = "ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;"
sparts = [
    f"ring r={FIELD_PRIME},(a1,a2,a3,b1,b2,b3,c),dp;",
    surf,
    "ideal SurfStd=std(surf);",
    f"poly q={candidate};",
    "q=reduce(q,SurfStd);",
    'if (q==0) { ERROR("candidate collapsed modulo surface"); }',
]
for j, e, chart, vals in rows:
    xk = NAMES[chart]
    gens = []
    for idx, name in enumerate(NAMES):
        if idx == chart:
            continue
        gens.append(f"{name}-{vals[idx]}*{xk}")
    sparts += [
        "ideal P=" + ",".join(gens) + ";",
        "ideal PS=std(surf+P);",
        "poly rr=reduce(q,PS);",
        f'if (rr==0) {{ print("GOAL4AJ_A1_FIRST_ORDER_NODE={j}:{e}:PASS"); }} else {{ print("GOAL4AJ_A1_FIRST_ORDER_NODE={j}:{e}:FAIL"); }}',
    ]
sparts += ['print("GOAL4AJ_A1_FIRST_ORDER_SINGULAR_DONE=PASS");', "quit;"]
singular_program = "\n".join(sparts) + "\n"

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-a1-first-order-gen13.sing"
    src.write_text(singular_program, encoding="utf-8")
    try:
        scp = subprocess.run(
            ["Singular", "-q", str(src)],
            text=True,
            capture_output=True,
            timeout=600,
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

node_results = {}
for line in sout.splitlines():
    if line.startswith("GOAL4AJ_A1_FIRST_ORDER_NODE="):
        j, e, status = line.split("=", 1)[1].split(":")
        node_results[int(j)] = {"target_order": int(e), "status": status}
error_text = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong"))
completed = (
    not timed_out
    and rc == 0
    and not error_text
    and len(node_results) == 48
    and "GOAL4AJ_A1_FIRST_ORDER_SINGULAR_DONE=PASS" in sout
)
if not completed:
    if serr:
        print("GOAL4AJ_A1_FIRST_ORDER_GEN13_STDERR=" + json.dumps(serr[-8000:]))
    raise SystemExit("Goal4AJ gen13 first-order audit did not complete")

positive = [j for j in range(93, 141) if denr[j] > 0]
positive_pass = sum(node_results[j]["status"] == "PASS" for j in positive)
all_positive_first_order = positive_pass == len(positive) == 44
all_nodes_first_order = sum(node_results[j]["status"] == "PASS" for j in range(93, 141))

if not incidence_ok:
    route = "DIVISOR_PACKET_EXCEPTIONAL_INCIDENCE_RELATION_MISMATCH"
elif not all_positive_first_order:
    route = "STRICT_CANDIDATE_NODE_MEMBERSHIP_OR_LOCATOR_ADAPTER_MISMATCH"
else:
    route = "FIRST_ORDER_MAPPING_CONSISTENT_GEN12_WALL_IS_HIGHER_ORDER_ONLY"

out = {
    "schema": "STAGE35_EX_GOAL4AJ_DEGREE19_A1_FIRST_ORDER_GEN13_DIAGNOSTIC_V1",
    "source_locks": {
        "gen11_script_blob_sha1": GEN11_BLOB,
        "gen11_canonical_sha256": GEN11_CANONICAL_SHA256,
        "gen12_failed_script_blob_sha1": GEN12_BLOB,
        "gen12_failed_run": GEN12_FAILED_RUN,
        "gen12_failed_job": GEN12_FAILED_JOB,
        "gen12_failed_canonical_sha256": GEN12_FAILED_CANONICAL_SHA256,
        "retained140_locator_blob_sha1": LOCATOR_BLOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "retained140_node_locator_sha256": LOCATOR_NODE_SHA256,
        "a1_exceptional_valuation_blob_sha1": A1_BLOB,
        "a1_exceptional_valuation_canonical_sha256": A1_CANONICAL_SHA256,
        "active_condition_packet_blob_sha1": ACTIVE_BLOB,
        "active_condition_packet_canonical_sha256": ACTIVE_CANONICAL_SHA256,
    },
    "coefficient_field": f"F_{FIELD_PRIME}",
    "degree": DEGREE,
    "candidate_sha256": candidate_sha256,
    "candidate_text_bytes": len(candidate.encode()),
    "strict_condition_section_space_dimension": 1,
    "exceptional_count": 48,
    "positive_exceptional_target_count": len(positive),
    "exceptional_incidence_relation_checked": True,
    "exceptional_incidence_relation_all_48_hold": incidence_ok,
    "incidence_rows": incidence_rows,
    "first_order_node_checks_completed": True,
    "positive_target_first_order_pass_count": positive_pass,
    "positive_target_first_order_total": len(positive),
    "all_positive_target_nodes_pass_first_order": all_positive_first_order,
    "all_48_node_first_order_pass_count": all_nodes_first_order,
    "node_results": {str(k): v for k, v in sorted(node_results.items())},
    "route_result": route,
    "higher_order_a1_conditions_rechecked": False,
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
print("GOAL4AJ_A1_FIRST_ORDER_GEN13_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_A1_FIRST_ORDER_GEN13=DONE", flush=True)
