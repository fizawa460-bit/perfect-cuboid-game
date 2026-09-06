#!/usr/bin/env python3
"""V91C1W exact NONCREDIT all-eight strict-scheme -> Picard64 diagnostic.

For the six direct-support schemes, prove that the observed known92 components
are exhaustive reduced decompositions by exact ideal-intersection equality,
then sum the corresponding retained Picard64 rows.  Independently verify the
parent linear-carrier total-transform relations including exceptional-node
contributions.

For the two zero-known92 schemes, use their single-component parent carrier
and the same exact exceptional valuation model as V91C1S to solve the strict
transform class from the total-transform hyperplane relation; independently
check the swap23 image via the exact Picard action.

Finally compute the strict, exceptional, and complete swap23 divisor-class
differences in retained Picard64 coordinates and reduce the complete row mod 2.
No marked-Brauer/mask20 credit is granted here.
"""
from __future__ import annotations

import json
import runpy
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
V_PATH = HERE / "diagnose_e3_v91c1v_actual_prime_known140_locator.py"

vns = runpy.run_path(str(V_PATH))
sns = vns["sns"]
kns = vns["kns"]

variables = sns["variables"]
ens = sns["ens"]
needed = sorted(sns["strict_package_difference"])
assert len(needed) == 8
matches = vns["matches"]
known_generators = vns["known_generators"]
known_rows = kns["known"]
hyperplane = kns["hyperplane"]
actions = kns["actions"]
assert len(known_rows) == 140 and len(hyperplane) == 64 and len(actions) == 2

old_to_canonical = sns["old_to_canonical"]
canonical_generators = sns["canonical_generators"]
prime_records = sns["prime_records"]
prime_action = sns["prime_action"]
carrier_refinements = sns["e11"]["prime_inventory"]["carrier_refinements"]
inventory = sns["inventory"]
WORD = sns["WORD"]
assert WORD == ["swap12", "swap13", "swap12"]

canonical_to_old = {}
for old_id, canonical_id in old_to_canonical.items():
    canonical_to_old.setdefault(canonical_id, []).append(old_id)
for ids in canonical_to_old.values():
    ids.sort()


def row_add(*rows):
    out = [0] * 64
    for row in rows:
        for j, x in enumerate(row):
            out[j] += int(x)
    return out


def row_scale(a, row):
    return [int(a) * int(x) for x in row]


def row_sub(a, b):
    return [int(x) - int(y) for x, y in zip(a, b)]


def act_row(row):
    # Row-coordinate convention from certify_two_coordinate_swap_picard_rows.py.
    for action in (actions[0], actions[1], actions[0]):
        row = kns["row_times_matrix"](row, action)
    return row


def canonical_id(gens):
    return ens["canonical_ideal"](gens, variables)[0]


def intersect_two(gens1, gens2, tag):
    t = sp.Symbol(f"_v91c1w_t_{tag}")
    gb = sp.groebner(
        [t * f for f in gens1] + [(1 - t) * g for g in gens2],
        t, *variables, order="lex", extension=sp.I,
    )
    out = [sp.expand(p.as_expr()) for p in gb.polys if not p.as_expr().has(t)]
    if not out:
        raise SystemExit("empty ideal-intersection elimination result")
    return out


def intersect_many(generator_lists, tag):
    out = list(generator_lists[0])
    for k, gens in enumerate(generator_lists[1:], start=1):
        out = intersect_two(out, gens, f"{tag}_{k}")
    return out


def exc_row(eids):
    rows = []
    for eid in eids:
        j = int(eid.split("_")[1])
        # EXC_j -> known140 class 92+j; Python row index is class-1.
        rows.append(known_rows[91 + j])
    return row_add(*rows) if rows else [0] * 64


def carrier_exceptionals(signature):
    form = [sns["qi"](z) for z in signature]
    out = []
    for eid, point in sns["node_points"].items():
        if sns["dot"](form, point) == sns["zero"]:
            out.append(eid)
    return sorted(out)


