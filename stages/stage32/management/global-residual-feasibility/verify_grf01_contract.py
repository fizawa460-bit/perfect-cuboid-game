#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CONTRACT = HERE / "GRF-01-CONTRACT.json"
EXPECTED_CANONICAL = "18ce801f45bd95fec8e0a2f6001eff9fd80a9b6f6b416ccc9190d3b37adc3c43"

LOCKS = {
    ROOT / "stages/stage32/MAIN-STATE.json": "b8df16056625db5fbb1947f1e927593de258f1ff",
    ROOT / "stages/stage32/management/hpadj-07/CARRIER-REALIZATION-WALL.json": "e4a35aa9bdd174ac64162839ec391cd57f7d9315",
    ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md": "2c1a4813a77b517482b6fef497f9a517c9d12fe6",
    ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json": "8a30e3aa30777460f344eb19836dc725dd442329",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ROOT / "stages/stage32/management/CUT196-AUDITED-RESULT.json": "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde",
}

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()

def csha(v: object) -> str:
    return hashlib.sha256(
        json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def main() -> None:
    for path, expected in LOCKS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(git_blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    c = json.loads(CONTRACT.read_text())
    stored = c.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CANONICAL and csha(c) == EXPECTED_CANONICAL,
        "GRF-01 contract canonical drift")
    req(c["status"] == "FAMILY_LEVEL_OBSTRUCTION_DESIGN_ONLY_HANDOFF_TO_178_NO_CREDIT",
        "GRF-01 status drift")
    req(not any(c["credit_firewall"].values()), "GRF-01 credit firewall opened")

    wall = json.loads((ROOT / "stages/stage32/management/hpadj-07/CARRIER-REALIZATION-WALL.json").read_text())
    cm = wall["corrected_mathematics"]
    req(cm["g0_group_cauchy_rejection"] ==
        "8*a^2+8*b^2+6*c^2>3*d^2+48*d+96", "g0 HPADJ formula drift")
    req(cm["g1_group_cauchy_rejection"] ==
        "8*a^2+8*b^2+6*c^2>3*d^2+48*d", "g1 HPADJ formula drift")

    handoff = json.loads((ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json").read_text())
    tm = handoff["terminal_to_picard64_map"]
    req(tm["inverse_denominator"] == 8, "selected64 denominator drift")
    req(tm["integrality_congruence"] ==
        "B_fixed*x11 + B_free*z53 == 0 (mod 8) coordinatewise",
        "selected64 integrality semantics drift")
    groups = handoff["stored_10_exceptional_coordinate_identity"]["groups"]
    req(groups == {"a":[103,102,101],"b":[99,97,98],"c":[95,94,93,96]},
        "HPADJ group identity drift")

    expected = {
        2: (8,128,16), 4: (4,32,16), 6: (8,128,16), 8: (2,8,0),
        10: (8,128,16), 12: (4,32,16), 14: (8,128,16), 16: (1,2,0),
    }
    for d, want in expected.items():
        r = math.gcd(d,16)
        m = 16 // r
        n = d // r
        mod = 2*m*m
        residue = (16*n*n + m*m*(d+2)) % mod
        req((m,mod,residue) == want, f"norm residue derivation drift at d={d}")

    req(c["ownership"]["lane178_owns"] == [
        "concrete FULL178 row/stratum/terminal target extraction",
        "bounded leaf search",
        "incidence/transport execution",
        "population replay",
        "exact subset certificate generation and identity accounting"
    ], "178 ownership firewall drift")
    req(c["cut_firewall"]["generic_cut_constraint_requires_source_locked_semantic_adapter"] is True,
        "CUT semantic firewall drift")

    print("PASS: Stage32 MAIN GRF-01 family-level obstruction design contract")
    print(f"canonical={EXPECTED_CANONICAL}")
    print("concrete_subset_generation_owner=stage32-01-178-mainbatch")

if __name__ == "__main__":
    main()
