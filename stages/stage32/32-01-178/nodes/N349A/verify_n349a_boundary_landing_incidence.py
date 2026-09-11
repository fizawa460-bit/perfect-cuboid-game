#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
ST33 = ROOT / "stages/stage33/33-07"
N349 = HERE.parent / "N349/RESULT.json"
AR_NOTE = RESIDUAL / "post1648ar-two-factor-slack-minimal-branches-source-note.md"
AS_NOTE = RESIDUAL / "post1648as-residual-inertia-tangent-preflight-source-note.md"
AQ_CERT = RESIDUAL / "post1648aq-residual-g-cusp-multiplicity-grid.json"
MARKING = ST33 / "stage32_picard_marking_retained.py"
BUNDLE = ST33 / "picard_base_rows_retained.py"

sys.path.insert(0, str(RESIDUAL))
import diagnose_stage32_post1648aq_residual_g_action_preflight as aq  # noqa: E402
from hperp_integral_adapter import HperpIntegralPairingAdapter, _parse_hperp  # noqa: E402

EXPECTED_N349 = "10bdf80d8e9755455133226ac1166da254fec8b956658a53fde769f33c5cd12b"
EXPECTED_AQ = "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    d = json.loads(path.read_text())
    claimed = d.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(d) != expected:
        raise ValueError(f"canonical regression: {path}")
    d["canonical_sha256_without_this_field"] = claimed
    return d


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    n349 = load_canonical(N349, EXPECTED_N349)
    if n349["aggregate"]["boundary_terminal_count"] != 21:
        raise ValueError("N349 terminal-count regression")
    if n349["aggregate"]["required_local_pair_at_every_node"] != [4, 4]:
        raise ValueError("N349 local-pair regression")
    if n349["aggregate"]["local_pair_evidence_unknown_count"] != 21:
        raise ValueError("N349 unknown-count regression")

    ar = AR_NOTE.read_text()
    for s in [
        "a1=4*A`, `a2=4*B",
        "The unique FSM-minimal type is `(A,B)=(1,1)`",
        "landing away from the two boundary-intersection points",
    ]:
        if s not in ar:
            raise ValueError(f"AR local-semantics regression: {s}")
    ass = AS_NOTE.read_text()
    for s in [
        "u -> -u",
        "fixed points on the exceptional `P1` are `u=0` and `u=infinity`",
        "finite nonzero exceptional ratio `u=lambda in C*`",
        "precisely the two boundary-intersection directions",
    ]:
        if s not in ass:
            raise ValueError(f"AS tangent-semantics regression: {s}")

    aq_cert = load_canonical(AQ_CERT, EXPECTED_AQ)
    marking = aq.load_retained(MARKING, "s32_n349a_marking")
    bundle = aq.load_retained(BUNDLE, "s32_n349a_bundle")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("marking canonical regression")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("bundle canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    gens = [aq.perm0(p) for p in marking["aut_action"]["permutations_1based"]]
    group = aq.close(gens)
    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]
    normal_orbits = aq.orbit_partition(set(range(92)), group)
    boundary_candidates = [o for o in normal_orbits if len(o) == 12 and {degrees[i] for i in o} == {4}]
    if len(boundary_candidates) != 1:
        raise ValueError("boundary orbit regression")
    boundary = sorted(boundary_candidates[0])

    boundary_incidence: dict[int, set[int]] = {}
    for i in boundary:
        inc = {j for j in range(92, 140) if int(full[i, j]) == 1}
        if len(inc) != 8:
            raise ValueError("boundary exceptional incidence regression")
        boundary_incidence[i] = inc

    dir81 = {x - 1 for x in aq_cert["factor_pullback"]["dir81_labels"]}
    dir105 = {x - 1 for x in aq_cert["factor_pullback"]["dir105_labels"]}
    if dir81 | dir105 != set(boundary) or dir81 & dir105:
        raise ValueError("factor-direction boundary split regression")

    H = [g for g in group if all(g[i] == i for i in boundary)]
    if len(H) != 8:
        raise ValueError("residual H order regression")
    exc_orbits = aq.orbit_partition(set(range(92, 140)), H)
    if sorted(len(o) for o in exc_orbits) != [4] * 12:
        raise ValueError("exceptional H-orbit regression")

    orbit_id_by_exc: dict[int, int] = {}
    for orbit_id, orbit in enumerate(sorted((sorted(o) for o in exc_orbits), key=lambda o: o[0]), start=1):
        for j in orbit:
            orbit_id_by_exc[j] = orbit_id

    rows = []
    for j in range(92, 140):
        incident = sorted(i for i in boundary if j in boundary_incidence[i])
        if len(incident) != 2:
            raise ValueError(f"exceptional label {j+1} does not have two boundary directions")
        a = [i for i in incident if i in dir81]
        b = [i for i in incident if i in dir105]
        if len(a) != 1 or len(b) != 1:
            raise ValueError(f"exceptional label {j+1} direction split regression")
        rows.append({
            "exceptional_label_1based": j + 1,
            "residual_H_orbit_id": orbit_id_by_exc[j],
            "boundary_pair_1based_unordered": [i + 1 for i in incident],
            "dir81_boundary_label_1based": a[0] + 1,
            "dir105_boundary_label_1based": b[0] + 1,
            "fixed_landing_count": 2,
            "fsm_minimal_requires_avoid_both_fixed_landings": True,
        })

    if len(rows) != 48:
        raise ValueError("N349A exceptional mapping count regression")
    if sum(len(v) for v in boundary_incidence.values()) != 96:
        raise ValueError("N349A incidence total regression")
    boundary_labels = [i + 1 for i in boundary]
    if sorted(set(boundary_labels)) != list(range(33, 45)):
        raise ValueError(f"boundary label regression: {boundary_labels}")

    result = {
        "schema": "STAGE32_32_01_178_N349A_BOUNDARY_LANDING_INCIDENCE_V1",
        "node_id": "N349A",
        "status": "EXACT_PREPARATORY_ADAPTER_NO_PROMOTION",
        "source_locks": {
            "n349_checkpoint_canonical": EXPECTED_N349,
            "n349_audit_status": "AUDIT_REQUIRED_NOT_CONSUMED",
            "aq_canonical": EXPECTED_AQ,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
            "ar_source_note_blob_sha1": git_blob_sha1(AR_NOTE),
            "as_source_note_blob_sha1": git_blob_sha1(AS_NOTE),
            "fsm_primary_source_doi": "10.1307/mmj/1480734014",
        },
        "local_reduction": {
            "n349_required_pair": [4, 4],
            "scaled_factor_orders": [1, 1],
            "exceptional_contact": 1,
            "exceptional_coordinate": "u",
            "inertia_action": "u -> -u",
            "fixed_landings": ["0", "infinity"],
            "fsm_minimal_landing": "lambda in C*",
            "equivalent_member_level_test": "on every one of the 48 exceptional curves, the strict-transform landing must avoid its two boundary-intersection points",
        },
        "boundary_geometry": {
            "boundary_normal_labels_1based": boundary_labels,
            "boundary_curve_count": 12,
            "exceptional_curve_count": 48,
            "boundary_exceptional_incidence_count": 96,
            "residual_H_exceptional_orbit_count": 12,
            "residual_H_exceptional_orbit_size": 4,
            "each_exceptional_has_exactly_two_boundary_directions": True,
            "each_boundary_has_exactly_eight_exceptional_incidents": True,
        },
        "exceptional_landing_map": rows,
        "aggregate": {
            "boundary_terminal_count": 21,
            "mapped_exceptional_count": 48,
            "forbidden_fixed_landing_count_per_member": 96,
            "actual_member_landing_certified_terminal_count": 0,
            "actual_member_landing_unknown_terminal_count": 21,
        },
        "conclusion": {
            "n349_pair_gap_reduced_to_finite_fixed_landing_avoidance_problem": True,
            "next_required_adapter": "ACTUAL_MEMBER_TO_48_EXCEPTIONAL_LANDING_POINTS_OR_EQUIVALENT_BOUNDARY_CONTACT_CERTIFICATE",
            "new_numerical_pruning_credit": False,
        },
        "semantics": {
            "n349_hostile_audit_still_required": True,
            "n349_not_promoted_by_this_adapter": True,
            "actual_integral_irreducible_member_not_constructed": True,
            "actual_member_landing_values_not_present": True,
            "picard_pairing_one_alone_does_not_certify_fixed_landing_avoidance": True,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N349A_BOUNDARY_LANDING_INCIDENCE_ADAPTER",
        "terminals": 21,
        "exceptional_mapped": 48,
        "fixed_landings_per_member": 96,
        "member_landings_certified": 0,
        "member_landings_unknown": 21,
        "canonical": result["canonical_sha256_without_this_field"],
        "pruning_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
