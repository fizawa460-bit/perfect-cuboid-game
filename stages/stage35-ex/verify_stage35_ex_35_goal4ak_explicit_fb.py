#!/usr/bin/env python3
"""Verify provisional exact Goal4AK explicit class-B rational function assembly."""
from __future__ import annotations

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage35-ex/35ex-35/goal4ak-explicit-fb-assembly.json"
ART_BLOB = "0df946bc8a85d635920f63df05283664cb85acd4"
ART_CANONICAL = "459185c925796b564365b6deede51262d3595574877f01c209425ea5c28fb2a8"
LOADER = ROOT / "stages/stage35-ex/35ex-35/goal4ak_explicit_fb.py"
LOADER_BLOB = "8b47b4453a630143690da04a238ffcd7dbf8c9b7"
CLAIM_SYNC = ROOT / "stages/stage35-ex/35ex-35/goal4aj-audited-claim-sync.json"
NUM_EQ = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-literal-numerator-divisor-equality.json"
DEN_LOCK = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-denominator-source-lock.md"
GOAL4Z = ROOT / "stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization-source-lock.md"
NUM_MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json"
DEN_MANIFEST = ROOT / "stages/stage35-ex/35ex-35/goal4ak-degree31-denominator-transport.json"

EXPECTED_BLOBS = {
    CLAIM_SYNC: "498a1e7554a8016863a6518cde91edd591f20b38",
    NUM_EQ: "a60034bb2b2e3cbd16d96fa26b76eeaf1210900f",
    DEN_LOCK: "95c0eef4a420234964217d3ceb41e57ea5e5b95d",
    GOAL4Z: "3a1c2174ee6e45bb693791ae2e974ed2f27fe2a3",
    NUM_MANIFEST: "85b52e921f36fc445fd243db1a3b3f65bb298966",
    DEN_MANIFEST: "651896391b7fcd2e79dd978d698e170af1e1cca9",
}


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical_without_field(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    assert git_blob(ART) == ART_BLOB
    assert git_blob(LOADER) == LOADER_BLOB
    for path, blob in EXPECTED_BLOBS.items():
        assert git_blob(path) == blob

    a = json.loads(ART.read_text(encoding="utf-8"))
    assert a["schema"] == "STAGE35_EX_35_GOAL4AK_EXPLICIT_F_B_ASSEMBLY_V1"
    assert a["canonical_sha256"] == ART_CANONICAL
    assert canonical_without_field(a) == ART_CANONICAL
    assert a["explicit_rational_function"]["definition"] == "F_B := A31 / B31"
    assert a["explicit_rational_function"]["same_homogeneous_degree"] is True
    assert a["explicit_rational_function"]["projective_ratio_well_defined"] is True
    assert a["explicit_rational_function"]["class_B_symbol"] == "(-1,F_B)"
    assert a["explicit_rational_function"]["class_B_equality_scope"] == "modulo Br_0(U)"
    assert a["route_result"]["explicit_F_B_materialized_provisional"] is True
    assert a["route_result"]["downstream_local_evaluation_released"] is False
    assert a["credit_firewall"]["hostile_audit_pending"] is True
    assert a["credit_firewall"]["authoritative_explicit_F_B_credit"] is False
    for k in ["local_evaluations_computed", "verticality_proved", "brauer_manin_obstruction_obtained", "E1_proved", "R29_PESCH_E1_closed", "R29_FIB2_closed", "stage35_closed", "theorem_credit", "receiver_credit", "endpoint_credit", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"]:
        assert a["credit_firewall"][k] is False

    # Replay both permanent transports before consuming them.
    runpy.run_path(str(ROOT / "stages/stage35-ex/verify_stage35_ex_35_goal4aj_qcandidate_chunks.py"), run_name="__main__")
    runpy.run_path(str(ROOT / "stages/stage35-ex/verify_stage35_ex_35_goal4ak_denominator_transport.py"), run_name="__main__")

    ns = runpy.run_path(str(LOADER))
    num, den = ns["load_terms"]()
    assert len(num) == 5924 and len(den) == 1542
    assert all(sum(ex) == 31 for _, ex in num + den)

    # Exact evaluator smoke test and projective degree-31 cancellation.
    candidates = [
        (1, 1, 1, 1, 1, 1, 1),
        (1, 2, 3, 4, 5, 6, 7),
        (1, -1, 2, -2, 3, -3, 4),
        (1, 2, -3, 5, -7, 11, 13),
        (1, 3, 5, 7, 11, 13, 17),
    ]
    chosen = None
    for p in candidates:
        b = ns["evaluate_terms"](den, p)
        if b != 0:
            chosen = p
            break
    assert chosen is not None
    av = ns["evaluate_terms"](num, chosen)
    bv = ns["evaluate_terms"](den, chosen)
    fb = av / bv
    scaled = tuple(2 * x for x in chosen)
    av2 = ns["evaluate_terms"](num, scaled)
    bv2 = ns["evaluate_terms"](den, scaled)
    assert av2 == av * (2 ** 31)
    assert bv2 == bv * (2 ** 31)
    assert av2 / bv2 == fb
    if chosen[0] == 1:
        assert ns["evaluate_FB_affine"](*chosen[1:]) == fb
    assert isinstance(fb, Fraction)

    print("STAGE35_EX_GOAL4AK_EXPLICIT_FB=PASS")
    print("numerator_sha256=" + a["permanent_transports"]["numerator"]["raw_sha256"])
    print("denominator_sha256=" + a["permanent_transports"]["denominator"]["raw_sha256"])
    print("downstream_local_evaluation_released=false")


if __name__ == "__main__":
    main()
