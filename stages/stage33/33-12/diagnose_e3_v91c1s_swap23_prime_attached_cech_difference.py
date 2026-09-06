#!/usr/bin/env python3
"""V91C1S NONCREDIT diagnostic: lift the V91C1Q/R swap23 word to actual
height-one primes and the 48 resolution exceptional primes, then materialize
acted-minus-original divisor vectors for the eight literal A2_02 Cech packages.

This intentionally stops before Pic/2 unless an exact Cech/Cartier-to-Picard
class reduction is actually present.  A zero package divisor is not promoted
to equality of H^2(mu2) classes.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
R_PATH = HERE / "diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py"
E11_PATH = S33 / "33-11e" / "verify_stage33_11e_prime_galois_transport.py"
E11_CERT = S33 / "33-11e" / "stage33-11e-prime-galois-transport-certificate.json"
E11_SOURCE = S33 / "33-11e" / "stage33-11e-source-lock.json"
D11_SOURCE = S33 / "33-11d" / "stage33-11d-source-lock.json"
NODES = S33 / "33-07" / "exceptional-p1-tangent-coordinates.json"
D_CERT = HERE / "e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"

E11_CERT_SHA = "1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
E11_SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
D11_SOURCE_SHA = "a7989a2e0bd58371f7eb4692a5f905c55007606d01b6b364f25558823ca52852"
D_CERT_SHA = "fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
EXPECTED_COMPONENTS = [
    "EXC_003", "EXC_004", "EXC_011", "EXC_012",
    "SIDE_002", "SIDE_004", "SIDE_006", "SIDE_008",
]
WORD = ["swap12", "swap13", "swap12"]
PERM23 = [0, 2, 1, 3, 5, 4, 6]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_checked(path: Path, expected: str | None = None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert csha(body) == claimed, path
    if expected is not None:
        assert claimed == expected, path
    return obj


def add(out, key, value):
    out[key] = out.get(key, 0) + int(value)
    if out[key] == 0:
        del out[key]


def subtract(left, right):
    out = dict(left)
    for key, value in right.items():
        add(out, key, -int(value))
    return dict(sorted(out.items()))


def sum_vectors(vectors):
    out = {}
    for vector in vectors:
        for key, value in vector.items():
            add(out, key, value)
    return dict(sorted(out.items()))


# Reuse the exact V91C1R coordinate word and literal A2_02 package source.
rns = runpy.run_path(str(R_PATH))
assert rns["result"]["success"] is True
assert rns["result"]["composed_coordinate_permutation"] == PERM23
assert rns["WORD"] == WORD
packages = rns["packages"]
assert sorted(packages) == sorted(EXPECTED_COMPONENTS)

# Reuse the audited 33-11d / exact 33-11e prime-refinement inventory.
ens = runpy.run_path(str(E11_PATH))
e11 = load_checked(E11_CERT, E11_CERT_SHA)
e11_source = load_checked(E11_SOURCE, E11_SOURCE_SHA)
d11_source = load_checked(D11_SOURCE, D11_SOURCE_SHA)
dcert = load_checked(D_CERT, D_CERT_SHA)
assert dcert["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert e11["summary"]["carrier_prime_refinement_coverage"] == "30/30"
assert e11["summary"]["unresolved_prime_transports"] == 0

inventory = {
    h: tuple(tuple(z) for z in sig)
    for h, sig in e11_source["carrier_inventory"].items()
}
by_sig = {sig: h for h, sig in inventory.items()}
assert len(inventory) == len(by_sig) == 30
perms = d11_source["certified_actions"]
assert perms["swap12"] == [1, 0, 2, 4, 3, 5, 6]
assert perms["swap13"] == [2, 1, 0, 5, 4, 3, 6]

carrier_action = {}
for carrier_id, sig in inventory.items():
    image_sig = ens["apply_word_signature"](sig, WORD)
    image_id = by_sig.get(image_sig)
    if image_id is None:
        raise SystemExit(f"swap23 carrier image absent: {carrier_id}")
    carrier_action[carrier_id] = image_id
assert all(carrier_action[carrier_action[h]] == h for h in carrier_action)

prime_inventory = e11["prime_inventory"]
refinements = prime_inventory["carrier_refinements"]
prime_records = {row["prime_id"]: row for row in prime_inventory["records"]}
assert set(refinements) == set(inventory)

variables = sp.symbols("a1 a2 a3 b1 b2 b3 c")
local = {str(x): x for x in variables} | {"i": sp.I}
exact_ids = {p for p, row in prime_records.items() if row["kind"] == "EXACT_REDUCED_PRIME_IDEAL"}
direct_ids = set(prime_records) - exact_ids

# Exact algebraic primes: act on the canonical ideal itself and re-canonicalize.
prime_action = {}
for prime_id in sorted(exact_ids):
    row = prime_records[prime_id]
    generators = [sp.sympify(text, locals=local) for text in row["canonical_groebner_basis"]]
    acted = [ens["apply_word_expr"](poly, WORD, variables) for poly in generators]
    image_id, _basis = ens["canonical_ideal"](acted, variables)
    if image_id not in exact_ids:
        raise SystemExit(f"swap23 exact-prime image absent: {prime_id} -> {image_id}")
    prime_action[prime_id] = image_id

# Direct supports use the audited carrier+support ID convention from 33-11e.
direct_lookup = {
    (row["carrier_id"], row["reduced_support"]): prime_id
    for prime_id, row in prime_records.items()
    if prime_id in direct_ids
}
for prime_id in sorted(direct_ids):
    row = prime_records[prime_id]
    support = ens["parse_poly"](row["reduced_support"], local)
    acted_support = ens["canonical_linear"](
        ens["apply_word_expr"](support, WORD, variables), variables
    )
    target_carrier = carrier_action[row["carrier_id"]]
    image_id = direct_lookup.get((target_carrier, acted_support))
    if image_id is None:
        raise SystemExit(
            f"swap23 direct-prime image absent: {prime_id}; "
            f"target_carrier={target_carrier}; support={acted_support}"
        )
    prime_action[prime_id] = image_id

assert set(prime_action) == set(prime_records)
assert all(prime_action[prime_action[p]] == p for p in prime_action)

# Prime-refinement equivariance is checked independently of A2_02 packages.
for carrier_id, pieces in refinements.items():
    acted = sorted(
        (prime_action[piece["prime_id"]], int(piece["multiplicity"]))
        for piece in pieces
    )
    target = sorted(
        (piece["prime_id"], int(piece["multiplicity"]))
        for piece in refinements[carrier_action[carrier_id]]
    )
    if acted != target:
        raise SystemExit(f"swap23 carrier refinement mismatch: {carrier_id}")

# Consume the already-materialized A2_02 signed actual-prime vectors.
a2 = next(row for row in e11["generator_records"] if row["source_direction"] == "A2_02")
strict_original = a2["component_signed_prime_vectors"]
assert sorted(strict_original) == sorted(EXPECTED_COMPONENTS)
strict_acted = {}
strict_difference = {}
for cid, vector in strict_original.items():
    acted = {}
    for prime_id, coeff in vector.items():
        add(acted, prime_action[prime_id], coeff)
    strict_acted[cid] = dict(sorted(acted.items()))
    strict_difference[cid] = subtract(strict_acted[cid], vector)
strict_package_original = sum_vectors(strict_original.values())
strict_package_acted = sum_vectors(strict_acted.values())
strict_package_difference = subtract(strict_package_acted, strict_package_original)

# Resolution exceptional primes: act directly on the 48 source-locked node points
# and evaluate each acted Q(i)-linear factor there.  This does not reuse cc/ct zero.
nodes = json.loads(NODES.read_text(encoding="utf-8"))
if "canonical_sha256" in nodes:
    body = dict(nodes); claimed = body.pop("canonical_sha256")
    assert claimed == csha(body)
models = nodes["exceptional_models"]
assert len(models) == 48

qi = rns["qi"]
qadd = lambda x, y: (x[0] + y[0], x[1] + y[1])
qmul = rns["qmul"]
zero = (Fraction(0), Fraction(0))

def point_signature(raw):
    norm, _pivot = rns["normalize_signature"](raw)
    return tuple(tuple(z) for z in norm)

node_by_sig = {}
node_points = {}
for row in models:
    eid = row["exceptional_id"]
    raw = row["node_point_ambient_P6_L_basis"]
    sig = point_signature(raw)
    assert sig not in node_by_sig
    node_by_sig[sig] = eid
    node_points[eid] = [qi(z) for z in raw]

node_action = {}
for sig, eid in node_by_sig.items():
    acted_sig = tuple(sig[j] for j in PERM23)
    norm, _pivot = rns["normalize_signature"]([list(z) for z in acted_sig])
    image = node_by_sig.get(tuple(tuple(z) for z in norm))
    if image is None:
        raise SystemExit(f"swap23 exceptional node image absent: {eid}")
    node_action[eid] = image
assert all(node_action[node_action[eid]] == eid for eid in node_action)

def dot(form, point):
    out = zero
    for a, b in zip(form, point):
        out = qadd(out, qmul(a, b))
    return out

def package_atoms(package, acted=False):
    atoms = []
    for factor in package["numerator_factors"]:
        sig = factor["coefficients_Qi"]
        if acted:
            sig = [sig[j] for j in PERM23]
        atoms.append((sig, int(factor["exponent"])))
    den = package["denominator"]
    sig = den["coefficients_Qi"]
    if acted:
        sig = [sig[j] for j in PERM23]
    atoms.append((sig, -int(den["exponent"])))
    return atoms

def exceptional_vector(package, acted=False):
    out = {eid: 0 for eid in node_points}
    for sig, exponent in package_atoms(package, acted=acted):
        form = [qi(z) for z in sig]
        for eid, point in node_points.items():
            if dot(form, point) == zero:
                out[eid] += exponent
    return {eid: coeff for eid, coeff in sorted(out.items()) if coeff}

exceptional_original = {cid: exceptional_vector(pkg) for cid, pkg in packages.items()}
exceptional_acted = {cid: exceptional_vector(pkg, acted=True) for cid, pkg in packages.items()}
# Independent covariance check: direct evaluation of g(f) equals transport of f's node valuations.
for cid, vector in exceptional_original.items():
    transported = {}
    for eid, coeff in vector.items():
        add(transported, node_action[eid], coeff)
    if dict(sorted(transported.items())) != exceptional_acted[cid]:
        raise SystemExit(f"swap23 exceptional valuation covariance failed: {cid}")
exceptional_difference = {
    cid: subtract(exceptional_acted[cid], exceptional_original[cid])
    for cid in EXPECTED_COMPONENTS
}
exceptional_package_original = sum_vectors(exceptional_original.values())
exceptional_package_acted = sum_vectors(exceptional_acted.values())
exceptional_package_difference = subtract(
    exceptional_package_acted, exceptional_package_original
)

component_summary = {}
for cid in EXPECTED_COMPONENTS:
    component_summary[cid] = {
        "strict_prime_difference_nonzero_coefficients": len(strict_difference[cid]),
        "exceptional_prime_difference_nonzero_coefficients": len(exceptional_difference[cid]),
        "full_attached_divisor_difference_zero": not strict_difference[cid] and not exceptional_difference[cid],
        "strict_prime_difference_sha256": csha(strict_difference[cid]),
        "exceptional_prime_difference_sha256": csha(exceptional_difference[cid]),
    }

full_package_zero = not strict_package_difference and not exceptional_package_difference
full_component_zero_count = sum(
    1 for row in component_summary.values() if row["full_attached_divisor_difference_zero"]
)
result = {
    "success": True,
    "marker": "V91C1S_SWAP23_PRIME_ATTACHED_CECH_DIFFERENCE_DIAGNOSTIC",
    "role": "EXACT_NONCREDIT_SWAP23_FULL_CODIM1_ATTACHMENT_DIAGNOSTIC",
    "q_word": WORD,
    "coordinate_permutation": PERM23,
    "carrier_inventory_closed_under_swap23": True,
    "carrier_count": len(inventory),
    "actual_prime_inventory_closed_under_swap23": True,
    "actual_prime_count": len(prime_records),
    "carrier_refinement_equivariant_under_swap23": True,
    "exceptional_node_inventory_closed_under_swap23": True,
    "exceptional_prime_count": len(node_points),
    "component_differences": component_summary,
    "components_with_zero_full_attached_divisor_difference": full_component_zero_count,
    "component_count": len(EXPECTED_COMPONENTS),
    "strict_transform_package_difference_zero": not strict_package_difference,
    "exceptional_package_difference_zero": not exceptional_package_difference,
    "full_codim1_package_difference_zero": full_package_zero,
    "strict_package_difference_nonzero_coefficients": len(strict_package_difference),
    "exceptional_package_difference_nonzero_coefficients": len(exceptional_package_difference),
    "strict_package_difference_sha256": csha(strict_package_difference),
    "exceptional_package_difference_sha256": csha(exceptional_package_difference),
    "prime_attached_component_difference_materialized": True,
    "pic2_cech_difference_class_computed": False,
    "a2_02_swap23_seed_fixed_mod_pic2": False,
    "a2_02_marked_brauer_image_excluded_from_mask20": False,
    "remaining_blocker_code": "EXPLICIT_SWAP23_CECH_CARTIER_DIFFERENCE_REDUCTION_INTO_RETAINED_PIC_OVER_2",
    "anti_inference": {
        "zero_total_divisor_promoted_to_h2_seed_fixedness": False,
        "principal_divisor_promoted_to_cech_pic2_zero": False,
        "target_mask20_used_as_source_data": False,
        "repository_wide_absence_claim": False,
    },
    "stage33_progress": "6/11",
    "credit": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1s_swap23_prime_attached_cech_difference.py,"
    "title=V91C1S_SWAP23_PRIME_ATTACHED_CECH_DIFFERENCE::"
    + f"full_package_zero={str(full_package_zero).lower()};"
    + f"component_zero={full_component_zero_count}/{len(EXPECTED_COMPONENTS)};"
    + "pic2=false"
)
