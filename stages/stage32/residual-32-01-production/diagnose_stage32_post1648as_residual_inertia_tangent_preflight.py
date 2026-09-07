#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
AQ_CERT = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"
AR_CERT = HERE / "post1648ar-two-factor-slack-minimal-branches.json"
sys.path.insert(0, str(HERE))

import diagnose_stage32_post1648aq_residual_g_action_preflight as aq  # noqa: E402
from hperp_integral_adapter import HperpIntegralPairingAdapter, RETAINED_BASIS_KNOWN_LABELS_1BASED, _parse_hperp  # noqa: E402


def fingerprint(g: tuple[int, ...]) -> str:
    raw = json.dumps([x + 1 for x in g], separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def main() -> None:
    aq_cert = json.loads(AQ_CERT.read_text())
    ar_cert = json.loads(AR_CERT.read_text())
    if aq_cert["canonical_sha256_without_this_field"] != "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e":
        raise ValueError("AQ canonical regression")
    if ar_cert["canonical_sha256_without_this_field"] != "dba5756e4b10c8bd6e412f1027b8edf693fb74f9ea90f9b591cc99437746a8dd":
        raise ValueError("AR canonical regression")

    marking = aq.load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_as_marking")
    bundle = aq.load_retained(ST33 / "picard_base_rows_retained.py", "s32_as_bundle")
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
    boundary = boundary_candidates[0]
    H = [g for g in group if all(g[i] == i for i in boundary)]
    if len(H) != 8 or Counter(aq.order(g) for g in H) != Counter({1: 1, 2: 7}):
        raise ValueError("residual H regression")

    boundary_incidence: dict[int, set[int]] = {}
    for i in boundary:
        inc = {j for j in range(92, 140) if int(full[i, j]) == 1}
        if len(inc) != 8:
            raise ValueError("boundary exceptional incidence regression")
        boundary_incidence[i] = inc

    dir81 = {x - 1 for x in aq_cert["factor_pullback"]["dir81_labels"]}
    dir105 = {x - 1 for x in aq_cert["factor_pullback"]["dir105_labels"]}
    if dir81 | dir105 != set(boundary) or dir81 & dir105:
        raise ValueError("AQ factor direction boundary split regression")

    basis_indices = [j - 1 for j in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    C = Matrix([[int(x) for x in json.loads(V6_PATH.read_text())["witness"]["picard_coordinates"]]])
    ident = tuple(range(140))

    element_rows = []
    by_fp = {}
    for g in H:
        if g == ident:
            continue
        fp = fingerprint(g)
        M = aq.action_matrix(g, coords, basis_indices)
        Cg = C * M
        fixed_exc = [i for i in range(92, 140) if g[i] == i]
        fixed_normal = [i for i in range(92) if g[i] == i]
        inertia_boundary = [
            i for i in boundary
            if boundary_incidence[i] and boundary_incidence[i].issubset(set(fixed_exc))
        ]
        row = {
            "fingerprint": fp,
            "C_dot_gC": int((C * gram * Cg.T)[0, 0]),
            "cycle_profile_140": aq.cycle_profile(g),
            "fixed_exceptional_count": len(fixed_exc),
            "fixed_exceptional_labels_1based": [i + 1 for i in fixed_exc],
            "fixed_normal_count": len(fixed_normal),
            "fixed_nonboundary_normal_count": len([i for i in fixed_normal if i not in boundary]),
            "boundary_inertia_labels_1based": [i + 1 for i in inertia_boundary],
            "boundary_inertia_dir81_count": len([i for i in inertia_boundary if i in dir81]),
            "boundary_inertia_dir105_count": len([i for i in inertia_boundary if i in dir105]),
        }
        element_rows.append(row)
        by_fp[fp] = row
    element_rows.sort(key=lambda r: (r["fixed_exceptional_count"], r["C_dot_gC"], r["fingerprint"]))

    exc_orbits = aq.orbit_partition(set(range(92, 140)), H)
    if sorted(len(o) for o in exc_orbits) != [4] * 12:
        raise ValueError("exceptional H-orbit regression")
    cusp_rows = []
    evec = [int(x) for x in json.loads(V6_PATH.read_text())["witness"]["all140_pairings"][92:]]
    for o in exc_orbits:
        stabilizers = [g for g in H if g[o[0]] == o[0]]
        if len(stabilizers) != 2:
            raise ValueError("exceptional point stabilizer not order 2")
        h = next(g for g in stabilizers if g != ident)
        fp = fingerprint(h)
        if any(h[j] != j for j in o):
            raise ValueError("abelian stabilizer does not fix whole exceptional orbit pointwise as labels")
        incident = [i for i in boundary if o[0] in boundary_incidence[i]]
        a = [i for i in incident if i in dir81]
        b = [i for i in incident if i in dir105]
        if len(a) != 1 or len(b) != 1:
            raise ValueError("cusp orbit boundary split regression")
        cusp_rows.append({
            "stabilizer_fingerprint": fp,
            "exceptional_labels_1based": [j + 1 for j in o],
            "dir81_boundary_label": a[0] + 1,
            "dir105_boundary_label": b[0] + 1,
            "v6_exceptional_mass": sum(evec[j - 92] for j in o),
        })
    cusp_rows.sort(key=lambda r: (r["stabilizer_fingerprint"], r["dir81_boundary_label"], r["dir105_boundary_label"]))

    cusp_by_h: dict[str, list[dict]] = defaultdict(list)
    for r in cusp_rows:
        cusp_by_h[r["stabilizer_fingerprint"]].append(r)
    inertia_rows = []
    for fp, rows in sorted(cusp_by_h.items()):
        er = by_fp[fp]
        inertia_rows.append({
            "fingerprint": fp,
            "C_dot_gC": er["C_dot_gC"],
            "fixed_exceptional_count": er["fixed_exceptional_count"],
            "boundary_inertia_labels_1based": er["boundary_inertia_labels_1based"],
            "target_cusp_orbit_count": len(rows),
            "target_cusp_mass_list": [r["v6_exceptional_mass"] for r in rows],
            "target_cusp_mass_sum": sum(r["v6_exceptional_mass"] for r in rows),
        })

    node_stabilizer_fps = sorted(cusp_by_h)
    non_node_elements = [r for r in element_rows if r["fingerprint"] not in cusp_by_h]
    min_minimal = int(ar_cert["minimal_branch_bound"]["minimum_FSM_minimal_A_B_1_1_branches"])
    if min_minimal != 186:
        raise ValueError("AR minimal branch regression")

    out = {
        "mode": "SCRATCH_POST1648AS_RESIDUAL_INERTIA_TANGENT_PREFLIGHT",
        "parents": {
            "AQ_canonical": aq_cert["canonical_sha256_without_this_field"],
            "AR_canonical": ar_cert["canonical_sha256_without_this_field"],
        },
        "residual_group": {
            "order": len(H),
            "nontrivial_element_count": 7,
            "element_rows": element_rows,
        },
        "node_stabilizers": {
            "distinct_nontrivial_stabilizer_count": len(node_stabilizer_fps),
            "fingerprints": node_stabilizer_fps,
            "inertia_rows": inertia_rows,
            "non_node_element_rows": non_node_elements,
            "exceptional_orbit_count": len(exc_orbits),
            "exceptional_orbit_sizes": [len(o) for o in exc_orbits],
        },
        "local_source_model": {
            "target_map": "(x,y,z)=(p^2,pq,q^2) -> (X,Z)=(x,z)",
            "node_stabilizer_action": "(x,y,z)->(x,-y,z)",
            "resolution_exceptional_coordinate_action": "u->-u",
            "exceptional_fixed_landings": ["0", "infinity"],
            "FSM_minimal_landing": "lambda in C*",
            "FSM_minimal_branch_fixed_by_node_stabilizer": False,
        },
        "AR_minimal_branch_pressure": {
            "minimum_FSM_minimal_branches": min_minimal,
            "minimum_on_some_target_cusp_by_12_point_pigeonhole": (min_minimal + 11) // 12,
            "minimum_on_some_exceptional_curve_by_48_curve_pigeonhole": (min_minimal + 47) // 48,
            "opposite_landing_collision_required_for_exceptional_C_intersect_hC_from_minimal_branches": True,
            "retained_lambda_or_jet_constraints_available": False,
        },
        "decision": {
            "v6_carrier_excluded": False,
            "bounded_wall": "RESIDUAL_G_TANGENT_ACTION_ALONE_DOES_NOT_FORCE_OPPOSITE_LANDING_COLLISIONS_FOR_THE_186_MINIMAL_BRANCHES",
            "next_missing_input": "MEMBER_LEVEL_EXCEPTIONAL_LANDING_VALUES_OR_JET_CONSTRAINTS_OR_A_GLOBAL_BOUND_ON_OFF_EXCEPTIONAL_C_INTERSECT_hC",
        },
        "firewalls": {
            "scratch_only": True,
            "retained_payload_emitted": False,
            "shared_MAIN_STATE_unchanged": True,
            "shared_authority_unchanged": True,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
