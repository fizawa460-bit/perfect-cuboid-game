#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1532-full-stoll-h-orbit-symmetry-negative.json"
CONTROLLER = ROOT / "stages/stage32/controller.json"
H_DECK = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json"
DIAG = HERE / "diagnose_stage32_post1529_full_stoll_h_orbit.py"

EXPECTED_CANONICAL = "6067bf47c856561917de355c0bb734580846f06fd3beaa81f43297721ca241aa"
EXPECTED_H_DECK_CANONICAL = "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"
EXPECTED_BLOBS = {
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json": "9cd6d7122b8a3149b8ab79396946d72b986649df",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1529_full_stoll_h_orbit.py": "3788b503a918db1431ca8be94b84627f2475c5a5",
    "stages/stage32/residual-32-01-production/post1532-full-stoll-h-orbit-symmetry-negative-source-note.md": "dc1b6cc88a8e45f8c7c256df0cb5bdb3b74f3c9c",
}


def canonical_sha(obj: dict) -> str:
    core = dict(obj)
    got = core.pop("canonical_sha256_without_this_field")
    calc = hashlib.sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if got != calc:
        raise SystemExit(f"canonical mismatch: field={got} calc={calc}")
    return calc


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    if cert["schema"] != "STAGE32_POST1532_FULL_STOLL_H_ORBIT_SYMMETRY_NEGATIVE_V1":
        raise SystemExit("certificate schema moved")
    if cert["status"] != "EXACT_BOUNDED_NEGATIVE_PENDING_HOSTILE_AUDIT":
        raise SystemExit("certificate lifecycle moved")
    if canonical_sha(cert) != EXPECTED_CANONICAL:
        raise SystemExit("certificate canonical moved")

    for rel, expected in EXPECTED_BLOBS.items():
        got = git_blob_sha(ROOT / rel)
        if got != expected:
            raise SystemExit(f"source-lock blob moved: {rel}: {got} != {expected}")

    locks = cert["source_locks"]
    if locks["recovered_v6_witness"] != {
        "path": "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
        "blob_sha1": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
        "canonical_sha256": "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8",
    }:
        raise SystemExit("recovered V6 source lock moved")
    if locks["retained_picard_stoll_action"] != {
        "path": "stages/stage33/33-07/stage32_picard_marking_retained.py",
        "blob_sha1": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
        "schema": "STAGE32_AUT_PERM_SOURCELOCK_V1",
        "generator_count": 9,
        "class_count": 140,
    }:
        raise SystemExit("retained Picard/Stoll action source lock moved")
    if locks["post1490_h_deck_asset"] != {
        "path": "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json",
        "blob_sha1": "9cd6d7122b8a3149b8ab79396946d72b986649df",
        "canonical_sha256": EXPECTED_H_DECK_CANONICAL,
    }:
        raise SystemExit("H-deck source lock moved")

    witness = json.loads((ROOT / locks["recovered_v6_witness"]["path"]).read_text())
    if canonical_sha(witness) != locks["recovered_v6_witness"]["canonical_sha256"]:
        raise SystemExit("recovered V6 canonical moved")
    if witness["target"]["row_id"] != "g1-d186" or len(witness["witness"]["all140_pairings"]) != 140:
        raise SystemExit("recovered V6 target/pairing vector moved")

    hdeck = json.loads(H_DECK.read_text())
    if hdeck["schema"] != "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BEAUVILLE_DECK_CROSS_EXCLUSION_V1":
        raise SystemExit("post1490 H-deck schema moved")
    if canonical_sha(hdeck) != EXPECTED_H_DECK_CANONICAL:
        raise SystemExit("post1490 H-deck canonical moved")
    hwords = hdeck["equivariant_adapter"]["modular_to_stoll"]
    if hwords != {"u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("post1490 H-deck words moved")

    target = cert["fixed_target"]
    if (target["row_id"], target["O"], target["qprime"], target["required_Q"]) != (
        "g1-d186", 210, 4, 602
    ):
        raise SystemExit("fixed target moved")

    finite = cert["finite_result"]
    if finite["retained_stoll_group_order"] != 1536:
        raise SystemExit("retained Stoll group order moved")
    if (finite["h_deck_group_order"], finite["h_orbit_size"]) != (4, 4):
        raise SystemExit("H group/orbit size moved")
    if finite["h_deck_words"] != {"id": "1", "u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"}:
        raise SystemExit("certificate H words moved")
    if finite["base_class_to_h_orbit_count"] != 4 or finite["base_class_to_h_orbit_outside_h_count"] != 0:
        raise SystemExit("base-to-H orbit result moved")
    if finite["setwise_h_orbit_stabilizer_count"] != 4 or finite["setwise_h_orbit_stabilizer_outside_h_count"] != 0:
        raise SystemExit("setwise H-orbit stabilizer result moved")

    expected_base = [
        {"word": "1", "H_matches": ["id"], "is_H_deck_element": True},
        {"word": "g7*g8", "H_matches": ["v"], "is_H_deck_element": True},
        {"word": "g7*g9", "H_matches": ["u"], "is_H_deck_element": True},
        {"word": "g8*g9", "H_matches": ["uv"], "is_H_deck_element": True},
    ]
    expected_setwise = [
        {"word": "1", "is_H_deck_element": True},
        {"word": "g7*g8", "is_H_deck_element": True},
        {"word": "g7*g9", "is_H_deck_element": True},
        {"word": "g8*g9", "is_H_deck_element": True},
    ]
    if finite["base_class_to_h_orbit_elements"] != expected_base:
        raise SystemExit("exact base-hit list moved")
    if finite["setwise_h_orbit_stabilizer_elements"] != expected_setwise:
        raise SystemExit("exact setwise stabilizer list moved")

    proc = subprocess.run(["python3", str(DIAG)], cwd=ROOT, text=True, capture_output=True, check=True)
    replay = json.loads(proc.stdout)
    replay_keys = [
        "retained_stoll_group_order",
        "h_deck_group_order",
        "h_orbit_size",
        "base_class_to_h_orbit_count",
        "base_class_to_h_orbit_outside_h_count",
        "base_class_to_h_orbit_elements",
        "setwise_h_orbit_stabilizer_count",
        "setwise_h_orbit_stabilizer_outside_h_count",
        "setwise_h_orbit_stabilizer_elements",
    ]
    for key in replay_keys:
        if replay[key] != finite[key]:
            raise SystemExit(f"diagnostic replay disagrees with certificate: {key}")
    if replay["scope"] != "EXACT_NUMERICAL_PICARD_ACTION_ONLY_NO_CORRESPONDENCE_EQUIVARIANCE_CREDIT":
        raise SystemExit("diagnostic scope firewall moved")

    decision = cert["decision"]
    if decision["result"] != "EXACT_BOUNDED_NEGATIVE" or decision["route_closed"] is not True:
        raise SystemExit("bounded-negative decision moved")
    if decision["closed_subroute"] != "REUSE_EXISTING_RETAINED_STOLL_SYMMETRY_OUTSIDE_H":
        raise SystemExit("closed-subroute scope moved")
    forbidden = [
        "O210_excluded",
        "Q602_excluded",
        "actual_T_commutation_proved",
        "O212_plus_advance_allowed",
        "controller_change_authorized",
    ]
    if any(decision[key] for key in forbidden):
        raise SystemExit("negative leaf illegally promotes Stage32 authority")
    if any(cert["firewalls"].values()):
        raise SystemExit("negative leaf credit firewall regression")

    controller = json.loads(CONTROLLER.read_text())
    ct = controller["fixed_target"]
    if controller.get("stage32_closed") is not False:
        raise SystemExit("controller unexpectedly closes Stage32")
    if (ct["row_id"], ct["O"], ct["qprime"], ct["Q"]) != ("g1-d186", 210, 4, 602):
        raise SystemExit("live controller O210/Q602 target moved")

    print("PASS STAGE32_POST1532_FULL_STOLL_H_ORBIT_SYMMETRY_NEGATIVE_V1")
    print("canonical_sha256=" + EXPECTED_CANONICAL)
    print("full_stoll_order=1536 H_order=4 H_orbit_size=4")
    print("base_hits=4 outside_H=0 setwise_stabilizer=4 outside_H=0")
    print("only_H_words=['1','g7*g8','g7*g9','g8*g9']")
    print("O210/Q602 remain OPEN; actual T commutation unproved; O212+ blocked; controller unchanged")


if __name__ == "__main__":
    main()
