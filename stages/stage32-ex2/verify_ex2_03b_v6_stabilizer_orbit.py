#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-03/v6-stabilizer-divisor-orbit-preflight.json"
PRIOR = ROOT / "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
BJ = ROOT / "stages/stage32/residual-32-01-production/post1648bj-cc-v6-aut-orbit-scratch-result.json"
BJ_VERIFY = ROOT / "stages/stage32/residual-32-01-production/verify_stage32_post1648bj_cc_v6_aut_orbit.py"
BJ_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648bj-cc-v6-aut-orbit-source-note.md"

LOCKS = {
    PRIOR: "222b4a17a75b397831fe6b641e9459d042aeec60",
    V6: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    BJ: "5601e1cdfd68ec0a92f8046e4e1a5ce245463ec7",
    BJ_VERIFY: "8493fe176730efe7e9e532edb08b7a3f08057a9c",
    BJ_NOTE: "9fba84c740f44539fd03aea3a3431d3fa6a73318",
}
EXPECTED_CANONICAL = "32922653ccac17e7177818890b6e41e0fccdd041f7a9f936b1b97b24c25fbef6"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    for path, expected in LOCKS.items():
        actual = blob(path)
        assert actual == expected, (path, actual, expected)

    cert = json.loads(CERT.read_text())
    prior = json.loads(PRIOR.read_text())
    v6 = json.loads(V6.read_text())
    bj = json.loads(BJ.read_text())

    assert cert["schema"] == "STAGE32EX2_EX2_03B_V6_STABILIZER_DIVISOR_ORBIT_PREFLIGHT_V1"
    assert cert["status"] == "PASS_EXACT_RETAINED_AUT_STABILIZER_TRIVIAL_SYMMETRY_DIVISOR_ORBIT_BLOCKED"
    assert cert["unit"] == "EX2-03B"
    assert cert["target"]["divisor_class"] == "V6"
    assert cert["target"]["zero_intersection_curve_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]
    assert prior["distinct_lane_route"]["next_leaf"] == "EX2-03B_SYMMETRY_DIVISOR_ORBIT_PREFLIGHT"
    assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"

    # Replay the source-bound retained Aut orbit calculation. The underlying
    # giant retained payloads stay runner-side through the existing Stage32 adapter.
    replay = subprocess.check_output([sys.executable, "-B", str(BJ_VERIFY)], cwd=ROOT, text=True)
    replay_obj = json.loads(replay)
    assert replay_obj["verdict"] == "PASS_STAGE32_POST1648BJ_CC_V6_AUT_ORBIT_EXACT_REPLAY"
    assert replay_obj["orbit_size"] == 1536
    assert replay_obj["stabilizer_size"] == 1

    orbit = bj["exact_aut_orbit"]
    assert orbit["orbit_size"] == 1536
    assert orbit["stabilizer_size"] == 1

    exact = cert["exact_finite_result"]
    assert exact["retained_aut_group_order"] == 1536
    assert exact["v6_aut_orbit_size"] == 1536
    assert exact["v6_stabilizer_size"] == 1
    assert exact["nonidentity_retained_aut_stabilizing_v6_exists"] is False
    assert exact["identity_is_only_retained_v6_stabilizer"] is True

    infer = cert["divisor_orbit_inference"]
    assert infer["same_linear_system_requires"] == "g(V6)=V6"
    assert infer["nonidentity_same_class_orbit_member_available_from_retained_aut"] is False
    assert infer["identity_produces_distinct_member"] is False
    assert infer["retained_aut_divisor_orbit_method_can_certify_zero_curve_nonfixedness"] is False
    assert infer["line_bundle_linearization_needed_for_this_negative_class_level_blocker"] is False

    route = cert["distinct_lane_route"]
    assert route["next_leaf"] == "EX2-03C_ALTERNATE_KNOWN140_DECOMPOSITION_PREFLIGHT"
    assert route["target_zero_labels_1based"] == [17, 21, 24, 25, 30, 31, 98]
    assert route["original_known140_decomposition_contains_all_target_zero_curves"] is True
    assert route["solver_miss_is_nonexistence_proof"] is False
    assert route["bounded_known140_search_is_complete_linear_system"] is False
    assert route["whole_fetch_giant_payload_into_chat_forbidden"] is True

    assert cert["exit"]["EX2_03B_complete"] is True
    assert cert["exit"]["symmetry_divisor_orbit_lane_blocked_within_retained_aut"] is True
    assert cert["exit"]["base_locus_or_fixed_part_credit_added"] is False
    assert cert["exit"]["stage_exhausted"] is False

    assert cert["claim_sync"]["triggered"] is False
    for key, value in cert["credit_firewall"].items():
        assert value is False, (key, value)

    payload = dict(cert)
    stored = payload.pop("canonical_sha256_without_this_field")
    assert stored == EXPECTED_CANONICAL
    assert csha(payload) == stored

    print(
        "Stage32EX2 EX2-03B: PASS; the retained Aut group has order/orbit 1536 and V6 stabilizer size 1, "
        "so no nonidentity retained automorphism can generate a distinct divisor inside |V6|. "
        "No fixed-part credit is added; route EX2-03C to alternate exact known140 decompositions."
    )


if __name__ == "__main__":
    main()
