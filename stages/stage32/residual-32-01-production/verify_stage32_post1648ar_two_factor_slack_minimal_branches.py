#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ar-two-factor-slack-minimal-branches.json"
NOTE = HERE / "post1648ar-two-factor-slack-minimal-branches-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648ar_two_factor_slack_minimal_branches.py"
AO = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
AQ = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"


def canonical_sha(obj: dict) -> str:
    y = dict(obj)
    y.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    expected = "dba5756e4b10c8bd6e412f1027b8edf693fb74f9ea90f9b591cc99437746a8dd"
    assert cert["canonical_sha256_without_this_field"] == expected
    assert canonical_sha(cert) == expected

    locks = cert["source_locks"]
    assert hashlib.sha256(NOTE.read_bytes()).hexdigest() == locks["source_note_sha256"]
    assert git_blob_sha1(NOTE) == locks["source_note_blob_sha1"]
    assert git_blob_sha1(DIAG) == locks["diagnostic_script_blob_sha1"]

    ao = json.loads(AO.read_text())
    aq = json.loads(AQ.read_text())
    assert ao["canonical_sha256_without_this_field"] == cert["parent"]["ao_canonical"]
    assert aq["canonical_sha256_without_this_field"] == cert["parent"]["aq_canonical"]

    proc = subprocess.run([sys.executable, "-B", str(DIAG)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(proc.stdout)
    assert x["mode"] == "SCRATCH_POST1648AR_TWO_FACTOR_SLACK_MINIMAL_BRANCHES"
    assert x["parents"]["AO_canonical"] == cert["parent"]["ao_canonical"]
    assert x["parents"]["AQ_canonical"] == cert["parent"]["aq_canonical"]
    assert x["exact_inputs"]["exceptional_mass"] == cert["exact_inputs"]["exceptional_mass"] == 266

    for n in ("81", "105"):
        dx = x["factor_slack"][n]
        dc = cert["exact_inputs"][f"factor_{n}"]
        assert dx["degree"] == dc["degree"]
        assert dx["q_boundary"] == dc["q_boundary"]
        assert dx["total_ramification"] == dc["total_ramification"]
        assert dx["slack"] == dc["slack"]

    c = x["combined_bound"]
    sc = cert["slack_identity"]
    mc = cert["minimal_branch_bound"]
    assert c["t_max"] == sc["t_max"] == 28
    assert c["minimum_node_branches"] == sc["minimum_node_branches"] == 238
    assert c["minimum_FSM_minimal_A_B_1_1_branches"] == mc["minimum_FSM_minimal_A_B_1_1_branches"] == 186
    assert c["minimal_branch_properties"]["exceptional_contact"] == 1
    assert c["minimal_branch_properties"]["factor_orders"] == [1, 1]
    assert c["minimal_branch_properties"]["factor_ramification_both_directions"] == 0
    assert c["minimal_branch_properties"]["node_boundary_contact_both_directions"] == 0
    assert x["exact_inputs"]["AQ_min_transverse_node_branches"] == cert["exact_inputs"]["aq_min_transverse_node_branches"] == 210

    assert cert["decision"]["v6_carrier_excluded"] is False
    assert cert["decision"]["Q602_excluded"] is False
    assert cert["decision"]["O210_excluded"] is False
    assert cert["decision"]["O212_plus_advance_allowed"] is False
    assert cert["guardrails"]["scratch_only"] is True
    assert cert["guardrails"]["shared_MAIN_STATE_unchanged"] is True
    assert cert["guardrails"]["shared_authority_unchanged"] is True

    print("PASS stage32 post1648AR two-factor slack minimal branches")
    print(json.dumps({
        "canonical": expected,
        "factor_slacks": [52, 28],
        "minimum_node_branches": 238,
        "minimum_FSM_minimal_branches": 186,
        "v6_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
