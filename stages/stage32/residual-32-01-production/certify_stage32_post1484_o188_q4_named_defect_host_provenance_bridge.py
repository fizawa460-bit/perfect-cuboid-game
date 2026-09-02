#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import defaultdict
from pathlib import Path

WITNESS_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
WITNESS_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
WITNESS_ALL140 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
BUDGET_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
BUDGET_BLOB = "dd5fdb8d2553d25a1479c1e5cff68a201c8396e3"
BUDGET_GENERATOR_BLOB = "b9aa8823df415119270a9b13c1559c5de05fd02a"
INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
INCIDENCE_BLOB = "b3f673aa73324ee731356eec2c0448592fd1e59b"
ADAPTER_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
ADAPTER_BLOB = "d3f9c82ab087ea4a2721737867159900a3f304c4"
SIGMA_ORDER_BLOB = "269a7a607ba195647f960c15c2b730273bc79a1b"
OUTPUT_CANONICAL = "daa994744ce2d27e82d23f6561ab48fed9abcaa60d95866638d3e8734ee810bc"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    claimed = obj.get("canonical_sha256_without_this_field")
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(f"canonical moved at {path}: claimed={claimed} actual={actual}")
    return obj


def literal_assignment(source: str, name: str):
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return ast.literal_eval(node.value)
    raise ValueError(f"missing literal assignment {name}")


