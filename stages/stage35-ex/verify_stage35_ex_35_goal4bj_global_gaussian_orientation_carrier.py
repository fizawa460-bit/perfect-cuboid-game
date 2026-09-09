#!/usr/bin/env python3
"""Verify Goal4BJ: support-cleaned global Gaussian quartic orientation carrier."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter-source-lock.md")
BI = P("stages/stage35-ex/35ex-35/goal4bi-secondary-orientation-hilbert-product-formula.json")
BH = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json")
BG = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility.json")
BF = P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "a1208a9ac7ec291074a36fe4d795e13b31eee22653fa83bcdef3b7eae120ac4e"
SRC_BLOB = "f0d022b9a560b0dd8e89e1b93689a1677c46edfe"
BI_BLOB = "86623f6dfdc6051cd2d9b76d8141786a425300bf"
BH_BLOB = "80534af2bc071cbc3a2d6426c495cd3d5e6dbefc"
BG_BLOB = "831e25e134e03659e555a2b0b0703c4fe53d36c4"
BF_BLOB = "b015280d80c958608bdbabd3a590c0bf482b25bc"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


for path, expected in ((SRC,SRC_BLOB),(BI,BI_BLOB),(BH,BH_BLOB),(BG,BG_BLOB),(BF,BF_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bi = json.loads(BI.read_text())
assert bi["canonical_sha256"] == "01593854a40595f968298435aee4e54c01fb0ce08ca832e92d6c2db617a1903e"
assert bi["result"]["rational_hilbert_product_route_fail_closed"] is True

src = SRC.read_text()
for marker in (
    "(BJ-Mpm)",
    "(BJ-partition)",
    "(BJ-status)",
    "(BJ-Xi)",
    "(BJ-val)",
    "(BJ-quartic-class)",
    "(BJ-squareclass)",
    "(BJ-J)",
    "DUAL_QUARTIC_CHARACTER_CONSTRUCTED=false",
    "35EX-35_GOAL4BK_DUAL_QUARTIC_CHARACTER_COFACTOR_UNIT_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bj_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bi"]["blob_sha1"] == BI_BLOB
assert art["source_locks"]["goal4bh"]["blob_sha1"] == BH_BLOB
assert art["source_locks"]["goal4bg"]["blob_sha1"] == BG_BLOB
assert art["source_locks"]["goal4bf"]["blob_sha1"] == BF_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "933e32403c2f87b65ac3e962647c59e71a35a291"
assert parent["aggregate_run"] == 34312324963
assert parent["aggregate_job"] == 102342539462
assert parent["hostile_audited"] is False

gp = art["gaussian_gcd_partition"]
assert gp["direction_A"]["factorization"] == "Sigma_a=M_minus*M_plus*M_zero"
assert gp["direction_A"]["pairwise_coprime"] is True
assert gp["nonreservoir_support_enters_partition"] is False
assert gp["support_cleaning_by_literal_divisor_of_Sigma"] is True

ps = art["primewise_status"]
assert ps["mutually_exclusive_exhaustive"] is True

carrier = art["global_orientation_carrier"]
assert carrier["Xi"] == "Xi_a*Xi_b*Xi_c"
assert carrier["valuation_rule"]["secondary_sigma_minus_one"] == "+1"
assert carrier["valuation_rule"]["secondary_sigma_plus_one"] == "-1"
assert carrier["valuation_rule"]["nonsecondary"] == "0"
assert carrier["finite_support"] == "selected reservoir Gaussian prime ideals only"

q = art["quartic_vs_quadratic"]
assert q["quartic_class_recovers_sigma"] is True
assert q["quartic_valuation_classes"] == {"sigma_minus_one":1,"sigma_plus_one":3,"nonsecondary":0}
assert q["quadratic_class_recovers_sigma"] is False
assert q["quadratic_K2_Hilbert_sufficient"] is False

n = art["norm_one_carrier"]
assert n["norm"] == "N_{Q(i)/Q}(J)=1"
assert n["hilbert90_presentation_explicit"] is True
assert n["norm_one_alone_obstructive"] is False

res = art["result"]
assert res["support_cleaning_adapter_obtained"] is True
assert res["global_gaussian_orientation_carrier_constructed"] is True
assert res["global_norm_one_carrier_constructed"] is True
assert res["quartic_class_recovers_sigma"] is True
assert res["quadratic_K2_Hilbert_recovers_sigma"] is False
assert res["dual_quartic_character_constructed"] is False
assert res["global_reciprocity_contradiction_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BK_DUAL_QUARTIC_CHARACTER_COFACTOR_UNIT_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BJ_GLOBAL_GAUSSIAN_ORIENTATION_CARRIER=PASS")
print("support_cleaning_adapter_obtained=true")
print("quartic_class_recovers_sigma=true")
print("dual_quartic_character_constructed=false")
print("canonical_sha256=" + EXPECTED)
