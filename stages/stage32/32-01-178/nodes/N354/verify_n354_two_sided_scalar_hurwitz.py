#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
N220 = HERE.parent / "N220"
sys.path.insert(0, str(N220))

import verify_n220_exact_symbolic_count as base
import verify_n220_exact_symbolic_count_fast as fast

ROOT = HERE.parents[4]
MANIFEST = ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json"
N353 = HERE.parent / "N353" / "RESULT.json"
N353_AUDIT = HERE.parent / "N353" / "HOSTILE-AUDIT-PASS.json"
RESULT = HERE / "RESULT.json"

EXPECTED_N353_REJECTED_STRATA = 12788
EXPECTED_N353_REJECTED_TERMINALS = 264541612417334415376
EXPECTED_N353_REMAINING_STRATA = 47703
EXPECTED_N353_REMAINING_TERMINALS = 346053443361304169755481593
EXPECTED_ODD_E_STRATA = 23798
EXPECTED_ODD_E_TERMINALS = 173026564978667598377973100
EXPECTED_LOWER_REJECT_STRATA = 6777
EXPECTED_LOWER_REJECT_TERMINALS = 134465921848239433742728391
EXPECTED_N354_REJECTED_STRATA = 30575
EXPECTED_N354_REJECTED_TERMINALS = 307492486826907032120701491
EXPECTED_N354_REMAINING_STRATA = 17128
EXPECTED_N354_REMAINING_TERMINALS = 38560956534397137634780102
EXPECTED_STREAM = "22449c7eafde95da5366e5092943aeb3cd47834bbe7379c9b47d14bb7d1d0439"
EXPECTED_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
EXPECTED_AUDIT_REVIEW = 5163144778
EXPECTED_AUDITED_HEAD = "0f8cee995e5c982cdb7ceceae14d69f91e65588d"


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def main() -> None:
    manifest = base.load_canonical(MANIFEST, base.EXPECTED_MANIFEST_CANONICAL)
    n353 = json.loads(N353.read_text())
    audit = json.loads(N353_AUDIT.read_text())
    retained = json.loads(RESULT.read_text())

    if audit["status"] != "PASS" or audit["review_id"] != EXPECTED_AUDIT_REVIEW:
        raise ValueError("N353 hostile-audit receipt regression")
    if audit["audited_exact_head"] != EXPECTED_AUDITED_HEAD:
        raise ValueError("N353 audited exact-head regression")
    if n353["aggregate"]["candidate_remaining_strata"] != EXPECTED_N353_REMAINING_STRATA:
        raise ValueError("N353 remaining-strata regression")
    if n353["aggregate"]["candidate_remaining_terminals"] != EXPECTED_N353_REMAINING_TERMINALS:
        raise ValueError("N353 remaining-terminal regression")
    if retained.get("canonical_sha256_without_this_field") != EXPECTED_RESULT_CANONICAL or csha(retained) != EXPECTED_RESULT_CANONICAL:
        raise ValueError("N354 retained RESULT canonical regression")

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    exact = base.build_exceptional_exact_mass_support()
    support_lt = fast.build_support_lt(exact)
    cumulative_exceptional: list[int] = []
    running = 0
    for e in range(base.MAX_E + 1):
        running += sum(exact[e])
        cumulative_exceptional.append(running)

    counts = {
        "N353_REJECT": [0, 0],
        "N354_ODD_E_REJECT": [0, 0],
        "N354_LOWER_INTERVAL_REJECT": [0, 0],
        "N354_REMAIN": [0, 0],
    }
    stream = hashlib.sha256()

    for row_id in rows:
        g, d = base.parse_row_id(row_id)
        legacy_emin = 8 if g == 0 else 4
        K = ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            survivor_exceptional = cumulative_exceptional[e] - fast.rejected_fast(exact, support_lt, e=e, required=K)
            normal_block = 19 * d - 5 * e + 1
            terminals = survivor_exceptional * normal_block

            if d > e + 4 * g - 4:
                status = "N353_REJECT"
            elif e & 1:
                status = "N354_ODD_E_REJECT"
            elif d < 2 * ceil_div(e, 6):
                status = "N354_LOWER_INTERVAL_REJECT"
            else:
                status = "N354_REMAIN"

            counts[status][0] += 1
            counts[status][1] += terminals
            rec = {"d": d, "e": e, "g": g, "post_n220_terminals": terminals, "status": status}
            stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    expected = {
        "N353_REJECT": [EXPECTED_N353_REJECTED_STRATA, EXPECTED_N353_REJECTED_TERMINALS],
        "N354_ODD_E_REJECT": [EXPECTED_ODD_E_STRATA, EXPECTED_ODD_E_TERMINALS],
        "N354_LOWER_INTERVAL_REJECT": [EXPECTED_LOWER_REJECT_STRATA, EXPECTED_LOWER_REJECT_TERMINALS],
        "N354_REMAIN": [EXPECTED_N354_REMAINING_STRATA, EXPECTED_N354_REMAINING_TERMINALS],
    }
    if counts != expected:
        raise ValueError(f"N354 census regression: {counts} != {expected}")
    if stream.hexdigest() != EXPECTED_STREAM:
        raise ValueError("N354 per-stratum stream regression")

    n354_rejected_strata = counts["N354_ODD_E_REJECT"][0] + counts["N354_LOWER_INTERVAL_REJECT"][0]
    n354_rejected_terminals = counts["N354_ODD_E_REJECT"][1] + counts["N354_LOWER_INTERVAL_REJECT"][1]
    if n354_rejected_strata != EXPECTED_N354_REJECTED_STRATA or n354_rejected_terminals != EXPECTED_N354_REJECTED_TERMINALS:
        raise ValueError("N354 aggregate rejection regression")

    print(json.dumps({
        "verdict": "PASS_N354_TWO_SIDED_SCALAR_HURWITZ_CENSUS",
        "audit_candidate_only": True,
        "n354_rejected_strata": n354_rejected_strata,
        "n354_rejected_terminals": n354_rejected_terminals,
        "remaining_strata": counts["N354_REMAIN"][0],
        "remaining_terminals": counts["N354_REMAIN"][1],
        "classification_stream_sha256": stream.hexdigest(),
        "full178_complete": False,
        "main_credit": False,
        "heavy_compute": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
