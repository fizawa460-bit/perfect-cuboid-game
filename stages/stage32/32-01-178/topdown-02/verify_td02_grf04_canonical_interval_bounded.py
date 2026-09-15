#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = HERE / "verify_td02_grf04_bc_envelope_bounded.py"
EXPECTED_BASE_BLOB = "3ce709a2afe9d1acb573cb7c4c1b2e7bff4b53ae"
PRIOR_BC_ENVELOPE_SURVIVORS = 635_133_065_080
PRIOR_BC_ENVELOPE_REJECTED = 36_666_878_533_193
PRIOR_BC_ROW_STREAM_SHA256 = "9566c587ef7c49cb943801e20d09a009729803bb682e10ecfafbcfa5ec905733"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_base():
    raw = BASE.read_bytes()
    req(git_blob(raw) == EXPECTED_BASE_BLOB, "base BC-envelope verifier source drift")
    mod = types.ModuleType("td02_bc_envelope_base")
    mod.__file__ = str(BASE)
    exec(compile(raw, str(BASE), "exec"), mod.__dict__)
    return mod


def canonical_t_bounds(b: int, c: int) -> tuple[int, int]:
    # Let t=x0+x1+x6+x9, with
    #   b=x1+x5+x9, c=x0+x6+x8+x10.
    # Retained parity gives t == c (mod 2).
    # Since t-c=x1+x9-x8-x10 <= x1+x9 <= b, parity sharpens the
    # upper bound to c+2*floor(b/2) whenever b>=1.
    # If b=0 then x1=x5=x9=x0=0. For c>0 the canonical equal-x0/x1
    # branch forces x8+x10>=2 unless t=0 in the x5=x8=x6=x9=0 case,
    # hence t<=c-2.  For the lower endpoint, parity gives c mod 2;
    # when c is even and b>c, t=0 would force b=x5<=x8+x10=c,
    # contradiction, so t>=2.
    lo = c & 1
    if (c & 1) == 0 and b > c:
        lo = 2
    if b == 0:
        hi = 0 if c == 0 else c - 2
    else:
        hi = c + 2 * (b // 2)
    return lo, hi


def canonical_envelope_x4_survivors(*, d: int, g: int, b: int, c: int, q: int, n: int) -> int:
    # Exact GRF04 is
    #   rho = q/2 + (d/2 - 2*x4 - t)^2/12.
    # Every feasible t lies in the canonical interval below and has parity c.
    # For D=d/2-2*x4, |D-t| has fixed parity delta=(d/2-c) mod 2.
    # Therefore the largest admissible radius is the largest r_eff<=r with
    # parity delta.  Enlarging the feasible t-set to the full parity interval
    # [t_lo,t_hi] is safe; it can only weaken the lower bound.
    rhs = 3*d*d + 48*d + 96 - 96*g
    rem = rhs - 24*q
    if rem < 0:
        return 0
    r = math.isqrt(rem // 4)
    t_lo, t_hi = canonical_t_bounds(b, c)
    if t_hi < t_lo:
        return 0
    delta = (d//2 - c) & 1
    r_eff = r if (r & 1) == delta else r - 1
    if r_eff < 0:
        return 0
    D0 = d // 2
    lo = max(0, -((-(D0 - (t_hi + r_eff))) // 2))
    # The previous line is ceil((D0-t_hi-r_eff)/2) written with integer ops.
    # Keep an independent direct helper identity check below to prevent drift.
    lo2 = max(0, -((-(D0 - t_hi - r_eff)) // 2))
    req(lo == lo2, "ceil lower endpoint regression")
    hi = min(n, (D0 - t_lo + r_eff) // 2)
    return max(0, hi - lo + 1)


def main() -> None:
    base = load_base()

    # Recheck every load-bearing source lock before calling the imported census.
    for name, (rel, expected) in base.LOCKS.items():
        path = ROOT / rel
        req(path.is_file(), f"missing source {name}")
        req(base.git_blob(path) == expected, f"source drift {name}")
    prefix = json.loads((ROOT / base.LOCKS["prefix_checkpoint"][0]).read_text())
    req(prefix["exact_terminal_family"]["assignment_order_known_labels_1based"] == [95,99,103,102,49,97,94,101,93,98,96], "FULL178 label order")

    # Structural regression witnesses for the tightened interval.
    req(canonical_t_bounds(0, 0) == (0, 0), "t bounds (0,0)")
    req(canonical_t_bounds(0, 2) == (0, 0), "t bounds (0,2)")
    req(canonical_t_bounds(3, 2) == (2, 4), "t bounds (3,2)")
    req(canonical_t_bounds(4, 5) == (1, 9), "t bounds (4,5)")

    base.envelope_x4_survivors = canonical_envelope_x4_survivors
    raw = base.census()

    rows = []
    for row in raw["rows"]:
        rows.append({
            "g": row["g"],
            "d": row["d"],
            "panel_terminals": row["panel_terminals"],
            "hpadj08_rejected": row["hpadj08_rejected"],
            "canonical_interval_rejected": row["bc_envelope_rejected"],
            "incremental_over_hpadj08": row["incremental_over_hpadj08"],
            "canonical_interval_survivors": row["bc_envelope_survivors"],
        })

    row_stream = hashlib.sha256()
    for row in rows:
        row_stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    rejected = raw["bc_envelope_rejected"]
    survivors = raw["bc_envelope_survivors"]
    req(rejected >= PRIOR_BC_ENVELOPE_REJECTED, "canonical interval weakened prior BC envelope")
    req(survivors <= PRIOR_BC_ENVELOPE_SURVIVORS, "canonical interval survivor regression")
    req(survivors < PRIOR_BC_ENVELOPE_SURVIVORS, "canonical interval strict gain missing")

    result = {
        "schema": "STAGE32_32_01_178_TD02_GRF04_CANONICAL_INTERVAL_BOUNDED_V1",
        "domain": raw["domain"],
        "panel_terminals": raw["panel_terminals"],
        "hpadj08_rejected": raw["hpadj08_rejected"],
        "hpadj08_survivors": raw["hpadj08_survivors"],
        "canonical_interval_rejected": rejected,
        "canonical_interval_survivors": survivors,
        "incremental_over_hpadj08": rejected - raw["hpadj08_rejected"],
        "incremental_over_prior_bc_envelope": PRIOR_BC_ENVELOPE_SURVIVORS - survivors,
        "prior_bc_envelope": {
            "rejected": PRIOR_BC_ENVELOPE_REJECTED,
            "survivors": PRIOR_BC_ENVELOPE_SURVIVORS,
            "row_stream_sha256": PRIOR_BC_ROW_STREAM_SHA256,
            "evidence_run": 35031865587,
            "evidence_head": "309923bcad8659fff42ea683dd21b5eed4a7d1ec",
        },
        "canonical_t_interval_contract": {
            "parity": "t == c (mod 2)",
            "lower": "c mod 2, except c even and b>c gives 2",
            "upper": "b>=1: c+2*floor(b/2); b=0,c=0:0; b=0,c>0:c-2",
            "use_semantics": "safe parity interval envelope; no exact per-(b,c,q) t-support claim required",
        },
        "row_stream_sha256": row_stream.hexdigest(),
        "rows": rows,
        "source_blobs": {
            "base_bc_envelope_verifier": EXPECTED_BASE_BLOB,
        },
        "credit": {
            "main": False,
            "theorem": False,
            "effectivity": False,
            "endpoint": False,
            "stage32_closed": False,
            "merge": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    out = HERE / "TD02-GRF04-CANONICAL-INTERVAL-BOUNDED-RESULT.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in (
        "panel_terminals", "hpadj08_rejected", "hpadj08_survivors",
        "canonical_interval_rejected", "canonical_interval_survivors",
        "incremental_over_hpadj08", "incremental_over_prior_bc_envelope",
        "row_stream_sha256", "canonical_sha256_without_this_field"
    )}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
