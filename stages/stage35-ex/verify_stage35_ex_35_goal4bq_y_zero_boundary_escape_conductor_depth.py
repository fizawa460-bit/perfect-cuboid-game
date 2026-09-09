#!/usr/bin/env python3
"""Verify Goal4BQ: exact y=0 boundary escape depth for 2-primary visible characters."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth-source-lock.md")
BP = P("stages/stage35-ex/35ex-35/goal4bp-post-gaussian-ray-tower-fresh-route-audit.json")
BB = P("stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction.json")
AQ = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence.json")
S22 = P("stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "6a1642dda5e86c545ae2ae8123e98114b7a339e587f77e6f4a26118a70f88360"
SRC_BLOB = "938ec1bcd7bb8ec196cb50bee9fdebc9f15a0d1f"
BP_BLOB = "a4f9be2a9b5f951a43e0d4714e8e6a04c048d467"
BB_BLOB = "54190746afae7e6e8fece7b065311a5ae0b36023"
AQ_BLOB = "593d22b7905d93451e43311540be1c219bbc75d7"
S22_BLOB = "537ca589cd45112cca4c8f8091f5c8c77264e70d"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


def v2_int(n: int) -> int:
    assert n
    n = abs(n)
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def v2_frac(q: Fraction) -> int:
    return v2_int(q.numerator) - v2_int(q.denominator)


for path, expected in ((SRC,SRC_BLOB),(BP,BP_BLOB),(BB,BB_BLOB),(AQ,AQ_BLOB),(S22,S22_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bp = json.loads(BP.read_text())
assert bp["canonical_sha256"] == "da3394acde77d9e7f13d83bc04466d6e8aafbeabac40314af286871d3dcf3c8e"
assert bp["selected_new_view"]["id"] == "Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH"
assert bp["next"]["unit"] == "35EX-35_GOAL4BQ_Y_ZERO_BOUNDARY_ESCAPE_CONDUCTOR_DEPTH_PREFLIGHT"

bb = json.loads(BB.read_text())
assert bb["result"]["every_finite_Brauer_subgroup_BM_nonempty"] is True
assert bb["result"]["full_infinite_Brauer_BM_nonempty_claimed"] is False

aq = json.loads(AQ.read_text())
assert aq["result"]["full_unit_character_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"
assert aq["result"]["finite_character_truncation_sufficient_claimed"] is False

# Exact anchor equations and 2-adic valuations.
x0 = Fraction(272,225)
p0 = Fraction(353,225)
assert p0*p0 == 1 + x0*x0
assert v2_frac(x0) == 4
assert v2_frac(p0) == 0

# The source proof is valuation-theoretic. Replay the key inequality for a
# deterministic range: m < 2m-1, so y dominates q-1 in q+y-1.
for m in range(6, 25):
    assert m < 2*m - 1
    assert min(m, 2*m - 1) == m
    # Sharp rational-height witness to the arithmetic implication only:
    y = Fraction(2**m, 1)
    assert v2_frac(y) == m
    assert max(abs(y.numerator), y.denominator) >= 2**m

src = SRC.read_text()
for marker in (
    "(BQ-m)", "(BQ-slice)", "(BQ-qminus1)", "(BQ-visible-depth)",
    "(BQ-Xn)", "(BQ-Fn)", "(BQ-separation)", "(BQ-depth-theorem)",
    "D(n)=n", "(BQ-height)", "rational realization", "Compactness firewall",
    "35EX-35_GOAL4BR_DERIVED_FOURTH_SQUARE_DEFECT_SQUARECLASS_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"] == "a88fdbad3480f0a6a254a02a001efd179e01528d"
assert art["stacked_parent"]["aggregate_run"] == 34319593575
assert art["stacked_parent"]["aggregate_job"] == 102364864481
assert art["source_locks"]["goal4bq_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bp"]["blob_sha1"] == BP_BLOB

sl = art["two_adic_slice"]
assert sl["minimum_m"] == 6
assert sl["v2_q_minus_1"] == "2*m-1"
assert sl["v2_q_plus_y_minus_1"] == "m"
cp = art["character_packet"]
assert cp["minimal_boundary_depth"] == "D(n)=n"
assert cp["sharp"] is True
ch = art["conditional_height"]
assert ch["height"] == "H(y)=max(|a|,|b|)>=2^n"
assert ch["rational_realization_proved"] is False
assert ch["global_endpoint_height_adapter_obtained"] is False
res = art["result"]
assert res["boundary_depth_D_n_equals_n"] is True
assert res["rational_realization_height_lower_bound_2pow_n"] is True
assert res["rational_realization_proved"] is False
assert res["global_endpoint_height_adapter_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BR_DERIVED_FOURTH_SQUARE_DEFECT_SQUARECLASS_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

print("STAGE35_EX_GOAL4BQ_Y_ZERO_BOUNDARY_ESCAPE_DEPTH=PASS")
print("boundary_depth_D_n_equals_n=true")
print("rational_realization_proved=false")
print("global_endpoint_height_adapter_obtained=false")
print("canonical_sha256=" + EXPECTED)
