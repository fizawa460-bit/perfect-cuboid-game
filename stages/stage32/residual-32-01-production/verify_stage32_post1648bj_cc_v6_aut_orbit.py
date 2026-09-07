#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
DIAG = HERE / "diagnose_stage32_post1648bj_cc_v6_aut_orbit.py"
RESULT = HERE / "post1648bj-cc-v6-aut-orbit-scratch-result.json"
NOTE = HERE / "post1648bj-cc-v6-aut-orbit-source-note.md"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
BI = HERE / "post1648bi-cc-fixed-mass-partition-scratch-result.json"
EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"


def main() -> None:
    committed = json.loads(RESULT.read_text())
    replay_text = subprocess.check_output([sys.executable, "-B", str(DIAG)], text=True)
    replay = json.loads(replay_text)
    if replay != committed:
        raise ValueError("BJ committed scratch result is stale relative to exact replay")

    v6 = json.loads(V6.read_text())
    bi = json.loads(BI.read_text())
    if v6["canonical_sha256_without_this_field"] != EXPECTED_V6_CANONICAL:
        raise ValueError("V6 canonical regression")
    if bi["v6"]["picard64_cc_invariant"] is not False:
        raise ValueError("BI cc-noninvariance regression")

    orbit = committed["exact_aut_orbit"]
    if orbit["orbit_size"] != 1536:
        raise ValueError("BJ V6 Aut orbit size regression")
    if orbit["stabilizer_size"] != 1:
        raise ValueError("BJ V6 Aut stabilizer regression")
    if orbit["cc_v6_in_aut_orbit"] is not False:
        raise ValueError("BJ cc(V6) orbit-separation regression")
    if orbit["aut_elements_sending_v6_to_cc_v6"] != 0:
        raise ValueError("BJ Aut hit-count regression")
    if committed["decision"]["semilinear_cc_aut_stabilizer_available"] is not False:
        raise ValueError("BJ semilinear firewall regression")

    fw = committed["firewalls"]
    for key in ("v6_carrier_excluded", "Q602_excluded", "O210_excluded", "O212_plus_advance_allowed"):
        if fw[key] is not False:
            raise ValueError(f"BJ firewall regression at {key}")

    note = NOTE.read_text()
    required = [
        "The Aut orbit of V6 has size 1536",
        "`cc(V6) notin Aut * V6`",
        "they are not three distinct Picard candidate classes",
        "does not localize the normalization nonbijectivity",
    ]
    missing = [x for x in required if x not in note]
    if missing:
        raise ValueError(f"BJ source-note scope regression: {missing}")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648BJ_CC_V6_AUT_ORBIT_EXACT_REPLAY",
        "orbit_size": orbit["orbit_size"],
        "stabilizer_size": orbit["stabilizer_size"],
        "cc_v6_in_aut_orbit": orbit["cc_v6_in_aut_orbit"],
        "aut_hit_count": orbit["aut_elements_sending_v6_to_cc_v6"],
        "v6_carrier_excluded": False,
        "Q602_excluded": False,
        "O210_excluded": False,
        "O212_plus_advance_allowed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
