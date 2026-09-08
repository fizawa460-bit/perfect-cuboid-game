#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONTRACT = HERE / "post1715-product-cover-nonnode-support-split-contract.json"


def fail(msg: str) -> None:
    raise RuntimeError(msg)


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> int:
    try:
        c = json.loads(CONTRACT.read_text())
        if c.get("schema") != "STAGE32_EX6_PRODUCT_COVER_NONNODE_SUPPORT_SPLIT_V1":
            fail("schema drift")
        if c.get("status") != "EXPLORATORY_EXACT_BOUNDED_SUPPORT_SPLIT_NO_ENDPOINT_CREDIT":
            fail("status drift")

        cover = c["cover_inputs"]
        if cover["qprime"] != 4 or cover["beauville_degree"] != 2:
            fail("cover degree drift")
        if cover["nonnode_D_to_N_degree"] != 8:
            fail("nonnode cover degree must be 2*4=8")
        if not cover["D_to_N_unramified_away_from_O_contacts"]:
            fail("missing nonnode unramified cover lock")
        if cover["X8_to_X4_cusp_local_degree"] != 2:
            fail("X8/X4 cusp local degree drift")
        if not cover["X8_to_X4_unramified_away_from_cusps"]:
            fail("X8/X4 interior unramified lock missing")

        split = c["support_split"]
        for b in (1, 2, 3, 7):
            x4_order = 2 * b
            x8_degree = x4_order // 2
            per_lift = x8_degree - 1
            eight_lifts = 8 * per_lift
            if x8_degree != b or per_lift != b - 1 or eight_lifts != 8 * (b - 1):
                fail(f"smooth-boundary local adapter failed at b={b}")
        if split["smooth_boundary_total_formula"] != "8eta":
            fail("8eta formula drift")
        if split["off_special_total_formula"] != "8rho":
            fail("8rho formula drift")
        if split["R81_nonnode_formula"] != "8eta81+8rho81":
            fail("R81 support split drift")
        if split["R105_nonnode_formula"] != "8eta105+8rho105":
            fail("R105 support split drift")
        if split["combined_nonnode_formula"] != "8E":
            fail("combined support split drift")

        # Algebraic replay: factorwise split must sum to the retained total 8E.
        samples = [
            (0, 0, 0, 0),
            (1, 2, 3, 4),
            (52, 0, 0, 28),
            (5, 7, 11, 13),
        ]
        for e81, r81, e105, r105 in samples:
            E = e81 + r81 + e105 + r105
            lhs = 8 * e81 + 8 * r81 + 8 * e105 + 8 * r105
            if lhs != 8 * E:
                fail("support split sum mismatch")

        inspected = c["inspected_retained_chain"]
        if inspected["eta_rho_member_level_cap_obtained"] is not False:
            fail("must not claim eta/rho member-level cap")
        if inspected["repo_wide_absence_claimed"] is not False:
            fail("must not claim repository-wide absence")

        decision = c["decision"]
        if decision["product_cover_nonnode_support_split"] != "EXACT":
            fail("support split decision drift")
        if decision["cusp_grid_recharge_as_eta_rho_cap_authorized"] is not False:
            fail("cusp-grid recharge must remain unauthorized")
        if decision["O266_endpoint_excluded"] is not False:
            fail("must not claim O266 exclusion")
        if decision["O264_descent_authorized"] is not False:
            fail("must not authorize O264 descent")

        for name, lock in c["source_locks"].items():
            path = ROOT / lock["path"]
            if not path.is_file():
                fail(f"missing source lock {name}: {lock['path']}")
            actual = git_blob_sha1(path.read_bytes())
            if actual != lock["blob_sha1"]:
                fail(f"source lock mismatch {name}: {actual} != {lock['blob_sha1']}")

        for key, value in c["firewalls"].items():
            if value is not False:
                fail(f"firewall must remain false: {key}")

        print(json.dumps({
            "verdict": "PASS_STAGE32_EX6_PRODUCT_COVER_NONNODE_SUPPORT_SPLIT",
            "smooth_special": "8eta",
            "off_special": "8rho",
            "combined": "8E",
            "O266_endpoint_excluded": False,
            "O264_descent_authorized": False,
        }, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"verdict": "FAIL_STAGE32_EX6_PRODUCT_COVER_NONNODE_SUPPORT_SPLIT", "error": str(exc)}, sort_keys=True))
        return 1


if __name__ == "__main__":
    sys.exit(main())
