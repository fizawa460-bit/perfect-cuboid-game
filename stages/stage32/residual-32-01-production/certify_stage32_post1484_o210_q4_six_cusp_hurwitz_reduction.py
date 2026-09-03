#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

BIDEGREE_BLOB = "072266f2ac5386316adc99e35a6444d2449656c8"
BIDEGREE_CANONICAL = "791870c37681702392e1e59d224f494ed791709d467efa68a20cf49bff4ab420"
V4_BLOB = "00eaebc3c57f6b5e3696c7bcd60eac5a53121f72"
V4_CANONICAL = "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5"
Q4_AUTHORITY_BLOB = "ac85353cbe56d04582aaf98c34e6b6c9483b21f1"
Q4_OLD_CANONICAL = "3617ef2e0717a1d75de0f3a271a4b0e25f3ed7e67e76f1e58b490d3fcba9d978"
LOCAL_BLOB = "dd5fdb8d2553d25a1479c1e5cff68a201c8396e3"
LOCAL_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
INCIDENCE_BLOB = "b3f673aa73324ee731356eec2c0448592fd1e59b"
INCIDENCE_CANONICAL = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
V6_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
EXPECTED_CANONICAL = "329cf00d5380f515386622f5b18bcf90e36a99c16715e462ef9219abe0d609e1"
FIRST = [34, 35, 38, 39, 42, 43]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def locked_json(path: Path, blob: str) -> dict:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return json.loads(raw)


def locked_text(path: Path, blob: str) -> str:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return raw.decode()


