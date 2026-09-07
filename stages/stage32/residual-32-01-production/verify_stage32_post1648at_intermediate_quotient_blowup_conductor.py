#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648at-intermediate-quotient-blowup-conductor.json"
NOTE = HERE / "post1648at-intermediate-quotient-blowup-conductor-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648at_intermediate_quotient_blowup_conductor.py"
EXPECTED = "bc11998f941f4791ac0a394c85725368659262a55ec8206288aefa5ee2241b86"


def canonical_sha(obj: dict) -> str:
    y = dict(obj)
    y.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["canonical_sha256_without_this_field"] == EXPECTED
    assert canonical_sha(cert) == EXPECTED
    locks = cert["source_locks"]
    assert git_blob_sha1(NOTE) == locks["source_note_blob_sha1"]
    assert git_blob_sha1(DIAG) == locks["diagnostic_blob_sha1"]

    proc = subprocess.run([sys.executable, "-B", str(DIAG)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(proc.stdout)
    assert x["mode"] == "SCRATCH_POST1648AT_INTERMEDIATE_QUOTIENT_BLOWUP_CONDUCTOR"

    r = cert["ramification_scope_correction"]
    xr = x["ramification_scope_correction"]
    assert xr["boundary_intersection_total"] == r["boundary_intersection_total"] == 292
    assert xr["exceptional_mass_not_divisorial_ramification"] == r["exceptional_mass"] == 266
    assert xr["composite_canonical_difference"] == r["composite_canonical_difference"] == 558
    assert r["exceptional_generic_point_is_divisorially_ramified"] is False

    c = cert["intermediate_curve"]
    xc = x["intermediate_quotient_curve"]
    assert xc["C_Y_square"] == c["C_Y_square"] == 10044
    assert xc["K_Y_dot_C_Y"] == c["K_Y_dot_C_Y"] == -106
    assert xc["arithmetic_genus"] == c["arithmetic_genus"] == 4970
    assert xc["delta"] == c["delta"] == 4969
    assert xc["additional_conductor_from_finite_H_quotient"] == c["finite_H_additional_conductor"] == 4497

    s = cert["finite_H_conductor_split"]
    xs = x["finite_H_conductor_split"]
    assert xs["node_inertia_boundary_sums"] == s["node_inertia_boundary_sums"] == [90,78,124]
    assert xs["node_inertia_contributions"] == s["node_inertia_contributions"] == [635,604,687]
    assert xs["non_node_total"] == s["non_node_total"] == 2571
    assert xs["total"] == s["total"] == 4497

    b = cert["blowdown"]
    xb = x["blowdown_to_P1xP1"]
    assert xb["target_cusp_multiplicities"] == b["target_cusp_multiplicities"]
    assert xb["sum_m"] == b["sum_m"] == 266
    assert xb["sum_m_squared"] == b["sum_m_squared"] == 6966
    assert xb["arithmetic_genus_jump"] == b["arithmetic_genus_jump"] == 3350
    assert xb["delta_jump"] == b["delta_jump"] == 3350

    t = cert["total_conductor"]
    xt = x["total_conductor"]
    assert xt["AP_required"] == t["AP_required"] == 7847
    assert xt["finite_H_quotient"] == t["finite_H_quotient"] == 4497
    assert xt["twelve_blowdowns"] == t["twelve_blowdowns"] == 3350

    assert cert["decision"]["v6_carrier_excluded"] is False
    assert cert["firewalls"]["Q602_excluded"] is False
    assert cert["firewalls"]["O210_excluded"] is False
    assert cert["firewalls"]["O212_plus_advance_allowed"] is False
    assert cert["firewalls"]["scratch_only"] is True

    print("PASS stage32 post1648AT intermediate quotient blowup conductor")
    print(json.dumps({
        "canonical": EXPECTED,
        "boundary_ramification_C": r["boundary_intersection_total"],
        "finite_H_conductor": c["finite_H_additional_conductor"],
        "blowdown_conductor": b["delta_jump"],
        "total": t["AP_required"],
        "v6_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
