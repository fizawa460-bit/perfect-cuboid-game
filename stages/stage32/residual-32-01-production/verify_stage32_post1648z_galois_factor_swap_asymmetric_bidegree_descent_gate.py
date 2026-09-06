#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648z-galois-factor-swap-asymmetric-bidegree-descent-gate.json"
NOTE = HERE / "post1648z-galois-factor-swap-asymmetric-bidegree-descent-source-note.md"
POST1484 = HERE / "post1484-v6-modular-factor-bidegree-boundary.json"
V6 = HERE.parent / "32-21" / "post1473-v6-witness-body-recovered.json"

EXPECTED_CERT_CANONICAL = "cc2fc48738e35d62883e7cf94f6b75c8153d066346b72a0b9ce05deaae1eb36b"
EXPECTED_NOTE_BLOB = "4ce77ed7aed56364a4a120980ac6de3be81cfbb9"
EXPECTED_POST1484_CANONICAL = "791870c37681702392e1e59d224f494ed791709d467efa68a20cf49bff4ab420"
EXPECTED_POST1484_BLOB = "072266f2ac5386316adc99e35a6444d2449656c8"
EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(path: Path, canonical: str, blob: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert canonical_sha(obj) == canonical
    assert obj["canonical_sha256_without_this_field"] == canonical
    assert git_blob_sha(path) == blob
    return obj


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL
    assert git_blob_sha(NOTE) == EXPECTED_NOTE_BLOB

    bideg = load_locked(POST1484, EXPECTED_POST1484_CANONICAL, EXPECTED_POST1484_BLOB)
    v6 = load_locked(V6, EXPECTED_V6_CANONICAL, EXPECTED_V6_BLOB)

    assert bideg["fixed_target"]["row_id"] == "g1-d186"
    assert bideg["modular_factor_bidegree"]["first_z"] == 105
    assert bideg["modular_factor_bidegree"]["second_w"] == 81
    assert bideg["modular_factor_bidegree"]["sum"] == 186
    assert v6["target"]["row_id"] == "g1-d186"
    assert v6["witness"]["self_intersection"] == 758

    ext = cert["external_source_lock"]["stoll_testa"]
    facts = ext["exact_supported_facts"]
    assert any("switches the two factors" in x for x in facts)
    assert any("Res_{Q(i)/Q}" in x for x in facts)
    assert any("exchanges the two geometric X(4) factor fibrations" in x for x in facts)

    der = cert["exact_derivation"]
    m = tuple(der["fixed_bidegree"])
    ms = tuple(der["conjugate_class_bidegree"])
    assert m == (105, 81)
    assert ms == (81, 105)
    assert ms == (m[1], m[0])
    assert m != ms
    assert der["bidegrees_equal"] is False
    assert der["sigma_D_equals_D"] is False
    assert der["fixed_V6_class_Q_galois_fixed"] is False
    assert der["fixed_V6_class_defined_over_Q"] is False

    rpc = cert["rational_point_consequence"]
    assert rpc["Q_defined_integral_irreducible_curve_in_exact_class_D_possible"] is False
    assert rpc["geometrically_irreducible_curve_in_D_can_have_infinite_Q_rational_subset"] is False
    assert rpc["isolated_Q_rational_points_excluded"] is False
    assert rpc["remaining_possible_location_for_Q_points"] == "C intersect sigma(C)"

    broad = cert["route_broadening"]
    assert broad["user_requested_third_perspective"] is True
    assert broad["marking_routes_paused"] is True
    assert broad["blind_rediscovery_performed"] is True
    assert broad["selected_route"] == "Q_GALOIS_FACTOR_SWAP_OF_MODULAR_FIBRATIONS_AND_ASYMMETRIC_BIDEGREE"

    decision = cert["decision"]
    assert decision["new_third_perspective_route_obtained"] is True
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert decision["O212_plus_advance_allowed"] is False

    fw = cert["firewalls"]
    assert not any([
        fw["scratch_result_promoted_to_MAIN_authority"],
        fw["scratch_result_promoted_to_current_credit"],
        fw["non_Q_fixed_class_promoted_to_geometric_nonexistence"],
        fw["infinite_Q_point_obstruction_promoted_to_isolated_Q_point_obstruction"],
        fw["intersection_support_computed"],
        fw["Q602_excluded"],
        fw["O210_excluded"],
        fw["receiver_credit"],
        fw["route_credit"],
        fw["theorem_credit"],
        fw["endpoint_credit"],
        fw["perfect_cuboid_credit"],
    ])

    print("POST1648Z_GALOIS_FACTOR_SWAP_ASYMMETRIC_BIDEGREE_DESCENT_GATE_COMPLETE")
    print("fixed_bidegree=(105,81) conjugate_bidegree=(81,105) sigma_D_ne_D=true")
    print("Q_defined_curve_in_class=false infinite_Q_subset=false isolated_Q_points_excluded=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
