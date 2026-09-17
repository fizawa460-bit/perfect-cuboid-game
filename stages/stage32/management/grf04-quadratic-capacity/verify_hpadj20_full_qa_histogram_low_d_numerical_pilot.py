#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "HPADJ20-FULL-QA-HISTOGRAM-LOW-D-NUMERICAL-PILOT.json"
EXPECTED_SCHEMA = "STAGE32_MAIN_HPADJ20_FULL_QA_HISTOGRAM_LOW_D_NUMERICAL_PILOT_V1"
EXPECTED_STATUS = "EXACT_LOW_D_NUMERICAL_PILOT_STRICT_AT_D12__FULL178_NOT_RUN__ZERO_MAIN_CREDIT"
EXPECTED_CANONICAL = "ebc454e2805cf737570ccdf2f50f64595f947b9dbaf15ca39cde9e3c5b905406"
EXPECTED_ROWS = ["g0-d008","g1-d008","g0-d010","g1-d010","g0-d012","g1-d012","g0-d014","g1-d014"]
EXPECTED_SOURCE_CANONICALS = {
    "g0-d008": "9cf7bf5745ee7d59393c33d2554b860e74d7ff7c9749c8a6bcbf88fd7197dbd2",
    "g1-d008": "53057a7ac4429a9943994fc08bacff57219b15cff9303b5c214393b600152f92",
    "g0-d010": "d2a8ee63989f9b143c9bacb5fe48bc54190f8c2fa7f5521faabb6c36b3b03a4f",
    "g1-d010": "52c9a79f843cb58ccda1e7b947fdf0da80eb82d07f0544f6375c78eb91575571",
    "g0-d012": "802e733182667fa576b66224408ddd1e041516b014af5e1b3dd4b5dc5269d659",
    "g1-d012": "23aee79bfd79c9f22a5b527dabac063ce00cedf0c061e37eee2f2568975ee812",
    "g0-d014": "5c873357c99a8a6dfce7f2fc044095c95ea8a05f269678e4f8389d6632eaf74d",
    "g1-d014": "1a3d697d00c0f4c488a5960e53b949fe7432dff39c0d8a78a0acc7500b473f8c",
}

def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")

def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def main() -> None:
    doc = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    if doc.get("schema") != EXPECTED_SCHEMA:
        fail("schema drift")
    if doc.get("status") != EXPECTED_STATUS:
        fail("status drift")
    if doc.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("recorded canonical drift")
    if canonical_sha(doc) != EXPECTED_CANONICAL:
        fail("canonical recomputation mismatch")

    fw = doc["firewalls"]
    for key, value in fw.items():
        if value is not False:
            fail(f"credit firewall opened: {key}")

    scope = doc["scope"]
    if scope["tested_rows"] != EXPECTED_ROWS:
        fail("tested row set/order drift")
    if scope["full178_replay_run"] is not False or scope["pilot_only"] is not True:
        fail("pilot/full178 semantics drift")

    rows = doc["rows"]
    if [row["row_id"] for row in rows] != EXPECTED_ROWS:
        fail("row payload order drift")

    strict = []
    equal = []
    sum_hp20 = 0
    sum_full = 0
    for row in rows:
        rid = row["row_id"]
        if row["source_artifact_canonical_sha256"] != EXPECTED_SOURCE_CANONICALS[rid]:
            fail(f"source artifact canonical drift: {rid}")
        if row["hpadj20_replayed_integer_upper"] != row["hpadj20_cell_integer_upper"]:
            fail(f"two-tier replay did not reproduce audited HPADJ20 cell: {rid}")

        exact = Fraction(
            row["full_qa_exact_objective_numerator"],
            row["full_qa_exact_objective_denominator"],
        )
        full_floor = exact.numerator // exact.denominator
        if full_floor != row["full_qa_cell_integer_upper"]:
            fail(f"full-qA floor mismatch: {rid}")
        delta = row["hpadj20_cell_integer_upper"] - row["full_qa_cell_integer_upper"]
        if delta != row["strict_improvement"] or delta < 0:
            fail(f"dominance/improvement mismatch: {rid}")

        if delta:
            strict.append(row)
        else:
            equal.append(row)
        sum_hp20 += row["hpadj20_cell_integer_upper"]
        sum_full += row["full_qa_cell_integer_upper"]

    if any(row["d"] <= 10 for row in strict):
        fail("strictness unexpectedly occurs at tested d<=10")
    if sorted({row["d"] for row in strict}) != [12, 14]:
        fail("tested strict-d set drift")
    if len(strict) != 4 or len(equal) != 4:
        fail("strict/equal row counts drift")

    obs = doc["boundary_observation"]
    if obs["first_tested_strict_d"] != min(row["d"] for row in strict):
        fail("first tested strict d mismatch")
    if obs["tested_equal_through_d"] != 10:
        fail("tested equality boundary drift")
    if obs["strict_rows"] != len(strict) or obs["equal_rows"] != len(equal):
        fail("boundary row-count mismatch")
    if obs["sum_tested_hpadj20_integer_upper"] != sum_hp20:
        fail("HPADJ20 pilot sum mismatch")
    if obs["sum_tested_full_qa_integer_upper"] != sum_full:
        fail("full-qA pilot sum mismatch")
    if obs["sum_tested_cellwise_integer_improvement"] != sum_hp20 - sum_full:
        fail("pilot improvement sum mismatch")
    if obs["sum_tested_cellwise_integer_improvement"] != 1_577_384:
        fail("expected low-d strict improvement drift")
    if obs["strict_global_full178_improvement_claimed"] is not False:
        fail("global FULL178 claim must remain false")

    print("PASS: HPADJ20 full-qA low-d numerical pilot binding verifier")
    print(f"  tested rows: {len(rows)}")
    print(f"  first tested strict d: {obs['first_tested_strict_d']}")
    print(f"  low-d cellwise integer tightening: {sum_hp20 - sum_full}")
    print("  MAIN credit: 0; FULL178 replay: not run")

if __name__ == "__main__":
    main()
