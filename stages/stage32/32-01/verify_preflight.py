#!/usr/bin/env python3
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
TRANSCRIPT = ROOT / "magma-preflight-stdout.txt"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def bound(genus: int, d: int) -> int:
    r = math.gcd(d, 16)
    m = 16 // r
    delta = 2 if genus == 0 else 0
    num = m * m * (d * d + 16 * d + 16 * delta)
    assert num % 16 == 0
    return num // 16


expected = {}
for genus, dmin, dmax in ((0, 2, 176), (1, 4, 192)):
    for d in range(dmin, dmax + 1, 2):
        r = math.gcd(d, 16)
        m = 16 // r
        n = d // r
        expected[(genus, d)] = (r, m, n, bound(genus, d))
assert len(expected) == 183
assert expected[(0, 2)] == (2, 8, 1, 272)
assert expected[(1, 4)] == (4, 4, 1, 80)

if not TRANSCRIPT.exists():
    raise SystemExit("missing Magma preflight transcript")
lines = TRANSCRIPT.read_text(encoding="utf-8").splitlines()

required = {
    "STAGE32_PREFLIGHT_BEGIN",
    "STAGE32_INVARIANT|PICARD_RANK|64",
    "STAGE32_INVARIANT|H2|16",
    "STAGE32_INVARIANT|HPERP_RANK|63",
    "STAGE32_INVARIANT|NODE_COUNT|48",
    "STAGE32_INVARIANT|KNOWN_FILTER_COUNT|140",
    "STAGE32_INVARIANT|WINDOW_ROW_COUNT|183",
    "STAGE32_REGRESSION|D2_BASE_D4_BASE_EQUAL|true",
    "STAGE32_REGRESSION|G0_D2_BOUND|272",
    "STAGE32_REGRESSION|G1_D4_BOUND|80",
    "STAGE32_AUT_PHASE_EXECUTED|false",
    "STAGE32_RAW_63D_CVP_STARTED|false",
    "STAGE32_PREFLIGHT_END",
}
missing = sorted(required.difference(lines))
if missing:
    raise SystemExit(f"missing transcript markers: {missing}")

seen = {}
for line in lines:
    if not line.startswith("STAGE32_ROW|"):
        continue
    parts = line.split("|")
    if len(parts) != 8:
        raise SystemExit(f"bad row format: {line}")
    _, gs, ds, rs, ms, ns, bs, base_norm_s = parts
    key = (int(gs), int(ds))
    if key in seen:
        raise SystemExit(f"duplicate row: {key}")
    actual = (int(rs), int(ms), int(ns), int(bs))
    if key not in expected:
        raise SystemExit(f"unexpected row: {key}")
    if actual != expected[key]:
        raise SystemExit(f"row mismatch {key}: expected {expected[key]}, got {actual}")
    if int(base_norm_s) < 0:
        raise SystemExit(f"negative positive-definite base norm for {key}")
    seen[key] = actual

if set(seen) != set(expected):
    missing_rows = sorted(set(expected).difference(seen))
    raise SystemExit(f"incomplete degree/genus ledger: missing {missing_rows[:10]}")

response_path = ROOT / "magma-preflight-response.json"
response = json.loads(response_path.read_text(encoding="utf-8"))
if response.get("upstream_git_blob_sha1") != EXPECTED_BLOB:
    raise SystemExit("response does not bind the pinned upstream blob")
if response.get("success") is not True:
    raise SystemExit("Magma response is not successful")

print(json.dumps({
    "stage": "32-01",
    "picard_preflight_verified": True,
    "window_row_count": len(seen),
    "known_filter_count": 140,
    "aut_phase_executed": False,
    "raw_63d_cvp_started": False,
    "upstream_blob": EXPECTED_BLOB,
}, sort_keys=True))