def carrier_piece_rows(carrier_id, class_rows):
    rows = []
    pieces = []
    for piece in carrier_refinements[carrier_id]:
        old_id = piece["prime_id"]
        cid = old_to_canonical[old_id]
        if cid not in class_rows:
            raise SystemExit(f"carrier {carrier_id}: class unavailable for {cid}")
        mult = int(piece["multiplicity"])
        rows.append(row_scale(mult, class_rows[cid]))
        pieces.append({"canonical_id": cid, "multiplicity": mult})
    return row_add(*rows), pieces

# Six direct-support schemes: exact reduced decomposition into their observed
# known92 components.  Exact equality of the target ideal with the intersection
# of component ideals proves exhaustivity; distinct component ideals give
# reduced multiplicity one in this decomposition.
direct_ids = [p for p in needed if matches[p]]
zero_ids = [p for p in needed if not matches[p]]
assert len(direct_ids) == 6 and len(zero_ids) == 2

class_rows = {}
direct_decompositions = {}
for pid in direct_ids:
    olds = canonical_to_old.get(pid, [])
    if len(olds) != 1:
        raise SystemExit(f"direct scheme canonical provenance not unique: {pid}")
    record = prime_records[olds[0]]
    if record["kind"] != "AUDITED_33_11D_DIRECT_PRIME_SUPPORT":
        raise SystemExit(f"multi-match scheme is not audited direct support: {pid}")
    comps = matches[pid]
    component_gens = [known_generators[j - 1] for j in comps]
    component_ids = [canonical_id(g) for g in component_gens]
    if len(set(component_ids)) != len(component_ids):
        raise SystemExit(f"duplicate known component ideal: {pid}")
    intersection = intersect_many(component_gens, pid[:10])
    intersection_id = canonical_id(intersection)
    if intersection_id != pid:
        raise SystemExit(f"known-component intersection not exhaustive for {pid}: {intersection_id}")
    row = row_add(*(known_rows[j - 1] for j in comps))
    class_rows[pid] = row
    direct_decompositions[pid] = {
        "known140_class_indices_1based": comps,
        "component_count": len(comps),
        "component_multiplicities": [1] * len(comps),
        "exact_ideal_intersection_equals_target": True,
        "decomposition_exhaustive": True,
        "decomposition_reduced": True,
        "source_kind": record["kind"],
        "source_carrier_id": record["carrier_id"],
        "source_scheme_multiplicity_in_carrier": int(record["scheme_multiplicity_in_carrier"]),
        "picard64_row": row,
    }

# Verify every direct parent-carrier total-transform relation.  This catches
# both carrier scheme multiplicities and exceptional-node corrections.
direct_carriers = sorted({
    prime_records[canonical_to_old[p][0]]["carrier_id"] for p in direct_ids
})
carrier_relations = {}
for carrier_id in direct_carriers:
    strict_sum, pieces = carrier_piece_rows(carrier_id, class_rows)
    eids = carrier_exceptionals(inventory[carrier_id])
    rhs = row_add(strict_sum, exc_row(eids))
    if rhs != hyperplane:
        raise SystemExit(f"direct carrier total-transform Picard relation failed: {carrier_id}")
    carrier_relations[carrier_id] = {
        "strict_pieces": pieces,
        "exceptional_ids": eids,
        "total_transform_equals_hyperplane": True,
    }

# The retained zero-match prime has one parent carrier and is the only strict
# refinement piece of that carrier.  Solve its strict-transform class from
# H = P + sum_E E.  The other zero-match scheme is its exact swap23 image;
# independently reconstruct its acted-carrier relation and compare with the
# exact Picard action.
retained_zero = [p for p in zero_ids if p in canonical_to_old]
outside_zero = [p for p in zero_ids if p not in canonical_to_old]
if len(retained_zero) != 1 or len(outside_zero) != 1:
    raise SystemExit("expected one retained and one outside-inventory zero-match scheme")
z0 = retained_zero[0]
z1 = outside_zero[0]
z0_old = canonical_to_old[z0]
if len(z0_old) != 1:
    raise SystemExit("zero-match retained provenance not unique")
z0_record = prime_records[z0_old[0]]
if z0_record["kind"] != "EXACT_REDUCED_PRIME_IDEAL":
    raise SystemExit("retained zero-match is not exact reduced prime ideal")
carriers = sorted({x["carrier_id"] for x in z0_record["transport_provenance"]})
if len(carriers) != 1:
    raise SystemExit("retained zero-match does not have one parent carrier")