def host_count(capacities: list[int], extra: int, twos: int, host: int) -> int:
    dp = {0: 1}
    for i, total in enumerate(capacities):
        nd: dict[int, int] = defaultdict(int)
        if i == host:
            if total < extra:
                return 0
            remainder = total - extra
            for x2, count in dp.items():
                for k2 in range(remainder // 2 + 1):
                    nd[x2 + k2] += count
        else:
            for x2, count in dp.items():
                for k2 in range(total // 2 + 1):
                    nd[x2 + k2] += count
        dp = dict(nd)
    return dp.get(twos, 0)


def pack_frontier(counts: list[int], pairs: list[tuple[int, int]], wmap: dict[int, int], extra: int, twos: int, expected: int) -> dict:
    candidates = [i for i, count in enumerate(counts) if count]
    boundary_pairs = sorted({pairs[i] for i in candidates})
    wpairs = sorted({(wmap[a], wmap[b]) for a, b in boundary_pairs})
    if sum(counts) != expected:
        raise ValueError(f"host-summed count mismatch: {sum(counts)} != {expected}")
    return {
        "unique_defect_contact_multiplicity": extra,
        "remaining_m2_count": twos,
        "aggregate_assignment_count_recovered_by_host_sum": sum(counts),
        "aggregate_assignment_count_expected": expected,
        "host_candidate_count": len(candidates),
        "candidate_exceptional_labels": [93 + i for i in candidates],
        "candidate_boundary_pairs": [f"{a}:{b}" for a, b in boundary_pairs],
        "candidate_ordered_weierstrass_pairs": [[a, b] for a, b in wpairs],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    repo = Path(__file__).resolve().parents[3]
    witness_path = repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
    budget_path = here / "post1473-o188-cusp-ramification-budget.json"
    budget_generator_path = here / "diagnose_stage32_post1473_o188_cusp_ramification_budget.py"
    incidence_path = here / "post1473-x8-marked-exceptional-incidence.json"
    adapter_path = here / "post1473-boundary-label-weierstrass-adapter.json"
    sigma_path = here / "diagnose_stage32_post1473_sigma_c_exceptional_replay.py"

    for path, blob in (
        (witness_path, WITNESS_BLOB),
        (budget_path, BUDGET_BLOB),
        (budget_generator_path, BUDGET_GENERATOR_BLOB),
        (incidence_path, INCIDENCE_BLOB),
        (adapter_path, ADAPTER_BLOB),
        (sigma_path, SIGMA_ORDER_BLOB),
    ):
        actual = git_blob_sha1(path)
        if actual != blob:
            raise ValueError(f"git blob moved at {path}: {actual}")

    witness = load_canonical(witness_path, WITNESS_CANONICAL)
    budget = load_canonical(budget_path, BUDGET_CANONICAL)
    incidence = load_canonical(incidence_path, INCIDENCE_CANONICAL)
    adapter = load_canonical(adapter_path, ADAPTER_CANONICAL)

    all140 = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != WITNESS_ALL140:
        raise ValueError("V6 all140 pairing order moved")
    capacities = [int(x) for x in budget["coarse_nodewise_nonexclusion"]["fixed_exceptional_totals"]]
    if len(capacities) != 48 or all140[92:] != capacities:
        raise ValueError("budget 48-vector no longer equals V6 all140 exceptional slice")

    generator_text = budget_generator_path.read_text()
    if [int(x) for x in literal_assignment(generator_text, "EXCEPTIONAL")] != capacities:
        raise ValueError("budget generator literal EXCEPTIONAL vector moved")
    if "post1473-v6-witness-body-recovered" in generator_text or "exceptional_label" in generator_text or "EXC_" in generator_text:
        raise ValueError("budget generator unexpectedly gained a named provenance transport; update this boundary")

    sigma_text = sigma_path.read_text()
    for required in (
        "if direct != p_list[92 + j]:",
        '"exceptional_id": f"EXC_{j + 1:03d}"',
        '"all140_curve_index_1based": 93 + j',
    ):
        if required not in sigma_text:
            raise ValueError(f"sigma-c order authority moved: {required}")

    incidence_rows = incidence["rows"]
    if len(incidence_rows) != 48 or [int(r["exceptional_label"]) for r in incidence_rows] != list(range(93, 141)):
        raise ValueError("marked exceptional-incidence row order moved")
    boundary_map = {int(k): int(v) for k, v in adapter["boundary_label_to_weierstrass_id"].items()}
    if sorted(boundary_map) != list(range(33, 45)) or sorted(set(boundary_map.values())) != list(range(1, 7)):
        raise ValueError("boundary/Weierstrass adapter moved")

    pairs = []
    named_rows = []
    for j, total in enumerate(capacities):
        row = incidence_rows[j]
        first = int(row["first_factor_boundary_label"])
        second = int(row["second_factor_boundary_label"])
        pairs.append((first, second))
        named_rows.append({
            "exceptional_id": f"EXC_{j + 1:03d}",
            "exceptional_label": 93 + j,
            "capacity": total,
            "first_factor_boundary_label": first,
            "second_factor_boundary_label": second,
            "first_projection_weierstrass_id": boundary_map[first],
            "second_projection_weierstrass_id": boundary_map[second],
        })

    b_counts = [host_count(capacities, 3, 38, j) for j in range(48)]
    c_counts = [host_count(capacities, 4, 37, j) for j in range(48)]
    for j, row in enumerate(named_rows):
        row["B_m3_host"] = b_counts[j] > 0
        row["C_m4_host"] = c_counts[j] > 0

    coarse = budget["coarse_nodewise_nonexclusion"]
    b_frontier = pack_frontier(b_counts, pairs, boundary_map, 3, 38, int(coarse["one_m3_plus_38_m2_nodewise_assignment_count"]))
    c_frontier = pack_frontier(c_counts, pairs, boundary_map, 4, 37, int(coarse["one_m4_plus_37_m2_nodewise_assignment_count"]))
    if b_frontier["host_candidate_count"] != 31 or c_frontier["host_candidate_count"] != 28:
        raise ValueError("named host frontier cardinality moved")
    if b_frontier["candidate_boundary_pairs"] != c_frontier["candidate_boundary_pairs"]:
        raise ValueError("B/C candidate boundary-pair frontier unexpectedly differs")

    all_realized_pairs = sorted({(int(r["first_factor_boundary_label"]), int(r["second_factor_boundary_label"])) for r in incidence_rows})
    retained_pairs = [tuple(map(int, p.split(":"))) for p in b_frontier["candidate_boundary_pairs"]]
    excluded_pairs = sorted(set(all_realized_pairs) - set(retained_pairs))
    if excluded_pairs != [(42, 44), (43, 41)]:
        raise ValueError(f"excluded pair frontier moved: {excluded_pairs}")
    excluded_wpairs = sorted((boundary_map[a], boundary_map[b]) for a, b in excluded_pairs)
    b_only = [93 + i for i in range(48) if b_counts[i] and not c_counts[i]]
    if b_only != [113, 122, 139]:
        raise ValueError(f"B-only host frontier moved: {b_only}")

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_NAMED_DEFECT_HOST_PROVENANCE_BRIDGE_V1",
        "stage": 32,
        "leaf": "POST1484_O188_Q4_NAMED_DEFECT_HOST_PROVENANCE_BRIDGE",
        "status": "PROVISIONAL_EXACT_REPLAY_BOUNDARY_PENDING_HOSTILE_AUDIT",
        "source_locks": {
            "v6_witness": {"path": "stages/stage32/32-21/post1473-v6-witness-body-recovered.json", "git_blob_sha1": WITNESS_BLOB, "canonical_sha256": WITNESS_CANONICAL, "all140_pairings_sha256": WITNESS_ALL140},
            "cusp_budget": {"path": "stages/stage32/residual-32-01-production/post1473-o188-cusp-ramification-budget.json", "git_blob_sha1": BUDGET_BLOB, "canonical_sha256": BUDGET_CANONICAL},
            "cusp_budget_generator": {"path": "stages/stage32/residual-32-01-production/diagnose_stage32_post1473_o188_cusp_ramification_budget.py", "git_blob_sha1": BUDGET_GENERATOR_BLOB},
            "marked_exceptional_incidence": {"path": "stages/stage32/residual-32-01-production/post1473-x8-marked-exceptional-incidence.json", "git_blob_sha1": INCIDENCE_BLOB, "canonical_sha256": INCIDENCE_CANONICAL},
            "boundary_weierstrass_adapter": {"path": "stages/stage32/residual-32-01-production/post1473-boundary-label-weierstrass-adapter.json", "git_blob_sha1": ADAPTER_BLOB, "canonical_sha256": ADAPTER_CANONICAL},
            "sigma_c_order_authority": {"path": "stages/stage32/residual-32-01-production/diagnose_stage32_post1473_sigma_c_exceptional_replay.py", "git_blob_sha1": SIGMA_ORDER_BLOB},
        },
        "provenance_bridge": {
            "budget_fixed_exceptional_totals_equal_v6_all140_pairings_exceptional_slice": True,
            "exceptional_slice_all140_indices_1based": {"first": 93, "last": 140, "count": 48},
            "named_join_count": 48,
            "ordered_join": "position j=0..47 -> all140 label 93+j -> EXC_{j+1:03d} -> marked incidence row -> two retained boundary labels -> two Weierstrass ids",
            "budget_generator_serializes_capacity_vector_without_names": True,
            "source_preserving_recovery": "The q'=4 nodewise capacity vector can be losslessly re-keyed by the upstream V6 all140 ordering and retained marked exceptional-incidence ordering; no guessed node choice is introduced.",
        },
        "named_exceptional_capacity_rows": named_rows,
        "named_defect_host_frontier": {
            "B_one_m3_plus_38_m2": b_frontier,
            "C_one_m4_plus_37_m2": c_frontier,
            "shared_candidate_boundary_pair_count": 10,
            "excluded_realized_boundary_pairs_for_both_B_and_C": [f"{a}:{b}" for a, b in excluded_pairs],
            "excluded_ordered_weierstrass_pairs_for_both_B_and_C": [[a, b] for a, b in excluded_wpairs],
            "B_only_exceptional_labels_not_C_hosts": b_only,
            "all_six_individual_weierstrass_ids_still_present": True,
            "unique_host_selected": False,
        },
        "conclusion": {
            "upstream_source_preserving_carrier_identifier_found": True,
            "previous_missing_join_repaired_for_nodewise_capacity_provenance": True,
            "B_host_frontier_reduced_from_48_to_31": True,
            "C_host_frontier_reduced_from_48_to_28": True,
            "realized_boundary_pair_frontier_reduced_from_12_to_10": True,
            "actual_q4_defect_host_identified": False,
            "remaining_gap": "A new source-locked q'=4 symmetry-breaking constraint must act on the named 31/28-node frontier; aggregate B/C data alone still does not select one host.",
        },
        "next_action": "Apply an exact q'=4 carrier-side symmetry-breaking invariant to the named defect-host rows, preserving EXC/all140/boundary-pair/Weierstrass identifiers. Do not reopen the aggregate B/C nonuniqueness or O186 baseline.",
        "firewalls": {"nodewise_capacity_assignment_is_not_analytic_branch_realization": True, "named_candidate_is_not_actual_carrier_branch": True, "host_nonuniqueness_remains": True, "O188_closed": False, "full178_authorized": False, "receiver_credit": False, "route_credit": False, "theorem_credit": False, "endpoint_credit": False, "perfect_cuboid_claim": False},
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    if result["canonical_sha256_without_this_field"] != OUTPUT_CANONICAL:
        raise ValueError(f"output canonical moved: {result['canonical_sha256_without_this_field']}")
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print("STAGE32_POST1484_O188_Q4_NAMED_DEFECT_HOST_PROVENANCE_BRIDGE=PASS")
    print("NAMED_JOIN_COUNT=48")
    print("B_HOST_CANDIDATES=31")
    print("C_HOST_CANDIDATES=28")
    print("BOUNDARY_PAIR_FRONTIER=10_OF_12")
    print("EXCLUDED_PAIRS=42:44,43:41")
    print(f"CERT_CANONICAL={OUTPUT_CANONICAL}")


if __name__ == "__main__":
    main()
