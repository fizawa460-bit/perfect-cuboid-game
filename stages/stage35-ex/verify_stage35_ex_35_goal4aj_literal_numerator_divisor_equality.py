#!/usr/bin/env python3
"""Verify Goal4AJ literal degree-31 numerator materialization and divisor equality."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-literal-numerator-divisor-equality.json"
G25 = ROOT / "stages/stage35-ex/35ex-35/goal4aj-gen25-g4-all27-exact-strict-certificate.json"
MAT = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-materialization.json"
MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json"
CHUNK_VERIFY = ROOT / "stages/stage35-ex/verify_stage35_ex_35_goal4aj_qcandidate_chunks.py"
GEN26 = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_numerator_exceptional_forced_bridge_gen26.py"
ACTIVE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_active_condition_packet.py"
QPEEL = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_q_hyperplane_factor_peel.py"
DEN19_BRIDGE = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree19-exceptional-forced-from-strict-source-lock.md"

EXPECTED_BLOBS = {
    CERT: "a60034bb2b2e3cbd16d96fa26b76eeaf1210900f",
    G25: "8c29fec40c93a4da27c7c37d149ef5877265fccf",
    MAT: "1bc208ed5010ec2d3f50d90b70db3698f860a134",
    MANIFEST: "85b52e921f36fc445fd243db1a3b3f65bb298966",
    CHUNK_VERIFY: "d000c3e65ffcb3e00d2dee8b7161a9dd0b4e4716",
    GEN26: "6386f52cf8c1dc4044ba2f6cc3bf0cc63c6f81c1",
    ACTIVE: "20da16902171b267294acee0f3b80997d8fd5246",
    QPEEL: "e5b41410e570d5e442afe985dd5b7f3355d5d653",
    DEN19_BRIDGE: "c125b09be3fcf572e5264f0c0b1db41ae9b74cf2",
}
EXPECTED_CERT_CANONICAL = "7ef8ce746f44ed729a3c87d21d6b5be4e7e711a4af087233951dd4ee80a20da9"
EXPECTED_G25_CANONICAL = "7399ef3d817578b2f052c97baada75c2a6166ee1313d32f5bed01f6736865513"
EXPECTED_GEN26_CANONICAL = "268ad742fff7bbe43491dbfebf29c7252091387cc08ca2c95c312db000c0ebaa"
EXPECTED_Q_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert calc == got
    return got


def run_checked(path: Path, marker: str) -> str:
    cp = subprocess.run([sys.executable, "-B", str(path)], text=True, capture_output=True, timeout=240)
    if cp.returncode != 0:
        raise SystemExit(f"{path.name} failed:\n{cp.stdout}\n{cp.stderr}")
    assert marker in cp.stdout
    return cp.stdout


def main() -> None:
    for path, blob in EXPECTED_BLOBS.items():
        assert git_blob(path) == blob, path

    # Permanent literal-Q transport must reconstruct exact candidate bytes.
    run_checked(CHUNK_VERIFY, "STAGE35_EX_GOAL4AJ_QCANDIDATE_CHUNKS=PASS")

    mat = json.loads(MAT.read_text(encoding="utf-8"))
    assert mat["q_candidate_sha256"] == EXPECTED_Q_SHA
    assert mat["q_candidate_text_bytes"] == 208802
    assert mat["support_count"] == mat["reconstructed_count"] == 5924
    assert mat["q_candidate_max_abs_numerator"] == 39155899
    assert mat["q_candidate_max_denominator"] == 174336

    g25 = json.loads(G25.read_text(encoding="utf-8"))
    assert canonical(g25) == EXPECTED_G25_CANONICAL
    assert g25["all_27_strict_exact_pass"] is True
    assert g25["exact_condition_coverage"] is True
    assert g25["strict_condition_count"] == 27
    assert g25["strict_total_multiplicity"] == 202
    assert len(g25["ordered_conditions"]) == 27
    assert g25["source_locks"]["candidate_sha256"] == EXPECTED_Q_SHA

    # Reproduce the exact 48-node exceptional bridge from locked retained incidence.
    out = run_checked(GEN26, "GOAL4AJ_GEN26_NUMERATOR_EXCEPTIONAL_BRIDGE=PASS")
    line = next(x for x in out.splitlines() if x.startswith("GOAL4AJ_GEN26_NUMERATOR_EXCEPTIONAL_BRIDGE_JSON="))
    g26 = json.loads(line.split("=", 1)[1])
    assert g26["canonical_sha256"] == EXPECTED_GEN26_CANONICAL
    assert g26["all_48_incidence_relations_hold"] is True
    assert g26["strict_condition_count"] == 27
    assert g26["strict_total_multiplicity"] == 202
    assert g26["exceptional_condition_count"] == 48
    assert len(g26["incidence_rows"]) == 48
    assert all(r["relation_holds"] for r in g26["incidence_rows"].values())

    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical(cert) == EXPECTED_CERT_CANONICAL
    assert cert["literal_q_numerator"]["q_coefficients_over_Q"] is True
    assert cert["literal_q_numerator"]["homogeneous_degree"] == 31
    assert cert["literal_q_numerator"]["support_count"] == 5924
    assert cert["literal_q_numerator"]["q_candidate_sha256"] == EXPECTED_Q_SHA
    assert cert["target_divisor"] == {
        "strict_condition_count": 27,
        "strict_total_multiplicity": 202,
        "exceptional_condition_count": 48,
        "retained_support_count": 75,
        "homogeneous_class": "31H",
        "strict_lower_bounds_exact": True,
        "exceptional_lower_bounds_forced_from_incidence": True,
    }
    eq = cert["divisor_equality_argument"]
    assert eq["candidate_pullback_divisor_class"] == "31H"
    assert eq["candidate_divisor_ge_target"] is True
    assert eq["difference_effective"] is True
    assert eq["difference_linearly_equivalent_to_zero"] is True
    assert eq["effective_linearly_trivial_divisor_on_projective_integral_surface_is_zero"] is True
    assert eq["candidate_divisor_equals_target"] is True
    rr = cert["route_result"]
    assert rr["goal4aj_literal_numerator_materialized"] is True
    assert rr["degree31_numerator_target_divisor_equality_proved"] is True
    fw = cert["credit_firewall"]
    assert fw["literal_degree31_numerator_coefficients_materialized"] is True
    assert fw["degree31_numerator_target_divisor_equality_proved"] is True
    assert fw["explicit_F_B_materialized"] is False
    assert fw["local_evaluations_computed"] is False
    assert fw["brauer_manin_obstruction_obtained"] is False
    assert fw["E1_proved"] is False and fw["stage35_closed"] is False
    assert fw["perfect_cuboid_existence_claim"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False

    print("STAGE35_EX_GOAL4AJ_LITERAL_NUMERATOR_DIVISOR_EQUALITY=PASS")
    print("certificate_canonical_sha256=" + EXPECTED_CERT_CANONICAL)
    print("q_candidate_sha256=" + EXPECTED_Q_SHA)


if __name__ == "__main__":
    main()