zcarrier = carriers[0]
zpieces = carrier_refinements[zcarrier]
if len(zpieces) != 1 or old_to_canonical[zpieces[0]["prime_id"]] != z0 or int(zpieces[0]["multiplicity"]) != 1:
    raise SystemExit("zero-match parent carrier is not a single multiplicity-one strict component")
z0_exc = carrier_exceptionals(inventory[zcarrier])
z0_row = row_sub(hyperplane, exc_row(z0_exc))
class_rows[z0] = z0_row
if row_add(z0_row, exc_row(z0_exc)) != hyperplane:
    raise SystemExit("retained zero-match total-transform relation failed")

if prime_action[z0] != z1 or prime_action.get(z1, z0) not in (z0, None):
    # z1 is outside retained inventory, so prime_action is not necessarily keyed by z1.
    if prime_action[z0] != z1:
        raise SystemExit("zero-match swap23 image mismatch")
acted_sig = ens["apply_word_signature"](inventory[zcarrier], WORD)
z1_exc = carrier_exceptionals(acted_sig)
z1_direct_row = row_sub(hyperplane, exc_row(z1_exc))
z1_action_row = act_row(z0_row)
if z1_direct_row != z1_action_row:
    raise SystemExit("outside zero-match acted-carrier class disagrees with Picard action")
class_rows[z1] = z1_direct_row

zero_relations = {
    z0: {
        "source_carrier_id": zcarrier,
        "carrier_strict_component_count": 1,
        "carrier_component_multiplicity": 1,
        "exceptional_ids": z0_exc,
        "total_transform_equals_hyperplane": True,
        "picard64_row": z0_row,
    },
    z1: {
        "source":"swap23 image of retained zero-match carrier/component",
        "exceptional_ids": z1_exc,
        "acted_total_transform_equals_hyperplane": True,
        "agrees_with_exact_swap23_picard_action": True,
        "picard64_row": z1_direct_row,
    },
}

if set(class_rows) != set(needed):
    raise SystemExit("not all eight strict schemes received Picard64 rows")

# Verify swap23 covariance of every strict scheme pair wherever the image is
# also among the eight package-difference schemes.
strict_action_checks = []
for pid in needed:
    image = prime_action.get(pid)
    if image in class_rows:
        if act_row(class_rows[pid]) != class_rows[image]:
            raise SystemExit(f"strict Picard swap23 covariance failed: {pid}")
        strict_action_checks.append({"source": pid, "target": image, "pass": True})

strict_row = [0] * 64
for pid, coeff in sns["strict_package_difference"].items():
    strict_row = row_add(strict_row, row_scale(coeff, class_rows[pid]))

exceptional_row = [0] * 64
for eid, coeff in sns["exceptional_package_difference"].items():
    exceptional_row = row_add(exceptional_row, row_scale(coeff, exc_row([eid])))

full_row = row_add(strict_row, exceptional_row)
full_mod2 = [x % 2 for x in full_row]
full_mod2_support = [i + 1 for i, x in enumerate(full_mod2) if x]

result = {
    "success": True,
    "credit": False,
    "marker": "V91C1W_ALL8_STRICT_SCHEMES_PICARD64_REDUCTION_DIAGNOSTIC",
    "strict_scheme_count": 8,
    "strict_scheme_picard64_classes_materialized": True,
    "direct_multi_match_scheme_count": 6,
    "direct_decompositions": direct_decompositions,
    "direct_carrier_relations": carrier_relations,
    "zero_match_scheme_count": 2,
    "zero_match_relations": zero_relations,
    "all_eight_exact_decomposition_or_direct_relation": True,
    "strict_swap23_picard_covariance_checks": strict_action_checks,
    "strict_package_picard64_row": strict_row,
    "exceptional_package_picard64_row": exceptional_row,
    "complete_swap23_difference_picard64_row": full_row,
    "complete_swap23_difference_mod2_row": full_mod2,
    "complete_swap23_difference_mod2_support_one_based": full_mod2_support,
    "pic2_cech_difference_class_computed": True,
    "complete_swap23_difference_zero_mod2": not full_mod2_support,
    "a2_02_swap23_seed_fixed_mod_pic2_promoted": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
}
print(json.dumps(result, sort_keys=True))
