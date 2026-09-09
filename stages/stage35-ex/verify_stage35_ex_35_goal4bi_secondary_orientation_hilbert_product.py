#!/usr/bin/env python3
"""Verify Goal4BI: rational Hilbert product cannot see Gaussian split orientation."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bi-secondary-orientation-hilbert-product-formula.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bi-secondary-orientation-hilbert-product-formula-source-lock.md")
BH = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json")
BE = P("stages/stage35-ex/35ex-35/goal4be-gcd-reservoir-quadratic-reciprocity-cycle.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "01593854a40595f968298435aee4e54c01fb0ce08ca832e92d6c2db617a1903e"
SRC_BLOB = "949ed443a97e8a702db7934db2cb78b0680ab22f"
BH_BLOB = "80534af2bc071cbc3a2d6426c495cd3d5e6dbefc"
BE_BLOB = "5f72efb10727980670adb10bf56a4df333978dc2"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


assert blob(SRC) == SRC_BLOB
assert blob(BH) == BH_BLOB
assert blob(BE) == BE_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bh = json.loads(BH.read_text())
assert bh["canonical_sha256"] == "33ccfe71c590b5f5515c44361bbf85558a1768827de88fb4e1c2f76c952b1a6b"
assert bh["result"]["phase_problem_reduced_to_mu2_orientation_torsor"] is True
assert bh["result"]["sigma_cycle_relation_obtained"] is False

be = json.loads(BE.read_text())
assert be["canonical_sha256"] == "feffef319deaf6104fc14f1b055462e70ae99068fd8564c73e8cf86abbae1a16"

src = SRC.read_text()
for marker in (
    "(BI-split-prime)",
    "(BI-split)",
    "(BI-H1)",
    "(BI-norm)",
    "(BI-product)",
    "(BI-Gaussian)",
    "RATIONAL_HILBERT_PRODUCT_ROUTE_FAIL_CLOSED=true",
    "35EX-35_GOAL4BJ_GLOBAL_GAUSSIAN_K2_OR_QUARTIC_CHARACTER_ADAPTER_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bi_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bh"]["blob_sha1"] == BH_BLOB
assert art["source_locks"]["goal4be"]["blob_sha1"] == BE_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "2d4839db40a676ef0ab57945d69a8cf14c80591d"
assert parent["aggregate_run"] == 34310546263
assert parent["aggregate_job"] == 102337324260
assert parent["hostile_audited"] is False

split = art["split_orientation"]
assert split["reservoir_prime_condition"] == "ell|s_a*s_b*s_c => ell=1 mod 4"
assert split["local_square"] == "-1 in Q_ell^{*2}"
assert split["sigma_is_rational_quadratic_character"] is False

rb = art["rational_hilbert_boundary"]
assert rb["reservoir_identity"] == "(-1,t)_ell=1 for every t in Q_ell^*"
assert rb["rational_hilbert_detects_sigma"] is False
assert rb["rational_norms_detect_sigma"] is False
assert rb["real_place_recovers_split_orientation"] is False
assert rb["two_adic_place_recovers_split_orientation_without_global_class"] is False

gr = art["global_reciprocity_requirement"]
assert gr["required_field"] == "Q(i)"
assert gr["global_gaussian_pair_constructed"] is False

res = art["result"]
assert res["reservoir_primes_split_in_Qi"] is True
assert res["sigma_is_split_prime_orientation"] is True
assert res["rational_hilbert_minus_one_trivial_at_reservoirs"] is True
assert res["rational_norm_forgets_sigma"] is True
assert res["rational_hilbert_product_route_fail_closed"] is True
assert res["global_gaussian_symbol_constructed"] is False
assert res["support_cleaning_adapter_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BJ_GLOBAL_GAUSSIAN_K2_OR_QUARTIC_CHARACTER_ADAPTER_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BI_SECONDARY_ORIENTATION_HILBERT_PRODUCT=PASS")
print("rational_hilbert_route_fail_closed=true")
print("global_gaussian_symbol_constructed=false")
print("canonical_sha256=" + EXPECTED)