def canonical_without_field(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return csha(body)


def local_base_change_ramification_index(e: int) -> int:
    return e // math.gcd(e, 2)


def group_m2_distribution(capacities: list[int]) -> dict[int, int]:
    dp = {0: 1}
    for total_m in capacities:
        nd: defaultdict[int, int] = defaultdict(int)
        for used, count in dp.items():
            for k2 in range(total_m // 2 + 1):
                nd[used + k2] += count
        dp = dict(nd)
    return dp


def build(repo: Path) -> dict:
    here = repo / "stages/stage32/residual-32-01-production"
    bidegree = locked_json(here / "post1484-v6-modular-factor-bidegree-boundary.json", BIDEGREE_BLOB)
    if canonical_without_field(bidegree) != BIDEGREE_CANONICAL:
        raise ValueError("audited bidegree canonical moved")
    if bidegree["modular_factor_bidegree"] != {"first_z": 105, "second_w": 81, "sum": 186, "both_nonconstant": True}:
        raise ValueError("modular bidegree moved")
    o210 = bidegree["O210_extremal_profile"]
    if o210["source_projection_ramification_totals"] != [0, 192] or o210["descended_projection_ramification_totals"] != [0, 48]:
        raise ValueError("O210 ramification boundary moved")
    if o210["forced_contact_histogram"] != {"m1_odd": 210, "m2_even": 28, "all_other_contacts": 0, "B": 238}:
        raise ValueError("O210 contact histogram moved")

    v4 = locked_json(here / "post1473-x8-v4-cusp-quotient.json", V4_BLOB)
    if canonical_without_field(v4) != V4_CANONICAL:
        raise ValueError("V4 quotient canonical moved")
    qg = v4["quotient_geometry"]
    required_qg = {"X8_to_C0_degree": 4, "X8_to_C0_etale": True, "genus_X8": 5, "genus_C0": 2, "C0_to_X4_degree": 2, "genus_X4": 0, "C0_to_X4_total_fixed_points": 6, "six_quotient_cusps_are_Weierstrass_points": True}
    for key, value in required_qg.items():
        if qg.get(key) != value:
            raise ValueError(f"V4 quotient field moved: {key}")

    authority = locked_text(here / "post1473-o188-q4-genus2-descent-source-note.md", Q4_AUTHORITY_BLOB)
    for needle in ("Cartesian torsor lemma", "finite degree is preserved by base change", "deg(R_phi)=4 deg(R_f)"):
        if needle not in authority:
            raise ValueError(f"qprime4 formal authority moved: {needle}")

    local = locked_json(here / "post1473-o188-cusp-ramification-budget.json", LOCAL_BLOB)
    if canonical_without_field(local) != LOCAL_CANONICAL:
        raise ValueError("local cusp adapter canonical moved")
    if "A_i=a_i/4" not in local["local_adapter"]["notation"]:
        raise ValueError("local cusp notation moved")

    incidence = locked_json(here / "post1473-x8-marked-exceptional-incidence.json", INCIDENCE_BLOB)
    if canonical_without_field(incidence) != INCIDENCE_CANONICAL:
        raise ValueError("exceptional incidence canonical moved")
    rows_by_label = {int(row["exceptional_label"]): row for row in incidence["rows"]}
    if sorted(rows_by_label) != list(range(93, 141)):
        raise ValueError("exceptional label range moved")

    v6 = locked_json(repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json", V6_BLOB)
    if v6.get("canonical_sha256_without_this_field") != V6_CANONICAL:
        raise ValueError("V6 canonical moved")
    all140 = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != ALL140_SHA:
        raise ValueError("V6 all140 vector moved")
    capacities = all140[92:]
    if len(capacities) != 48 or sum(capacities) != 266:
        raise ValueError("exceptional capacities moved")

    first_rows = {int(r["boundary_label"]): r for r in bidegree["resolved_cusp_fiber_intersections"] if r["factor"] == "first_z"}
    if sorted(first_rows) != FIRST:
        raise ValueError("first cusp labels moved")
    c_dot_l = {label: int(first_rows[label]["C_dot_L"]) for label in FIRST}
    if c_dot_l != {34: 26, 35: 31, 38: 26, 39: 25, 42: 40, 43: 34} or sum(c_dot_l.values()) != 182:
        raise ValueError("first strict-boundary intersections moved")

    O = 210
    genus_N = 1
    genus_Y = 1 + O // 2
    if genus_Y != 106:
        raise ValueError("genus Y replay failed")
    degrees = [105, 81]
    descended_ram = [0, 48]

    # Local normalization of t^e=s^2 has gcd(e,2) branches and ramification
    # index e/gcd(e,2) over the s-line.  Hence an etale normalized base
    # change over a branch value permits only e=1 or e=2; away from a branch
    # value it permits only e=1.
    zero_branch_local = [e for e in range(1, 267) if local_base_change_ramification_index(e) == 1]
    if zero_branch_local != [1, 2]:
        raise ValueError(f"double-base-change zero ramification set moved: {zero_branch_local}")
    rh_N_first = 2 * 105
    if rh_N_first != 210:
        raise ValueError("genus-one degree-105 RH replay failed")
    total_cusp_degree = 6 * 105
    transpositions = rh_N_first
    fixed_points = total_cusp_degree - 2 * transpositions
    if fixed_points != 210:
        raise ValueError("six-cusp fixed-point count replay failed")

    # O210 first-etale forces every exceptional contact to be m=1 or m=2.
    # The 28 m=2 contacts are precisely the exceptional simple-ramification
    # contribution.  Group those 28 contacts by first-factor cusp using the
    # retained 48-node incidence.  This quotients the 4.39e16 nodewise
    # assignments down to distinct first-cusp cycle-type vectors.
    grouped_caps: dict[int, list[int]] = {label: [] for label in FIRST}
    for exc in range(93, 141):
        first = int(rows_by_label[exc]["first_factor_boundary_label"])
        grouped_caps[first].append(capacities[exc - 93])
    if any(len(grouped_caps[label]) != 8 for label in FIRST):
        raise ValueError("first cusp incidence partition moved")
    distributions = {label: group_m2_distribution(grouped_caps[label]) for label in FIRST}

    support_vectors: list[tuple[int, ...]] = []
    weighted_assignments = 0
    def rec(i: int, remaining: int, vector: list[int], weight: int) -> None:
        nonlocal weighted_assignments
        if i == len(FIRST):
            if remaining == 0:
                support_vectors.append(tuple(vector))
                weighted_assignments += weight
            return
        label = FIRST[i]
        for k2, count in distributions[label].items():
            if k2 <= remaining:
                rec(i + 1, remaining - k2, vector + [k2], weight * count)
    rec(0, 28, [], 1)
    if len(support_vectors) != 214239:
        raise ValueError(f"first cusp cycle support moved: {len(support_vectors)}")
    if weighted_assignments != o210["nodewise_assignment_count"] or weighted_assignments != 43949136035405189:
        raise ValueError("nodewise weighted count moved")

    per_cusp = []
    for i, label in enumerate(FIRST):
        vals = {v[i] for v in support_vectors}
        kmin, kmax = min(vals), max(vals)
        rmin, rmax = c_dot_l[label] + kmin, c_dot_l[label] + kmax
        per_cusp.append({
            "boundary_label": label,
            "C_dot_L": c_dot_l[label],
            "m2_contact_count_min": kmin,
            "m2_contact_count_max": kmax,
            "transposition_count_min": rmin,
            "transposition_count_max": rmax,
            "fixed_point_count_max": 105 - 2 * rmin,
            "fixed_point_count_min": 105 - 2 * rmax,
        })
    if sum(c_dot_l.values()) + 28 != 210:
        raise ValueError("strict-boundary plus exceptional simple ramification moved")

    result = {
        "schema": "STAGE32_POST1484_O210_Q4_SIX_CUSP_HURWITZ_REDUCTION_V1",
        "stage": 32,
        "leaf": "POST1484_O210_Q4_FIRST_PROJECTION_SIX_CUSP_HURWITZ_REDUCTION",
        "status": "PROVISIONAL_EXACT_REPLAY_PENDING_HOSTILE_AUDIT",
        "fixed_target": {"row_id": "g1-d186", "d": 186, "e": 266, "z": [-15, 62, -44, 26, 32]},
        "source_locks": {
            "audited_bidegree_boundary": {"path": "stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-boundary.json", "blob_sha1": BIDEGREE_BLOB, "canonical_sha256": BIDEGREE_CANONICAL},
            "v4_cusp_quotient": {"path": "stages/stage32/residual-32-01-production/post1473-x8-v4-cusp-quotient.json", "blob_sha1": V4_BLOB, "canonical_sha256": V4_CANONICAL},
            "qprime4_cartesian_torsor_authority": {"path": "stages/stage32/residual-32-01-production/post1473-o188-q4-genus2-descent-source-note.md", "blob_sha1": Q4_AUTHORITY_BLOB, "old_o188_certificate_canonical_sha256": Q4_OLD_CANONICAL, "reuse_scope": "formal V4 Cartesian torsor/base-change lemma only; old O188 degree-93 and ramification-2 values are not reused"},
            "local_cusp_adapter": {"path": "stages/stage32/residual-32-01-production/post1473-o188-cusp-ramification-budget.json", "blob_sha1": LOCAL_BLOB, "canonical_sha256": LOCAL_CANONICAL},
            "exceptional_incidence": {"path": "stages/stage32/residual-32-01-production/post1473-x8-marked-exceptional-incidence.json", "blob_sha1": INCIDENCE_BLOB, "canonical_sha256": INCIDENCE_CANONICAL},
            "v6_witness": {"path": "stages/stage32/32-21/post1473-v6-witness-body-recovered.json", "blob_sha1": V6_BLOB, "canonical_sha256": V6_CANONICAL, "all140_pairings_sha256": ALL140_SHA},
        },
        "audited_O210_inputs": {"O": O, "qprime": 4, "modular_factor_bidegree": degrees, "D_to_X8_degrees": degrees, "D_to_X8_ramification": [0, 192], "forced_contact_histogram": {"m1_odd": 210, "m2_even": 28, "B": 238}, "coarse_nodewise_assignment_count": weighted_assignments},
        "v4_descent": {"genus_N": genus_N, "Y_to_N_degree": 2, "Y_to_N_ramification": O, "genus_Y": genus_Y, "C0_genus": 2, "X8_to_C0_degree": 4, "X8_to_C0_etale": True, "Y_to_C0_degrees": degrees, "Y_to_C0_ramification": descended_ram, "first_projection_etale": True, "second_projection_ramified": True},
        "first_projection_base_change": {"N_to_X4_degree": 105, "genus_N": 1, "genus_X4": 0, "C0_to_X4_degree": 2, "C0_to_X4_branch_values": 6, "branch_values": "the six quotient cusps / Weierstrass points", "normalized_local_base_change": "for local degree e over a branch value, gcd(e,2) normalized branches occur and each Y->C0 ramification index is e/gcd(e,2)", "etale_local_degrees_over_six_branch_values": [1, 2], "ramification_allowed_away_from_six_branch_values": False, "riemann_hurwitz_total_ramification_N_to_X4": rh_N_first, "consequence": "N->X(4)=P1 is branched only over the six modular cusp values and every ramification point is simple"},
        "six_cusp_hurwitz_data": {"degree": 105, "branch_value_count": 6, "permutation_group": "S_105", "branch_permutations": "six involutions; cycle type at cusp j is 2^r_j 1^s_j with 2*r_j+s_j=105", "total_transpositions": transpositions, "total_fixed_points": fixed_points, "strict_boundary_simple_ramification_total": 182, "exceptional_m2_simple_ramification_total": 28, "m2_distribution_constraint": "sum_j k_j=28 and r_j=C_dot_L_j+k_j", "first_cusp_cycle_type_support_count": len(support_vectors), "nodewise_weighted_assignment_count": weighted_assignments, "per_cusp_support": per_cusp, "monodromy_obligation": "find or exclude a transitive six-involution tuple with product identity for at least one reachable k-vector; then impose compatibility with the simultaneous degree-81 map Y->C0 of ramification 48"},
        "negative_reuse": {"old_odd_etale_self_correspondence_obstruction_applicable": False, "reason": "the old commensurator argument required both projections to be etale; at O=210 the second descended projection has ramification 48"},
        "verdict": {"O210_excluded": False, "first_projection_geometry_reduced_to_exact_six_cusp_hurwitz_problem": True, "next_exact_leaf": "O210_Q4_SIX_CUSP_HURWITZ_MONODROMY_AND_SECOND_PROJECTION_COMPATIBILITY"},
        "firewalls": {"O188_reopened": False, "full178_authorized": False, "receiver_credit": False, "route_credit": False, "theorem_credit": False, "endpoint_credit": False, "perfect_cuboid_claim": False},
    }
    result["canonical_sha256_without_this_field"] = canonical_without_field(result)
    if result["canonical_sha256_without_this_field"] != EXPECTED_CANONICAL:
        raise ValueError(f"canonical moved: {result['canonical_sha256_without_this_field']}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[3]
    result = build(repo)
    if args.check:
        expected = json.loads(args.check.read_text())
        if expected != result:
            raise SystemExit("certificate mismatch")
        print("PASS", result["canonical_sha256_without_this_field"])
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
