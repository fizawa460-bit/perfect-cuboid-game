#!/usr/bin/env python3
"""Goal4AJ gen20: independent second-prime replay of the degree-31 numerator strict line.

Gen19 showed that the unique F_32009 line admits a complete one-prime centered
integer reconstruction, but that reconstruction fails the first exact strict
condition.  This diagnostic does not promote that failed lift.  Instead it asks
whether the same 27 strict conditions again cut the degree-31 quotient space to
one dimension at an independent good split prime p=32057.

A second unique modular line is only preflight evidence for a future multi-prime
projective/CRT reconstruction.  It is not a Q lift, literal numerator, F_B,
local evaluation, Brauer-Manin obstruction, E1, Stage35, theorem, receiver, or
endpoint credit.
"""
from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN17 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_truncated_strict_kernel_gen17.py"
GEN19 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_degree31_rational_reconstruction_gen19.py"

GEN17_BLOB = "8631c9818c2431d66dddc861472babf0f53a7b2b"
GEN19_BLOB = "5b6fbb5d66ff21c47f8c18124c869e949311bd5b"
GEN19_RUN = 34186299860
GEN19_JOB = 101935224637
GEN19_CANONICAL = "b01efb62377c5a629e24e7a2006f256610054e238f663a9d184f9626b3a33afd"
GEN19_ROUTE = "ONE_PRIME_RATIONAL_RECONSTRUCTION_COMPLETE_BUT_FIRST_STRICT_EXACT_FAIL"

DEN31_NOTE_BLOB = "95c0eef4a420234964217d3ceb41e57ea5e5b95d"
STRICT_PACKET_OLD = "d3af7bfe3fd390b4af8d6688d6ab885716cff1738400a218f09413dffde6936c"
STRICT_PACKET = "4f9c446900aab6d79e433bf84400e3b82d07ab9c4c38e749c3167d6e449a3717"

P1 = 32009
P1_CANDIDATE_SHA256 = "7d0020181c37b6ee7e203061bda0088ea5f072ac358b275e4b7446b2c40282a5"
P1_TERM_COUNT = 5924
P2 = 32057
P2_I_ROOT = 8059
P2_SQRT2_ROOT = 14662
DEGREE = 31


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


assert git_blob(GEN17) == GEN17_BLOB
assert git_blob(GEN19) == GEN19_BLOB
assert P2 % 8 == 1
assert pow(P2_I_ROOT, 2, P2) == P2 - 1
assert pow(P2_SQRT2_ROOT, 2, P2) == 2

# Patch only the source-locked parameters needed to replay gen17 at p2.
src = GEN17.read_text(encoding="utf-8")
repls = [
    ('DEN31_NOTE_BLOB = "__DEN31_NOTE_BLOB__"', f'DEN31_NOTE_BLOB = "{DEN31_NOTE_BLOB}"'),
    (f'STRICT_PACKET_SHA256 = "{STRICT_PACKET_OLD}"', f'STRICT_PACKET_SHA256 = "{STRICT_PACKET}"'),
    ("FIELD_PRIME = 32009", f"FIELD_PRIME = {P2}"),
    ("I_ROOT = 10754", f"I_ROOT = {P2_I_ROOT}"),
    ("SQRT2_ROOT = 8047", f"SQRT2_ROOT = {P2_SQRT2_ROOT}"),
    ("ring r=32009,(a1,a2,a3,b1,b2,b3,c),dp;", f"ring r={P2},(a1,a2,a3,b1,b2,b3,c),dp;"),
    ("number ii=10754;", f"number ii={P2_I_ROOT};"),
    ("number ss=8047;", f"number ss={P2_SQRT2_ROOT};"),
]
for old, new in repls:
    if src.count(old) != 1:
        raise SystemExit(f"gen20 source patch cardinality mismatch: {old!r}")
    src = src.replace(old, new, 1)

ns = {"__name__": "__main__", "__file__": str(GEN17)}
buf = io.StringIO()
with redirect_stdout(buf):
    exec(compile(src, str(GEN17) + "[gen20-p32057]", "exec"), ns)

g20base = ns["out"]
candidates = ns["candidates"]
assert g20base["field_prime"] == P2
assert g20base["coefficient_field"] == f"F_{P2}"
assert g20base["degree_cap"] == DEGREE
assert g20base["numerator_strict_condition_count"] == 27
assert g20base["numerator_strict_total_multiplicity"] == 202
assert g20base["numerator_strict_kernel_completed"] is True

candidate = candidates[0] if len(candidates) == 1 else None
candidate_sha = hashlib.sha256(candidate.encode()).hexdigest() if candidate is not None else None
candidate_bytes = len(candidate.encode()) if candidate is not None else None
term_count = None
if candidate is not None:
    term_count = 0
    for m in re.finditer(r"([+-]?)([^+-]+)", candidate):
        _, body = m.groups()
        if body:
            term_count += 1

unique_second_prime = (
    g20base["strict_condition_section_space_degree31_dimension"] == 1
    and len(candidates) == 1
)
matching_term_count = unique_second_prime and term_count == P1_TERM_COUNT
route = (
    "SECOND_PRIME_UNIQUE_DEGREE31_LINE_MATCHING_TERM_COUNT_MULTI_PRIME_RECONSTRUCTION_READY"
    if matching_term_count
    else "SECOND_PRIME_RESULT_DOES_NOT_YET_SUPPORT_MATCHED_MULTI_PRIME_RECONSTRUCTION"
)

out = {
    "schema": "STAGE35_EX_GOAL4AJ_NUMERATOR_DEGREE31_SECOND_PRIME_GEN20_DIAGNOSTIC_V1",
    "source_locks": {
        "gen17_script_blob_sha1": GEN17_BLOB,
        "gen19_script_blob_sha1": GEN19_BLOB,
        "gen19_run": GEN19_RUN,
        "gen19_job": GEN19_JOB,
        "gen19_canonical_sha256": GEN19_CANONICAL,
        "gen19_route": GEN19_ROUTE,
        "strict_curve_packet_sha256": STRICT_PACKET,
        "degree31_denominator_source_lock_blob_sha1": DEN31_NOTE_BLOB,
    },
    "degree": DEGREE,
    "first_prime": P1,
    "first_prime_candidate_sha256": P1_CANDIDATE_SHA256,
    "first_prime_term_count": P1_TERM_COUNT,
    "second_prime": P2,
    "second_prime_i_root": P2_I_ROOT,
    "second_prime_sqrt2_root": P2_SQRT2_ROOT,
    "second_prime_strict_space_dimension": g20base["strict_condition_section_space_degree31_dimension"],
    "second_prime_candidate_count": len(candidates),
    "second_prime_candidate_sha256": candidate_sha,
    "second_prime_candidate_text_bytes": candidate_bytes,
    "second_prime_candidate_term_count": term_count,
    "second_prime_unique_line": unique_second_prime,
    "term_count_matches_first_prime": matching_term_count,
    "multi_prime_projective_reconstruction_ready": matching_term_count,
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
print("GOAL4AJ_NUM31_SECOND_PRIME_GEN20_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")), flush=True)
print("GOAL4AJ_NUM31_SECOND_PRIME_GEN20=DONE", flush=True)
