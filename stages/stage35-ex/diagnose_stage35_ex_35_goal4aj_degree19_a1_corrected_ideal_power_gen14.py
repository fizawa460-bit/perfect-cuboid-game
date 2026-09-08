#!/usr/bin/env python3
"""Goal4AJ gen14: replay gen12 A1 jets with actual ideal powers P^e.

Gen12 used power(P,e).  Gen13 then showed an internal contradiction: every
positive target node passes first-order membership in surf+P, while gen12
reported FAIL even at the four nodes with e=1.  This leaf changes exactly the
jet-power construction to Singular ideal exponentiation P^e, retaining the
same candidate, node locator, projective-chart saturation, and A1 targets.

Diagnostic only.  A modular success does not materialize a Q-section and gives
no F_B/local-evaluation/E1/Stage35/theorem/endpoint credit.
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
LOCATOR = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_retained140_component_locator.py"
A1 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_a1_exceptional_valuation.py"

GEN11_BLOB = "1722fdf949915443985ce1c512b4d5474b18cd1e"
LOCATOR_BLOB = "978207d2a854b24a7d532ece93a016222a979ff1"
A1_BLOB = "096a3699d32522c3fb7556f398e5f2d39a2866d9"
GEN11_CANONICAL_SHA256 = "8c457f6c9a89f89548c382e1d371298e8ca45022e526a4a09f2618e364b2ab1f"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
LOCATOR_NODE_SHA256 = "5f562c9c06c31119dfbdccc746f3f980a0e6e6de84d4c4d3971ef8a7bf67a2f0"
GEN12_FAILED_RUN = 34162971655
GEN12_FAILED_JOB = 101868422186
GEN12_FAILED_CANONICAL_SHA256 = "dc2bb44ade74d518dc1b54ba279219c174a2edc634ad67c40ed6db7eca6ec776"
GEN13_SUCCESS_RUN = 34172951309
GEN13_SUCCESS_JOB = 101896701915
GEN13_CANONICAL_SHA256 = "21e9a9087e0ca955afe3ae66b5b7b352bb806cb599b9f483af92844e733def23"
FIELD_PRIME = 32009
I_ROOT = 10754
SQRT2_ROOT = 8047
DEGREE = 19
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN11) == GEN11_BLOB
assert git_blob(LOCATOR) == LOCATOR_BLOB
assert git_blob(A1) == A1_BLOB
assert pow(I_ROOT, 2, FIELD_PRIME) == FIELD_PRIME - 1
assert pow(SQRT2_ROOT, 2, FIELD_PRIME) == 2

cp = subprocess.run(
    [sys.executable, "-B", str(GEN11)], text=True, capture_output=True, timeout=300
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
candidate = cand_line.split("=", 1)[1]
assert len(candidate.encode()) == 35004
candidate_sha256 = hashlib.sha256(candidate.encode()).hexdigest()

buf = io.StringIO()
with redirect_stdout(buf):
    loc_ns = runpy.run_path(str(LOCATOR))
node_map = loc_ns["node_map"]
locator_out = loc_ns["out"]
assert locator_out["canonical_sha256"] == LOCATOR_CANONICAL_SHA256
assert locator_out["exceptional_node_locator_sha256"] == LOCATOR_NODE_SHA256
assert len(node_map) == 48

buf = io.StringIO()
with redirect_stdout(buf):
    a1_ns = runpy.run_path(str(A1))
denr = {int(k): int(v) for k, v in a1_ns["DENR"].items()}
assert sorted(denr) == list(range(93, 141))
assert sum(v > 0 for v in denr.values()) == 44
assert max(denr.values()) == 18


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

surf = "ideal surf=a1^2+a2^2-b3^2,a2^2+a3^2-b1^2,a1^2+a3^2-b2^2,a1^2+a2^2+a3^2-c^2;"
sparts = [
    'LIB "elim.lib";',
    f"ring r={FIELD_PRIME},(a1,a2,a3,b1,b2,b3,c),dp;",
    surf,
    "ideal SurfStd=std(surf);",
    f"poly q={candidate};",
    "q=reduce(q,SurfStd);",
    'if (q==0) { ERROR("candidate collapsed modulo surface"); }',
]
for j, e, chart, vals in rows:
    if e == 0:
        sparts.append(f'print("GOAL4AJ_A1_CORRECTED_NODE={j}:0:SKIP");')
        continue
    xk = NAMES[chart]
    gens = [
        f"{name}-{vals[idx]}*{xk}"
        for idx, name in enumerate(NAMES)
        if idx != chart
    ]
    sparts += [
        "ideal P=" + ",".join(gens) + ";",
        f"ideal Pe=P^{e};",
        "ideal J=surf+Pe;",
        f"list JL=sat(J,ideal({xk}));",
        "ideal JS=std(JL[1]);",
        "poly rr=reduce(q,JS);",
        f'if (rr==0) {{ print("GOAL4AJ_A1_CORRECTED_NODE={j}:{e}:PASS"); }} else {{ print("GOAL4AJ_A1_CORRECTED_NODE={j}:{e}:FAIL"); }}',
    ]
sparts += ['print("GOAL4AJ_A1_CORRECTED_SINGULAR_DONE=PASS");', "quit;"]
program = "\n".join(sparts) + "\n"

with tempfile.TemporaryDirectory() as td:
    src = Path(td) / "goal4aj-a1-corrected-gen14.sing"
    src.write_text(program, encoding="utf-8")
    try:
        scp = subprocess.run(
            ["Singular", "-q", str(src)], text=True, capture_output=True, timeout=1200
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
    if line.startswith("GOAL4AJ_A1_CORRECTED_NODE="):
        j, e, status = line.split("=", 1)[1].split(":")
        node_results[int(j)] = {"target_order": int(e), "status": status}
error_text = any(t in sout.lower() for t in ("error occurred", "? error", "? cannot", "? wrong"))
checked = sum(v["target_order"] > 0 for v in node_results.values())
passed = sum(v["target_order"] > 0 and v["status"] == "PASS" for v in node_results.values())
completed = (
    not timed_out
    and rc == 0
    and not error_text
    and len(node_results) == 48
    and checked == 44
    and "GOAL4AJ_A1_CORRECTED_SINGULAR_DONE=PASS" in sout
)
if not completed:
    if serr:
        print("GOAL4AJ_A1_CORRECTED_GEN14_STDERR=" + json.dumps(serr[-8000:]))
    raise SystemExit("Goal4AJ gen14 corrected ideal-power replay did not complete")

all_pass = passed == 44
order1_nodes = [j for j in range(93, 141) if denr[j] == 1]
order1_all_pass = all(node_results[j]["status"] == "PASS" for j in order1_nodes)
route = (
    "GEN12_POWER_CALL_WALL_REMOVED_ALL_A1_TARGETS_PASS"
    if all_pass
    else "CORRECTED_IDEAL_POWER_STILL_HAS_HIGHER_ORDER_FAILURES"
)
out = {
    "schema": "STAGE35_EX_GOAL4AJ_DEGREE19_A1_CORRECTED_IDEAL_POWER_GEN14_DIAGNOSTIC_V1",
    "source_locks": {
        "gen11_script_blob_sha1": GEN11_BLOB,
        "gen11_canonical_sha256": GEN11_CANONICAL_SHA256,
        "retained140_locator_blob_sha1": LOCATOR_BLOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "retained140_node_locator_sha256": LOCATOR_NODE_SHA256,
        "a1_exceptional_valuation_blob_sha1": A1_BLOB,
        "gen12_failed_run": GEN12_FAILED_RUN,
        "gen12_failed_job": GEN12_FAILED_JOB,
        "gen12_failed_canonical_sha256": GEN12_FAILED_CANONICAL_SHA256,
        "gen13_success_run": GEN13_SUCCESS_RUN,
        "gen13_success_job": GEN13_SUCCESS_JOB,
        "gen13_canonical_sha256": GEN13_CANONICAL_SHA256,
    },
    "coefficient_field": f"F_{FIELD_PRIME}",
    "degree": DEGREE,
    "candidate_sha256": candidate_sha256,
    "candidate_text_bytes": len(candidate.encode()),
    "strict_condition_section_space_dimension": 1,
    "jet_power_operator": "Singular ideal exponentiation P^e",
    "legacy_gen12_power_call_reused": False,
    "checked_nonzero_target_count": checked,
    "passed_nonzero_target_count": passed,
    "order1_target_nodes": order1_nodes,
    "order1_target_all_pass": order1_all_pass,
    "all_44_a1_targets_pass_corrected_ideal_power": all_pass,
    "node_results": {str(k): v for k, v in sorted(node_results.items())},
    "route_result": route,
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
print("GOAL4AJ_A1_CORRECTED_GEN14_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_A1_CORRECTED_GEN14=DONE", flush=True)
